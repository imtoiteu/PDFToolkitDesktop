# PDF Toolkit — Desktop App (Tauri)

A local, **fully offline** desktop build of PDF Toolkit that reuses the existing
web UI unchanged. All PDF/image processing runs on your machine — no file ever
leaves the device.

The web/LAN build is untouched: the desktop app is an additive wrapper around
the same `dist/` output, produced via a separate `--mode tauri` build path.

---

## Architecture (why it's built this way)

- **Frontend-only wrapper, no bundled backend.** Every tool already runs
  client-side (pdf-lib, pdf.js, qpdf, pdfium, tesseract.js, wasm-vips,
  Ghostscript, PyMuPDF, cpdf — all JS/WASM). There is no server to start, so the
  desktop app is just the web UI in a native window.
- **Tauri v2, not Electron.** Tauri uses the OS-native webview (WebKitGTK on
  Linux, WKWebView on macOS, WebView2 on Windows), giving a ~10 MB core binary
  instead of a bundled ~120 MB Chromium, plus native dialogs and a Rust security
  model.
- **Native "Save As".** The web UI's single `downloadFile()` helper
  (`src/js/utils/helpers.ts`, used at ~311 call sites) detects the Tauri runtime
  and routes output bytes to a Rust `save_file` command that shows a native save
  dialog and writes the file where the user chooses. In a normal browser it
  falls back to the usual blob download — no other code changed.
- **Native file picker.** The existing `<input type="file">` / drag-and-drop
  already open the OS file picker inside the webview; nothing to change.
- **Offline WASM.** Three modules (PyMuPDF, Ghostscript, cpdf) normally load
  from a CDN. The desktop build (`.env.tauri`) repoints them at the locally
  bundled copies under `/wasm/...`, which `scripts/copy-wasm-to-dist.mjs` copies
  into `dist/wasm/` at build time.
- **SharedArrayBuffer.** Several WASM modules need cross-origin isolation. The
  required `Cross-Origin-Opener-Policy` / `Cross-Origin-Embedder-Policy` headers
  are set on the Tauri asset protocol via `app.security.headers` in
  `tauri.conf.json`.
- **Service worker** auto-disables under Tauri (the app is already local).

### Files added (all additive / reversible)

```
src-tauri/                     Tauri project (Rust shell)
  tauri.conf.json              window, COOP/COEP headers, build hooks
  Cargo.toml, build.rs
  src/main.rs, src/lib.rs      save_file native command
  capabilities/default.json
  icons/                       generated from public/images/favicon-512x512.png
.env.tauri                     points WASM modules at local /wasm paths
scripts/copy-wasm-to-dist.mjs  bundles wasm/ into dist/ for offline use
.github/workflows/desktop-build.yml   macOS/Windows/Linux CI matrix
```

Plus three tiny, guarded edits: `downloadFile()` native-save branch
(`helpers.ts`), a Tauri guard in `sw-register.ts`, and mode-gated skipping of
brotli/gzip in `vite.config.ts`. None affect the web/LAN build.

---

## Commands

### Prerequisites

