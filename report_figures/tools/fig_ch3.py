#!/usr/bin/env python3
"""Sinh các hình chương 3 — Xây dựng và triển khai hệ thống."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagramlib import Scene, emit  # noqa: E402
from fig_ch2 import seq  # noqa: E402

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ================================================================= Hình 3.1
def fig_3_1():
    sc = Scene("Hình 3.1 - Cấu trúc mã nguồn và môi trường phát triển",
               1180, 860)
    sc.node("root", 420, 30, 340, 50, "PDFToolkitDesktop/",
            kind="ui", shape="round", font_size=14, bold=True)

    cols = [
        ("c1", 30, "src/", "ui", [
            "js/logic — 132 mô-đun nghiệp vụ (47.499 dòng)",
            "js/utils — 43 mô-đun tiện ích (9.281 dòng)",
            "js/workflow — engine + 79 nút (8.484 dòng)",
            "js/compare — so sánh tài liệu (2.897 dòng)",
            "js/types — 69 tệp khai báo kiểu",
            "js/config, js/i18n, js/handlers",
            "pages/ — 117 trang công cụ HTML",
            "partials/ — navbar, footer, modal",
            "css/ — Tailwind 4 + CSS riêng",
            "tests/ — 39 tệp kiểm thử Vitest",
        ]),
        ("c2", 320, "src-tauri/", "native", [
            "src/main.rs — điểm vào tiến trình",
            "src/lib.rs — lệnh save_file",
            "tauri.conf.json — cửa sổ, COOP/COEP",
            "capabilities/default.json",
            "Cargo.toml — tauri 2, plugin-dialog",
            "build.rs — tauri_build::build()",
            "icons/ — sinh từ favicon-512",
        ]),
        ("c3", 610, "wasm/  +  public/", "engine", [
            "wasm/pymupdf — Pyodide 54 MB",
            "wasm/ocr — Tesseract core + eng 47 MB",
            "wasm/gs — Ghostscript 15 MB",
            "wasm/cpdf — CoherentPDF 6 MB",
            "public/qpdf.wasm — 1,3 MB",
            "public/workers/ — 8 Web Worker",
            "public/locales/ — 21 ngôn ngữ",
            "public/pdfjs-viewer, embedpdf",
        ]),
        ("c4", 900, "cấu hình & kịch bản", "accent", [
            "vite.config.ts — 802 dòng, 131 điểm vào",
            "vitest.config.ts, tsconfig.json",
            "eslint.config.mjs — security + no-unsanitized",
            "scripts/ — 13 kịch bản Node",
            ".env.tauri — trỏ WASM về /wasm",
            ".github/workflows/ — 9 quy trình CI",
            "Dockerfile* — chỉ cho bản LAN/web",
            "docs/ — VitePress",
        ]),
    ]
    for cid, x, title, kind, items in cols:
        h = 60 + len(items) * 44
        sc.group(cid, x, 130, 250, h, "", kind)
        sc.node(cid + "_h", x + 15, 145, 220, 44, title, kind=kind,
                shape="round", font_size=13, bold=True)
        sc.edge("root", cid + "_h", exit="s", entry="n", color="#4F46E5")
        y = 200
        for it in items:
            sc.node(f"{cid}_{y}", x + 15, y, 220, 38, it, kind="neutral",
                    shape="rect", font_size=10)
            y += 44

    sc.node("env", 30, 720, 1120, 100,
            "Môi trường phát triển đã kiểm chứng từ cấu hình dự án:  "
            "Node.js ≥ 20 (CI dùng 20)  ·  npm  ·  Rust ≥ 1.77.2 (rust-version "
            "trong Cargo.toml)  ·  Vite 8  ·  TypeScript 5.9  ·  Vitest 4  ·  "
            "Tauri CLI 2\n\n"
            "Phụ thuộc hệ thống theo nền tảng:  Linux — libwebkit2gtk-4.1-dev, "
            "libsoup-3.0-dev, librsvg2-dev, libappindicator3-dev, patchelf   |   "
            "Windows — Visual Studio Build Tools (C++) + WebView2 Runtime   |   "
            "macOS — Xcode Command Line Tools",
            kind="accent", shape="round", font_size=11)
    return emit(sc, "fig_3_1_source_tree", OUT)


# ================================================================= Hình 3.2
def fig_3_2():
    sc = Scene("Hình 3.2 - Khuôn mẫu hiện thực một công cụ", 1160, 800)

    sc.group("g1", 40, 40, 1080, 190,
             "Bước 1 — Trang HTML tĩnh (khuôn mẫu chung cho 117 trang công cụ)",
             "ui")
    items = [
        ("h1", 66, "navbar / footer\n(Handlebars partial)"),
        ("h2", 276, "#drop-zone\n+ #file-input"),
        ("h3", 486, "#tool-options\n(tham số riêng)"),
        ("h4", 696, "#process-btn\n+ #loader-modal"),
        ("h5", 906, "#alert-modal\n+ #back-to-tools"),
    ]
    for nid, x, label in items:
        sc.node(nid, x, 100, 190, 66, label, kind="ui", shape="round",
                font_size=11)
    sc.node("i18nattr", 66, 178, 1030, 38,
            "Mọi nhãn mang thuộc tính data-i18n=\"tools:<tên công cụ>.<khoá>\" "
            "để applyTranslations() thay thế văn bản khi đổi ngôn ngữ",
            kind="accent", shape="rect", font_size=11)

    sc.group("g2", 40, 260, 1080, 250,
             "Bước 2 — Mô-đun nghiệp vụ src/js/logic/<tool>-page.ts", "logic")
    l = [
        ("m1", 66, "DOMContentLoaded\nđăng ký sự kiện", 190),
        ("m2", 276, "handleFileSelect()\nlọc MIME / phần mở rộng", 190),
        ("m3", 486, "updateUI()\nhiển thị tệp, bật tham số", 190),
        ("m4", 696, "process()\nthực thi phép biến đổi", 190),
        ("m5", 906, "resetState()\ngiải phóng, dọn giao diện", 190),
    ]
    for nid, x, label, w in l:
        sc.node(nid, x, 320, w, 66, label, kind="logic", shape="round",
                font_size=11)
    for a, b in zip([x[0] for x in l], [x[0] for x in l][1:]):
        sc.edge(a, b, exit="e", entry="w", style="straight")
    sc.node("state2", 66, 400, 500, 44,
            "Trạng thái cục bộ của trang (pageState) hoặc state dùng chung "
            "trong src/js/state.ts",
            kind="data", shape="rect", font_size=11)
    sc.node("guard", 596, 400, 500, 44,
            "Kiểm tra tiền điều kiện: tệp hợp lệ, tham số bắt buộc, "
            "mô-đun WASM đã cấu hình",
            kind="warn", shape="rect", font_size=11)

    sc.group("g3", 40, 540, 1080, 230,
             "Bước 3 — Gọi tiện ích dùng chung và động cơ xử lý", "engine")
    u = [
        ("u1", 66, "batchDecryptIfNeeded()\nxử lý tệp có mật khẩu"),
        ("u2", 276, "loadPdfDocument() /\ngetPDFDocument()"),
        ("u3", 486, "phép biến đổi:\npdf-lib · qpdf · cpdf · PyMuPDF"),
        ("u4", 696, "new Blob([bytes])\n+ deduplicateFileName()"),
        ("u5", 906, "downloadFile()\n→ save_file (Tauri)"),
    ]
    for nid, x, label in u:
        sc.node(nid, x, 600, 190, 66, label, kind="engine", shape="round",
                font_size=11)
    for a, b in zip([x[0] for x in u], [x[0] for x in u][1:]):
        sc.edge(a, b, exit="e", entry="w", style="straight")
    sc.node("obs", 66, 682, 1030, 60,
            "Phản hồi cho người dùng trong suốt quá trình: showLoader(text) → "
            "cập nhật văn bản theo từng bước → hideLoader() → "
            "showAlert(title, message, type, callback)",
            kind="ui", shape="rect", font_size=11)

    sc.edge("h4", "m4", exit="s", entry="n", color="#4F46E5",
            label="sự kiện click")
    sc.edge("m4", "u1", exit="s", entry="n", color="#059669",
            waypoints=[(791, 470), (161, 470)])
    return emit(sc, "fig_3_2_tool_template", OUT)


# ================================================================= Hình 3.3
def fig_3_3():
    sc = Scene("Hình 3.5 - Cơ chế lưu tệp native", 1140, 700)

    sc.group("web", 40, 40, 520, 420, "Ngữ cảnh WebView (JavaScript)", "ui")
    sc.node("op", 70, 100, 460, 56,
            "Mô-đun nghiệp vụ sinh Blob kết quả",
            kind="logic", shape="round")
    sc.node("dl", 70, 176, 460, 56, "downloadFile(blob, filename)",
            sub="src/js/utils/helpers.ts — ~311 điểm gọi",
            kind="accent", shape="round")
    sc.node("det", 60, 246, 480, 84, "isTauriRuntime()",
            sub="__TAURI_INTERNALS__ / __TAURI__", kind="data",
            shape="diamond", font_size=11)
    sc.node("br", 70, 340, 220, 96,
            "browserDownload()\n<a download> + createObjectURL + "
            "revokeObjectURL",
            kind="neutral", shape="round", font_size=11)
    sc.node("tv", 310, 340, 220, 96,
            "tauriSaveFile()\nblob.arrayBuffer() → Uint8Array → "
            "invoke('save_file')",
            kind="ui", shape="round", font_size=11)

    sc.group("rust", 600, 40, 500, 420, "Ngữ cảnh Rust (tiến trình native)",
             "native")
    sc.node("cmd", 630, 100, 440, 60, "#[tauri::command] async fn save_file",
            sub="tham số: filename: String, bytes: Vec<u8>",
            kind="native", shape="round")
    sc.node("dlg", 630, 180, 440, 60, "app.dialog().file()",
            sub=".set_file_name(&filename).blocking_save_file()",
            kind="native", shape="round")
    sc.node("res", 630, 260, 440, 60, "Người dùng chọn vị trí?",
            kind="data", shape="diamond", font_size=11)
    sc.node("wr", 630, 340, 210, 96, "std::fs::write(path, bytes)\n→ Ok(true)",
            kind="native", shape="round", font_size=11)
    sc.node("cancel", 860, 340, 210, 96, "None → Ok(false)\n(huỷ, không phải lỗi)",
            kind="warn", shape="round", font_size=11)

    sc.node("cap", 40, 500, 1060, 60,
            "capabilities/default.json chỉ khai báo quyền core:default — WebView "
            "KHÔNG có quyền fs hay dialog; toàn bộ tương tác với hệ tệp phải đi "
            "qua đúng một lệnh Rust duy nhất",
            kind="warn", shape="round", font_size=11)
    sc.node("fb", 40, 580, 1060, 60,
            "Cơ chế dự phòng: nếu invoke('save_file') ném lỗi, tauriSaveFile() "
            "ghi log và gọi lại browserDownload() để kết quả không bị mất",
            kind="accent", shape="round", font_size=11)

    sc.edge("op", "dl", exit="s", entry="n", style="straight")
    sc.edge("dl", "det", exit="s", entry="n", style="straight")
    sc.edge("det", "br", "Không", exit="w", entry="n",
            waypoints=[(180, 288)], color="#475569")
    sc.edge("det", "tv", "Có", exit="e", entry="n",
            waypoints=[(420, 288)], color="#4F46E5")
    sc.edge("tv", "cmd", "IPC Tauri", exit="e", entry="w",
            waypoints=[(570, 388), (570, 130)], color="#4F46E5")
    sc.edge("cmd", "dlg", exit="s", entry="n", style="straight")
    sc.edge("dlg", "res", exit="s", entry="n", style="straight")
    sc.edge("res", "wr", "Có", exit="s", entry="n",
            waypoints=[(850, 330), (735, 330)], color="#059669")
    sc.edge("res", "cancel", "Không", exit="e", entry="n",
            waypoints=[(1090, 290), (1090, 320), (965, 320)], color="#DC2626")
    return emit(sc, "fig_3_5_native_save", OUT)


# ================================================================= Hình 3.4
def fig_3_4():
    sc = Scene("Hình 3.7 - Giải quyết nguồn mô-đun WASM", 1160, 800)

    sc.node("build", 40, 40, 380, 96, "Thời điểm biên dịch",
            sub="vite build --mode tauri nạp .env.tauri",
            kind="accent", shape="round", font_size=13, bold=True)
    sc.node("envv", 40, 150, 380, 170,
            "VITE_WASM_PYMUPDF_URL=/wasm/pymupdf/\n"
            "VITE_WASM_GS_URL=/wasm/gs/\n"
            "VITE_WASM_CPDF_URL=/wasm/cpdf/\n"
            "VITE_TESSERACT_WORKER_URL=/wasm/ocr/worker.min.js\n"
            "VITE_TESSERACT_CORE_URL=/wasm/ocr/core\n"
            "VITE_TESSERACT_LANG_URL=/wasm/ocr/lang-data\n"
            "VITE_OCR_FONT_BASE_URL=/wasm/ocr/fonts",
            kind="data", shape="note", font_size=10, align="left")

    sc.node("wp", 450, 40, 320, 96, "WasmProviderManager",
            sub="src/js/utils/wasm-provider.ts",
            kind="logic", shape="round", font_size=13, bold=True)
    sc.node("order", 450, 150, 320, 170,
            "Thứ tự ưu tiên khi lấy URL:\n"
            "1. Giá trị người dùng đặt trong localStorage\n"
            "     (khoá bentopdf:wasm-providers)\n"
            "2. Giá trị ENV_DEFAULTS từ biến VITE_*\n"
            "3. CDN_DEFAULTS (jsDelivr) — chỉ bản web\n\n"
            "Mọi URL phải thuộc BUILTIN_TRUSTED_HOSTS,\n"
            "nếu không sẽ bị loại và ghi cảnh báo.",
            kind="neutral", shape="note", font_size=10, align="left")

    sc.node("loaders", 800, 40, 320, 96, "Các bộ nạp chuyên biệt",
            sub="pymupdf-loader · ghostscript-loader · cpdf-helper · "
                "tesseract-runtime · libreoffice-loader",
            kind="engine", shape="round", font_size=13, bold=True)
    sc.node("cache", 800, 150, 320, 170,
            "Mỗi bộ nạp giữ một thể hiện singleton\nvà một loadPromise dùng "
            "chung để tránh\nnạp trùng khi nhiều thao tác cùng gọi.\n\n"
            "cpdf-helper nạp bằng thẻ <script>;\nmerge.worker.js nạp bằng "
            "importScripts().",
            kind="neutral", shape="note", font_size=10, align="left")

    sc.node("disk", 40, 370, 1080, 110,
            "dist/wasm/ được đóng gói vào ứng dụng bởi scripts/copy-wasm-to-dist.mjs\n\n"
            "pymupdf/ (54 MB — Pyodide, numpy, opencv, pymupdf, pdf2docx, "
            "python-docx)   ·   ocr/ (47 MB — 8 biến thể tesseract-core, "
            "eng.traineddata.gz, NotoSans)   ·   gs/ (15 MB)   ·   cpdf/ (6 MB)",
            kind="data", shape="round", font_size=11)

    sc.node("coop", 40, 510, 530, 118,
            "Yêu cầu cách ly nguồn gốc\n\n"
            "tauri.conf.json → app.security.headers đặt\n"
            "Cross-Origin-Opener-Policy: same-origin\n"
            "Cross-Origin-Embedder-Policy: require-corp\n"
            "→ SharedArrayBuffer khả dụng cho các mô-đun WASM đa luồng",
            kind="native", shape="round", font_size=11)
    sc.node("gate", 600, 510, 520, 118,
            "Cổng kiểm tra trước khi chạy\n\n"
            "requireWasm(pkg) → WasmProvider.isConfigured(pkg)\n"
            "Nếu thiếu: showWasmRequiredDialog() liệt kê các tính năng phụ "
            "thuộc và mở trang wasm-settings.html",
            kind="warn", shape="round", font_size=11)

    sc.node("net", 40, 650, 1080, 110,
            "Kết luận về phụ thuộc mạng của bản desktop\n\n"
            "Không có yêu cầu mạng nào cho các thao tác lõi. Hai tính năng duy "
            "nhất chủ động dùng mạng: (1) đóng dấu thời gian RFC 3161 tới máy "
            "chủ TSA do người dùng chọn; (2) tải phông chữ CJK/Noto theo yêu "
            "cầu khi OCR ngôn ngữ tương ứng. Cả hai chỉ chạy khi người dùng "
            "trực tiếp kích hoạt.",
            kind="ui", shape="round", font_size=11)

    sc.edge("build", "wp", exit="e", entry="w", style="straight")
    sc.edge("wp", "loaders", exit="e", entry="w", style="straight")
    sc.edge("envv", "order", exit="e", entry="w", style="straight", dashed=True,
            arrow="none")
    sc.edge("order", "cache", exit="e", entry="w", style="straight",
            dashed=True, arrow="none")
    sc.edge("loaders", "disk", exit="s", entry="n",
            waypoints=[(970, 350)], color="#EA580C")
    sc.edge("disk", "coop", exit="s", entry="n",
            waypoints=[(305, 495)], color="#334155")
    sc.edge("disk", "gate", exit="s", entry="n",
            waypoints=[(860, 495)], color="#DC2626")
    return emit(sc, "fig_3_7_wasm_resolution", OUT)


# ================================================================= Hình 3.5
def fig_3_5():
    sc = Scene("Hình 3.9 - Quy trình hiện thực OCR", 1160, 900)
    steps = [
        ("s1", 40, "createConfiguredTesseractWorker(language, OEM=1, logger)",
         "engine", "assertTesseractLanguagesAvailable() kiểm tra ngôn ngữ khả dụng; "
                   "buildTesseractWorkerOptions() yêu cầu cả ba biến worker/core/lang "
                   "phải được đặt cùng nhau"),
        ("s2", 120, "setParameters({tessedit_pageseg_mode, tessedit_char_whitelist})",
         "engine", "PSM mặc định AUTO; danh sách ký tự cho phép do người dùng nhập"),
        ("s3", 200, "Nạp phông theo ngôn ngữ — getFontForLanguage()",
         "accent", "languageToFontFamily ánh xạ ngôn ngữ sang họ phông; tách riêng "
                   "phông Latin khi trộn chữ Latin với CJK/Ấn/Ả Rập; dự phòng Helvetica"),
        ("s4", 280, "Vòng lặp từng trang: pdfjs.getPage(i).render(scale = resolution)",
         "logic", "Kết xuất trang ra canvas theo độ phân giải người dùng chọn"),
        ("s5", 360, "binarizeCanvas() — tuỳ chọn nhị phân hoá ngưỡng 128",
         "logic", "Độ sáng = 0,299R + 0,587G + 0,114B"),
        ("s6", 440, "recognizeWithTimeout(worker, canvas, 5 phút/trang)",
         "engine", "Trả về text và hOCR; quá hạn được ghi thành cảnh báo thay vì huỷ "
                   "toàn bộ tài liệu"),
        ("s7", 520, "parseHocrDocument() + scaleOcrPageToPdfPoints()",
         "logic", "Chuyển toạ độ hộp bao từ điểm ảnh sang điểm PDF"),
        ("s8", 600, "copyPages() trang gốc sang tài liệu mới (pdf-lib)",
         "engine", "Giữ nguyên hình ảnh gốc, không kết xuất lại"),
        ("s9", 680, "drawOcrTextLayer() — vẽ từng từ với opacity = 0",
         "engine", "Tính góc xoay từ textangle và độ dốc đường cơ sở; chèn dấu cách "
                   "khi injectWordBreaks; đảo thứ tự từ với dòng RTL"),
        ("s10", 760, "Dọn dẹp và lưu: canvas 0×0, page.cleanup(), pdf.cleanup() "
                     "mỗi 25 trang, worker.terminate()",
         "warn", "Bảo đảm bộ nhớ không tăng tuyến tính với tài liệu nhiều trang"),
    ]
    for nid, y, label, kind, note in steps:
        sc.node(nid, 40, y, 560, 64, label, kind=kind, shape="round",
                font_size=11)
        sc.node(nid + "_n", 630, y, 490, 64, note, kind="neutral",
                shape="note", font_size=10)
        sc.edge(nid, nid + "_n", exit="e", entry="w", style="straight",
                arrow="none", color="#CBD5E1")
    order = [s[0] for s in steps]
    for a, b in zip(order, order[1:]):
        sc.edge(a, b, exit="s", entry="n", style="straight")

    sc.node("warn", 40, 840, 1080, 46,
            "OcrResult trả về kèm mảng warnings[] gồm bốn loại: "
            "recognize-timeout · recognize-error · draw-error · page-error — "
            "được hiển thị cho người dùng sau khi xử lý",
            kind="warn", shape="round", font_size=11)
    sc.edge("s10", "warn", exit="s", entry="n", style="straight",
            color="#DC2626")
    return emit(sc, "fig_3_9_ocr_pipeline", OUT)


# ================================================================= Hình 3.6
def fig_3_6():
    sc = Scene("Hình 3.8 - Hai chiến lược nén PDF", 1160, 720)
    sc.node("in", 430, 40, 300, 56, "Tệp PDF đầu vào + mức nén đã chọn",
            kind="ui", shape="round", font_size=12, bold=True)

    sc.group("g1", 40, 130, 530, 470,
             "Chiến lược 1 — Condense (PyMuPDF, giữ văn bản)", "engine")
    sc.node("a1", 66, 180, 478, 50, "performCondenseCompression(blob, level)",
            kind="engine", shape="round", font_size=11)
    sc.node("a2", 66, 244, 478, 130,
            "Bảng tham số CONDENSE_PRESETS\n\n"
            "light        chất lượng 90 · DPI đích 150 · ngưỡng 200\n"
            "balanced   chất lượng 75 · DPI đích 96 · ngưỡng 150\n"
            "aggressive chất lượng 50 · DPI đích 72 · ngưỡng 100\n"
            "extreme    chất lượng 30 · DPI đích 60 · ngưỡng 96",
            kind="neutral", shape="note", font_size=10, align="left")
    sc.node("a3", 66, 388, 478, 76,
            "Thao tác: lấy mẫu lại ảnh nhúng, tuỳ chọn chuyển xám, gỡ siêu dữ "
            "liệu và ảnh thu nhỏ, tạo tập con phông (subsetFonts)",
            kind="engine", shape="round", font_size=11)
    sc.node("a4", 66, 478, 478, 76,
            "Lưu với garbage = 4, deflate, clean, useObjstms\n"
            "Nếu lỗi: thử lại với images.enabled = false và đánh dấu "
            "usedFallback",
            kind="warn", shape="round", font_size=11)

    sc.group("g2", 600, 130, 520, 470,
             "Chiến lược 2 — Photon (kết xuất lại thành ảnh)", "logic")
    sc.node("b1", 626, 180, 468, 50, "performPhotonCompression(buffer, level)",
            kind="logic", shape="round", font_size=11)
    sc.node("b2", 626, 244, 468, 130,
            "Bảng tham số PHOTON_PRESETS\n\n"
            "light        tỉ lệ 2,00 · chất lượng JPEG 0,85\n"
            "balanced   tỉ lệ 1,50 · chất lượng JPEG 0,65\n"
            "aggressive tỉ lệ 1,20 · chất lượng JPEG 0,45\n"
            "extreme    tỉ lệ 1,00 · chất lượng JPEG 0,25",
            kind="neutral", shape="note", font_size=10, align="left")
    sc.node("b3", 626, 388, 468, 76,
            "Mỗi trang: pdf.js render → canvas → canvas.toBlob('image/jpeg') → "
            "pdf-lib embedJpg + drawImage",
            kind="logic", shape="round", font_size=11)
    sc.node("b4", 626, 478, 468, 76,
            "Giải phóng canvas ngay sau mỗi trang (width = height = 0)\n"
            "Hệ quả: mất lớp văn bản, tài liệu trở thành ảnh",
            kind="warn", shape="round", font_size=11)

    for a, b in [("a1", "a2"), ("a2", "a3"), ("a3", "a4")]:
        sc.edge(a, b, exit="s", entry="n", style="straight")
    for a, b in [("b1", "b2"), ("b2", "b3"), ("b3", "b4")]:
        sc.edge(a, b, exit="s", entry="n", style="straight")
    sc.edge("in", "a1", exit="s", entry="n", waypoints=[(305, 155)],
            color="#EA580C", label="giữ được văn bản")
    sc.edge("in", "b1", exit="s", entry="n", waypoints=[(860, 155)],
            color="#059669", label="ưu tiên giảm dung lượng")

    sc.node("out", 380, 630, 400, 56,
            "So sánh dung lượng trước / sau và tải xuống kết quả",
            kind="ui", shape="round", font_size=12, bold=True)
    sc.edge("a4", "out", exit="s", entry="w", waypoints=[(305, 610)],
            color="#475569")
    sc.edge("b4", "out", exit="s", entry="e", waypoints=[(860, 610)],
            color="#475569")
    return emit(sc, "fig_3_8_compression", OUT)


# ================================================================= Hình 3.7
def fig_3_7():
    sc = Scene("Hình 3.11 - Quản lý dữ liệu tạm và bộ nhớ", 1160, 760)

    sc.node("src", 40, 40, 260, 70, "Tệp người dùng chọn",
            sub="đối tượng File của trình duyệt", kind="data", shape="round")
    sc.node("ab", 340, 40, 260, 70, "ArrayBuffer / Uint8Array",
            sub="file.arrayBuffer()", kind="data", shape="round")
    sc.node("blob", 640, 40, 260, 70, "Blob kết quả",
            sub="application/pdf, image/*, application/zip",
            kind="data", shape="round")
    sc.node("save", 940, 40, 180, 70, "Ghi ra đĩa",
            sub="chỉ ở bước cuối", kind="native", shape="round")
    sc.edge("src", "ab", exit="e", entry="w", style="straight")
    sc.edge("ab", "blob", exit="e", entry="w", style="straight",
            label="xử lý")
    sc.edge("blob", "save", exit="e", entry="w", style="straight")

    rows = [
        ("r1", "Hệ tệp ảo MEMFS của qpdf",
         "FS.writeFile('/input.pdf') → callMain() → FS.readFile('/output.pdf')",
         "Khối finally gọi FS.unlink() cho cả hai đường dẫn, kể cả khi qpdf ném "
         "ngoại lệ; thể hiện qpdf được giữ singleton nên chỉ nạp một lần"),
        ("r2", "Hệ tệp ảo của Ghostscript",
         "cùng khuôn mẫu MEMFS cho chuyển PDF/A và chuyển phông thành đường nét",
         "Mô-đun được lưu trong cachedGsModule để tái sử dụng giữa các lần gọi"),
        ("r3", "Hệ tệp ảo Pyodide của PyMuPDF",
         "Blob được nạp trực tiếp vào Python; document.close() sau mỗi thao tác",
         "Bộ nạp giữ cachedPyMuPDF và loadPromise để tránh khởi tạo lại Pyodide"),
        ("r4", "Canvas kết xuất trang",
         "canvas.width = canvas.height = 0 ngay sau khi dùng xong",
         "Áp dụng trong OCR, nén Photon, PDF → ảnh, sinh ảnh thu nhỏ"),
        ("r5", "Đối tượng CoherentPDF",
         "coherentpdf.deletePdf() cho mọi tài liệu đã nạp trong merge.worker.js",
         "Bộ nhớ WASM của cpdf không được thu gom tự động nên phải giải phóng tường minh"),
        ("r6", "Chuyển quyền sở hữu bộ đệm",
         "postMessage(message, [transferable]) khi gửi dữ liệu sang Web Worker",
         "Tránh nhân đôi bộ nhớ với tệp lớn; bộ đệm gốc trở nên không dùng được"),
        ("r7", "Đối tượng URL tạm",
         "URL.createObjectURL() luôn đi kèm URL.revokeObjectURL()",
         "Dùng trong nhánh tải xuống của trình duyệt và khi xem trước tài liệu"),
    ]
    y = 150
    for nid, title, how, why in rows:
        sc.node(nid, 40, y, 280, 76, title, kind="engine", shape="round",
                font_size=11, bold=True)
        sc.node(nid + "_h", 340, y, 380, 76, how, kind="neutral",
                shape="rect", font_size=10)
        sc.node(nid + "_w", 740, y, 380, 76, why, kind="accent",
                shape="rect", font_size=10)
        sc.edge(nid, nid + "_h", exit="e", entry="w", style="straight",
                arrow="none", color="#CBD5E1")
        sc.edge(nid + "_h", nid + "_w", exit="e", entry="w", style="straight",
                arrow="none", color="#CBD5E1")
        y += 84

    sc.text(580, 130, "Cơ chế", size=11, bold=True, anchor="middle",
            color="#334155")
    sc.text(930, 130, "Lý do và phạm vi áp dụng", size=11, bold=True,
            anchor="middle", color="#334155")
    sc.text(180, 130, "Vùng dữ liệu tạm", size=11, bold=True, anchor="middle",
            color="#334155")
    return emit(sc, "fig_3_11_temp_data", OUT)


# ================================================================= Hình 3.8
def fig_3_8():
    sc = Scene("Hình 3.12 - Luồng xử lý lỗi", 1160, 800)
    sc.node("op", 430, 40, 300, 56, "Thao tác đang thực thi",
            kind="ui", shape="round", font_size=13, bold=True)

    cats = [
        ("c1", 30, "Lỗi đầu vào", "warn",
         "Không có tệp · sai định dạng · tham số bắt buộc để trống",
         "showAlert('No File' / 'Input Required') trước khi bắt đầu xử lý"),
        ("c2", 315, "Tệp có mật khẩu", "accent",
         "pdf.js ném PasswordException; cpdf/PyMuPDF báo xác thực thất bại",
         "Hộp thoại nhập mật khẩu đơn lẻ hoặc theo lô; nhớ mật khẩu trong phiên"),
        ("c3", 600, "Thiếu mô-đun WASM", "engine",
         "WasmProvider.isConfigured() trả về false hoặc tải tệp thất bại",
         "showWasmRequiredDialog() nêu rõ các tính năng phụ thuộc và lối cấu hình"),
        ("c4", 885, "Lỗi trong quá trình xử lý", "logic",
         "Ngoại lệ từ qpdf/cpdf/PyMuPDF, lỗi Web Worker, quá hạn OCR",
         "try/catch bao quanh thao tác; hideLoader(); showAlert với thông điệp "
         "đã chuẩn hoá"),
    ]
    for nid, x, title, kind, when, how in cats:
        sc.node(nid, x, 150, 250, 56, title, kind=kind, shape="round",
                font_size=12, bold=True)
        sc.node(nid + "_w", x, 220, 250, 110, when, kind="neutral",
                shape="note", font_size=10)
        sc.node(nid + "_h", x, 344, 250, 120, how, kind="neutral",
                shape="rect", font_size=10)
        sc.edge("op", nid, exit="s", entry="n", color="#4F46E5")
        sc.edge(nid, nid + "_w", exit="s", entry="n", style="straight",
                arrow="none", color="#CBD5E1")
        sc.edge(nid + "_w", nid + "_h", exit="s", entry="n", style="straight",
                arrow="none", color="#CBD5E1")

    sc.node("norm", 30, 500, 1105, 66,
            "Chuẩn hoá thông điệp: normalizeErrorMessage() trong pdf-decrypt.ts "
            "bóc tách Pdf.PDFError(\"…\") của CoherentPDF và phần đuôi "
            "ERROR: … của các mô-đun khác thành câu ngắn gọn cho người dùng",
            kind="accent", shape="round", font_size=11)
    sc.node("clean", 30, 582, 545, 90,
            "Dọn dẹp bắt buộc trong khối finally\n\n"
            "hideLoader() · FS.unlink() · worker.terminate() · document.close() "
            "· deletePdf() · giải phóng canvas",
            kind="engine", shape="round", font_size=11)
    sc.node("log", 600, 582, 535, 90,
            "Ghi vết cục bộ\n\n"
            "console.error / console.warn / console.info với tiền tố mô-đun "
            "([PDF Decrypt], [WasmProvider], [SW], [CPDF]); không có nhật ký "
            "phía máy chủ",
            kind="neutral", shape="round", font_size=11)
    sc.node("fb", 30, 692, 1105, 70,
            "Cơ chế suy giảm nhẹ nhàng: giải mã thử CoherentPDF rồi PyMuPDF · "
            "nén thử có ảnh rồi không ảnh · phông thất bại thì dùng Helvetica · "
            "lưu native thất bại thì quay về tải xuống kiểu trình duyệt · "
            "OCR quá hạn ở một trang không làm hỏng cả tài liệu",
            kind="ui", shape="round", font_size=11)

    for c in ("c1", "c2", "c3", "c4"):
        sc.edge(c + "_h", "norm", exit="s", entry="n", dashed=True,
                color="#94A3B8")
    sc.edge("norm", "clean", exit="s", entry="n", waypoints=[(302, 574)],
            color="#475569")
    sc.edge("norm", "log", exit="s", entry="n", waypoints=[(867, 574)],
            color="#475569")
    return emit(sc, "fig_3_12_error_handling", OUT)


# ================================================================= Hình 3.9
def fig_3_9():
    sc = Scene("Hình 3.13 - Quy trình biên dịch và đóng gói", 1160, 800)
    chain = [
        ("p1", 40, "npm run tauri:build", "ui",
         "Kích hoạt beforeBuildCommand khai báo trong tauri.conf.json"),
        ("p2", 40, "npm run build:tauri", "logic",
         "vite build --mode tauri  →  nạp .env.tauri, bỏ qua nén brotli/gzip"),
        ("p3", 40, "tsc + Vite: 131 điểm vào HTML", "logic",
         "14 trang gốc + 117 trang công cụ; Tailwind, Handlebars partial, "
         "node polyfill (buffer, stream, util, zlib, process)"),
        ("p4", 40, "node scripts/copy-wasm-to-dist.mjs", "engine",
         "Sao chép wasm/ (121 MB) vào dist/wasm/ bằng fs.cp thuần Node "
         "(chạy được trên cả ba hệ điều hành)"),
        ("p5", 40, "cargo build --release", "native",
         "profile.release: lto = true, codegen-units = 1, opt-level = \"s\", "
         "panic = \"abort\", strip = true"),
        ("p6", 40, "tauri bundle", "native",
         "Nhúng dist/ vào nhị phân và sinh gói cài đặt theo nền tảng"),
    ]
    y = 60
    for nid, x, label, kind, note in chain:
        sc.node(nid, x, y, 420, 62, label, kind=kind, shape="round",
                font_size=12, bold=True)
        sc.node(nid + "_n", 490, y, 630, 62, note, kind="neutral",
                shape="note", font_size=10)
        sc.edge(nid, nid + "_n", exit="e", entry="w", style="straight",
                arrow="none", color="#CBD5E1")
        y += 82
    order = [c[0] for c in chain]
    for a, b in zip(order, order[1:]):
        sc.edge(a, b, exit="s", entry="n", style="straight")

    sc.group("gout", 40, 570, 1080, 130, "Đầu ra trong src-tauri/target/release/",
             "data")
    outs = [
        ("o1", 66, "pdf-toolkit\n(nhị phân thô)"),
        ("o2", 276, "bundle/appimage/*.AppImage\nbundle/deb/*.deb"),
        ("o3", 486, "bundle/dmg/*.dmg\nbundle/macos/*.app"),
        ("o4", 696, "bundle/msi/*.msi\nbundle/nsis/*setup.exe"),
        ("o5", 906, "Artifact CI\n(9 quy trình GitHub Actions)"),
    ]
    for nid, x, label in outs:
        sc.node(nid, x, 620, 190, 62, label, kind="data", shape="round",
                font_size=11)
    sc.edge("p6", "o1", exit="s", entry="n", waypoints=[(250, 600), (161, 600)],
            color="#334155")

    sc.node("note", 40, 720, 1080, 60,
            "Giới hạn đã được ghi nhận trong tài liệu dự án: gói cài đặt macOS và "
            "Windows không thể biên dịch chéo từ Linux, phải chạy trên máy chạy "
            "hệ điều hành tương ứng thông qua ma trận CI desktop-build.yml; các "
            "gói hiện chưa được ký số nên hệ điều hành sẽ cảnh báo ở lần chạy đầu.",
            kind="warn", shape="round", font_size=11)
    return emit(sc, "fig_3_13_build_pipeline", OUT)


# ================================================================ Hình 3.10
def fig_3_10():
    sc = Scene("Hình 3.6 - Cơ chế đa ngữ và mặc định tiếng Việt", 1160, 780)

    sc.node("boot", 40, 40, 340, 76, "init() trong main.ts",
            sub="nếu localStorage chưa có i18nextLng thì đặt 'vi'",
            kind="ui", shape="round", font_size=12, bold=True)
    sc.node("res", 420, 40, 340, 76, "getLanguageFromUrl()",
            sub="thứ tự: tiền tố URL → localStorage → navigator.languages "
                "→ VITE_DEFAULT_LANGUAGE → 'en'",
            kind="logic", shape="round", font_size=12, bold=True)
    sc.node("init", 800, 40, 320, 76, "initI18n()",
            sub="i18next + HttpBackend, hai không gian tên common và tools",
            kind="logic", shape="round", font_size=12, bold=True)

    sc.node("locales", 40, 160, 520, 130,
            "public/locales/<lang>/common.json  ·  tools.json\n\n"
            "21 ngôn ngữ: en, vi, ar, be, da, de, es, fr, id, it, ja, ko, nl, "
            "pt, ru, sk, sv, tr, uk, zh, zh-TW\n"
            "Bản tiếng Việt: 272 khoá trong common.json và 890 khoá trong "
            "tools.json",
            kind="data", shape="note", font_size=11, align="left")
    sc.node("apply", 600, 160, 520, 130,
            "applyTranslations()\n\n"
            "Duyệt mọi phần tử mang data-i18n và thay nội dung; "
            "injectLanguageSwitcher() thêm bộ chọn ngôn ngữ; "
            "setLanguageInPlace() đổi ngôn ngữ mà không tải lại trang",
            kind="logic", shape="round", font_size=11, align="left")

    sc.node("web", 40, 340, 520, 150,
            "Bản web (production)\n\n"
            "scripts/generate-i18n-pages.mjs sinh sẵn thư mục /vi/, /fr/, … cho "
            "từng trang; rewriteLinks() thêm tiền tố ngôn ngữ vào mọi liên kết "
            "nội bộ; sitemap và thẻ hreflang được sinh kèm",
            kind="accent", shape="round", font_size=11, align="left")
    sc.node("tauri", 600, 340, 520, 150,
            "Bản desktop (Tauri)\n\n"
            "Không sinh trang theo ngôn ngữ. rewriteLinks() phải bỏ qua, nếu "
            "không mọi liên kết sẽ trỏ tới /vi/<tool>.html không tồn tại — đây "
            "chính là lỗi thẻ công cụ không bấm được ở lần tải đầu, đã sửa ở "
            "commit 4a63fa9",
            kind="warn", shape="round", font_size=11, align="left")

    sc.node("guard", 40, 530, 1080, 90,
            "Điều kiện bảo vệ sau khi sửa lỗi (src/js/i18n/i18n.ts)\n\n"
            "const isTauri = import.meta.env.MODE === 'tauri' || "
            "'__TAURI_INTERNALS__' in window || '__TAURI__' in window;\n"
            "if (import.meta.env.DEV || isTauri) return;   // giữ nguyên liên "
            "kết phẳng, dùng cơ chế đổi ngôn ngữ tại chỗ",
            kind="engine", shape="round", font_size=11)
    sc.node("id", 40, 650, 1080, 90,
            "Nguyên tắc thiết kế bảo đảm tính ổn định\n\n"
            "Danh mục và công cụ được định danh bằng tên nội bộ cố định "
            "(getToolIdFromHref lấy phần tên tệp .html); chỉ nhãn hiển thị được "
            "dịch. Nhờ vậy việc đổi ngôn ngữ không làm thay đổi định danh, "
            "không ảnh hưởng tới cấu hình DISABLE_TOOLS hay config.json.",
            kind="ui", shape="round", font_size=11)

    sc.edge("boot", "res", exit="e", entry="w", style="straight")
    sc.edge("res", "init", exit="e", entry="w", style="straight")
    sc.edge("init", "locales", exit="s", entry="n",
            waypoints=[(960, 140), (300, 140)], color="#059669",
            label="tải tài nguyên")
    sc.edge("locales", "apply", exit="e", entry="w", style="straight")
    sc.edge("apply", "web", exit="s", entry="n",
            waypoints=[(860, 315), (300, 315)], color="#0284C7")
    sc.edge("apply", "tauri", exit="s", entry="n", style="straight",
            color="#DC2626")
    sc.edge("tauri", "guard", exit="s", entry="n", style="straight",
            color="#DC2626")
    return emit(sc, "fig_3_6_i18n", OUT)


if __name__ == "__main__":
    for fn in [fig_3_1, fig_3_2, fig_3_3, fig_3_4, fig_3_5, fig_3_6, fig_3_7,
               fig_3_8, fig_3_9, fig_3_10]:
        print("ok", fn())
