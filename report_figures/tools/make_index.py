#!/usr/bin/env python3
"""Sinh FIGURE_INDEX.md và MANUAL_SCREENSHOTS.md từ chính nội dung báo cáo."""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Bằng chứng mã nguồn cho từng hình — đối chiếu trực tiếp với kho mã.
EVIDENCE = {
    "fig_2_1_use_case":
        "src/js/config/tools.ts (7 nhóm, 127 mục); src/js/logic/* (132 mô-đun); "
        "src/js/config/timestamp-tsa.ts; src-tauri/src/lib.rs (save_file)",
    "fig_2_2_context":
        "src-tauri/tauri.conf.json; src-tauri/capabilities/default.json; "
        ".env.tauri; src/js/utils/wasm-provider.ts; wasm/ (121 MB); "
        "src/js/config/timestamp-tsa.ts; src/js/utils/font-loader.ts",
    "fig_2_3_layered_architecture":
        "src-tauri/src/{main.rs,lib.rs}; src-tauri/tauri.conf.json (app.security."
        "headers); src/js/{main.ts,ui.ts,state.ts}; src/js/logic/ (47.499 dòng); "
        "src/js/utils/ (43 mô-đun); package.json (danh sách thư viện)",
    "fig_2_4_component_architecture":
        "Câu lệnh import trong src/js/main.ts, src/js/logic/*.ts, "
        "src/js/workflow/*.ts, src/js/utils/*.ts; public/workers/*.js; "
        "public/locales/vi/{common,tools}.json",
    "fig_2_5_deployment":
        "package.json (scripts build:tauri, tauri:build); "
        "scripts/copy-wasm-to-dist.mjs; src-tauri/Cargo.toml; "
        ".github/workflows/desktop-build.yml (ma trận 4 cấu hình); DESKTOP.md",
    "fig_2_6_processing_pipeline":
        "src/js/logic/merge-pdf-page.ts; src/js/logic/encrypt-pdf-page.ts; "
        "src/js/utils/password-prompt.ts; src/js/utils/wasm-provider.ts "
        "(requireWasm); src/js/utils/helpers.ts (downloadFile); src/js/ui.ts",
    "fig_2_7_engine_routing":
        "package.json (dependencies); src/js/utils/{cpdf-helper,pymupdf-loader,"
        "ghostscript-loader,tesseract-runtime}.ts; src/js/utils/helpers.ts "
        "(initializeQpdf); src/js/logic/digital-sign-pdf.ts",
    "fig_2_8_sequence_merge":
        "src/js/logic/merge-pdf-page.ts (merge, refreshMergeUI); "
        "public/workers/merge.worker.js (mergePDFs); "
        "src/js/utils/password-prompt.ts (batchDecryptIfNeeded); "
        "src/js/utils/helpers.ts (downloadFile); src-tauri/src/lib.rs",
    "fig_2_9_sequence_encrypt":
        "src/js/logic/encrypt-pdf-page.ts (encryptPdf); "
        "src/js/utils/helpers.ts (initializeQpdf); public/qpdf.wasm",
    "fig_2_10_workflow_engine":
        "src/js/workflow/engine.ts (getUpstreamNodes, topologicalSort, "
        "validateEncryptOrdering, executeWorkflow); src/js/workflow/"
        "{editor,serialization,types,errors}.ts; src/js/workflow/nodes/ (79 tệp)",
    "fig_2_11_data_model":
        "src/js/workflow/types.ts (PDFData, ImageData, MultiPDFData); "
        "src/js/state.ts; src/js/utils/wasm-provider.ts (STORAGE_KEY); "
        "src/js/i18n/i18n.ts (i18nextLng)",
    "fig_2_12_navigation":
        "src/js/main.ts (dựng thanh bên và lưới thẻ công cụ); "
        "src/js/config/tools.ts; vite.config.ts (131 điểm vào); "
        "src/partials/*.html; src/js/utils/password-prompt.ts",
    "fig_2_13_security_layers":
        "src-tauri/capabilities/default.json; src-tauri/tauri.conf.json; "
        "src/js/utils/wasm-provider.ts (BUILTIN_TRUSTED_HOSTS); "
        "src/js/utils/sanitize.ts; src/js/utils/helpers.ts (escapeHtml, "
        "sanitizeEmailHtml); src/js/logic/{encrypt-pdf-page,digital-sign-pdf}.ts",
    "fig_3_1_source_tree":
        "Cây thư mục kho mã; thống kê số dòng bằng wc -l; du -sm wasm/*; "
        "package.json; src-tauri/Cargo.toml; .github/workflows/",
    "fig_3_2_tool_template":
        "src/pages/merge-pdf.html (khuôn mẫu HTML); src/js/logic/"
        "{merge-pdf-page,encrypt-pdf-page,compress-pdf-page}.ts; src/js/ui.ts",
    "fig_3_5_native_save":
        "src/js/utils/helpers.ts (isTauriRuntime, browserDownload, "
        "tauriSaveFile, downloadFile); src-tauri/src/lib.rs (save_file); "
        "src-tauri/capabilities/default.json",
    "fig_3_6_i18n":
        "src/js/i18n/i18n.ts (getLanguageFromUrl, initI18n, applyTranslations, "
        "rewriteLinks); src/js/main.ts (đặt mặc định 'vi'); "
        "scripts/generate-i18n-pages.mjs; commit 4a63fa9",
    "fig_3_7_wasm_resolution":
        ".env.tauri (7 biến); src/js/utils/wasm-provider.ts; "
        "src/js/utils/{pymupdf-loader,ghostscript-loader,cpdf-helper,"
        "tesseract-runtime}.ts; scripts/copy-wasm-to-dist.mjs; "
        "src-tauri/tauri.conf.json (COOP/COEP)",
    "fig_3_8_compression":
        "src/js/utils/compress.ts (CONDENSE_PRESETS, PHOTON_PRESETS, "
        "performCondenseCompression, performPhotonCompression); "
        "src/js/logic/compress-pdf-page.ts",
    "fig_3_9_ocr_pipeline":
        "src/js/utils/ocr.ts (performOcr, drawOcrTextLayer, binarizeCanvas, "
        "recognizeWithTimeout); src/js/utils/hocr-transform.ts; "
        "src/js/utils/{tesseract-runtime,font-loader}.ts; "
        "src/js/config/font-mappings.ts",
    "fig_3_11_temp_data":
        "src/js/logic/encrypt-pdf-page.ts (khối finally, FS.unlink); "
        "src/js/utils/ocr.ts (PDF_CLEANUP_INTERVAL_PAGES); "
        "src/js/utils/compress.ts (giải phóng canvas); "
        "public/workers/merge.worker.js (deletePdf); "
        "src/js/utils/helpers.ts (revokeObjectURL)",
    "fig_3_12_error_handling":
        "src/js/ui.ts (showAlert, showLoader); "
        "src/js/utils/pdf-decrypt.ts (normalizeErrorMessage, thử tuần tự); "
        "src/js/utils/wasm-provider.ts (showWasmRequiredDialog); "
        "src/js/utils/ocr.ts (OcrWarning)",
    "fig_3_13_build_pipeline":
        "package.json (scripts); src-tauri/tauri.conf.json (beforeBuildCommand); "
        "scripts/copy-wasm-to-dist.mjs; src-tauri/Cargo.toml (profile.release); "
        ".github/workflows/desktop-build.yml; DESKTOP.md (mục Output location)",
    "fig_4_1_test_environment":
        "vite.config.ts (khối test); src/tests/setup.ts; package.json (scripts "
        "test, lint, security); eslint.config.mjs; .github/workflows/"
        "{codeql,trivy-scan}.yml; DESKTOP.md (Smoke test checklist)",
    "fig_4_2_test_distribution":
        "Đếm trực tiếp lời gọi it()/test() trong src/tests/ — 39 tệp, 641 ca",
    "fig_4_3_functional_test_flow":
        "DESKTOP.md (Smoke test checklist); src/js/logic/*-page.ts (các nhánh "
        "kiểm tra đầu vào); src/js/utils/helpers.ts (parsePageRanges)",
    "fig_4_5_bundle_composition":
        "du -sm wasm/* và du -sm wasm/ocr/*, wasm/pymupdf/assets; "
        "ls -la public/{qpdf.wasm,coherentpdf.browser.min.js}; "
        "DESKTOP.md (Known limitations — bundle size)",
    "fig_4_6_evaluation_criteria":
        "Tổng hợp từ yêu cầu phi chức năng (Chương 2) và bằng chứng đã nêu ở "
        "các hình 3.7, 4.2 và 4.5",
}

