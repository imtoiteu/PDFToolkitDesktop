#!/usr/bin/env python3
"""Sinh các hình chương 4 — Thử nghiệm và đánh giá hệ thống."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagramlib import Scene, emit  # noqa: E402

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def bar_chart(sc, x0, y0, w, h, data, unit="", kind="ui", max_val=None,
              label_w=250, bar_h=32, gap=14, note=None):
    """Biểu đồ cột ngang; mỗi cột là một hình chữ nhật độc lập, chỉnh sửa được."""
    mx = max_val or max(v for _, v in data)
    plot_w = w - label_w - 90
    y = y0
    for i, (name, val) in enumerate(data):
        sc.node(f"lbl{y0}_{i}", x0, y, label_w, bar_h, name, kind="neutral",
                shape="rect", font_size=11, align="left")
        bw = max(4, plot_w * val / mx)
        sc.node(f"bar{y0}_{i}", x0 + label_w + 10, y, bw, bar_h, "",
                kind=kind, shape="rect")
        sc.text(x0 + label_w + 20 + bw, y + bar_h / 2 + 4,
                f"{val:g}{unit}", size=11, bold=True, anchor="start",
                color="#0F172A")
        y += bar_h + gap
    # trục
    sc.node(f"ax{y0}", x0 + label_w + 8, y0 - 4, 2, y - y0 - gap + 8, "",
            kind="neutral", shape="rect")
    if note:
        sc.text(x0, y + 8, note, size=10, anchor="start", color="#475569")
    return y


# ================================================================= Hình 4.1
def fig_4_1():
    sc = Scene("Hình 4.1 - Kiến trúc môi trường thử nghiệm", 1160, 760)

    sc.group("g1", 40, 40, 540, 320, "Kiểm thử tự động (bộ kiểm thử có sẵn trong kho mã)", "logic")
    sc.node("vt", 66, 92, 488, 60, "Vitest 4 + môi trường jsdom 28",
            sub="cấu hình trong vite.config.ts → test", kind="logic",
            shape="round")
    sc.node("setup", 66, 164, 488, 56, "src/tests/setup.ts",
            sub="thiết lập chung trước mỗi bộ kiểm thử", kind="logic",
            shape="round")
    sc.node("cov", 66, 232, 488, 56, "Đo độ phủ bằng @vitest/coverage-v8",
            sub="npm run test:coverage", kind="logic", shape="round")
    sc.node("cmd", 66, 300, 488, 44,
            "npm run test  ·  test:run  ·  test:ui  ·  test:watch",
            kind="accent", shape="rect", font_size=11)

    sc.group("g2", 620, 40, 500, 320, "Phân tích tĩnh và quét bảo mật", "warn")
    sc.node("es", 646, 92, 448, 60, "ESLint 10 + typescript-eslint",
            sub="eslint-plugin-security, eslint-plugin-no-unsanitized",
            kind="warn", shape="round")
    sc.node("lsec", 646, 164, 448, 56, "npm run lint:security",
            sub="no-unsanitized/method|property, detect-eval-with-expression",
            kind="warn", shape="round")
    sc.node("cq", 646, 232, 448, 56, "CodeQL security-extended",
            sub=".github/workflows/codeql.yml — theo lịch hằng tuần",
            kind="warn", shape="round")
    sc.node("tv", 646, 300, 448, 44,
            "Trivy quét ảnh container  ·  npm audit --audit-level=high",
            kind="accent", shape="rect", font_size=11)

    sc.group("g3", 40, 400, 1080, 200,
             "Kiểm thử thủ công trên ứng dụng đã đóng gói", "ui")
    manual = [
        ("m1", 66, "Danh sách kiểm tra khói\ntrong DESKTOP.md"),
        ("m2", 276, "Chạy ngoại tuyến\n(ngắt kết nối mạng)"),
        ("m3", 486, "Quan sát tab Network\ncủa DevTools"),
        ("m4", 696, "Kiểm tra hộp thoại lưu\nnative và trường hợp huỷ"),
        ("m5", 906, "Đổi ngôn ngữ VI ⇄ EN\nvà khởi động lại"),
    ]
    for nid, x, label in manual:
        sc.node(nid, x, 450, 190, 66, label, kind="ui", shape="round",
                font_size=11)
    sc.node("mnote", 66, 530, 1030, 50,
            "Bao gồm các thao tác đại diện: Merge PDF (pdf-lib/cpdf) · "
            "JPG → PDF · Compress (Ghostscript) · PDF → PNG (PyMuPDF) · "
            "Encrypt/Decrypt (qpdf) · OCR (Tesseract, dữ liệu eng cục bộ)",
            kind="accent", shape="rect", font_size=11)

    sc.node("lim", 40, 630, 1080, 100,
            "Giới hạn của môi trường thử nghiệm trong khuôn khổ đề tài\n\n"
            "Máy chủ dùng để phân tích mã nguồn không có màn hình đồ hoạ và "
            "không đủ tài nguyên đĩa/bộ nhớ để cài đặt toàn bộ phụ thuộc và "
            "biên dịch ứng dụng. Vì vậy các số liệu về thời gian xử lý, mức "
            "tiêu thụ bộ nhớ và ảnh chụp giao diện chưa được đo trực tiếp; "
            "báo cáo chỉ trình bày phương pháp đo và các tiêu chí đánh giá.",
            kind="warn", shape="round", font_size=11)
    return emit(sc, "fig_4_1_test_environment", OUT)


# ================================================================= Hình 4.2
def fig_4_2():
    sc = Scene("Hình 4.2 - Phân bố ca kiểm thử tự động", 1120, 620)
    sc.text(560, 46, "Số ca kiểm thử theo nhóm chức năng "
                     "(tổng 641 ca trong 39 tệp)",
            size=14, bold=True, anchor="middle", color="#0F172A")
    data = [
        ("Chuyển đổi và nhập/xuất tệp (8 tệp)", 182),
        ("Thao tác PDF lõi (8 tệp)", 151),
        ("Tiện ích và hạ tầng (8 tệp)", 114),
        ("Bảo mật, chữ ký số, XSS (7 tệp)", 103),
        ("OCR và biến đổi hOCR (5 tệp)", 59),
        ("So sánh tài liệu (3 tệp)", 32),
    ]
    bar_chart(sc, 60, 90, 1000, 400, data, unit=" ca", kind="ui")
    sc.node("src", 60, 400, 1000, 180,
            "Nguồn số liệu: đếm trực tiếp số lời gọi it()/test() trong thư mục "
            "src/tests của kho mã nguồn.\n\n"
            "Các tệp có nhiều ca nhất: hocr-transform (45) · pdf-operations (42) "
            "· helpers (41) · comic-info (39) · image-effects (34) · "
            "password-prompt (33) · tiff-to-pdf (29) · diff-text-runs (28) · "
            "deduplicate-filename (28) · xml-to-pdf (26) · watermark (23) · "
            "xss-replay (22).\n\n"
            "Lưu ý: đây là số ca kiểm thử hiện có trong kho mã, không phải kết "
            "quả chạy — kết quả chạy chưa được thu thập trên môi trường phân "
            "tích (xem Hình 4.1).",
            kind="neutral", shape="note", font_size=11)
    return emit(sc, "fig_4_2_test_distribution", OUT)


# ================================================================= Hình 4.3
def fig_4_3():
    sc = Scene("Hình 4.3 - Quy trình kiểm thử chức năng", 1160, 760)
    steps = [
        ("t1", "Chuẩn bị dữ liệu thử: PDF văn bản, PDF nhiều trang, PDF quét, "
                "PDF có mật khẩu, ảnh JPG/PNG/TIFF, tài liệu văn phòng"),
        ("t2", "Chọn công cụ cần kiểm thử từ màn hình làm việc hoặc mở trực tiếp "
                "trang công cụ"),
        ("t3", "Nạp tệp bằng cả hai đường: hộp thoại chọn tệp của hệ điều hành và "
                "kéo–thả vào drop-zone"),
        ("t4", "Kiểm tra phản hồi giao diện: danh sách tệp, số trang, ảnh thu nhỏ, "
                "thông báo lỗi khi tệp sai định dạng"),
        ("t5", "Nhập tham số biên: khoảng trang rỗng, khoảng trang không hợp lệ, "
                "mật khẩu sai, giá trị vượt số trang"),
        ("t6", "Thực thi và quan sát loader; với thao tác dài kiểm tra giao diện "
                "không bị treo"),
        ("t7", "Kiểm tra hộp thoại lưu native: lưu thành công, huỷ hộp thoại, "
                "ghi đè tệp đã tồn tại"),
        ("t8", "Mở tệp kết quả bằng trình đọc PDF độc lập để xác nhận tính hợp lệ "
                "của tài liệu"),
        ("t9", "Lặp lại toàn bộ trong trạng thái ngắt kết nối mạng và quan sát tab "
                "Network để xác nhận không có yêu cầu ra ngoài"),
        ("t10", "Ghi nhận kết quả theo mẫu: mã ca, đầu vào, thao tác, kết quả "
                 "mong đợi, kết quả thực tế, kết luận Đạt/Không đạt"),
    ]
    y = 40
    for i, (nid, label) in enumerate(steps):
        sc.node(nid, 120, y, 780, 56, f"{i+1}.  {label}", kind="logic",
                shape="round", font_size=11, align="left")
        y += 68
    order = [s[0] for s in steps]
    for a, b in zip(order, order[1:]):
        sc.edge(a, b, exit="s", entry="n", style="straight")

    sc.node("cls", 930, 120, 200, 200,
            "Phân loại ca kiểm thử\n\n"
            "• Đường đi thuận lợi\n"
            "• Giá trị biên\n"
            "• Đầu vào không hợp lệ\n"
            "• Huỷ giữa chừng\n"
            "• Tài liệu lớn",
            kind="accent", shape="note", font_size=11, align="left")
    sc.node("ev", 930, 400, 200, 200,
            "Bằng chứng thu thập\n\n"
            "• Ảnh chụp màn hình\n"
            "• Tệp kết quả\n"
            "• Nhật ký console\n"
            "• Danh sách yêu cầu mạng\n"
            "• Dung lượng trước/sau",
            kind="data", shape="note", font_size=11, align="left")
    sc.node("no", 10, 660, 1140, 70,
            "Trạng thái hiện tại: quy trình trên đã được đặc tả đầy đủ và một "
            "phần đã được phản ánh trong danh sách kiểm tra khói của DESKTOP.md, "
            "nhưng chưa được thực hiện trên ứng dụng đã đóng gói trong phạm vi "
            "đề tài này; các bảng kết quả trong Chương 4 vì vậy để trống cột "
            "'kết quả thực tế'.",
            kind="warn", shape="round", font_size=11)
    return emit(sc, "fig_4_3_functional_test_flow", OUT)


# ================================================================= Hình 4.4
def fig_4_4():
    sc = Scene("Hình 4.5 - Cấu thành dung lượng tài nguyên ngoại tuyến",
               1120, 640)
    sc.text(560, 46, "Dung lượng các mô-đun WASM đóng gói kèm ứng dụng "
                     "(đo bằng du -sm trên kho mã)",
            size=14, bold=True, anchor="middle", color="#0F172A")
    data = [
        ("wasm/pymupdf — Pyodide, PyMuPDF, numpy, OpenCV", 54),
        ("wasm/ocr — 8 biến thể tesseract-core + eng", 47),
        ("wasm/gs — Ghostscript", 15),
        ("wasm/cpdf — CoherentPDF", 6),
    ]
    bar_chart(sc, 60, 90, 1010, 260, data, unit=" MB", kind="engine",
              label_w=390)
    sc.node("detail", 60, 300, 1010, 300,
            "Phân rã chi tiết\n\n"
            "wasm/pymupdf/assets:  pymupdf 17 MB · numpy 12 MB · opencv 12 MB · "
            "pyodide.asm.wasm 8,1 MB · python_stdlib.zip 2,3 MB · lxml 1,7 MB · "
            "fonttools 1,1 MB · pyodide.asm.js 988 KB · pdf2docx, python-docx, "
            "pymupdf4llm, typing_extensions\n\n"
            "wasm/ocr:  core 44 MB (tesseract-core, -simd, -relaxedsimd và các "
            "biến thể -lstm, mỗi biến thể gồm .js, .wasm và .wasm.js) · "
            "lang-data 3 MB (eng.traineddata.gz) · fonts 1 MB "
            "(NotoSans-Regular.ttf) · worker.min.js 109 KB\n\n"
            "wasm/gs:  gs.wasm 14,8 MB + gs.js 37 KB\n"
            "wasm/cpdf:  bốn biến thể coherentpdf (browser/node × thường/min)\n\n"
            "Ngoài thư mục wasm/ còn có public/qpdf.wasm 1,3 MB và "
            "public/coherentpdf.browser.min.js 1,3 MB được đóng gói trong dist/.\n\n"
            "Tổng cộng 121 MB tài nguyên xử lý, phù hợp với ước lượng dung lượng "
            "gói cài đặt 250–300 MB nêu trong tài liệu DESKTOP.md.",
            kind="neutral", shape="note", font_size=11)
    return emit(sc, "fig_4_5_bundle_composition", OUT)


# ================================================================= Hình 4.5
def fig_4_5():
    sc = Scene("Hình 4.6 - Khung tiêu chí đánh giá", 1160, 800)
    sc.node("root", 430, 40, 300, 56, "Đánh giá PDF Toolkit Desktop",
            kind="ui", shape="round", font_size=13, bold=True)

    groups = [
        ("g1", 30, "Tính đúng đắn chức năng", "logic", [
            "Tệp kết quả mở được bằng trình đọc độc lập",
            "Số trang và thứ tự trang đúng như yêu cầu",
            "Bookmark và nhãn trang được giữ khi ghép",
            "Siêu dữ liệu thay đổi đúng mong đợi",
        ], "Đo bằng kiểm thử chức năng thủ công + 641 ca kiểm thử tự động"),
        ("g2", 320, "Bảo mật và quyền riêng tư", "warn", [
            "Không có yêu cầu mạng khi dùng thao tác lõi",
            "Mật khẩu và khoá riêng không rời khỏi bộ nhớ",
            "Nội dung đã che (redact) không phục hồi được",
            "Đầu vào độc hại không thực thi được mã",
        ], "Đo bằng tab Network, kiểm tra tệp kết quả, 22 ca kiểm thử XSS"),
        ("g3", 610, "Hiệu năng và tài nguyên", "engine", [
            "Thời gian xử lý theo số trang và kích thước tệp",
            "Mức bộ nhớ đỉnh khi xử lý tài liệu lớn",
            "Giao diện còn phản hồi trong khi xử lý",
            "Thời gian khởi động và nạp mô-đun WASM",
        ], "CHƯA ĐO — cần chạy trên máy có giao diện đồ hoạ"),
        ("g4", 900, "Khả dụng và triển khai", "accent", [
            "Chạy được hoàn toàn ngoại tuyến",
            "Cài đặt được trên ba hệ điều hành",
            "Giao diện tiếng Việt đầy đủ và nhất quán",
            "Thông báo lỗi rõ ràng, có hướng khắc phục",
        ], "Đo bằng danh sách kiểm tra khói và ma trận CI"),
    ]
    for gid, x, title, kind, items, how in groups:
        sc.node(gid, x, 150, 250, 56, title, kind=kind, shape="round",
                font_size=12, bold=True)
        sc.edge("root", gid, exit="s", entry="n", color="#4F46E5")
        y = 220
        for it in items:
            sc.node(f"{gid}_{y}", x, y, 250, 62, it, kind="neutral",
                    shape="rect", font_size=10)
            y += 70
        sc.node(gid + "_how", x, y + 6, 250, 90, how,
                kind=kind, shape="note", font_size=10)

    sc.node("legend", 30, 700, 1120, 80,
            "Quy ước trình bày kết quả trong Chương 4\n\n"
            "Tiêu chí đã có bằng chứng trực tiếp từ mã nguồn hoặc cấu hình được "
            "trình bày kèm dẫn chứng tệp và dòng lệnh. Tiêu chí cần đo trên "
            "ứng dụng đang chạy được ghi rõ là CHƯA ĐO, kèm phương pháp đo đề "
            "xuất; báo cáo không đưa ra bất kỳ con số ước lượng nào cho các "
            "tiêu chí này.",
            kind="warn", shape="round", font_size=11)
    return emit(sc, "fig_4_6_evaluation_criteria", OUT)


if __name__ == "__main__":
    for fn in [fig_4_1, fig_4_2, fig_4_3, fig_4_4, fig_4_5]:
        print("ok", fn())
