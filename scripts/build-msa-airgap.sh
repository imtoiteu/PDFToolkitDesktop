#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# MSA PDF Toolkit — air-gap build orchestrator (macOS/Linux)
# ============================================================
# Produces a single self-contained Docker image (default tag msa-pdf:1.0)
# that runs fully offline, with all WASM/OCR assets baked in and served
# same-origin at /wasm. No BentoPDF source files are modified.
#
# Run on an INTERNET-CONNECTED machine with Docker + Node + curl, then transfer
# the exported tar to the air-gapped network.
#
# Usage:
#   bash scripts/build-msa-airgap.sh
#   OCR_LANGUAGES="eng,deu,fra" bash scripts/build-msa-airgap.sh
#
# Env overrides:
#   OCR_LANGUAGES   (default: eng)
#   BRAND_NAME      (default: "MSA PDF Toolkit")
#   FOOTER_TEXT     (default: "© 2026 MSA — Internal use only.")
#   DISABLE_TOOLS   (default: timestamp-pdf)
#   BASE_TAG        (default: msa-pdf-base:1.0)
#   FINAL_TAG       (default: msa-pdf:1.0)
#   TAR_OUT         (default: ./msa-pdf.tar)
#   FORCE_DOWNLOAD  (set to 1 to refetch WASM even if bundle exists)
#   SKIP_EXPORT     (set to 1 to skip docker save)
# ============================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

OCR_LANGUAGES="${OCR_LANGUAGES:-eng}"
BRAND_NAME="${BRAND_NAME:-MSA PDF Toolkit}"
FOOTER_TEXT="${FOOTER_TEXT:-© 2026 MSA — Internal use only.}"
DISABLE_TOOLS="${DISABLE_TOOLS:-timestamp-pdf}"
BASE_TAG="${BASE_TAG:-msa-pdf-base:1.0}"
FINAL_TAG="${FINAL_TAG:-msa-pdf:1.0}"
TAR_OUT="${TAR_OUT:-./msa-pdf.tar}"
BUNDLE_DIR="./airgap-bundle"
WASM_DIR="$PROJECT_ROOT/wasm"

echo "==> Prerequisite check"
for cmd in docker node curl npm; do
  command -v "$cmd" >/dev/null 2>&1 || { echo "ERROR: '$cmd' not found on PATH."; exit 1; }
done
docker info >/dev/null 2>&1 || { echo "ERROR: Docker daemon not running. Start Docker Desktop."; exit 1; }
echo "    OK (docker, node, curl, npm present; daemon up)"

echo "==> [1/5] Download WASM + OCR assets (langs: ${OCR_LANGUAGES})"
# Reuse a previous download if the bundle already has the packages (avoids re-fetching ~70MB).
REUSE_WASM=()
if ls "${BUNDLE_DIR}"/bentopdf-pymupdf-wasm-*.tgz >/dev/null 2>&1; then
  echo "    Found existing bundle in ${BUNDLE_DIR} — reusing (pass FORCE_DOWNLOAD=1 to refetch)."
  [ "${FORCE_DOWNLOAD:-0}" = "1" ] || REUSE_WASM=(--skip-wasm)
fi
bash scripts/prepare-airgap.sh \
  --wasm-base-url http://placeholder.local/wasm \
  --ocr-languages "${OCR_LANGUAGES}" \
  --skip-docker \
  "${REUSE_WASM[@]}" \
  --output-dir "${BUNDLE_DIR}"

echo "==> [2/5] Extract WASM into ${WASM_DIR}"
rm -rf "${WASM_DIR}"
# setup.sh attempts a (harmless) docker load and ends with a start prompt — auto-decline.
printf 'N\n' | WASM_EXTRACT_DIR="${WASM_DIR}" bash "${BUNDLE_DIR}/setup.sh" || true
# Sanity: the loaders need these paths to exist.
for p in pymupdf gs cpdf ocr/worker.min.js ocr/core ocr/lang-data ocr/fonts; do
  [ -e "${WASM_DIR}/${p}" ] || { echo "ERROR: expected ${WASM_DIR}/${p} after extraction."; exit 1; }
done
echo "    OK (wasm/ layout present)"

echo "==> [3/5] Build base app image: ${BASE_TAG}"
docker build -f Dockerfile -t "${BASE_TAG}" \
  --build-arg SIMPLE_MODE=true \
  --build-arg DISABLE_TOOLS="${DISABLE_TOOLS}" \
  --build-arg VITE_BRAND_NAME="${BRAND_NAME}" \
  --build-arg VITE_FOOTER_TEXT="${FOOTER_TEXT}" \
  --build-arg VITE_WASM_PYMUPDF_URL=/wasm/pymupdf/ \
  --build-arg VITE_WASM_GS_URL=/wasm/gs/ \
  --build-arg VITE_WASM_CPDF_URL=/wasm/cpdf/ \
  --build-arg VITE_TESSERACT_WORKER_URL=/wasm/ocr/worker.min.js \
  --build-arg VITE_TESSERACT_CORE_URL=/wasm/ocr/core \
  --build-arg VITE_TESSERACT_LANG_URL=/wasm/ocr/lang-data \
  --build-arg VITE_OCR_FONT_BASE_URL=/wasm/ocr/fonts \
  --build-arg VITE_TESSERACT_AVAILABLE_LANGUAGES="${OCR_LANGUAGES}" \
  .

echo "==> [4/5] Bake WASM into final image: ${FINAL_TAG}"
docker build -f Dockerfile.airgap --build-arg BASE_IMAGE="${BASE_TAG}" -t "${FINAL_TAG}" .

if [ "${SKIP_EXPORT:-0}" = "1" ]; then
  echo "==> [5/5] Skipping export (SKIP_EXPORT=1)"
else
  echo "==> [5/5] Export single artifact: ${TAR_OUT}"
  docker save "${FINAL_TAG}" -o "${TAR_OUT}"
fi

echo ""
echo "Done. Image: ${FINAL_TAG}"
echo "Smoke test (then turn Wi-Fi off and re-test):"
echo "  docker run -d --name msa-test -p 8090:8080 ${FINAL_TAG} && open http://localhost:8090"
echo "Air-gap deploy:"
echo "  docker load -i $(basename "${TAR_OUT}")"
echo "  docker run -d --name msa-pdf -p 8090:8080 --restart unless-stopped ${FINAL_TAG}"