FIG_ORDER = [
    ("Hình 2.1", "fig_2_1_use_case",
     "Biểu đồ ca sử dụng tổng quát của hệ thống PDF Toolkit Desktop", "chapter2"),
    ("Hình 2.2", "fig_2_2_context",
     "Biểu đồ ngữ cảnh của hệ thống PDF Toolkit Desktop", "chapter2"),
    ("Hình 2.3", "fig_2_3_layered_architecture",
     "Kiến trúc phân tầng tổng thể của hệ thống", "chapter2"),
    ("Hình 2.4", "fig_2_4_component_architecture",
     "Kiến trúc thành phần và quan hệ phụ thuộc giữa các mô-đun", "chapter2"),
    ("Hình 2.5", "fig_2_5_deployment",
     "Kiến trúc triển khai của hệ thống qua ba giai đoạn", "chapter2"),
    ("Hình 2.6", "fig_2_6_processing_pipeline",
     "Quy trình xử lý tài liệu tổng quát của hệ thống", "chapter2"),
    ("Hình 2.7", "fig_2_7_engine_routing",
     "Bản đồ phân bổ thao tác cho các động cơ xử lý", "chapter2"),
    ("Hình 2.8", "fig_2_8_sequence_merge",
     "Biểu đồ tuần tự quá trình ghép nhiều tài liệu PDF", "chapter2"),
    ("Hình 2.9", "fig_2_9_sequence_encrypt",
     "Biểu đồ tuần tự quá trình mã hoá tài liệu PDF", "chapter2"),
    ("Hình 2.10", "fig_2_10_workflow_engine",
     "Mô hình thực thi của luồng xử lý tự động", "chapter2"),
    ("Hình 2.11", "fig_2_11_data_model",
     "Mô hình dữ liệu trong bộ nhớ và dữ liệu cấu hình bền vững", "chapter2"),
    ("Hình 2.12", "fig_2_12_navigation",
     "Cấu trúc điều hướng của giao diện người dùng", "chapter2"),
    ("Hình 2.13", "fig_2_13_security_layers",
     "Mô hình năm lớp bảo vệ dữ liệu của hệ thống", "chapter2"),
    ("Hình 3.1", "fig_3_1_source_tree",
     "Cấu trúc mã nguồn và môi trường phát triển của hệ thống", "chapter3"),
    ("Hình 3.2", "fig_3_2_tool_template",
     "Khuôn mẫu hiện thực một công cụ trong hệ thống", "chapter3"),
    ("Hình 3.3", None,
     "Màn hình làm việc chính của PDF Toolkit Desktop", "chapter3"),
    ("Hình 3.4", None,
     "Thanh bên danh mục và chức năng tìm kiếm công cụ", "chapter3"),
    ("Hình 3.5", "fig_3_5_native_save",
     "Cơ chế lưu tệp bản địa qua lệnh save_file của tầng Rust", "chapter3"),
    ("Hình 3.6", "fig_3_6_i18n",
     "Cơ chế đa ngữ và điều kiện bảo vệ cho bản dựng desktop", "chapter3"),
    ("Hình 3.7", "fig_3_7_wasm_resolution",
     "Cơ chế giải quyết nguồn mô-đun WebAssembly cho bản desktop", "chapter3"),
    ("Hình 3.8", "fig_3_8_compression",
     "Hai chiến lược nén tài liệu và tham số của từng chiến lược", "chapter3"),
    ("Hình 3.9", "fig_3_9_ocr_pipeline",
     "Chuỗi xử lý của chức năng nhận dạng ký tự quang học", "chapter3"),
    ("Hình 3.10", None,
     "Giao diện trình dựng luồng xử lý tự động", "chapter3"),
    ("Hình 3.11", "fig_3_11_temp_data",
     "Các cơ chế quản lý dữ liệu tạm và bộ nhớ", "chapter3"),
    ("Hình 3.12", "fig_3_12_error_handling",
     "Chiến lược xử lý lỗi và phản hồi cho người dùng", "chapter3"),
    ("Hình 3.13", "fig_3_13_build_pipeline",
     "Quy trình biên dịch và đóng gói ứng dụng desktop", "chapter3"),
    ("Hình 3.14", None,
     "Giao diện công cụ ghép tài liệu ở hai chế độ làm việc", "chapter3"),
    ("Hình 3.15", None,
     "Giao diện công cụ tách và tổ chức lại trang", "chapter3"),
    ("Hình 3.16", None,
     "Giao diện công cụ nén tài liệu và kết quả so sánh dung lượng", "chapter3"),
    ("Hình 3.17", None,
     "Giao diện chức năng mã hoá và giải mã tài liệu", "chapter3"),
    ("Hình 3.18", None,
     "Giao diện chức năng nhận dạng ký tự quang học", "chapter3"),
    ("Hình 3.19", None,
     "Hộp thoại lưu tệp bản địa của hệ điều hành", "chapter3"),
    ("Hình 3.20", None,
     "Trang cấu hình nguồn mô-đun xử lý và bộ chọn ngôn ngữ", "chapter3"),
    ("Hình 4.1", "fig_4_1_test_environment",
     "Kiến trúc môi trường thử nghiệm của hệ thống", "chapter4"),
    ("Hình 4.2", "fig_4_2_test_distribution",
     "Phân bố ca kiểm thử tự động theo nhóm chức năng", "chapter4"),
    ("Hình 4.3", "fig_4_3_functional_test_flow",
     "Quy trình kiểm thử chức năng đối với một công cụ", "chapter4"),
    ("Hình 4.4", None,
     "Kiểm chứng khả năng hoạt động ngoại tuyến qua tab mạng của công cụ phát "
     "triển", "chapter4"),
    ("Hình 4.5", "fig_4_5_bundle_composition",
     "Cấu thành dung lượng tài nguyên WebAssembly đóng gói kèm ứng dụng",
     "chapter4"),
    ("Hình 4.6", "fig_4_6_evaluation_criteria",
     "Khung tiêu chí đánh giá hệ thống và trạng thái thực hiện", "chapter4"),
]


