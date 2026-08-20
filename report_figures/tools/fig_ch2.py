#!/usr/bin/env python3
"""Sinh các hình chương 2 — Phân tích và thiết kế hệ thống."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagramlib import Scene, emit  # noqa: E402

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------------------------------------------- helpers
def seq(sc, lifelines, messages, top=40, head_h=46, row0=120, row_h=52,
        foot_pad=40):
    """Dựng biểu đồ tuần tự: hộp tiêu đề, đường đời, hộp kích hoạt, thông điệp."""
    xs = {}
    for name, (nid, x, w, kind) in lifelines.items():
        xs[name] = x + w / 2
        sc.node(nid, x, top, w, head_h, name, kind=kind, shape="round",
                font_size=11, bold=True)
    bottom = row0 + len(messages) * row_h + foot_pad
    for name, (nid, x, w, kind) in lifelines.items():
        cx = x + w / 2
        sc.node(nid + "_foot", cx - 5, bottom, 10, 14, "", kind="neutral",
                shape="rect", font_size=8)
        sc.edge(nid, nid + "_foot", exit="s", entry="n", style="straight",
                dashed=True, arrow="none", color="#94A3B8")
    for i, (src, dst, label, kind) in enumerate(messages):
        y = row0 + i * row_h
        color = {"call": "#4F46E5", "ret": "#059669",
                 "err": "#DC2626", "self": "#EA580C"}[kind]

        if src == dst or kind == "self":
            cx = xs[src]
            a = f"act{i}a_{lifelines[src][0]}"
            b = f"act{i}b_{lifelines[src][0]}"
            sc.node(a, cx - 6, y - 20, 12, 20, "", kind="ui", shape="rect")
            sc.node(b, cx - 6, y + 6, 12, 20, "", kind="ui", shape="rect")
            sc.edge(a, b, f"{i+1}. {label}", exit="e", entry="e",
                    style="straight", color=color, font_size=10,
                    waypoints=[(cx + 46, y - 10), (cx + 46, y + 16)],
                    label_dx=150, label_dy=-14)
            continue

        pid = {}
        for who in (src, dst):
            cx = xs[who]
            nid = f"act{i}_{lifelines[who][0]}"
            sc.node(nid, cx - 6, y - 11, 12, 22, "", kind="ui", shape="rect")
            pid[who] = nid
        sc.edge(pid[src], pid[dst], f"{i+1}. {label}",
                exit="e" if xs[dst] > xs[src] else "w",
                entry="w" if xs[dst] > xs[src] else "e",
                style="straight", dashed=(kind == "ret"),
                color=color, font_size=10, label_dy=-12)
    return bottom


# ================================================================= Hình 2.1
def fig_2_1():
    sc = Scene("Hình 2.1 - Biểu đồ ca sử dụng tổng quát", 1180, 900)
    sc.group("bnd", 300, 30, 580, 840, "Ứng dụng PDF Toolkit Desktop", "ui")

    sc.node("usr", 70, 360, 130, 110, "Người dùng", kind="native",
            shape="actor", font_size=13, bold=True)
    sc.node("fs", 970, 150, 150, 110, "Hệ thống tệp\ncục bộ", kind="native",
            shape="actor", font_size=12, bold=True)
    sc.node("tsa", 970, 600, 150, 110, "Máy chủ TSA\n(RFC 3161)",
            kind="external", shape="actor", font_size=12, bold=True)

    ucs = [
        ("uc1", "Nạp tệp đầu vào\n(chọn tệp / kéo–thả)"),
        ("uc2", "Tổ chức và quản lý trang\n(ghép, tách, xoay, xoá…)"),
        ("uc3", "Chuyển đổi định dạng\n(sang PDF / từ PDF)"),
        ("uc4", "Chỉnh sửa và chú thích\ntài liệu"),
        ("uc5", "Nén và tối ưu hoá\ntài liệu"),
        ("uc6", "Bảo mật tài liệu\n(mã hoá, giải mã, quyền)"),
        ("uc7", "Ký số và kiểm tra\nchữ ký số"),
        ("uc8", "Nhận dạng ký tự quang học\n(OCR)"),
        ("uc9", "Xây dựng luồng xử lý\ntự động (Workflow)"),
        ("uc10", "Lưu kết quả bằng hộp thoại\ncủa hệ điều hành"),
        ("uc11", "Thiết lập ngôn ngữ và\nnguồn mô-đun WASM"),
    ]
    y = 70
    for nid, label in ucs:
        sc.node(nid, 330, y, 520, 58, label, kind="logic", shape="ellipse",
                font_size=11)
        sc.edge("usr", nid, exit="e", entry="w", style="straight",
                arrow="none", color="#334155")
        y += 72

    sc.edge("uc1", "fs", exit="e", entry="w", style="straight",
            arrow="open", color="#475569", label="đọc tệp")
    sc.edge("uc10", "fs", exit="e", entry="w", arrow="open", color="#475569",
            label="ghi tệp", waypoints=[(915, 799), (915, 205)])
    sc.edge("uc7", "tsa", exit="e", entry="w", style="straight",
            dashed=True, arrow="open", color="#DB2777",
            label="«tuỳ chọn» đóng dấu thời gian")

    sc.text(590, 890, "Ghi chú: hệ thống không có tác nhân quản trị và không có "
                      "máy chủ ứng dụng; mọi ca sử dụng được thực thi cục bộ.",
            size=11, anchor="middle", color="#475569")
    return emit(sc, "fig_2_1_use_case", OUT)


# ================================================================= Hình 2.2
def fig_2_2():
    sc = Scene("Hình 2.2 - Biểu đồ ngữ cảnh", 1120, 720)
    sc.node("app", 400, 300, 320, 130,
            "PDF Toolkit Desktop\n(Tauri v2 + WebView)",
            kind="ui", shape="round", font_size=14, bold=True,
            sub="Toàn bộ xử lý diễn ra trên máy người dùng")

    sc.node("user", 80, 300, 150, 110, "Người dùng", kind="native",
            shape="actor", font_size=13, bold=True)
    sc.node("os", 420, 90, 280, 80,
            "Hệ điều hành\n(hộp thoại chọn/lưu tệp, WebView)",
            kind="native", shape="round", font_size=12)
    sc.node("fs", 420, 560, 280, 80,
            "Hệ thống tệp cục bộ\n(tệp nguồn và tệp kết quả)",
            kind="data", shape="cyl", font_size=12)
    sc.node("wasm", 60, 540, 260, 90,
            "Kho mô-đun WASM đóng gói kèm\n(dist/wasm — 121 MB)",
            kind="engine", shape="round", font_size=12)
    sc.node("tsa", 850, 200, 220, 80,
            "Máy chủ TSA\n(DigiCert, Sectigo, FreeTSA…)",
            kind="external", shape="round", font_size=12, dashed=True)
    sc.node("font", 850, 350, 220, 80,
            "Nguồn phông chữ CJK/Noto\n(tải theo yêu cầu)",
            kind="external", shape="round", font_size=12, dashed=True)
    sc.node("cdn", 850, 500, 220, 90,
            "CDN jsDelivr\n(chỉ dùng cho bản web;\nbản desktop KHÔNG dùng)",
            kind="external", shape="round", font_size=11, dashed=True)

    sc.edge("user", "app", "thao tác, tham số", exit="e", entry="w")
    sc.edge("app", "user", "kết quả, thông báo", exit="w", entry="e",
            waypoints=[(360, 410), (300, 410), (300, 375)], color="#059669")
    sc.edge("os", "app", "sự kiện chọn tệp", exit="s", entry="n",
            waypoints=[(500, 240)], color="#475569")
    sc.edge("app", "os", "yêu cầu hộp thoại lưu", exit="n", entry="s",
            waypoints=[(620, 240)], color="#4F46E5")
    sc.edge("os", "fs", "đọc / ghi", exit="e", entry="e",
            waypoints=[(780, 130), (780, 600)], color="#475569")
    sc.edge("app", "wasm", "nạp cục bộ", exit="w", entry="n", color="#EA580C")
    sc.edge("app", "tsa", "«tuỳ chọn» RFC 3161", exit="e", entry="w",
            dashed=True, color="#DB2777")
    sc.edge("app", "font", "«tuỳ chọn» tải phông", exit="e", entry="w",
            dashed=True, color="#DB2777")
    sc.edge("app", "cdn", "không sử dụng", exit="e", entry="w",
            dashed=True, arrow="none", color="#DB2777")

    sc.text(560, 690,
            "Ranh giới hệ thống: không có máy chủ ứng dụng, không có cơ sở dữ "
            "liệu, không có luồng tải tệp lên mạng.",
            size=11, anchor="middle", color="#475569")
    return emit(sc, "fig_2_2_context", OUT)


# ================================================================= Hình 2.3
def fig_2_3():
    sc = Scene("Hình 2.3 - Kiến trúc tổng thể", 1160, 990)
    layers = [
        ("L1", 40, "Tầng vỏ ứng dụng native — Tauri v2 / Rust", "native", [
            ("main.rs\nđiểm vào tiến trình", 60),
            ("lib.rs — lệnh save_file\n(hộp thoại lưu native)", 60),
            ("tauri-plugin-dialog", 60),
            ("capabilities/default.json\n(chỉ core:default)", 60),
        ]),
        ("L2", 190, "Tầng WebView của hệ điều hành", "native", [
            ("WebKitGTK\n(Linux)", 60),
            ("WKWebView\n(macOS)", 60),
            ("WebView2\n(Windows)", 60),
            ("COOP/COEP → SharedArrayBuffer", 60),
        ]),
        ("L3", 340, "Tầng giao diện — HTML đa trang + TypeScript", "ui", [
            ("131 trang công cụ\n(index + src/pages)", 60),
            ("main.ts — sidebar,\ntìm kiếm, thẻ công cụ", 60),
            ("ui.ts — loader,\nhộp thoại, thumbnail", 60),
            ("i18n (21 ngôn ngữ,\nmặc định tiếng Việt)", 60),
        ]),
        ("L4", 490, "Tầng điều phối nghiệp vụ", "logic", [
            ("src/js/logic — 132 mô-đun\nnghiệp vụ theo công cụ", 60),
            ("workflow/ — engine,\neditor, 79 nút xử lý", 60),
            ("state.ts — trạng thái\nphiên làm việc", 60),
            ("compare/ — so sánh\ntài liệu (Web Worker)", 60),
        ]),
        ("L5", 640, "Tầng tiện ích và điều phối tài nguyên", "accent", [
            ("wasm-provider.ts\n(nguồn WASM + danh sách tin cậy)", 60),
            ("helpers.ts — downloadFile,\nqpdf, parsePageRanges", 60),
            ("password-prompt.ts,\npdf-decrypt.ts", 60),
            ("tesseract-runtime.ts,\nfont-loader.ts", 60),
        ]),
        ("L6", 790, "Tầng động cơ xử lý (JavaScript / WebAssembly)", "engine", [
            ("pdf-lib · pdf.js · PDFKit\n· jsPDF · pdfium", 60),
            ("qpdf-wasm\n(mã hoá/giải mã)", 60),
            ("CoherentPDF · Ghostscript\n· PyMuPDF (Pyodide)", 60),
            ("Tesseract.js · wasm-vips\n· LibreOffice-WASM", 60),
        ]),
    ]
    for gid, y, title, kind, items in layers:
        sc.group(gid, 40, y, 1080, 120, title, kind)
        x = 66
        for label, h in items:
            sc.node(f"{gid}_{x}", x, y + 40, 245, h, label, kind=kind,
                    shape="round", font_size=11)
            x += 262

    for a, b in [("L1", "L2"), ("L2", "L3"), ("L3", "L4"),
                 ("L4", "L5"), ("L5", "L6")]:
        ya = [l for l in layers if l[0] == a][0][1]
        yb = [l for l in layers if l[0] == b][0][1]
        sc.text(30, (ya + yb) / 2 + 62, "", size=10)
    for y in (170, 320, 470, 620, 770):
        sc.text(580, y + 10, "▼", size=14, anchor="middle", color="#4F46E5")

    sc.text(580, 960,
            "Luồng phụ thuộc một chiều: tầng trên chỉ gọi xuống tầng dưới; "
            "không có tiến trình máy chủ nào trong kiến trúc.",
            size=11, anchor="middle", color="#475569")
    return emit(sc, "fig_2_3_layered_architecture", OUT)


# ================================================================= Hình 2.4
def fig_2_4():
    sc = Scene("Hình 2.4 - Kiến trúc thành phần", 1180, 860)

    sc.group("g1", 40, 40, 330, 250, "Điểm vào và khung giao diện", "ui")
    sc.node("html", 60, 90, 290, 56, "Trang HTML công cụ",
            sub="src/pages/*.html + partials", kind="ui", shape="round")
    sc.node("main", 60, 158, 290, 56, "main.ts",
            sub="sidebar, tìm kiếm, thẻ công cụ", kind="ui", shape="round")
    sc.node("ui", 60, 226, 290, 50, "ui.ts / mobileMenu.ts",
            sub="loader, alert, thumbnail", kind="ui", shape="round")

    sc.group("g2", 410, 40, 340, 250, "Cấu hình và quốc tế hoá", "accent")
    sc.node("tools", 430, 90, 300, 56, "config/tools.ts",
            sub="7 nhóm, 127 mục công cụ", kind="accent", shape="round")
    sc.node("pdftools", 430, 158, 300, 56, "config/pdf-tools.ts",
            sub="phân loại kiểu nạp tệp", kind="accent", shape="round")
    sc.node("i18n", 430, 226, 300, 50, "i18n/*  +  public/locales",
            sub="21 ngôn ngữ, 1.162 khoá (vi)", kind="accent", shape="round")

    sc.group("g3", 790, 40, 350, 250, "Trạng thái và nhập liệu", "data")
    sc.node("state", 810, 90, 310, 56, "state.ts",
            sub="files, pdfDoc, activeTool", kind="data", shape="round")
    sc.node("fh", 810, 158, 310, 56, "handlers/fileHandler.ts",
            sub="chọn tệp, kéo–thả, kiểm tra", kind="data", shape="round")
    sc.node("dis", 810, 226, 310, 50, "utils/disabled-tools.ts",
            sub="config.json + DISABLE_TOOLS", kind="data", shape="round")

    sc.group("g4", 40, 330, 710, 260, "Tầng nghiệp vụ", "logic")
    sc.node("logic", 60, 380, 320, 60, "src/js/logic — 132 mô-đun",
            sub="mỗi công cụ một mô-đun trang", kind="logic", shape="round")
    sc.node("wf", 400, 380, 330, 60, "src/js/workflow",
            sub="engine · editor · 79 nút · serialization",
            kind="logic", shape="round")
    sc.node("cmp", 60, 460, 320, 60, "src/js/compare",
            sub="engine + Web Worker so sánh", kind="logic", shape="round")
    sc.node("worker", 400, 460, 330, 60, "public/workers/*.js",
            sub="8 Web Worker (merge, attachments, JSON, TOC)",
            kind="logic", shape="round")

    sc.group("g5", 790, 330, 350, 260, "Tiện ích dùng chung (43 mô-đun)",
             "accent")
    sc.node("wp", 810, 380, 310, 52, "wasm-provider.ts",
            sub="URL + danh sách máy chủ tin cậy", kind="accent", shape="round")
    sc.node("hp", 810, 440, 310, 52, "helpers.ts",
            sub="downloadFile, qpdf, parsePageRanges", kind="accent",
            shape="round")
    sc.node("pw", 810, 500, 310, 52, "password-prompt · pdf-decrypt",
            sub="hỏi mật khẩu, giải mã theo lô", kind="accent", shape="round")

    sc.group("g6", 40, 630, 1100, 190, "Động cơ xử lý và tài nguyên cục bộ",
             "engine")
    eng = [
        ("pdf-lib\n+ fontkit", 60), ("pdf.js\n(pdfjs-dist)", 60),
        ("qpdf-wasm", 60), ("CoherentPDF", 60), ("PyMuPDF\n(Pyodide)", 60),
        ("Ghostscript", 60), ("Tesseract.js", 60),
    ]
    x = 62
    for label, h in eng:
        sc.node(f"e{x}", x, 680, 145, h, label, kind="engine", shape="round",
                font_size=11)
        x += 155
    sc.node("assets", 62, 752, 1058, 48,
            "dist/wasm  —  pymupdf 54 MB · ocr 47 MB · gs 15 MB · cpdf 6 MB   |   "
            "public/locales · fonts · qpdf.wasm · coherentpdf.browser.min.js",
            kind="data", shape="round", font_size=11)

    sc.edge("html", "main", exit="s", entry="n", style="straight")
    sc.edge("main", "ui", exit="s", entry="n", style="straight")
    sc.edge("main", "tools", exit="e", entry="w", style="straight")
    sc.edge("main", "i18n", exit="e", entry="w",
            waypoints=[(390, 186), (390, 251)], color="#0284C7")
    sc.edge("html", "logic", exit="s", entry="n",
            waypoints=[(120, 340)], color="#059669")
    sc.edge("fh", "state", exit="n", entry="s", style="straight",
            color="#CA8A04")
    sc.edge("state", "logic", "trạng thái phiên", exit="w", entry="n",
            waypoints=[(790, 118), (790, 320), (220, 320)], color="#CA8A04")
    sc.edge("logic", "hp", exit="e", entry="w",
            waypoints=[(760, 410), (760, 466)], color="#059669")
    sc.edge("logic", "pw", exit="e", entry="w",
            waypoints=[(752, 410), (752, 526)], color="#059669")
    sc.edge("wf", "logic", exit="w", entry="e", style="straight", dashed=True)
    sc.text(390, 356, "dùng lại các mô-đun tiện ích", size=10,
            anchor="middle", color="#475569")
    sc.edge("logic", "worker", exit="e", entry="w",
            waypoints=[(400, 410)], color="#059669")
    sc.edge("hp", "e372", "qpdf.wasm", exit="s", entry="n",
            waypoints=[(965, 610), (447, 610)], color="#EA580C")
    sc.edge("wp", "e527", "URL mô-đun\nWASM", exit="s", entry="n",
            waypoints=[(1010, 630), (602, 630)], color="#EA580C")
    sc.edge("wp", "e682", exit="s", entry="n",
            waypoints=[(1035, 645), (757, 645)], color="#EA580C")
    sc.edge("wp", "e837", exit="s", entry="n",
            waypoints=[(1060, 660), (912, 660)], color="#EA580C")
    sc.edge("logic", "e62", exit="s", entry="n",
            waypoints=[(140, 660)], color="#EA580C")
    return emit(sc, "fig_2_4_component_architecture", OUT)


# ================================================================= Hình 2.5
def fig_2_5():
    sc = Scene("Hình 2.5 - Kiến trúc triển khai", 1160, 800)

    sc.group("dev", 40, 40, 520, 350, "Máy phát triển", "accent")
    sc.node("src", 66, 90, 220, 56, "Mã nguồn TypeScript",
            sub="src/js — 71,4 nghìn dòng", kind="ui", shape="round")
    sc.node("vite", 66, 162, 220, 56, "Vite 8 + TypeScript",
            sub="npm run build:tauri", kind="logic", shape="round")
    sc.node("copy", 66, 234, 220, 56, "copy-wasm-to-dist.mjs",
            sub="wasm/ → dist/wasm", kind="logic", shape="round")
    sc.node("dist", 320, 90, 215, 56, "dist/",
            sub="HTML, JS, CSS, locales", kind="data", shape="round")
    sc.node("distw", 320, 162, 215, 56, "dist/wasm/",
            sub="121 MB mô-đun ngoại tuyến", kind="data", shape="round")
    sc.node("cargo", 320, 234, 215, 56, "Cargo / Rust 1.77+",
            sub="tauri build", kind="native", shape="round")

    sc.group("ci", 600, 40, 520, 350,
             "CI — .github/workflows/desktop-build.yml", "native")
    sc.node("m1", 626, 88, 224, 62, "macos-latest (arm64)",
            sub="--target aarch64-apple-darwin", kind="native", shape="round",
            font_size=11)
    sc.node("m2", 626, 158, 224, 62, "macos-latest (x86_64)",
            sub="--target x86_64-apple-darwin", kind="native", shape="round",
            font_size=11)
    sc.node("m3", 626, 228, 224, 62, "windows-latest",
            sub="MSVC + WebView2", kind="native", shape="round", font_size=11)
    sc.node("m4", 626, 298, 224, 62, "ubuntu-22.04",
            sub="WebKitGTK 4.1", kind="native", shape="round", font_size=11)
    sc.node("art", 878, 158, 220, 132, "Artifact CI",
            sub="dmg · app · msi · exe · deb · AppImage", kind="data",
            shape="round")

    sc.group("run", 40, 430, 1080, 300, "Máy người dùng cuối", "ui")
    sc.node("inst", 70, 480, 240, 70, "Gói cài đặt",
            sub=".dmg / .msi / .AppImage / .deb", kind="data", shape="round")
    sc.node("bin", 350, 480, 240, 70, "Tiến trình native",
            sub="pdf-toolkit (Rust, Tauri v2)", kind="native", shape="round")
    sc.node("wv", 630, 480, 240, 70, "WebView hệ điều hành",
            sub="COOP/COEP bật sẵn", kind="native", shape="round")
    sc.node("assets2", 910, 480, 190, 70, "Tài nguyên nhúng",
            sub="dist/ + dist/wasm", kind="data", shape="round")
    sc.node("fs2", 350, 604, 240, 64, "Hệ thống tệp người dùng",
            sub="qua hộp thoại save_file", kind="data", shape="cyl")
    sc.node("net", 700, 604, 400, 64,
            "Mạng: chỉ dùng khi bật đóng dấu thời gian TSA hoặc tải phông CJK",
            kind="external", shape="round", dashed=True, font_size=11)

    sc.edge("src", "vite", exit="s", entry="n", style="straight")
    sc.edge("vite", "dist", exit="e", entry="w", style="straight")
    sc.edge("vite", "copy", exit="s", entry="n", style="straight")
    sc.edge("copy", "distw", exit="e", entry="w", style="straight")
    sc.edge("dist", "cargo", exit="s", entry="n",
            waypoints=[(427, 130)], color="#475569")
    sc.edge("distw", "cargo", exit="s", entry="n", style="straight")
    sc.edge("cargo", "inst", exit="s", entry="n",
            waypoints=[(427, 410), (190, 410)], color="#475569")
    for m in ("m1", "m2", "m3", "m4"):
        sc.edge(m, "art", exit="e", entry="w", style="ortho")
    sc.edge("art", "inst", exit="s", entry="n",
            waypoints=[(987, 410), (190, 410)], color="#475569")
    sc.edge("inst", "bin", exit="e", entry="w", style="straight")
    sc.edge("bin", "wv", exit="e", entry="w", style="straight")
    sc.edge("wv", "assets2", exit="e", entry="w", style="straight")
    sc.edge("bin", "fs2", exit="s", entry="n", label="save_file", style="straight")
    sc.edge("wv", "net", exit="s", entry="n", dashed=True, color="#DB2777")
    return emit(sc, "fig_2_5_deployment", OUT)


# ================================================================= Hình 2.6
def fig_2_6():
    sc = Scene("Hình 2.6 - Quy trình xử lý tài liệu tổng quát", 940, 1230)
    steps = [
        ("s1", "Người dùng chọn công cụ trên màn hình làm việc", "ui", "round"),
        ("s2", "Nạp tệp: <input type=\"file\"> hoặc kéo–thả vào drop-zone",
         "ui", "round"),
        ("s3", "Lọc theo kiểu MIME / phần mở rộng, đưa vào state.files",
         "logic", "round"),
        ("d1", "Tệp có mã hoá?", "data", "diamond"),
        ("s4", "batchDecryptIfNeeded(): hỏi mật khẩu, thử CoherentPDF rồi PyMuPDF",
         "accent", "round"),
        ("s5", "Nạp tài liệu: pdf.js để hiển thị, pdf-lib/cpdf để thao tác",
         "logic", "round"),
        ("s6", "Hiển thị xem trước, số trang, cho phép sắp xếp và nhập tham số",
         "ui", "round"),
        ("s7", "Người dùng bấm nút xử lý → showLoader()", "ui", "round"),
        ("d2", "Cần mô-đun WASM ngoài?", "data", "diamond"),
        ("s8", "requireWasm(): kiểm tra cấu hình, nạp từ dist/wasm hoặc báo lỗi",
         "engine", "round"),
        ("s9", "Thực thi phép biến đổi trên luồng chính hoặc trong Web Worker",
         "engine", "round"),
        ("d3", "Thành công?", "data", "diamond"),
        ("s10", "Đóng gói kết quả thành Blob (application/pdf, image/*, zip…)",
         "logic", "round"),
        ("s11", "downloadFile(): phát hiện Tauri → invoke('save_file')",
         "native", "round"),
        ("s12", "Hộp thoại lưu của hệ điều hành, ghi tệp tới vị trí đã chọn",
         "native", "round"),
        ("s13", "showAlert('Success') → giải phóng bộ nhớ, đặt lại trạng thái",
         "logic", "round"),
    ]
    y = 40
    for nid, label, kind, shape in steps:
        h = 74 if shape == "diamond" else 56
        w = 300 if shape == "diamond" else 560
        x = 300 if shape == "diamond" else 170
        sc.node(nid, x, y, w, h, label, kind=kind, shape=shape, font_size=11)
        y += h + 12

    order = [s[0] for s in steps]
    for a, b in zip(order, order[1:]):
        sc.edge(a, b, exit="s", entry="n", style="straight")

    sc.node("err", 690, 762, 190, 96,
            "showAlert('Error')\nghi log console\ndọn MEMFS / huỷ Worker",
            kind="warn", shape="round", font_size=11)
    sc.edge("d3", "err", "Không", exit="e", entry="n", color="#DC2626")
    sc.edge("err", "s7", "người dùng thử lại", exit="e", entry="e",
            waypoints=[(890, 810), (890, 480), (760, 480)],
            dashed=True, color="#DC2626")
    sc.edge("d1", "s5", "Không", exit="e", entry="e",
            waypoints=[(660, 245), (660, 384)], color="#475569")
    sc.edge("d2", "s9", "Không", exit="e", entry="e",
            waypoints=[(660, 625), (660, 704)], color="#475569")
    sc.text(470, 1205,
            "Toàn bộ dữ liệu trung gian tồn tại trong bộ nhớ tiến trình; "
            "không có tệp tạm nào được ghi ra đĩa trước bước 15.",
            size=11, anchor="middle", color="#475569")
    return emit(sc, "fig_2_6_processing_pipeline", OUT)


# ================================================================= Hình 2.7
def fig_2_7():
    sc = Scene("Hình 2.7 - Bản đồ điều phối động cơ xử lý", 1160, 1000)
    sc.node("op", 430, 30, 300, 56, "Yêu cầu thao tác PDF",
            kind="ui", shape="round", font_size=13, bold=True)

    rows = [
        ("pdflib", "pdf-lib (+ fontkit)", "engine",
         "Xoay, xoá và trích trang; đóng dấu chìm; đánh số trang; đầu và chân "
         "trang; gộp nhiều trang lên một tờ; làm phẳng; chuẩn hoá khổ giấy; "
         "nhúng phông và vẽ lớp văn bản cho kết quả OCR"),
        ("pdfjs", "pdf.js (pdfjs-dist)", "engine",
         "Kết xuất trang ra canvas; sinh ảnh thu nhỏ; xem trước tài liệu; "
         "trích văn bản; PDF sang ảnh; hiệu ứng bản quét; phát hiện tài liệu "
         "có mật khẩu"),
        ("qpdf", "qpdf-wasm", "engine",
         "Mã hoá AES-256; giải mã; đặt quyền in, sao chép và chỉnh sửa; "
         "tuyến tính hoá; sửa chữa tệp hỏng"),
        ("cpdf", "CoherentPDF", "engine",
         "Ghép tệp có giữ nhãn trang; tách theo bookmark; sinh mục lục; "
         "chuyển đổi PDF ↔ JSON; thêm, sửa và trích tệp đính kèm; sửa bookmark"),
        ("pymu", "PyMuPDF trên Pyodide", "engine",
         "Nén ảnh nhúng; PDF sang văn bản, Markdown, SVG và DOCX; trích ảnh và "
         "bảng; EPUB, MOBI, FB2, XPS và CBZ sang PDF; khử nghiêng trang quét"),
        ("gs", "Ghostscript", "engine",
         "Chuyển đổi sang PDF/A-1b, PDF/A-2b và PDF/A-3b; chuyển phông chữ "
         "thành đường nét vector"),
        ("tess", "Tesseract.js", "engine",
         "Nhận dạng ký tự đa ngôn ngữ; sinh dữ liệu hOCR chứa toạ độ, góc "
         "nghiêng và độ dốc đường cơ sở của từng từ"),
        ("vips", "wasm-vips, heic2any, utif", "engine",
         "Giải mã và biến đổi các định dạng ảnh ngoài luồng phổ thông: HEIC, "
         "TIFF, PSD, JPEG 2000"),
        ("lo", "LibreOffice-WASM", "engine",
         "Chuyển tài liệu văn phòng sang PDF: DOCX, XLSX, PPTX, ODT, ODS, ODP, "
         "ODG, RTF, WPD, WPS, PUB, VSD, Pages"),
        ("sign", "zgapdfsigner + node-forge", "engine",
         "Ký số bằng chứng thư X.509 từ tệp PFX hoặc PEM; đóng dấu thời gian "
         "RFC 3161; kiểm tra chữ ký và chuỗi chứng thư"),
    ]
    y = 130
    for nid, name, kind, desc in rows:
        sc.node(nid, 40, y, 300, 68, name, kind=kind, shape="round",
                font_size=12, bold=True)
        sc.node(nid + "_d", 360, y, 760, 68, desc, kind="neutral",
                shape="rect", font_size=11, align="left")
        sc.edge(nid, nid + "_d", exit="e", entry="w", style="straight",
                arrow="none", color="#CBD5E1")
        sc.edge("op", nid, exit="s", entry="n",
                waypoints=[(580, 110), (190, 110)], color="#4F46E5")
        y += 78

    sc.node("gate", 40, y + 12, 1080, 78,
            "Cổng kiểm tra chung cho ba mô-đun được cấu hình bên ngoài "
            "(CoherentPDF, PyMuPDF, Ghostscript): "
            "WasmProvider.isConfigured() — nếu chưa khả dụng, "
            "showWasmRequiredDialog() liệt kê các tính năng phụ thuộc và mở "
            "trang cấu hình thay vì để thao tác thất bại âm thầm",
            kind="warn", shape="round", font_size=11)
    for nid in ("cpdf", "pymu", "gs"):
        ny = sc.nodes[nid].y + 34
        sc.edge(nid, "gate", exit="w", entry="w",
                waypoints=[(18, ny), (18, y + 51)], dashed=True,
                color="#DC2626", arrow="none")
    sc.height = y + 120
    return emit(sc, "fig_2_7_engine_routing", OUT)


# ================================================================= Hình 2.8
def fig_2_8():
    lifelines = {
        "Người dùng": ("l1", 40, 150, "native"),
        "merge-pdf-page.ts": ("l2", 220, 190, "ui"),
        "password-prompt.ts": ("l3", 440, 190, "accent"),
        "merge.worker.js": ("l4", 660, 175, "logic"),
        "CoherentPDF (WASM)": ("l5", 855, 185, "engine"),
        "helpers.downloadFile": ("l6", 1060, 190, "accent"),
        "Rust save_file": ("l7", 1270, 165, "native"),
    }
    msgs = [
        ("Người dùng", "merge-pdf-page.ts", "chọn / kéo-thả tệp PDF", "call"),
        ("merge-pdf-page.ts", "password-prompt.ts", "batchDecryptIfNeeded(files)", "call"),
        ("password-prompt.ts", "merge-pdf-page.ts", "danh sách tệp đã giải mã", "ret"),
        ("merge-pdf-page.ts", "merge-pdf-page.ts", "pdfjsLib.getDocument() → số trang, thumbnail", "self"),
        ("Người dùng", "merge-pdf-page.ts", "sắp xếp bằng SortableJS, nhập khoảng trang", "call"),
        ("Người dùng", "merge-pdf-page.ts", "bấm nút Merge → merge()", "call"),
        ("merge-pdf-page.ts", "merge-pdf-page.ts", "isCpdfAvailable() → dựng danh sách jobs", "self"),
        ("merge-pdf-page.ts", "merge.worker.js", "postMessage({files, jobs, cpdfUrl}, transfer)", "call"),
        ("merge.worker.js", "CoherentPDF (WASM)", "importScripts() → fromMemory / parsePagespec", "call"),
        ("merge.worker.js", "CoherentPDF (WASM)", "mergeSame(pdfs, ranges) → toMemory()", "call"),
        ("CoherentPDF (WASM)", "merge.worker.js", "ArrayBuffer kết quả", "ret"),
        ("merge.worker.js", "merge-pdf-page.ts", "postMessage({status:'success', pdfBytes})", "ret"),
        ("merge-pdf-page.ts", "helpers.downloadFile", "downloadFile(blob, 'merged.pdf')", "call"),
        ("helpers.downloadFile", "Rust save_file", "invoke('save_file', {filename, bytes})", "call"),
        ("Rust save_file", "helpers.downloadFile", "true / false (người dùng huỷ)", "ret"),
        ("merge-pdf-page.ts", "Người dùng", "showAlert('Success') + đặt lại trạng thái", "ret"),
    ]
    sc = Scene("Hình 2.8 - Biểu đồ tuần tự ghép PDF", 1460, 1030)
    bottom = seq(sc, lifelines, msgs)
    sc.text(730, bottom + 60,
            "Các nút CoherentPDF được giải phóng bằng deletePdf() ngay sau khi "
            "sinh kết quả; ArrayBuffer được chuyển quyền sở hữu (transferable) "
            "để tránh nhân đôi bộ nhớ.",
            size=11, anchor="middle", color="#475569")
    return emit(sc, "fig_2_8_sequence_merge", OUT)


# ================================================================= Hình 2.9
def fig_2_9():
    lifelines = {
        "Người dùng": ("l1", 40, 150, "native"),
        "encrypt-pdf-page.ts": ("l2", 230, 200, "ui"),
        "helpers.initializeQpdf": ("l3", 470, 210, "accent"),
        "qpdf-wasm (MEMFS)": ("l4", 720, 200, "engine"),
        "downloadFile / Tauri": ("l5", 960, 210, "native"),
    }
    msgs = [
        ("Người dùng", "encrypt-pdf-page.ts", "chọn một tệp PDF", "call"),
        ("Người dùng", "encrypt-pdf-page.ts", "nhập mật khẩu người dùng / chủ sở hữu", "call"),
        ("encrypt-pdf-page.ts", "encrypt-pdf-page.ts", "kiểm tra bắt buộc: userPassword ≠ rỗng", "self"),
        ("encrypt-pdf-page.ts", "helpers.initializeQpdf", "initializeQpdf() — singleton", "call"),
        ("helpers.initializeQpdf", "qpdf-wasm (MEMFS)", "createModule({locateFile: qpdf.wasm})", "call"),
        ("helpers.initializeQpdf", "encrypt-pdf-page.ts", "thể hiện qpdf sẵn sàng (đã lưu vào bộ đệm)", "ret"),
        ("encrypt-pdf-page.ts", "qpdf-wasm (MEMFS)", "FS.writeFile('/input.pdf', bytes)", "call"),
        ("encrypt-pdf-page.ts", "qpdf-wasm (MEMFS)", "callMain([--encrypt, u, o, 256, …, /output.pdf])", "call"),
        ("qpdf-wasm (MEMFS)", "encrypt-pdf-page.ts", "mã trả về / ngoại lệ", "ret"),
        ("encrypt-pdf-page.ts", "qpdf-wasm (MEMFS)", "FS.readFile('/output.pdf')", "call"),
        ("encrypt-pdf-page.ts", "downloadFile / Tauri", "Blob → downloadFile(blob, tên gốc)", "call"),
        ("encrypt-pdf-page.ts", "qpdf-wasm (MEMFS)", "FS.unlink('/input.pdf') và '/output.pdf'", "call"),
        ("encrypt-pdf-page.ts", "Người dùng", "showAlert('Success') + resetState()", "ret"),
    ]
    sc = Scene("Hình 2.9 - Biểu đồ tuần tự mã hoá PDF", 1240, 900)
    bottom = seq(sc, lifelines, msgs)
    sc.text(620, bottom + 60,
            "Khối finally luôn gọi FS.unlink() cho cả tệp vào và tệp ra trong hệ "
            "tệp ảo MEMFS, kể cả khi qpdf ném ngoại lệ.",
            size=11, anchor="middle", color="#475569")
    return emit(sc, "fig_2_9_sequence_encrypt", OUT)


# ================================================================ Hình 2.10
def fig_2_10():
    sc = Scene("Hình 2.10 - Mô hình thực thi luồng xử lý tự động", 1160, 780)
    sc.group("g1", 40, 40, 500, 300, "Trình soạn thảo trực quan (Rete.js)", "ui")
    sc.node("editor", 66, 90, 210, 56, "editor.ts",
            sub="NodeEditor + AreaPlugin", kind="ui", shape="round")
    sc.node("nodes", 66, 162, 210, 56, "79 lớp nút",
            sub="nodes/registry.ts", kind="ui", shape="round")
    sc.node("ser", 66, 234, 210, 56, "serialization.ts",
            sub="JSON, WORKFLOW_VERSION = 1", kind="ui", shape="round")
    sc.node("sock", 310, 90, 210, 200,
            "sockets.ts\n\nKiểu dữ liệu truyền giữa các nút:\n"
            "• PDFData\n• ImageData\n• MultiPDFData",
            kind="data", shape="note", font_size=11)

    sc.group("g2", 580, 40, 540, 300, "engine.ts — bộ thực thi", "logic")
    sc.node("term", 606, 90, 230, 52, "Xác định nút cuối",
            sub="không có kết nối đầu ra", kind="logic", shape="round")
    sc.node("up", 606, 152, 230, 52, "getUpstreamNodes()",
            sub="duyệt BFS ngược", kind="logic", shape="round")
    sc.node("topo", 606, 214, 230, 52, "topologicalSort()",
            sub="Kahn — phát hiện chu trình", kind="logic", shape="round")
    sc.node("val", 870, 90, 230, 52, "validateEncryptOrdering()",
            sub="Encrypt chỉ nối tới nút Output", kind="logic", shape="round")
    sc.node("fetch", 870, 152, 230, 52, "DataflowEngine.fetch()",
            sub="thực thi tuần tự theo thứ tự", kind="logic", shape="round")
    sc.node("prog", 870, 214, 230, 52, "onProgress()",
            sub="idle → running → completed/error", kind="logic", shape="round")

    sc.node("err", 340, 400, 470, 70,
            "WorkflowError(nodeName): dừng luồng, tô đỏ nút lỗi, đưa các nút "
            "đang chạy về trạng thái idle",
            kind="warn", shape="round", font_size=11)

    sc.group("g3", 40, 520, 1080, 210, "Ví dụ đồ thị người dùng dựng được", "accent")
    chain = [
        ("n1", 66, "PDF Input", "data"),
        ("n2", 246, "Merge", "logic"),
        ("n3", 426, "Watermark", "logic"),
        ("n4", 606, "Compress", "logic"),
        ("n5", 786, "Encrypt", "logic"),
        ("n6", 966, "Download PDF", "ui"),
    ]
    for nid, x, label, kind in chain:
        sc.node(nid, x, 590, 150, 58, label, kind=kind, shape="round",
                font_size=12, bold=True)
    for a, b in zip([c[0] for c in chain], [c[0] for c in chain][1:]):
        sc.edge(a, b, exit="e", entry="w", style="straight")
    sc.node("note2", 66, 668, 1030, 44,
            "Nút Encrypt bắt buộc nằm ngay trước nút Output — mọi biến đổi sau "
            "khi mã hoá đều bị chặn bởi validateEncryptOrdering()",
            kind="warn", shape="note", font_size=11)

    sc.edge("editor", "term", exit="e", entry="w",
            waypoints=[(560, 118)], color="#059669")
    sc.edge("term", "up", exit="s", entry="n", style="straight")
    sc.edge("up", "topo", exit="s", entry="n", style="straight")
    sc.edge("topo", "val", exit="e", entry="w",
            waypoints=[(853, 240), (853, 116)], color="#059669")
    sc.edge("val", "fetch", exit="s", entry="n", style="straight")
    sc.edge("fetch", "prog", exit="s", entry="n", style="straight")
    sc.edge("fetch", "err", exit="s", entry="e", color="#DC2626",
            waypoints=[(985, 380), (860, 380)], label="ngoại lệ")
    sc.edge("nodes", "sock", exit="e", entry="w", style="straight",
            dashed=True)
    sc.edge("fetch", "n1", exit="s", entry="n",
            waypoints=[(985, 490), (141, 490)], color="#059669",
            label="gọi data() từng nút")
    return emit(sc, "fig_2_10_workflow_engine", OUT)


# ================================================================ Hình 2.11
def fig_2_11():
    sc = Scene("Hình 2.11 - Mô hình dữ liệu trong bộ nhớ", 1140, 700)

    sc.node("t1", 60, 60, 300, 190,
            "PDFData\n\n"
            "type: 'pdf'\n"
            "document: PDFDocument (pdf-lib)\n"
            "bytes: Uint8Array\n"
            "filename: string",
            kind="data", shape="round", font_size=11, align="left")
    sc.node("t2", 420, 60, 300, 190,
            "ImageData\n\n"
            "type: 'image'\n"
            "blob: Blob\n"
            "filename: string",
            kind="data", shape="round", font_size=11, align="left")
    sc.node("t3", 780, 60, 300, 190,
            "MultiPDFData\n\n"
            "type: 'multi-pdf'\n"
            "items: PDFData[]",
            kind="data", shape="round", font_size=11, align="left")

    sc.node("st", 60, 300, 480, 170,
            "state (src/js/state.ts)\n\n"
            "activeTool: string | null\n"
            "files: File[]\n"
            "pdfDoc: PDFDocument | null\n"
            "pdfPages: unknown[]\n"
            "currentPdfUrl: string | null",
            kind="ui", shape="round", font_size=11, align="left")
    sc.node("ls", 600, 300, 480, 170,
            "localStorage (dữ liệu bền vững duy nhất)\n\n"
            "i18nextLng — ngôn ngữ giao diện\n"
            "bentopdf:wasm-providers — URL mô-đun WASM\n"
            "phím tắt do người dùng đặt lại\n\n"
            "Không lưu nội dung tài liệu, không lưu mật khẩu",
            kind="accent", shape="round", font_size=11, align="left")

    sc.node("mem", 60, 520, 1020, 130,
            "Vùng dữ liệu tạm trong bộ nhớ tiến trình\n\n"
            "ArrayBuffer / Uint8Array của tệp gốc  ·  Canvas kết xuất trang  ·  "
            "MEMFS của qpdf và Ghostscript (/input.pdf, /output.pdf)  ·  "
            "Hệ tệp ảo Pyodide của PyMuPDF  ·  Blob kết quả trước khi lưu\n\n"
            "Tất cả bị huỷ khi đóng cửa sổ; không có tệp tạm nào được ghi lên đĩa.",
            kind="engine", shape="round", font_size=11)

    sc.edge("t1", "st", exit="s", entry="n", dashed=True, arrow="none",
            color="#94A3B8")
    sc.edge("t3", "ls", exit="s", entry="n", dashed=True, arrow="none",
            color="#94A3B8")
    sc.edge("st", "mem", exit="s", entry="n", color="#EA580C")
    sc.edge("ls", "mem", exit="s", entry="n", dashed=True, arrow="none",
            color="#94A3B8")
    return emit(sc, "fig_2_11_data_model", OUT)


# ================================================================ Hình 2.12
def fig_2_12():
    sc = Scene("Hình 2.13 - Các lớp bảo vệ dữ liệu", 1120, 820)
    rings = [
        (40, 40, 1040, 740, "Lớp 1 — Kiến trúc: không tải tệp lên mạng", "ui"),
        (100, 110, 920, 600, "Lớp 2 — Cách ly tiến trình của vỏ Tauri", "native"),
        (160, 180, 800, 460, "Lớp 3 — Kiểm soát nguồn mã thực thi", "accent"),
        (220, 250, 680, 320, "Lớp 4 — Vệ sinh dữ liệu đầu vào", "logic"),
        (280, 320, 560, 180, "Lớp 5 — Mật mã trên tài liệu", "engine"),
    ]
    for x, y, w, h, label, kind in rings:
        sc.group(f"r{y}", x, y, w, h, label, kind)

    sc.node("n1", 300, 350, 520, 60,
            "qpdf-wasm: mã hoá AES-256, đặt mật khẩu người dùng và chủ sở hữu, "
            "cờ hạn chế in/sao chép/sửa",
            kind="engine", shape="round", font_size=11)
    sc.node("n2", 300, 420, 520, 62,
            "zgapdfsigner + node-forge: ký số X.509 từ PFX/PEM, khoá riêng chỉ "
            "tồn tại trong bộ nhớ trang; đóng dấu thời gian RFC 3161",
            kind="engine", shape="round", font_size=11)

    sc.node("n3", 240, 546, 640, 42,
            "sanitize.ts: gỡ JavaScript, tệp nhúng, siêu dữ liệu, chú thích, "
            "liên kết, cây cấu trúc; redact.ts xoá vĩnh viễn nội dung",
            kind="logic", shape="round", font_size=11)
    sc.node("n4", 240, 594, 640, 42,
            "DOMPurify + escapeHtml + sanitizeEmailHtml cho mọi nội dung do tệp "
            "cung cấp; 22 ca kiểm thử tái hiện tấn công XSS",
            kind="logic", shape="round", font_size=11)

    sc.node("n5", 180, 650, 760, 42,
            "WasmProvider: chỉ chấp nhận URL thuộc danh sách máy chủ tin cậy; "
            "URL lạ trong localStorage bị loại bỏ khi khởi động",
            kind="accent", shape="round", font_size=11)

    sc.node("n6", 120, 700, 880, 42,
            "capabilities/default.json chỉ cấp core:default — WebView không có "
            "quyền hệ tệp; mọi thao tác ghi đi qua lệnh save_file của Rust",
            kind="native", shape="round", font_size=11)

    sc.node("n7", 60, 748, 1000, 26,
            "Không có tài khoản, không có phiên đăng nhập, không có nhật ký phía "
            "máy chủ, không có dữ liệu đo đạc gửi đi",
            kind="ui", shape="round", font_size=11)
    return emit(sc, "fig_2_13_security_layers", OUT)


# ================================================================ Hình 2.13
def fig_2_13():
    sc = Scene("Hình 2.12 - Cấu trúc điều hướng giao diện", 1160, 760)
    sc.node("home", 430, 40, 300, 66, "Màn hình làm việc (index.html)",
            sub="thanh bên + lưới thẻ công cụ + ô tìm kiếm",
            kind="ui", shape="round", font_size=12, bold=True)

    cats = [
        ("c1", 30, "Popular Tools (12)"),
        ("c2", 190, "Edit & Annotate (20)"),
        ("c3", 350, "Convert to PDF (33)"),
        ("c4", 510, "Convert from PDF (16)"),
        ("c5", 670, "Organize & Manage (27)"),
        ("c6", 830, "Optimize & Repair (10)"),
        ("c7", 990, "Secure PDF (9)"),
    ]
    for nid, x, label in cats:
        sc.node(nid, x, 170, 145, 62, label, kind="accent", shape="round",
                font_size=11)
        sc.edge("home", nid, exit="s", entry="n", color="#4F46E5")

    sc.node("tool", 350, 300, 460, 66,
            "Trang công cụ độc lập (src/pages/<tool>.html)",
            sub="một trang HTML + một mô-đun logic cho mỗi công cụ",
            kind="ui", shape="round", font_size=12, bold=True)
    for nid, _, _ in cats:
        sc.edge(nid, "tool", exit="s", entry="n", color="#0284C7")

    steps = [
        ("t1", 40, "Khu vực nạp tệp\n(drop-zone + input)"),
        ("t2", 240, "Bảng tham số\ncủa công cụ"),
        ("t3", 440, "Xem trước trang\n/ kéo thả sắp xếp"),
        ("t4", 640, "Nút xử lý\n+ loader tiến trình"),
        ("t5", 840, "Hộp thoại lưu\ncủa hệ điều hành"),
    ]
    for nid, x, label in steps:
        sc.node(nid, x, 430, 180, 62, label, kind="logic", shape="round",
                font_size=11)
    for a, b in zip([s[0] for s in steps], [s[0] for s in steps][1:]):
        sc.edge(a, b, exit="e", entry="w", style="straight")
    sc.edge("tool", "t1", exit="s", entry="n",
            waypoints=[(580, 400), (130, 400)], color="#059669")

    sc.node("m1", 40, 560, 260, 60, "Hộp thoại thông báo",
            sub="showAlert(title, message, type)", kind="warn", shape="round",
            font_size=11)
    sc.node("m2", 330, 560, 260, 60, "Hộp thoại nhập mật khẩu",
            sub="đơn lẻ và theo lô", kind="warn", shape="round", font_size=11)
    sc.node("m3", 620, 560, 260, 60, "Hộp thoại yêu cầu mô-đun WASM",
            sub="showWasmRequiredDialog()", kind="warn", shape="round",
            font_size=11)
    sc.node("m4", 910, 560, 210, 60, "Cài đặt / phím tắt",
            sub="settings-modal.html", kind="warn", shape="round", font_size=11)
    for m in ("m1", "m2", "m3", "m4"):
        sc.edge("tool", m, exit="s", entry="n", dashed=True, color="#DC2626",
                waypoints=[(580, 530)])

    sc.node("sp", 40, 670, 1080, 56,
            "Trang phụ trợ dùng chung: tools.html · pdf-converter.html · "
            "pdf-editor.html · pdf-security.html · pdf-merge-split.html · "
            "wasm-settings.html · about / faq / privacy / terms / licensing / 404",
            kind="neutral", shape="round", font_size=11)
    sc.edge("home", "sp", exit="w", entry="n",
            waypoints=[(20, 73), (20, 640), (580, 640)], dashed=True,
            color="#94A3B8")
    return emit(sc, "fig_2_12_navigation", OUT)


if __name__ == "__main__":
    for fn in [fig_2_1, fig_2_2, fig_2_3, fig_2_4, fig_2_5, fig_2_6, fig_2_7,
               fig_2_8, fig_2_9, fig_2_10, fig_2_11, fig_2_12, fig_2_13]:
        print("ok", fn())
