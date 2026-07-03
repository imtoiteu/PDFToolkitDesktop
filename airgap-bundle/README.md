# BentoPDF Air-Gapped Deployment Bundle

**BentoPDF v2.8.5** | Generated on 2026-06-14 10:58:01 UTC

## Contents

| File | Description |
| --- | --- |
| `bentopdf.tar` | Docker image |
| `bentopdf-pymupdf-wasm-0.11.16.tgz` | PyMuPDF WASM module |
| `bentopdf-gs-wasm-0.1.1.tgz` | Ghostscript WASM module |
| `coherentpdf-2.5.5.tgz` | CoherentPDF WASM module |
| `tesseract.js-7.0.0.tgz` | Tesseract browser worker package |
| `tesseract.js-core-7.0.0.tgz` | Tesseract core runtime package |
| `tesseract-langdata/` | OCR language data files (eng) |
| `ocr-fonts/` | OCR text-layer font files |
| `setup.sh` | Automated setup script |
| `README.md` | This file |

## WASM Configuration

The Docker image was built with these WASM URLs:

- **PyMuPDF:** `http://placeholder.local/wasm/pymupdf/`
- **Ghostscript:** `http://placeholder.local/wasm/gs/`
- **CoherentPDF:** `http://placeholder.local/wasm/cpdf/`
- **OCR Worker:** `http://placeholder.local/wasm/ocr/worker.min.js`
- **OCR Core:** `http://placeholder.local/wasm/ocr/core`
- **OCR Lang Data:** `http://placeholder.local/wasm/ocr/lang-data`
- **OCR Font Base:** `http://placeholder.local/wasm/ocr/fonts`

Bundled OCR languages: **eng**

Bundled OCR fonts:

- **Noto Sans** -> `NotoSans-Regular.ttf`

These URLs are baked into the app at build time. The user's browser fetches
WASM files from these URLs at runtime.

## Quick Setup

Transfer this entire directory to the air-gapped network, then:

```bash
bash setup.sh
```

The setup script will:
1. Load the Docker image
2. Extract WASM packages to `./wasm/` (override with `WASM_EXTRACT_DIR`)
3. Optionally start the BentoPDF container

## Manual Setup

### 1. Load the Docker image

```bash
docker load -i bentopdf.tar
```

### 2. Extract WASM packages

Extract to your internal web server's document root:

```bash
mkdir -p ./wasm/pymupdf ./wasm/gs ./wasm/cpdf ./wasm/ocr/core ./wasm/ocr/lang-data ./wasm/ocr/fonts

# PyMuPDF
tar xzf bentopdf-pymupdf-wasm-0.11.16.tgz -C ./wasm/pymupdf --strip-components=1

# Ghostscript (extract assets/ to root)
TEMP_GS=$(mktemp -d)
tar xzf bentopdf-gs-wasm-0.1.1.tgz -C $TEMP_GS
cp -r $TEMP_GS/package/assets/* ./wasm/gs/
rm -rf $TEMP_GS

# CoherentPDF (extract dist/ to root)
TEMP_CPDF=$(mktemp -d)
tar xzf coherentpdf-2.5.5.tgz -C $TEMP_CPDF
cp -r $TEMP_CPDF/package/dist/* ./wasm/cpdf/
rm -rf $TEMP_CPDF

# Tesseract worker
TEMP_TESS=$(mktemp -d)
tar xzf tesseract.js-7.0.0.tgz -C $TEMP_TESS
cp $TEMP_TESS/package/dist/worker.min.js ./wasm/ocr/worker.min.js
rm -rf $TEMP_TESS

# Tesseract core
tar xzf tesseract.js-core-7.0.0.tgz -C ./wasm/ocr/core --strip-components=1

# OCR language data
cp ./tesseract-langdata/*.traineddata.gz ./wasm/ocr/lang-data/

# OCR fonts
cp ./ocr-fonts/* ./wasm/ocr/fonts/
```

### 3. Configure your web server

Ensure these paths are accessible at the configured URLs:

| URL | Serves From |
| --- | --- |
| `http://placeholder.local/wasm/pymupdf/` | `./wasm/pymupdf/` |
| `http://placeholder.local/wasm/gs/` | `./wasm/gs/` |
| `http://placeholder.local/wasm/cpdf/` | `./wasm/cpdf/` |
| `http://placeholder.local/wasm/ocr/worker.min.js` | `./wasm/ocr/worker.min.js` |
| `http://placeholder.local/wasm/ocr/core` | `./wasm/ocr/core/` |
| `http://placeholder.local/wasm/ocr/lang-data` | `./wasm/ocr/lang-data/` |
| `http://placeholder.local/wasm/ocr/fonts` | `./wasm/ocr/fonts/` |

### 4. Run BentoPDF

```bash
docker run -d --name bentopdf -p 3000:8080 --restart unless-stopped bentopdf
```

Open: http://localhost:3000
