#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# BentoPDF Air-Gapped Setup Script
# Generated on 2026-06-14 10:58:01 UTC
# BentoPDF v2.8.5
# ============================================================
# Transfer this entire directory to the air-gapped network,
# then run this script.
# ============================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# --- Check prerequisites ---
if ! command -v docker &>/dev/null; then
  echo "ERROR: docker is required but not found."
  echo "Install Docker first: https://docs.docker.com/get-docker/"
  exit 1
fi

if ! docker info &>/dev/null; then
  echo "ERROR: Docker daemon is not running. Start Docker and try again."
  exit 1
fi

# --- Configuration (baked in at generation time) ---
IMAGE_NAME="bentopdf"
WASM_BASE_URL="http://placeholder.local/wasm"
DOCKER_PORT="${1:-3000}"

# Where to extract WASM files (override with WASM_EXTRACT_DIR env var)
WASM_DIR="${WASM_EXTRACT_DIR:-${SCRIPT_DIR}/wasm}"

echo ""
echo "============================================================"
echo "  BentoPDF Air-Gapped Setup"
echo "  Version: 2.8.5"
echo "============================================================"
echo ""
echo "  Docker image:  ${IMAGE_NAME}"
echo "  WASM base URL: ${WASM_BASE_URL}"
echo "  WASM extract:  ${WASM_DIR}"
echo "  Port:          ${DOCKER_PORT}"
echo ""

# --- Step 1: Load Docker Image ---
echo "[1/3] Loading Docker image..."
if [ -f "${SCRIPT_DIR}/bentopdf.tar" ]; then
  docker load -i "${SCRIPT_DIR}/bentopdf.tar"
  echo "  Docker image '${IMAGE_NAME}' loaded."
else
  echo "  WARNING: bentopdf.tar not found. Skipping Docker load."
  echo "  Make sure the image '${IMAGE_NAME}' is already available."
fi

# --- Step 2: Extract WASM Packages ---
echo ""
echo "[2/3] Extracting WASM packages to ${WASM_DIR}..."

mkdir -p "${WASM_DIR}/pymupdf" "${WASM_DIR}/gs" "${WASM_DIR}/cpdf" "${WASM_DIR}/ocr/core" "${WASM_DIR}/ocr/lang-data" "${WASM_DIR}/ocr/fonts"

# PyMuPDF: package has dist/ and assets/ at root
echo "  Extracting PyMuPDF..."
tar xzf "${SCRIPT_DIR}"/bentopdf-pymupdf-wasm-*.tgz -C "${WASM_DIR}/pymupdf" --strip-components=1

# Ghostscript: browser expects gs.js and gs.wasm at root
echo "  Extracting Ghostscript..."
TEMP_GS="$(mktemp -d)"
tar xzf "${SCRIPT_DIR}"/bentopdf-gs-wasm-*.tgz -C "${TEMP_GS}"
if [ -d "${TEMP_GS}/package/assets" ]; then
  cp -r "${TEMP_GS}/package/assets/"* "${WASM_DIR}/gs/"
else
  cp -r "${TEMP_GS}/package/"* "${WASM_DIR}/gs/"
fi
rm -rf "${TEMP_GS}"

# CoherentPDF: browser expects coherentpdf.browser.min.js at root
echo "  Extracting CoherentPDF..."
TEMP_CPDF="$(mktemp -d)"
tar xzf "${SCRIPT_DIR}"/coherentpdf-*.tgz -C "${TEMP_CPDF}"
if [ -d "${TEMP_CPDF}/package/dist" ]; then
  cp -r "${TEMP_CPDF}/package/dist/"* "${WASM_DIR}/cpdf/"
else
  cp -r "${TEMP_CPDF}/package/"* "${WASM_DIR}/cpdf/"
fi
rm -rf "${TEMP_CPDF}"

# Tesseract worker: browser expects a single worker.min.js file
echo "  Extracting Tesseract worker..."
TEMP_TESS="$(mktemp -d)"
tar xzf "${SCRIPT_DIR}/tesseract.js-7.0.0.tgz" -C "${TEMP_TESS}"
cp "${TEMP_TESS}/package/dist/worker.min.js" "${WASM_DIR}/ocr/worker.min.js"
rm -rf "${TEMP_TESS}"

# Tesseract core: browser expects the full tesseract.js-core directory
echo "  Extracting Tesseract core..."
tar xzf "${SCRIPT_DIR}/tesseract.js-core-7.0.0.tgz" -C "${WASM_DIR}/ocr/core" --strip-components=1

# OCR language data: copy the bundled traineddata files
echo "  Installing OCR language data..."
cp "${SCRIPT_DIR}"/tesseract-langdata/*.traineddata.gz "${WASM_DIR}/ocr/lang-data/"

# OCR fonts: copy the bundled font files for searchable text layer rendering
echo "  Installing OCR fonts..."
cp "${SCRIPT_DIR}"/ocr-fonts/* "${WASM_DIR}/ocr/fonts/"

echo "  WASM files extracted to: ${WASM_DIR}"
echo ""
echo "  IMPORTANT: Ensure these paths are served by your internal web server:"
echo "    ${WASM_BASE_URL}/pymupdf/  ->  ${WASM_DIR}/pymupdf/"
echo "    ${WASM_BASE_URL}/gs/       ->  ${WASM_DIR}/gs/"
echo "    ${WASM_BASE_URL}/cpdf/     ->  ${WASM_DIR}/cpdf/"
echo "    ${WASM_BASE_URL}/ocr/worker.min.js  ->  ${WASM_DIR}/ocr/worker.min.js"
echo "    ${WASM_BASE_URL}/ocr/core           ->  ${WASM_DIR}/ocr/core/"
echo "    ${WASM_BASE_URL}/ocr/lang-data      ->  ${WASM_DIR}/ocr/lang-data/"
echo "    ${WASM_BASE_URL}/ocr/fonts          ->  ${WASM_DIR}/ocr/fonts/"

# --- Step 3: Start BentoPDF ---
echo ""
echo "[3/3] Ready to start BentoPDF"
echo ""
echo "  To start manually:"
echo "    docker run -d --name bentopdf -p ${DOCKER_PORT}:8080 --restart unless-stopped ${IMAGE_NAME}"
echo ""
echo "  Then open: http://localhost:${DOCKER_PORT}"
echo ""

read -r -p "Start BentoPDF now? (y/N): " REPLY
if [[ "${REPLY:-}" =~ ^[Yy]$ ]]; then
  docker run -d --name bentopdf -p "${DOCKER_PORT}:8080" --restart unless-stopped "${IMAGE_NAME}"
  echo ""
  echo "  BentoPDF is running at http://localhost:${DOCKER_PORT}"
fi