def collect_placeholders():
    """Đọc lại đặc tả khung giữ chỗ từ chính mã sinh báo cáo."""
    import builder
    import content_c
    import content_d

    class Collector(builder.Report):
        def __init__(self):
            super().__init__()

        def figure(self, *a, **k):
            return None

        def table(self, *a, **k):
            return None

        def placeholder(self, fig_label, caption, what, steps):
            self.placeholders.append((fig_label, caption, what, steps))

    c = Collector()
    content_c.build(c)
    content_d.build(c)
    return c.placeholders


def main():
    svg_dir = os.path.join(ROOT, "svg")
    dio_dir = os.path.join(ROOT, "drawio")

    lines = []
    lines.append("# FIGURE INDEX — Báo cáo đề tài PDF Toolkit Desktop\n")
    lines.append(
        "Bảng chỉ mục toàn bộ hình vẽ của báo cáo "
        "`BAO_CAO_DE_TAI_PDFTOOLKIT_DESKTOP.docx`.\n"
    )
    lines.append(
        "Mọi sơ đồ kỹ thuật đều được sinh từ một mô tả duy nhất và xuất ra hai "
        "định dạng: `.drawio` (đối tượng mxGraph gốc, mọi hộp / mũi tên / nhãn "
        "đều chỉnh sửa được trong diagrams.net) và `.svg` (vector, được chèn "
        "vào tệp Word). Bản SVG được nhúng vào Word bằng phần mở rộng "
        "`asvg:svgBlip` kèm một ảnh PNG độ phân giải cao làm bản dự phòng cho "
        "trình đọc cũ.\n"
    )
    lines.append("## Quy ước trạng thái\n")
    lines.append(
        "| Trạng thái | Ý nghĩa |\n"
        "| --- | --- |\n"
        "| `GENERATED` | Sơ đồ đã sinh đầy đủ từ bằng chứng mã nguồn, có cả "
        "`.drawio` và `.svg`, đã chèn vào Word |\n"
        "| `GENERATED_WITH_LIMITATIONS` | Đã sinh nhưng một phần nội dung là "
        "phương pháp/đề xuất chứ không phải số đo thực tế |\n"
        "| `MANUAL_SCREENSHOT_REQUIRED` | Cần ảnh chụp màn hình ứng dụng thật; "
        "trong Word hiện là khung giữ chỗ |\n"
    )

    lines.append("## Bảng chỉ mục hình\n")
    lines.append(
        "| Hình | Tiêu đề | Bằng chứng mã nguồn | Draw.io | SVG | Đã chèn Word | "
        "Trạng thái |"
    )
    lines.append("| --- | --- | --- | --- | --- | --- | --- |")

    n_gen = n_lim = n_manual = 0
    for label, name, title, chapter in FIG_ORDER:
        if name is None:
            lines.append(
                "| %s | %s | — (ảnh giao diện thực tế) | — | — | Khung giữ chỗ | "
                "MANUAL_SCREENSHOT_REQUIRED |" % (label, title)
            )
            n_manual += 1
            continue
        has_svg = os.path.exists(os.path.join(svg_dir, name + ".svg"))
        has_dio = os.path.exists(os.path.join(dio_dir, name + ".drawio"))
        ev = EVIDENCE.get(name, "")
        limited = name in (
            "fig_4_3_functional_test_flow",
            "fig_4_5_evaluation_criteria",
            "fig_4_1_test_environment",
        )
        status = "GENERATED_WITH_LIMITATIONS" if limited else "GENERATED"
        if limited:
            n_lim += 1
        else:
            n_gen += 1
        lines.append(
            "| %s | %s | %s | `drawio/%s.drawio`%s | `svg/%s.svg`%s | Có | %s |"
            % (label, title, ev, name, "" if has_dio else " (THIẾU)",
               name, "" if has_svg else " (THIẾU)", status)
        )

    lines.append("")
    lines.append("## Tổng hợp\n")
    lines.append("| Chỉ tiêu | Số lượng |")
    lines.append("| --- | --- |")
    lines.append("| Tổng số hình trong báo cáo | %d |" % len(FIG_ORDER))
    lines.append("| Sơ đồ kỹ thuật đã sinh (GENERATED) | %d |" % n_gen)
    lines.append(
        "| Sơ đồ đã sinh có giới hạn (GENERATED_WITH_LIMITATIONS) | %d |" % n_lim)
    lines.append("| Khung giữ chỗ cần ảnh chụp thủ công | %d |" % n_manual)
    lines.append("| Tệp `.drawio` | %d |" % len(os.listdir(dio_dir)))
    lines.append("| Tệp `.svg` | %d |" % len(os.listdir(svg_dir)))
    lines.append("| Ảnh chụp màn hình đã có | 0 |")

    lines.append("")
    lines.append("## Chưa được hỗ trợ bởi mã nguồn (NOT_SUPPORTED_BY_SOURCE)\n")
    lines.append(
        "Những loại sơ đồ sau **không được vẽ** vì mã nguồn không hiện thực "
        "thành phần tương ứng. Việc vẽ chúng sẽ là bịa đặt kiến trúc:\n"
    )
    lines.append(
        "- Sơ đồ thực thể quan hệ / lược đồ cơ sở dữ liệu — hệ thống không có "
        "cơ sở dữ liệu; dữ liệu bền vững duy nhất là ba khoá trong "
        "`localStorage` (xem Hình 2.11).\n"
        "- Sơ đồ luồng gọi API máy chủ — không có máy chủ ứng dụng, không có "
        "điểm cuối API nào trong kho mã của bản desktop.\n"
        "- Sơ đồ xác thực / phân quyền người dùng — không có tài khoản, không "
        "có phiên đăng nhập, không có vai trò (xem Hình 2.1).\n"
        "- Sơ đồ hàng đợi tác vụ hoặc bộ điều phối tác vụ nền — xử lý diễn ra "
        "đồng bộ trên luồng chính hoặc trong Web Worker theo từng thao tác.\n"
        "- Sơ đồ kiến trúc microservice / dịch vụ đám mây — không tồn tại "
        "trong bản desktop.\n"
        "- Biểu đồ thời gian xử lý và mức tiêu thụ bộ nhớ — chưa có số đo "
        "thực tế; phương pháp đo được trình bày ở Bảng 4.7 thay cho biểu đồ "
        "bịa số liệu.\n"
    )

    lines.append("## Cách tái sinh toàn bộ hình\n")
    lines.append("```bash")
    lines.append("cd report_figures/tools")
    lines.append("python3 fig_ch2.py     # Hình 2.1 – 2.13")
    lines.append("python3 fig_ch3.py     # Hình 3.1 – 3.13 (phần sơ đồ)")
    lines.append("python3 fig_ch4.py     # Hình 4.1 – 4.5")
    lines.append("python3 make_report.py # dựng lại tệp Word")
    lines.append("python3 make_index.py  # dựng lại hai tệp chỉ mục này")
    lines.append("```")

    with open(os.path.join(ROOT, "FIGURE_INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    # ------------------------------------------------------------------
    phs = collect_placeholders()
    out = []
    out.append("# MANUAL SCREENSHOTS — danh sách ảnh cần chụp thủ công\n")
    out.append(
        "Báo cáo `BAO_CAO_DE_TAI_PDFTOOLKIT_DESKTOP.docx` hiện có **%d khung "
        "giữ chỗ** cho ảnh chụp giao diện. Các ảnh này không thể chụp tự động "
        "trên máy chủ phân tích vì máy không có giao diện đồ hoạ và không đủ "
        "tài nguyên để biên dịch ứng dụng (chi tiết ở Bảng 4.1 của báo cáo).\n"
        % len(phs)
    )
    out.append("## Chuẩn bị chung\n")
    out.append(
        "1. Dùng máy có giao diện đồ hoạ, cài **Node.js ≥ 20** và "
        "**Rust ≥ 1.77.2**.\n"
        "2. Cài phụ thuộc hệ thống theo nền tảng (xem `DESKTOP.md`).\n"
        "3. Chạy `npm install`, sau đó `npm run tauri:dev` để chạy bản phát "
        "triển, hoặc `npm run tauri:build` rồi cài đặt gói sinh ra.\n"
        "4. Đặt ngôn ngữ giao diện là **tiếng Việt** trước khi chụp, để ảnh "
        "khớp với nội dung báo cáo.\n"
        "5. Chuẩn bị sẵn bộ tệp mẫu theo Bảng 4.2 của báo cáo.\n"
        "6. Chụp ở độ phân giải tối thiểu **1600 × 1000** để chữ trong ảnh còn "
        "đọc được khi in, lưu ở định dạng **PNG**.\n"
        "7. Đặt tệp ảnh vào thư mục `report_figures/screenshots/` theo đúng tên "
        "gợi ý ở từng mục dưới đây.\n"
    )
    out.append("## Danh sách ảnh cần chụp\n")
    for label, caption, what, steps in phs:
        num = label.replace("Hình ", "").replace(".", "_")
        out.append("### %s\n" % label)
        out.append("**Chú thích trong báo cáo:** %s\n" % caption)
        out.append("**Tên tệp gợi ý:** `screenshots/hinh_%s.png`\n" % num)
        out.append("**Nội dung cần thể hiện:** %s\n" % what)
        out.append("**Các bước thực hiện:**\n")
        for i, st in enumerate(steps):
            out.append("%d. %s" % (i + 1, st))
        out.append("")
    out.append("## Cách chèn ảnh vào báo cáo\n")
    out.append(
        "Có hai cách. Cách thủ công: mở tệp Word, tìm khung màu cam có dòng "
        "`[CHỖ DÀNH CHO ẢNH CHỤP MÀN HÌNH – Hình x.y]`, xoá khung đó và chèn "
        "ảnh vào đúng vị trí, giữ nguyên dòng chú thích bên dưới.\n"
    )
    out.append(
        "Cách tự động: đặt các tệp ảnh vào `report_figures/screenshots/` theo "
        "đúng tên gợi ý, sau đó sửa lời gọi `r.placeholder(...)` tương ứng "
        "trong `report_figures/tools/content_c.py` và `content_d.py` thành "
        "`r.screenshot(\"hinh_x_y.png\", \"<chú thích>\")` rồi chạy lại "
        "`python3 make_report.py`.\n"
    )
    with open(os.path.join(ROOT, "MANUAL_SCREENSHOTS.md"), "w",
              encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")

    print("FIGURE_INDEX.md và MANUAL_SCREENSHOTS.md đã được sinh.")
    print("Hình tổng:", len(FIG_ORDER), "| GENERATED:", n_gen,
          "| GIỚI HẠN:", n_lim, "| CẦN CHỤP:", n_manual)


if __name__ == "__main__":
    main()
