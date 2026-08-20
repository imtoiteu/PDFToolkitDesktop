# FIGURE INDEX — Báo cáo đề tài PDF Toolkit Desktop

Bảng chỉ mục toàn bộ hình vẽ của báo cáo `BAO_CAO_DE_TAI_PDFTOOLKIT_DESKTOP.docx`.

Mọi sơ đồ kỹ thuật đều được sinh từ một mô tả duy nhất và xuất ra hai định dạng: `.drawio` (đối tượng mxGraph gốc, mọi hộp / mũi tên / nhãn đều chỉnh sửa được trong diagrams.net) và `.svg` (vector, được chèn vào tệp Word). Bản SVG được nhúng vào Word bằng phần mở rộng `asvg:svgBlip` kèm một ảnh PNG độ phân giải cao làm bản dự phòng cho trình đọc cũ.

## Quy ước trạng thái

| Trạng thái | Ý nghĩa |
| --- | --- |
| `GENERATED` | Sơ đồ đã sinh đầy đủ từ bằng chứng mã nguồn, có cả `.drawio` và `.svg`, đã chèn vào Word |
| `GENERATED_WITH_LIMITATIONS` | Đã sinh nhưng một phần nội dung là phương pháp/đề xuất chứ không phải số đo thực tế |
| `MANUAL_SCREENSHOT_REQUIRED` | Cần ảnh chụp màn hình ứng dụng thật; trong Word hiện là khung giữ chỗ |

## Bảng chỉ mục hình