All platforms: **Node 20+** and **Rust 1.77+** (`cargo`; install via
<https://rustup.rs>).

- **macOS:** Xcode command-line tools — `xcode-select --install`. Builds run
  natively on Apple Silicon (arm64) and Intel (x86_64); use
  `--target aarch64-apple-darwin` / `--target x86_64-apple-darwin` to pick one.
- **Windows:** **Visual Studio Build Tools** with the *Desktop development with
  C++* workload, plus the **WebView2 Runtime** (already present on Windows 10
  21H2+ / Windows 11).
- **Linux:** WebKitGTK + supporting dev packages:
  ```bash
  sudo apt-get install -y \
    libwebkit2gtk-4.1-dev libsoup-3.0-dev librsvg2-dev \
    libappindicator3-dev patchelf
  ```

> The dev and build commands below are **identical on macOS, Windows and
> Linux** — only the prerequisites and the produced installer format differ.

### Dev (hot-reload, opens a native window)
```bash
npm install
npm run tauri:dev
```
Runs `vite` (dev server on :5173) and launches the desktop window against it.

### Build (production installers)
```bash
npm run tauri:build
```
This runs `npm run build:tauri` (frontend + offline WASM) then compiles and
bundles the native app.

Frontend-only (no native shell), e.g. for the LAN build, is unchanged:
`npm run build`.

### Output location
```
src-tauri/target/release/pdf-toolkit                     # raw binary
src-tauri/target/release/bundle/
  ├─ appimage/PDF Toolkit_2.8.5_amd64.AppImage           # Linux
  ├─ deb/PDF Toolkit_2.8.5_amd64.deb                     # Linux
  ├─ dmg/PDF Toolkit_2.8.5_*.dmg   +  macos/PDF Toolkit.app   # macOS
  └─ msi/…msi  +  nsis/…setup.exe                        # Windows
```

### Cross-platform builds
macOS and Windows **cannot** be cross-compiled from Linux (they need their own
SDKs and signing). Use the included CI workflow
(`.github/workflows/desktop-build.yml`) — run it via *Actions → Desktop build →
Run workflow*, or push a `desktop-v*` tag. It builds all three OSes on native
runners and uploads the installers as artifacts.

---

## Verifying it runs offline (no VPS / server dependency)

The desktop app has **no** dependency on the VPS/LAN URL or any external server
for its core features. To prove it:

1. **Static check** — no VPS/server host is baked in. All processing is
   client-side WASM/JS; the desktop build repoints the three CDN-loaded modules
   at local `/wasm/...` paths via `.env.tauri`:
   ```bash
   grep -rn "VITE_WASM_\|VITE_TESSERACT_" .env.tauri   # all point at /wasm/...
   ```
2. **Runtime check** — launch the app, open DevTools (dev build:
   `npm run tauri:dev` → right-click → Inspect), go to the **Network** tab, and
   run a tool (Merge, Compress, OCR…). You should see **no** requests to
   `cdn.jsdelivr.net` or any remote host — only `tauri://` / `asset://` /
   `http://tauri.localhost` loads.
3. **Airplane-mode check** — fully disconnect the network and repeat the smoke
   test below. Every core tool still works.

The only two features that reach the network *by design* are trusted-timestamp
(TSA) signing and on-demand CJK/Noto font download; neither runs unless you
explicitly use them.

---

## Troubleshooting

| Symptom | Cause / Fix |
| --- | --- |
| `cargo: command not found` | Install Rust: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \| sh`, then restart the shell. |
| Linux: `error: failed to run custom build command for 'webkit2gtk-sys'` or `Package webkit2gtk-4.1 was not found` | Install the WebKitGTK dev packages (see Prerequisites): `sudo apt-get install -y libwebkit2gtk-4.1-dev libsoup-3.0-dev librsvg2-dev libappindicator3-dev patchelf`. |
| Windows: build fails linking / `link.exe not found` | Install **Visual Studio Build Tools** with the *Desktop development with C++* workload, and the **WebView2 Runtime** (preinstalled on Win 10/11 21H2+). |
| macOS: `xcrun: error: invalid active developer path` | Install command-line tools: `xcode-select --install`. |
| A WASM tool fails with a 404 / network error | `dist/wasm/` is missing. Run `npm run build:tauri` (it runs `scripts/copy-wasm-to-dist.mjs`) before `tauri build`, or use `npm run tauri:build` which chains both. |
| Blank/white window on launch | Stale `dist/`. Delete `dist/` and rebuild with `npm run build:tauri`. In dev, make sure the Vite dev server on `:5173` is up (started automatically by `npm run tauri:dev`). |
| Cross-OS build fails from Linux | Expected — macOS/Windows installers can't be cross-compiled. Use the CI workflow (`.github/workflows/desktop-build.yml`) on native runners. |
| SharedArrayBuffer / cross-origin isolation errors | The COOP/COEP headers come from `app.security.headers` in `tauri.conf.json`; don't remove them. |

---

## Known limitations

- **Bundle size (~250–300 MB).** Offline OCR (tesseract + language data),
  PyMuPDF/Pyodide, Ghostscript and LibreOffice-WASM are all bundled. This is the
  cost of "works fully offline." To shrink, drop unused modules from `wasm/` and
  the corresponding `.env.tauri` entries.
- **No code signing / notarization.** Installers are unsigned, so macOS
  Gatekeeper / Windows SmartScreen will warn on first launch. Add signing certs
  in the CI workflow for distribution.
- **Two features stay online-only (by design):** trusted-timestamp (TSA) signing
  and on-demand CJK/Noto font download. Everything else is fully offline.
- **Webview differences.** Rendering uses each OS's webview, so rare
  visual/behavioral differences vs. Chrome are possible (esp. WebKitGTK).
- **Large-file save** passes bytes over the Tauri IPC; multi-hundred-MB outputs
  save a little slower than a browser blob download.
- **`msa-pdf.tar` and the Docker/nginx files are not used** by the desktop app —
  they belong to the LAN/container deployment.

---

## Smoke test checklist

Run `npm run tauri:dev` (or launch a built binary) and verify:

- [ ] App opens in a native window titled "PDF Toolkit"; homepage renders with
      sidebar categories and the VI/EN switcher.
- [ ] **Offline:** disconnect the network — the app still loads and tools work.
- [ ] Language switch VI ⇄ EN works and persists after restart.
- [ ] **Merge PDF** (pdf-lib): add 2+ PDFs → merge → native Save dialog appears →
      file is written to the chosen location and opens correctly.
- [ ] **JPG → PDF** (image pipeline): pick images via the OS picker → convert →
      save.
- [ ] **Compress PDF** (Ghostscript WASM): confirms local `/wasm/gs/` loads (no
      network request).
- [ ] **PDF → PNG / rasterize** (PyMuPDF WASM): confirms local `/wasm/pymupdf/`.
- [ ] **Encrypt/Decrypt** (qpdf WASM): set a password, then remove it.
- [ ] **OCR PDF** (tesseract): confirms local `/wasm/ocr/` core + `eng`
      language data load offline.
- [ ] Cancelling the native Save dialog leaves no file and shows no error.
- [ ] Open a second tool page and confirm navigation between pages works.
- [ ] DevTools console (dev build) shows no failed network requests to
      `cdn.jsdelivr.net` during core tool use.