| Hình | Tiêu đề | Bằng chứng mã nguồn | Draw.io | SVG | Đã chèn Word | Trạng thái |
| --- | --- | --- | --- | --- | --- | --- |
| Hình 2.1 | Biểu đồ ca sử dụng tổng quát của hệ thống PDF Toolkit Desktop | src/js/config/tools.ts (7 nhóm, 127 mục); src/js/logic/* (132 mô-đun); src/js/config/timestamp-tsa.ts; src-tauri/src/lib.rs (save_file) | `drawio/fig_2_1_use_case.drawio` | `svg/fig_2_1_use_case.svg` | Có | GENERATED |
| Hình 2.2 | Biểu đồ ngữ cảnh của hệ thống PDF Toolkit Desktop | src-tauri/tauri.conf.json; src-tauri/capabilities/default.json; .env.tauri; src/js/utils/wasm-provider.ts; wasm/ (121 MB); src/js/config/timestamp-tsa.ts; src/js/utils/font-loader.ts | `drawio/fig_2_2_context.drawio` | `svg/fig_2_2_context.svg` | Có | GENERATED |
| Hình 2.3 | Kiến trúc phân tầng tổng thể của hệ thống | src-tauri/src/{main.rs,lib.rs}; src-tauri/tauri.conf.json (app.security.headers); src/js/{main.ts,ui.ts,state.ts}; src/js/logic/ (47.499 dòng); src/js/utils/ (43 mô-đun); package.json (danh sách thư viện) | `drawio/fig_2_3_layered_architecture.drawio` | `svg/fig_2_3_layered_architecture.svg` | Có | GENERATED |
| Hình 2.4 | Kiến trúc thành phần và quan hệ phụ thuộc giữa các mô-đun | Câu lệnh import trong src/js/main.ts, src/js/logic/*.ts, src/js/workflow/*.ts, src/js/utils/*.ts; public/workers/*.js; public/locales/vi/{common,tools}.json | `drawio/fig_2_4_component_architecture.drawio` | `svg/fig_2_4_component_architecture.svg` | Có | GENERATED |
| Hình 2.5 | Kiến trúc triển khai của hệ thống qua ba giai đoạn | package.json (scripts build:tauri, tauri:build); scripts/copy-wasm-to-dist.mjs; src-tauri/Cargo.toml; .github/workflows/desktop-build.yml (ma trận 4 cấu hình); DESKTOP.md | `drawio/fig_2_5_deployment.drawio` | `svg/fig_2_5_deployment.svg` | Có | GENERATED |
| Hình 2.6 | Quy trình xử lý tài liệu tổng quát của hệ thống | src/js/logic/merge-pdf-page.ts; src/js/logic/encrypt-pdf-page.ts; src/js/utils/password-prompt.ts; src/js/utils/wasm-provider.ts (requireWasm); src/js/utils/helpers.ts (downloadFile); src/js/ui.ts | `drawio/fig_2_6_processing_pipeline.drawio` | `svg/fig_2_6_processing_pipeline.svg` | Có | GENERATED |
| Hình 2.7 | Bản đồ phân bổ thao tác cho các động cơ xử lý | package.json (dependencies); src/js/utils/{cpdf-helper,pymupdf-loader,ghostscript-loader,tesseract-runtime}.ts; src/js/utils/helpers.ts (initializeQpdf); src/js/logic/digital-sign-pdf.ts | `drawio/fig_2_7_engine_routing.drawio` | `svg/fig_2_7_engine_routing.svg` | Có | GENERATED |
| Hình 2.8 | Biểu đồ tuần tự quá trình ghép nhiều tài liệu PDF | src/js/logic/merge-pdf-page.ts (merge, refreshMergeUI); public/workers/merge.worker.js (mergePDFs); src/js/utils/password-prompt.ts (batchDecryptIfNeeded); src/js/utils/helpers.ts (downloadFile); src-tauri/src/lib.rs | `drawio/fig_2_8_sequence_merge.drawio` | `svg/fig_2_8_sequence_merge.svg` | Có | GENERATED |
| Hình 2.9 | Biểu đồ tuần tự quá trình mã hoá tài liệu PDF | src/js/logic/encrypt-pdf-page.ts (encryptPdf); src/js/utils/helpers.ts (initializeQpdf); public/qpdf.wasm | `drawio/fig_2_9_sequence_encrypt.drawio` | `svg/fig_2_9_sequence_encrypt.svg` | Có | GENERATED |
| Hình 2.10 | Mô hình thực thi của luồng xử lý tự động | src/js/workflow/engine.ts (getUpstreamNodes, topologicalSort, validateEncryptOrdering, executeWorkflow); src/js/workflow/{editor,serialization,types,errors}.ts; src/js/workflow/nodes/ (79 tệp) | `drawio/fig_2_10_workflow_engine.drawio` | `svg/fig_2_10_workflow_engine.svg` | Có | GENERATED |
| Hình 2.11 | Mô hình dữ liệu trong bộ nhớ và dữ liệu cấu hình bền vững | src/js/workflow/types.ts (PDFData, ImageData, MultiPDFData); src/js/state.ts; src/js/utils/wasm-provider.ts (STORAGE_KEY); src/js/i18n/i18n.ts (i18nextLng) | `drawio/fig_2_11_data_model.drawio` | `svg/fig_2_11_data_model.svg` | Có | GENERATED |
| Hình 2.12 | Cấu trúc điều hướng của giao diện người dùng | src/js/main.ts (dựng thanh bên và lưới thẻ công cụ); src/js/config/tools.ts; vite.config.ts (131 điểm vào); src/partials/*.html; src/js/utils/password-prompt.ts | `drawio/fig_2_12_navigation.drawio` | `svg/fig_2_12_navigation.svg` | Có | GENERATED |
| Hình 2.13 | Mô hình năm lớp bảo vệ dữ liệu của hệ thống | src-tauri/capabilities/default.json; src-tauri/tauri.conf.json; src/js/utils/wasm-provider.ts (BUILTIN_TRUSTED_HOSTS); src/js/utils/sanitize.ts; src/js/utils/helpers.ts (escapeHtml, sanitizeEmailHtml); src/js/logic/{encrypt-pdf-page,digital-sign-pdf}.ts | `drawio/fig_2_13_security_layers.drawio` | `svg/fig_2_13_security_layers.svg` | Có | GENERATED |
| Hình 3.1 | Cấu trúc mã nguồn và môi trường phát triển của hệ thống | Cây thư mục kho mã; thống kê số dòng bằng wc -l; du -sm wasm/*; package.json; src-tauri/Cargo.toml; .github/workflows/ | `drawio/fig_3_1_source_tree.drawio` | `svg/fig_3_1_source_tree.svg` | Có | GENERATED |
| Hình 3.2 | Khuôn mẫu hiện thực một công cụ trong hệ thống | src/pages/merge-pdf.html (khuôn mẫu HTML); src/js/logic/{merge-pdf-page,encrypt-pdf-page,compress-pdf-page}.ts; src/js/ui.ts | `drawio/fig_3_2_tool_template.drawio` | `svg/fig_3_2_tool_template.svg` | Có | GENERATED |
| Hình 3.3 | Màn hình làm việc chính của PDF Toolkit Desktop | — (ảnh giao diện thực tế) | — | — | Khung giữ chỗ | MANUAL_SCREENSHOT_REQUIRED |
| Hình 3.4 | Thanh bên danh mục và chức năng tìm kiếm công cụ | — (ảnh giao diện thực tế) | — | — | Khung giữ chỗ | MANUAL_SCREENSHOT_REQUIRED |
| Hình 3.5 | Cơ chế lưu tệp bản địa qua lệnh save_file của tầng Rust | src/js/utils/helpers.ts (isTauriRuntime, browserDownload, tauriSaveFile, downloadFile); src-tauri/src/lib.rs (save_file); src-tauri/capabilities/default.json | `drawio/fig_3_5_native_save.drawio` | `svg/fig_3_5_native_save.svg` | Có | GENERATED |
| Hình 3.6 | Cơ chế đa ngữ và điều kiện bảo vệ cho bản dựng desktop | src/js/i18n/i18n.ts (getLanguageFromUrl, initI18n, applyTranslations, rewriteLinks); src/js/main.ts (đặt mặc định 'vi'); scripts/generate-i18n-pages.mjs; commit 4a63fa9 | `drawio/fig_3_6_i18n.drawio` | `svg/fig_3_6_i18n.svg` | Có | GENERATED |
| Hình 3.7 | Cơ chế giải quyết nguồn mô-đun WebAssembly cho bản desktop | .env.tauri (7 biến); src/js/utils/wasm-provider.ts; src/js/utils/{pymupdf-loader,ghostscript-loader,cpdf-helper,tesseract-runtime}.ts; scripts/copy-wasm-to-dist.mjs; src-tauri/tauri.conf.json (COOP/COEP) | `drawio/fig_3_7_wasm_resolution.drawio` | `svg/fig_3_7_wasm_resolution.svg` | Có | GENERATED |
| Hình 3.8 | Hai chiến lược nén tài liệu và tham số của từng chiến lược | src/js/utils/compress.ts (CONDENSE_PRESETS, PHOTON_PRESETS, performCondenseCompression, performPhotonCompression); src/js/logic/compress-pdf-page.ts | `drawio/fig_3_8_compression.drawio` | `svg/fig_3_8_compression.svg` | Có | GENERATED |
| Hình 3.9 | Chuỗi xử lý của chức năng nhận dạng ký tự quang học | src/js/utils/ocr.ts (performOcr, drawOcrTextLayer, binarizeCanvas, recognizeWithTimeout); src/js/utils/hocr-transform.ts; src/js/utils/{tesseract-runtime,font-loader}.ts; src/js/config/font-mappings.ts | `drawio/fig_3_9_ocr_pipeline.drawio` | `svg/fig_3_9_ocr_pipeline.svg` | Có | GENERATED |
| Hình 3.10 | Giao diện trình dựng luồng xử lý tự động | — (ảnh giao diện thực tế) | — | — | Khung giữ chỗ | MANUAL_SCREENSHOT_REQUIRED |
| Hình 3.11 | Các cơ chế quản lý dữ liệu tạm và bộ nhớ | src/js/logic/encrypt-pdf-page.ts (khối finally, FS.unlink); src/js/utils/ocr.ts (PDF_CLEANUP_INTERVAL_PAGES); src/js/utils/compress.ts (giải phóng canvas); public/workers/merge.worker.js (deletePdf); src/js/utils/helpers.ts (revokeObjectURL) | `drawio/fig_3_11_temp_data.drawio` | `svg/fig_3_11_temp_data.svg` | Có | GENERATED |
| Hình 3.12 | Chiến lược xử lý lỗi và phản hồi cho người dùng | src/js/ui.ts (showAlert, showLoader); src/js/utils/pdf-decrypt.ts (normalizeErrorMessage, thử tuần tự); src/js/utils/wasm-provider.ts (showWasmRequiredDialog); src/js/utils/ocr.ts (OcrWarning) | `drawio/fig_3_12_error_handling.drawio` | `svg/fig_3_12_error_handling.svg` | Có | GENERATED |
| Hình 3.13 | Quy trình biên dịch và đóng gói ứng dụng desktop | package.json (scripts); src-tauri/tauri.conf.json (beforeBuildCommand); scripts/copy-wasm-to-dist.mjs; src-tauri/Cargo.toml (profile.release); .github/workflows/desktop-build.yml; DESKTOP.md (mục Output location) | `drawio/fig_3_13_build_pipeline.drawio` | `svg/fig_3_13_build_pipeline.svg` | Có | GENERATED |
| Hình 3.14 | Giao diện công cụ ghép tài liệu ở hai chế độ làm việc | — (ảnh giao diện thực tế) | — | — | Khung giữ chỗ | MANUAL_SCREENSHOT_REQUIRED |
| Hình 3.15 | Giao diện công cụ tách và tổ chức lại trang | — (ảnh giao diện thực tế) | — | — | Khung giữ chỗ | MANUAL_SCREENSHOT_REQUIRED |
| Hình 3.16 | Giao diện công cụ nén tài liệu và kết quả so sánh dung lượng | — (ảnh giao diện thực tế) | — | — | Khung giữ chỗ | MANUAL_SCREENSHOT_REQUIRED |
| Hình 3.17 | Giao diện chức năng mã hoá và giải mã tài liệu | — (ảnh giao diện thực tế) | — | — | Khung giữ chỗ | MANUAL_SCREENSHOT_REQUIRED |
| Hình 3.18 | Giao diện chức năng nhận dạng ký tự quang học | — (ảnh giao diện thực tế) | — | — | Khung giữ chỗ | MANUAL_SCREENSHOT_REQUIRED |
| Hình 3.19 | Hộp thoại lưu tệp bản địa của hệ điều hành | — (ảnh giao diện thực tế) | — | — | Khung giữ chỗ | MANUAL_SCREENSHOT_REQUIRED |
| Hình 3.20 | Trang cấu hình nguồn mô-đun xử lý và bộ chọn ngôn ngữ | — (ảnh giao diện thực tế) | — | — | Khung giữ chỗ | MANUAL_SCREENSHOT_REQUIRED |
| Hình 4.1 | Kiến trúc môi trường thử nghiệm của hệ thống | vite.config.ts (khối test); src/tests/setup.ts; package.json (scripts test, lint, security); eslint.config.mjs; .github/workflows/{codeql,trivy-scan}.yml; DESKTOP.md (Smoke test checklist) | `drawio/fig_4_1_test_environment.drawio` | `svg/fig_4_1_test_environment.svg` | Có | GENERATED_WITH_LIMITATIONS |
| Hình 4.2 | Phân bố ca kiểm thử tự động theo nhóm chức năng | Đếm trực tiếp lời gọi it()/test() trong src/tests/ — 39 tệp, 641 ca | `drawio/fig_4_2_test_distribution.drawio` | `svg/fig_4_2_test_distribution.svg` | Có | GENERATED |
| Hình 4.3 | Quy trình kiểm thử chức năng đối với một công cụ | DESKTOP.md (Smoke test checklist); src/js/logic/*-page.ts (các nhánh kiểm tra đầu vào); src/js/utils/helpers.ts (parsePageRanges) | `drawio/fig_4_3_functional_test_flow.drawio` | `svg/fig_4_3_functional_test_flow.svg` | Có | GENERATED_WITH_LIMITATIONS |
| Hình 4.4 | Kiểm chứng khả năng hoạt động ngoại tuyến qua tab mạng của công cụ phát triển | — (ảnh giao diện thực tế) | — | — | Khung giữ chỗ | MANUAL_SCREENSHOT_REQUIRED |
| Hình 4.5 | Cấu thành dung lượng tài nguyên WebAssembly đóng gói kèm ứng dụng | du -sm wasm/* và du -sm wasm/ocr/*, wasm/pymupdf/assets; ls -la public/{qpdf.wasm,coherentpdf.browser.min.js}; DESKTOP.md (Known limitations — bundle size) | `drawio/fig_4_5_bundle_composition.drawio` | `svg/fig_4_5_bundle_composition.svg` | Có | GENERATED |
| Hình 4.6 | Khung tiêu chí đánh giá hệ thống và trạng thái thực hiện | Tổng hợp từ yêu cầu phi chức năng (Chương 2) và bằng chứng đã nêu ở các hình 3.7, 4.2 và 4.5 | `drawio/fig_4_6_evaluation_criteria.drawio` | `svg/fig_4_6_evaluation_criteria.svg` | Có | GENERATED |

## Tổng hợp

| Chỉ tiêu | Số lượng |
| --- | --- |
| Tổng số hình trong báo cáo | 39 |
| Sơ đồ kỹ thuật đã sinh (GENERATED) | 26 |
| Sơ đồ đã sinh có giới hạn (GENERATED_WITH_LIMITATIONS) | 2 |
| Khung giữ chỗ cần ảnh chụp thủ công | 11 |
| Tệp `.drawio` | 28 |
| Tệp `.svg` | 28 |
| Ảnh chụp màn hình đã có | 0 |

## Chưa được hỗ trợ bởi mã nguồn (NOT_SUPPORTED_BY_SOURCE)

Những loại sơ đồ sau **không được vẽ** vì mã nguồn không hiện thực thành phần tương ứng. Việc vẽ chúng sẽ là bịa đặt kiến trúc:

- Sơ đồ thực thể quan hệ / lược đồ cơ sở dữ liệu — hệ thống không có cơ sở dữ liệu; dữ liệu bền vững duy nhất là ba khoá trong `localStorage` (xem Hình 2.11).
- Sơ đồ luồng gọi API máy chủ — không có máy chủ ứng dụng, không có điểm cuối API nào trong kho mã của bản desktop.
- Sơ đồ xác thực / phân quyền người dùng — không có tài khoản, không có phiên đăng nhập, không có vai trò (xem Hình 2.1).
- Sơ đồ hàng đợi tác vụ hoặc bộ điều phối tác vụ nền — xử lý diễn ra đồng bộ trên luồng chính hoặc trong Web Worker theo từng thao tác.
- Sơ đồ kiến trúc microservice / dịch vụ đám mây — không tồn tại trong bản desktop.
- Biểu đồ thời gian xử lý và mức tiêu thụ bộ nhớ — chưa có số đo thực tế; phương pháp đo được trình bày ở Bảng 4.7 thay cho biểu đồ bịa số liệu.

## Cách tái sinh toàn bộ hình

```bash
cd report_figures/tools
python3 fig_ch2.py     # Hình 2.1 – 2.13
python3 fig_ch3.py     # Hình 3.1 – 3.13 (phần sơ đồ)
python3 fig_ch4.py     # Hình 4.1 – 4.5
python3 make_report.py # dựng lại tệp Word
python3 make_index.py  # dựng lại hai tệp chỉ mục này
```
