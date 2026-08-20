# -*- coding: utf-8 -*-
"""Chương 4, Kết luận và Tài liệu tham khảo."""


def build(r):
    r.h1("CHƯƠNG 4. THỬ NGHIỆM VÀ ĐÁNH GIÁ HỆ THỐNG")

    # ==================================================================
    r.h2("1. Môi trường và phương pháp thử nghiệm")

    r.h3("1.1. Môi trường thử nghiệm")
    r.p(
        "Việc thử nghiệm một ứng dụng desktop xử lý tài liệu đòi hỏi ba loại "
        "môi trường khác nhau, phục vụ ba mục đích khác nhau. Hình 4.1 trình "
        "bày kiến trúc tổng thể của môi trường thử nghiệm cùng ranh giới giữa "
        "phần đã thực hiện được và phần còn phải bổ sung."
    )
    r.figure(
        "fig_4_1_test_environment",
        "Hình 4.1. Kiến trúc môi trường thử nghiệm của hệ thống",
    )
    r.p(
        "Môi trường thứ nhất là môi trường kiểm thử tự động. Dự án dùng khung "
        "kiểm thử Vitest phiên bản 4 chạy trên môi trường mô phỏng cây tài liệu "
        "jsdom phiên bản 28. Cấu hình kiểm thử được đặt ngay trong tệp cấu hình "
        "chính của bộ dựng, với một tệp thiết lập chung chạy trước mỗi bộ kiểm "
        "thử. Công cụ đo độ phủ dùng bộ máy V8 và loại trừ các thư mục không "
        "cần đo gồm thư viện bên ngoài, chính thư mục kiểm thử, các tệp cấu "
        "hình, tệp khai báo kiểu và thư mục kết quả dựng."
    )
    r.p(
        "Bốn lệnh được cung cấp cho các tình huống khác nhau: chạy ở chế độ "
        "theo dõi thay đổi, chạy một lần rồi thoát, chạy kèm giao diện đồ hoạ, "
        "và chạy kèm báo cáo độ phủ. Việc môi trường kiểm thử dùng jsdom thay "
        "vì trình duyệt thật quyết định phạm vi những gì có thể kiểm thử tự "
        "động, sẽ được phân tích ở mục 2."
    )
    r.p(
        "Môi trường thứ hai là môi trường phân tích tĩnh và quét bảo mật, chạy "
        "trong quy trình tích hợp liên tục. Thành phần gồm ESLint phiên bản 10 "
        "kết hợp typescript-eslint với hai bộ luật an toàn, một lệnh quét bảo "
        "mật chuyên biệt bật ba luật ở mức lỗi, phân tích CodeQL với bộ truy "
        "vấn mở rộng về bảo mật chạy theo lịch hằng tuần, quét lỗ hổng ảnh "
        "container bằng Trivy, và kiểm tra phụ thuộc bằng lệnh kiểm toán của "
        "npm ở ngưỡng nghiêm trọng cao."
    )
    r.p(
        "Môi trường thứ ba là môi trường kiểm thử thủ công trên ứng dụng đã "
        "đóng gói. Tài liệu kỹ thuật của dự án cung cấp một danh sách kiểm tra "
        "khói gồm mười một mục, bao trùm các thao tác đại diện cho từng nhóm "
        "động cơ xử lý: ghép tệp cho pdf-lib và CoherentPDF, chuyển ảnh sang "
        "PDF cho chuỗi xử lý ảnh, nén cho Ghostscript, chuyển PDF sang ảnh cho "
        "PyMuPDF, mã hoá và giải mã cho qpdf, và nhận dạng ký tự cho "
        "Tesseract. Danh sách này còn bao gồm ba mục kiểm chứng đặc thù của bản "
        "desktop: chạy khi ngắt mạng, huỷ hộp thoại lưu, và quan sát tab mạng "
        "để xác nhận không có yêu cầu ra ngoài."
    )
    r.p(
        "Cần nêu rõ và nhất quán một giới hạn quan trọng của đề tài. Máy chủ "
        "được dùng để phân tích mã nguồn và soạn thảo báo cáo không có màn hình "
        "đồ hoạ, chỉ còn khoảng 9,5 gigabyte dung lượng đĩa trống trên tổng số "
        "145 gigabyte và khoảng 1 gigabyte bộ nhớ khả dụng trên tổng số 7 "
        "gigabyte, đồng thời chạy Node.js phiên bản 18 trong khi dự án yêu cầu "
        "phiên bản 20 trở lên. Việc cài đặt toàn bộ cây phụ thuộc và biên dịch "
        "ứng dụng trong điều kiện đó có nguy cơ làm cạn kiệt tài nguyên máy "
        "chủ. Vì vậy bộ kiểm thử tự động chưa được thực thi và ứng dụng chưa "
        "được chạy để thu thập số liệu hiệu năng cũng như ảnh chụp giao diện."
    )
    r.p(
        "Hệ quả của giới hạn này được xử lý theo nguyên tắc trung thực tuyệt "
        "đối: báo cáo trình bày đầy đủ cấu trúc bộ kiểm thử, quy trình kiểm thử "
        "và phương pháp đo, nhưng không đưa ra bất kỳ con số kết quả nào chưa "
        "được đo. Bảng 4.1 tổng hợp cấu hình môi trường thử nghiệm cùng trạng "
        "thái thực hiện của từng thành phần."
    )
    r.table(
        "Bảng 4.1. Cấu hình môi trường thử nghiệm và trạng thái thực hiện",
        ["Thành phần", "Cấu hình / phiên bản", "Trạng thái trong đề tài"],
        [
            ["Khung kiểm thử đơn vị", "Vitest 4.0.18 trên jsdom 28.1.0",
             "Đã có trong kho mã, chưa thực thi trên môi trường phân tích"],
            ["Đo độ phủ", "@vitest/coverage-v8 4.0.18",
             "Đã cấu hình, chưa thực thi"],
            ["Phân tích tĩnh", "ESLint 10.0.2 + typescript-eslint 8.56.1",
             "Đã cấu hình với hai bộ luật an toàn, chưa thực thi"],
            ["Quét mã bảo mật", "CodeQL, bộ truy vấn security-extended",
             "Đã cấu hình quy trình chạy hằng tuần trên kho GitHub"],
            ["Quét ảnh container", "Trivy",
             "Đã cấu hình; áp dụng cho bản triển khai container, không áp dụng "
             "cho bản desktop"],
            ["Kiểm toán phụ thuộc", "npm audit ở ngưỡng high",
             "Đã cấu hình trong kịch bản security:audit"],
            ["Ứng dụng desktop để kiểm thử thủ công",
             "Gói cài đặt cho macOS / Windows / Linux",
             "Chưa biên dịch được trên môi trường phân tích"],
            ["Máy phân tích mã nguồn",
             "Linux 6.8, 4 nhân CPU, 7 GB RAM, không có giao diện đồ hoạ, "
             "Node.js 18",
             "Đủ để đọc và phân tích mã nguồn; không đủ để dựng và chạy ứng dụng"],
        ],
        widths=[4, 5, 6],
        font_size=11,
    )

    r.h3("1.2. Bộ dữ liệu và phương pháp thử nghiệm")
    r.p(
        "Do đặc thù của hệ thống là xử lý tài liệu chứ không phải nhận dạng hay "
        "phân loại, bộ dữ liệu thử nghiệm không cần dữ liệu gán nhãn mà cần độ "
        "đa dạng về đặc điểm cấu trúc. Bảng 4.2 đề xuất thành phần bộ dữ liệu "
        "thử nghiệm, được xây dựng trên cơ sở phân tích các nhánh xử lý có "
        "trong mã nguồn."
    )
    r.table(
        "Bảng 4.2. Thành phần bộ dữ liệu thử nghiệm đề xuất",
        ["Nhóm dữ liệu", "Đặc điểm", "Nhánh xử lý cần kiểm chứng"],
        [
            ["PDF văn bản thuần",
             "5–20 trang, có lớp văn bản, phông chuẩn",
             "Ghép, tách, xoay, trích trang, đánh số trang, đóng dấu chìm"],
            ["PDF nhiều trang",
             "≥ 200 trang, dung lượng ≥ 20 MB",
             "Kiểm chứng cơ chế dọn dẹp định kỳ và kết xuất ảnh thu nhỏ theo lô"],
            ["PDF quét ảnh",
             "Không có lớp văn bản, độ phân giải 200–300 DPI",
             "Nhận dạng ký tự, khử nghiêng, hiệu ứng bản quét, nén"],
            ["PDF quét chất lượng thấp",
             "Ảnh mờ, nghiêng nhẹ, nền màu",
             "Tuỳ chọn nhị phân hoá, cơ chế hạn thời nhận dạng theo trang"],
            ["PDF nhiều ảnh nhúng",
             "Ảnh độ phân giải cao, dung lượng ≥ 10 MB",
             "Hai chiến lược nén và các mức tham số"],
            ["PDF có bookmark nhiều cấp",
             "Cây bookmark ≥ 3 cấp",
             "Ghép giữ bookmark, tách theo bookmark, sinh mục lục"],
            ["PDF có nhãn trang không liên tục",
             "Đánh số La Mã ở phần đầu, số Ả Rập ở phần thân",
             "Tuỳ chọn giữ nhãn trang khi ghép"],
            ["PDF đã mã hoá",
             "Mật khẩu người dùng; và một tệp có mật khẩu chủ sở hữu riêng",
             "Phát hiện mã hoá, hỏi mật khẩu theo lô, giải mã thử tuần tự hai "
             "động cơ"],
            ["PDF có biểu mẫu",
             "Trường văn bản, hộp kiểm, danh sách chọn",
             "Điền biểu mẫu, làm phẳng, tạo biểu mẫu"],
            ["PDF có chú thích và tệp nhúng",
             "Chú thích nhiều loại, ít nhất một tệp đính kèm",
             "Gỡ chú thích, làm sạch, trích tệp đính kèm"],
            ["PDF có trang xoay sẵn",
             "Một số trang có góc xoay khác 0",
             "Cộng dồn góc xoay thay vì đặt tuyệt đối"],
            ["PDF khổ trang không đồng nhất",
             "Trộn A4, A3 và khổ tuỳ ý",
             "Chuẩn hoá khổ trang, gộp nhiều trang lên một tờ, dàn trang sách gấp"],
            ["Ảnh nhiều định dạng",
             "JPG, PNG, WebP, BMP, TIFF, HEIC, PSD, SVG",
             "Chuẩn hoá ảnh trước khi nhúng, đường giải mã qua canvas"],
            ["Tài liệu văn phòng",
             "DOCX, XLSX, PPTX, ODT, RTF, và ít nhất một định dạng cũ",
             "Chuyển đổi qua LibreOffice-WASM"],
            ["Thư điện tử",
             "Tệp EML và MSG, có HTML và tệp đính kèm",
             "Phân tích thư, làm sạch HTML, xử lý liên kết bọc"],
            ["Tệp PDF hỏng",
             "Bảng tham chiếu chéo sai, tệp bị cắt cụt",
             "Chức năng sửa tệp và nhánh xử lý lỗi"],
        ],
        widths=[3.5, 4.5, 7],
        font_size=10,
    )
    r.p(
        "Phương pháp thử nghiệm gồm bốn tầng, áp dụng theo thứ tự từ rẻ tới "
        "đắt. Tầng thứ nhất là kiểm thử đơn vị tự động cho các hàm logic thuần "
        "tuý — đây là tầng duy nhất đã tồn tại đầy đủ trong kho mã. Tầng thứ "
        "hai là phân tích tĩnh và quét bảo mật, cũng đã được cấu hình sẵn. Tầng "
        "thứ ba là kiểm thử chức năng thủ công theo kịch bản trên ứng dụng đã "
        "đóng gói. Tầng thứ tư là đo hiệu năng và tài nguyên với bộ dữ liệu có "
        "quy mô xác định."
    )
    r.p(
        "Hai tầng đầu có thể thực hiện trên bất kỳ máy nào đủ tài nguyên cài "
        "đặt phụ thuộc. Hai tầng sau bắt buộc phải thực hiện trên máy có giao "
        "diện đồ hoạ và phải lặp lại trên cả ba hệ điều hành, bởi ba bộ máy "
        "WebView khác nhau có thể cho kết quả khác nhau ở một số nhánh xử lý."
    )

    # ==================================================================
    r.h2("2. Kiểm thử tự động")

    r.h3("2.1. Cấu trúc và phạm vi bao phủ của bộ kiểm thử")
    r.p(
        "Kho mã nguồn chứa 39 tệp kiểm thử với tổng cộng 641 ca kiểm thử, xác "
        "định bằng cách đếm số lời gọi hàm khai báo ca kiểm thử trong thư mục "
        "kiểm thử. Hình 4.2 trình bày phân bố số ca kiểm thử theo nhóm chức "
        "năng."
    )
    r.figure(
        "fig_4_2_test_distribution",
        "Hình 4.2. Phân bố ca kiểm thử tự động theo nhóm chức năng",
    )
    r.p(
        "Nhóm chuyển đổi và nhập xuất tệp có số ca nhiều nhất với 182 ca trong "
        "8 tệp. Phần lớn tập trung ở ba mô-đun: sinh siêu dữ liệu cho định dạng "
        "truyện tranh với 39 ca, xử lý ảnh TIFF với 29 ca, và chuyển XML sang "
        "PDF với 26 ca. Đặc điểm chung của nhóm này là các hàm biến đổi dữ liệu "
        "thuần tuý, đầu vào và đầu ra đều xác định được, nên rất phù hợp với "
        "kiểm thử đơn vị."
    )
    r.p(
        "Nhóm thao tác PDF lõi có 151 ca trong 8 tệp, tập trung ở mô-đun các "
        "phép toán PDF với 42 ca, mô-đun đóng dấu chìm với 23 ca, mô-đun chuẩn "
        "hoá khổ trang với 19 ca, và ba mô-đun liên quan tới xoay trang với "
        "tổng cộng 51 ca. Con số 51 ca dành riêng cho việc xoay trang đáng được "
        "ghi nhận: nó phản ánh đúng mức độ tinh tế của bài toán cộng dồn góc "
        "xoay đã phân tích ở Chương 3."
    )
    r.p(
        "Nhóm tiện ích và hạ tầng có 114 ca, trong đó mô-đun trợ giúp chung có "
        "41 ca kiểm tra các hàm nhận diện khổ giấy chuẩn, quy đổi đơn vị, "
        "chuyển mã màu, định dạng dung lượng, phân tích chuỗi khoảng trang, cắt "
        "ngắn tên tệp và thoát ký tự HTML. Mô-đun khử trùng lặp tên tệp có 28 "
        "ca — con số cao cho một chức năng tưởng như đơn giản, cho thấy các "
        "trường hợp biên về tên tệp đã được xử lý kỹ."
    )
    r.p(
        "Nhóm bảo mật, chữ ký số và chống tấn công chèn mã có 103 ca trong 7 "
        "tệp. Đáng chú ý nhất là mô-đun hỏi mật khẩu với 33 ca và tệp tái hiện "
        "tấn công chèn mã với 22 ca. Ba mô-đun liên quan tới dấu thời gian có "
        "tổng cộng 33 ca."
    )
    r.p(
        "Nhóm nhận dạng ký tự có 59 ca, trong đó mô-đun biến đổi hOCR chiếm 45 "
        "ca — số ca nhiều nhất trong một tệp. Điều này phản ánh đúng độ phức "
        "tạp của việc quy đổi toạ độ, phân tích hộp bao, tính đường cơ sở và "
        "tính hệ số co ngang đã trình bày ở mục 3.6 của Chương 3. Nhóm so sánh "
        "tài liệu có 32 ca, chủ yếu ở mô-đun so khớp chuỗi văn bản với 28 ca."
    )
    r.p(
        "Về phạm vi bao phủ, cần phân tích thẳng thắn giới hạn của cách tiếp "
        "cận này. Bảng 4.3 đối chiếu những gì bộ kiểm thử hiện tại kiểm chứng "
        "được với những gì nó không thể kiểm chứng."
    )
    r.table(
        "Bảng 4.3. Phạm vi và giới hạn của bộ kiểm thử tự động hiện có",
        ["Loại hành vi", "Kiểm thử tự động hiện tại", "Lý do / phương pháp thay thế"],
        [
            ["Hàm biến đổi dữ liệu thuần tuý (phân tích khoảng trang, quy đổi "
             "toạ độ, chuẩn hoá văn bản, sinh siêu dữ liệu)",
             "Bao phủ tốt",
             "Đầu vào và đầu ra xác định, không phụ thuộc môi trường"],
            ["Logic cấu hình và phân nhánh (xác định ngôn ngữ, danh mục công "
             "cụ, tuỳ chọn động cơ nhận dạng)",
             "Bao phủ tốt",
             "Có thể mô phỏng biến môi trường và bộ nhớ cục bộ trong jsdom"],
            ["Tương tác giao diện đơn giản (hiển thị hộp thoại, đặt lại trạng "
             "thái, chuyển đổi loại đóng dấu chìm)",
             "Bao phủ một phần",
             "jsdom mô phỏng được cây tài liệu nhưng không mô phỏng bố cục và "
             "kết xuất"],
            ["Phép biến đổi PDF thực sự trên tệp thật",
             "Bao phủ hạn chế",
             "Cần môi trường có WebAssembly đầy đủ; một số ca dùng tệp PDF nhỏ "
             "dựng bằng pdf-lib"],
            ["Kết xuất trang ra canvas",
             "Không bao phủ",
             "jsdom không hiện thực ngữ cảnh vẽ 2D; cần trình duyệt thật"],
            ["Nhận dạng ký tự đầu cuối",
             "Không bao phủ (chỉ 2 ca kiểm tra khung gọi)",
             "Cần động cơ Tesseract thật và thời gian chạy dài"],
            ["Lệnh lưu tệp bản địa",
             "Không bao phủ",
             "Cần tiến trình Tauri thật; kiểm thử thủ công theo danh sách khói"],
            ["Khác biệt giữa ba bộ máy WebView",
             "Không bao phủ",
             "Cần chạy trên cả ba hệ điều hành"],
            ["Hiệu năng và mức tiêu thụ bộ nhớ",
             "Không bao phủ",
             "Cần đo trên ứng dụng đã đóng gói với bộ dữ liệu quy mô xác định"],
        ],
        widths=[5, 3.5, 6],
        font_size=10,
    )
    r.p(
        "Nhận xét chung: bộ kiểm thử tự động hiện tại có cấu trúc hợp lý và "
        "tập trung đúng vào những phần có tỉ lệ lợi ích trên chi phí cao nhất — "
        "các hàm logic thuần tuý nơi lỗi dễ phát sinh và khó phát hiện bằng "
        "mắt. Tuy nhiên nó không thay thế được kiểm thử chức năng đầu cuối, và "
        "khoảng trống lớn nhất nằm ở việc kiểm chứng các phép biến đổi PDF trên "
        "tệp thật. Hướng bổ sung được đề xuất ở mục 5.3."
    )

    r.h3("2.2. Kiểm thử liên quan tới an toàn thông tin")
    r.p(
        "Trong bộ kiểm thử tự động, tệp tái hiện tấn công chèn mã đáng được "
        "phân tích riêng vì nó thể hiện một cách tiếp cận đáng ghi nhận: kiểm "
        "thử được viết để tái hiện lại đúng những chuỗi tấn công đã được báo "
        "cáo, thay vì chỉ kiểm tra hàm làm sạch có được gọi hay không."
    )
    r.p(
        "Tệp này gồm 22 ca kiểm thử chia thành sáu nhóm, bao trùm bốn đường dẫn "
        "dữ liệu có nguy cơ. Đường thứ nhất là chuỗi xử lý Markdown sang PDF: "
        "chuỗi tấn công được đưa qua đúng cấu hình bộ phân tích Markdown mà "
        "ứng dụng dùng, kết xuất thành HTML, làm sạch bằng DOMPurify, rồi kiểm "
        "tra kết quả. Đường thứ hai là tên tệp — điểm mà nội dung do người dùng "
        "kiểm soát đi thẳng vào giao diện. Đường thứ ba là nội dung HTML trong "
        "thư điện tử. Đường thứ tư là thông tin chứng thư số hiển thị khi kiểm "
        "tra chữ ký."
    )
    r.p(
        "Hàm kiểm chứng dùng chung của tệp này kiểm tra bốn điều kiện trên kết "
        "quả đã làm sạch: không còn thẻ kịch bản; không còn thuộc tính bắt đầu "
        "bằng tiền tố xử lý sự kiện; không còn thuộc tính điều hướng hoặc nguồn "
        "nào có giá trị bắt đầu bằng giao thức thực thi kịch bản; và không còn "
        "khung nhúng có thuộc tính nội dung tài liệu. Bốn điều kiện này bao "
        "trùm các kỹ thuật chèn mã phổ biến nhất."
    )
    r.p(
        "Bên cạnh kiểm thử, phần bảo mật còn được kiểm soát bằng phân tích "
        "tĩnh. Cấu hình ESLint bật hai bộ luật chuyên biệt và nâng năm luật lên "
        "mức lỗi: phát hiện lời gọi thực thi biểu thức động, phát hiện cách tạo "
        "vùng đệm không an toàn, phát hiện bộ sinh số ngẫu nhiên không đủ mạnh "
        "cho mục đích mật mã, phát hiện ký tự đảo chiều hiển thị, và phát hiện "
        "việc vô hiệu hoá cơ chế thoát ký tự của bộ tạo khuôn mẫu."
    )
    r.p(
        "Một chi tiết đáng ghi nhận trong cấu hình là việc tắt có chủ ý một số "
        "luật không phù hợp với ngữ cảnh: luật cảnh báo về đường dẫn tệp không "
        "phải hằng số, luật cảnh báo về biểu thức chính quy không phải hằng số, "
        "và luật cảnh báo về truy cập thuộc tính đối tượng bằng biến. Ba luật "
        "này sinh ra rất nhiều cảnh báo giả trong một ứng dụng xử lý tệp phía "
        "máy khách, và việc tắt chúng có kèm giữ nguyên các luật quan trọng cho "
        "thấy cấu hình được cân nhắc chứ không sao chép máy móc."
    )
    r.p(
        "Ở mức quy trình, kho mã có một móc chạy trước khi ghi nhận thay đổi, "
        "tự động chạy công cụ kiểm tra và định dạng trên các tệp thay đổi. Kết "
        "hợp với phân tích CodeQL hằng tuần và kiểm toán phụ thuộc, hệ thống có "
        "một tầng phòng vệ tự động tương đối đầy đủ ở mức mã nguồn."
    )

    # ==================================================================
    r.h2("3. Kiểm thử chức năng")

    r.h3("3.1. Quy trình kiểm thử chức năng")
    r.p(
        "Do bộ kiểm thử tự động không bao phủ được các phép biến đổi PDF thực "
        "sự và toàn bộ phần tương tác bản địa, kiểm thử chức năng thủ công là "
        "tầng kiểm chứng không thể thiếu. Hình 4.3 trình bày quy trình kiểm thử "
        "chức năng gồm mười bước."
    )
    r.figure(
        "fig_4_3_functional_test_flow",
        "Hình 4.3. Quy trình kiểm thử chức năng đối với một công cụ",
    )
    r.p(
        "Quy trình bắt đầu bằng việc chuẩn bị bộ dữ liệu theo Bảng 4.2, sau đó "
        "mở công cụ cần kiểm thử. Bước nạp tệp phải thực hiện bằng cả hai "
        "đường: hộp thoại chọn tệp và kéo–thả, bởi hai đường này đi qua hai "
        "nhánh mã khác nhau và đã từng có trường hợp một nhánh hoạt động còn "
        "nhánh kia thì không."
    )
    r.p(
        "Bước kiểm tra phản hồi giao diện xác nhận danh sách tệp, số trang, ảnh "
        "thu nhỏ và thông báo lỗi khi tệp sai định dạng. Bước nhập tham số biên "
        "là bước quan trọng nhất về mặt phát hiện lỗi: chuỗi khoảng trang rỗng "
        "phải được hiểu là toàn bộ trang, chuỗi không hợp lệ phải được bỏ qua "
        "mà không làm hỏng thao tác, mật khẩu sai phải cho phép nhập lại, và "
        "giá trị vượt số trang phải bị loại."
    )
    r.p(
        "Bước thực thi quan sát chỉ báo tải và kiểm tra giao diện không bị "
        "treo. Bước kiểm tra hộp thoại lưu bao gồm ba tình huống: lưu thành "
        "công, huỷ hộp thoại, và ghi đè tệp đã tồn tại. Bước mở tệp kết quả "
        "bằng trình đọc PDF độc lập là bước xác nhận cuối cùng — một tệp mà "
        "ứng dụng tạo ra nhưng trình đọc khác không mở được là một lỗi nghiêm "
        "trọng dù mọi bước trước đó đều thành công."
    )
    r.p(
        "Bước áp chót lặp lại toàn bộ quy trình trong trạng thái ngắt kết nối "
        "mạng, đồng thời quan sát tab mạng của công cụ phát triển. Đây là bước "
        "kiểm chứng trực tiếp cho yêu cầu PC-01 và PC-02. Bước cuối cùng ghi "
        "nhận kết quả theo mẫu thống nhất gồm sáu trường."
    )

    r.h3("3.2. Kịch bản kiểm thử chức năng tiêu biểu")
    r.p(
        "Bảng 4.4 trình bày mười lăm kịch bản kiểm thử tiêu biểu, được xây dựng "
        "trên cơ sở phân tích các nhánh xử lý và các điểm rủi ro đã nhận diện "
        "trong mã nguồn. Cột kết quả thực tế được để trống, phù hợp với trạng "
        "thái đã nêu ở mục 1.1."
    )
    r.table(
        "Bảng 4.4. Kịch bản kiểm thử chức năng tiêu biểu",
        ["Mã", "Đầu vào và thao tác", "Kết quả mong đợi", "Kết quả thực tế"],
        [
            ["KT-01",
             "Ghép ba tệp PDF ở chế độ tệp, không nhập khoảng trang",
             "Tệp kết quả có tổng số trang bằng tổng ba tệp, thứ tự trang đúng "
             "thứ tự hiển thị trên danh sách", ""],
            ["KT-02",
             "Ghép ba tệp, nhập khoảng “1-2, 4” cho tệp thứ hai",
             "Chỉ ba trang 1, 2, 4 của tệp thứ hai xuất hiện trong kết quả", ""],
            ["KT-03",
             "Ghép ở chế độ trang: kéo trang cuối của tệp thứ ba lên đầu",
             "Trang được kéo xuất hiện đầu tiên trong kết quả; các trang liên "
             "tiếp còn lại giữ nguyên thứ tự", ""],
            ["KT-04",
             "Ghép hai tệp có nhãn trang khác nhau, bật tuỳ chọn giữ nhãn trang",
             "Hệ thống đánh số của mỗi tài liệu nguồn được bảo toàn trong kết "
             "quả", ""],
            ["KT-05",
             "Nạp một tệp đã mã hoá vào công cụ ghép",
             "Hộp thoại nhập mật khẩu theo lô hiện ra, ghi rõ tên tệp; sau khi "
             "nhập đúng, tệp được xử lý bình thường", ""],
            ["KT-06",
             "Nạp ba tệp cùng mật khẩu vào công cụ ghép",
             "Chỉ phải nhập mật khẩu một lần cho cả ba tệp", ""],
            ["KT-07",
             "Mã hoá một tệp chỉ với mật khẩu người dùng",
             "Tệp yêu cầu mật khẩu khi mở; thông báo thành công nêu rõ tài liệu "
             "không có hạn chế sử dụng", ""],
            ["KT-08",
             "Mã hoá với mật khẩu người dùng và mật khẩu chủ sở hữu khác nhau",
             "Tệp yêu cầu mật khẩu khi mở; các thao tác in, sao chép, chỉnh sửa "
             "bị đánh dấu hạn chế trong thuộc tính tài liệu", ""],
            ["KT-09",
             "Giải mã tệp vừa mã hoá ở KT-08 bằng mật khẩu người dùng",
             "Tệp kết quả mở được không cần mật khẩu", ""],
            ["KT-10",
             "Nén một tệp nhiều ảnh bằng chiến lược giữ văn bản, mức cân bằng",
             "Dung lượng giảm; văn bản trong tệp kết quả vẫn tìm kiếm và sao "
             "chép được", ""],
            ["KT-11",
             "Nén cùng tệp bằng chiến lược kết xuất lại ảnh, mức cân bằng",
             "Dung lượng giảm nhiều hơn KT-10; tệp kết quả không còn lớp văn "
             "bản", ""],
            ["KT-12",
             "Nhận dạng ký tự trên tệp quét 5 trang, ngôn ngữ eng, bật nhị phân "
             "hoá",
             "Tệp kết quả giữ nguyên hình ảnh gốc; chọn và sao chép được văn "
             "bản; vị trí văn bản khớp với chữ trên ảnh", ""],
            ["KT-13",
             "Xoay 90 độ một tệp có sẵn trang xoay 90 độ",
             "Trang đã xoay sẵn có góc 180 độ trong kết quả, không phải 90 độ", ""],
            ["KT-14",
             "Huỷ hộp thoại lưu sau khi thao tác hoàn tất",
             "Không tệp nào được ghi ra đĩa; không hiện thông báo lỗi; ứng dụng "
             "trở về trạng thái sẵn sàng", ""],
            ["KT-15",
             "Ngắt kết nối mạng, thực hiện lần lượt sáu thao tác lõi đại diện "
             "cho sáu động cơ xử lý",
             "Cả sáu thao tác hoàn thành bình thường; tab mạng không ghi nhận "
             "yêu cầu nào ra ngoài", ""],
        ],
        widths=[1.2, 5, 5.5, 2.5],
        font_size=10,
    )
    r.p(
        "Ba kịch bản trong bảng đáng được nhấn mạnh vì chúng kiểm chứng trực "
        "tiếp những điểm thiết kế đã phân tích ở các chương trước. Kịch bản "
        "KT-13 kiểm chứng logic cộng dồn góc xoay — điểm mà 51 ca kiểm thử tự "
        "động đã bao phủ ở mức hàm nhưng cần xác nhận ở mức tệp thật. Kịch bản "
        "KT-14 kiểm chứng quyết định thiết kế coi việc huỷ hộp thoại không phải "
        "là lỗi. Kịch bản KT-15 kiểm chứng yêu cầu quan trọng nhất của toàn hệ "
        "thống."
    )

    r.h3("3.3. Kiểm chứng khả năng hoạt động ngoại tuyến")
    r.p(
        "Do khả năng hoạt động ngoại tuyến là yêu cầu cốt lõi, việc kiểm chứng "
        "nó cần được thực hiện theo ba mức độc lập, mỗi mức có giá trị bằng "
        "chứng khác nhau. Bảng 4.5 trình bày ba mức này."
    )
    r.table(
        "Bảng 4.5. Ba mức kiểm chứng khả năng hoạt động ngoại tuyến",
        ["Mức", "Phương pháp", "Giá trị bằng chứng", "Trạng thái"],
        [
            ["Mức 1 — Kiểm chứng tĩnh",
             "Đọc tệp .env.tauri xác nhận cả bảy biến trỏ về đường dẫn cục bộ; "
             "đọc kịch bản sao chép tài nguyên; kiểm tra thư mục wasm/ có đủ "
             "bốn mô-đun",
             "Chứng minh cấu hình không trỏ ra ngoài; không chứng minh được "
             "hành vi khi chạy",
             "ĐÃ THỰC HIỆN — kết quả đúng như thiết kế (xem Bảng 3.1)"],
            ["Mức 2 — Quan sát khi chạy",
             "Mở công cụ phát triển của WebView, chuyển sang tab mạng, thực "
             "hiện lần lượt các thao tác lõi và ghi nhận toàn bộ yêu cầu",
             "Chứng minh trực tiếp không có yêu cầu ra ngoài trong điều kiện có "
             "mạng",
             "CHƯA THỰC HIỆN — cần máy có giao diện đồ hoạ"],
            ["Mức 3 — Kiểm chứng ngắt mạng",
             "Ngắt hoàn toàn kết nối mạng của máy, chạy lại toàn bộ danh sách "
             "kiểm tra khói",
             "Bằng chứng mạnh nhất: nếu ứng dụng hoạt động đầy đủ khi không có "
             "mạng thì chắc chắn nó không phụ thuộc mạng",
             "CHƯA THỰC HIỆN — cần ứng dụng đã đóng gói"],
        ],
        widths=[3, 5.5, 5, 3.5],
        font_size=10,
    )
    r.p(
        "Kết quả kiểm chứng ở mức 1 đã được trình bày trong Bảng 3.1 của "
        "Chương 3 và có thể tóm tắt như sau: mười trong số mười hai nhóm chức "
        "năng không có phụ thuộc mạng nào; nhóm nhận dạng ký tự cho các ngôn "
        "ngữ ngoài tiếng Anh phụ thuộc vào việc dữ liệu ngôn ngữ tương ứng có "
        "được bổ sung vào thư mục cục bộ hay không; hai nhóm còn lại là ký số "
        "với chứng thư cần tải chuỗi và đóng dấu thời gian thì phụ thuộc mạng "
        "theo đúng thiết kế."
    )
    r.p(
        "Cần nhấn mạnh rằng bằng chứng ở mức 1 tuy có giá trị nhưng không đủ. "
        "Cấu hình đúng không loại trừ khả năng một thư viện bên thứ ba tự phát "
        "sinh yêu cầu mạng mà mã của dự án không kiểm soát. Chỉ có kiểm chứng ở "
        "mức 2 và mức 3 mới trả lời được câu hỏi này một cách dứt khoát, và đây "
        "là nội dung được đề xuất thực hiện ở mục 5.3."
    )
    r.placeholder(
        "Hình 4.4",
        "Hình 4.4. Kiểm chứng khả năng hoạt động ngoại tuyến qua tab mạng của "
        "công cụ phát triển",
        "Cửa sổ ứng dụng đặt cạnh bảng công cụ phát triển đang mở tab Network, "
        "sau khi đã thực hiện xong một thao tác lõi, cho thấy không có yêu cầu "
        "nào tới máy chủ bên ngoài.",
        [
            "Chạy ứng dụng ở chế độ phát triển (npm run tauri:dev) để mở được "
            "công cụ phát triển của WebView.",
            "Bấm chuột phải trong cửa sổ ứng dụng và chọn Inspect, chuyển sang "
            "tab Network.",
            "Xoá danh sách yêu cầu hiện có, sau đó thực hiện một thao tác lõi "
            "(ví dụ Merge PDF hoặc Compress PDF).",
            "Chờ thao tác hoàn tất, KHÔNG lọc danh sách yêu cầu.",
            "Chụp toàn màn hình, bảo đảm nhìn rõ toàn bộ danh sách yêu cầu và "
            "thấy rằng không có mục nào trỏ tới cdn.jsdelivr.net hay bất kỳ máy "
            "chủ từ xa nào.",
            "Lặp lại quy trình sau khi ngắt kết nối mạng và chụp thêm một ảnh "
            "cho thấy thao tác vẫn hoàn thành.",
        ],
    )
    r.p(
        "Một điểm nữa cần lưu ý trong quá trình kiểm chứng mức 2: trình phục vụ "
        "ngoại tuyến đã bị vô hiệu hoá trong bản desktop, nên mọi yêu cầu quan "
        "sát được trên tab mạng đều là yêu cầu thật, không bị che khuất bởi tầng "
        "bộ nhớ đệm. Đây là một lợi thế cho việc kiểm chứng, và cũng là một lý "
        "do bổ sung cho quyết định vô hiệu hoá trình phục vụ đó."
    )

    # ==================================================================
    r.h2("4. Đánh giá tài nguyên và hiệu năng")

    r.h3("4.1. Cấu thành dung lượng tài nguyên ngoại tuyến")
    r.p(
        "Dung lượng gói cài đặt là cái giá trực tiếp của yêu cầu hoạt động "
        "ngoại tuyến, nên việc phân tích cấu thành dung lượng có giá trị thực "
        "tế trong việc cân nhắc các phương án tối ưu. Đây cũng là nhóm số liệu "
        "duy nhất trong Chương 4 được đo trực tiếp, bằng cách thống kê dung "
        "lượng thư mục trên kho mã nguồn. Hình 4.4 trình bày kết quả."
    )
    r.figure(
        "fig_4_5_bundle_composition",
        "Hình 4.5. Cấu thành dung lượng tài nguyên WebAssembly đóng gói kèm "
        "ứng dụng",
    )
    r.p(
        "Tổng dung lượng thư mục tài nguyên WebAssembly là 121 megabyte, chia "
        "cho bốn mô-đun. Bảng 4.6 trình bày phân rã chi tiết cùng nhận xét về "
        "khả năng tối ưu của từng thành phần."
    )
    r.table(
        "Bảng 4.6. Phân rã dung lượng tài nguyên và khả năng tối ưu",
        ["Thành phần", "Dung lượng", "Nội dung chính", "Khả năng tối ưu"],
        [
            ["wasm/pymupdf", "54 MB",
             "pymupdf 17 MB, numpy 12 MB, opencv 12 MB, pyodide.asm.wasm 8,1 MB, "
             "thư viện chuẩn Python 2,3 MB, lxml 1,7 MB, fonttools 1,1 MB, "
             "pdf2docx, python-docx, pymupdf4llm",
             "Có thể loại numpy và OpenCV nếu không dùng chức năng khử nghiêng; "
             "loại pdf2docx và python-docx nếu không dùng chuyển sang DOCX"],
            ["wasm/ocr", "47 MB",
             "core 44 MB gồm 8 biến thể tesseract-core, lang-data 3 MB "
             "(eng.traineddata.gz), fonts 1 MB (NotoSans), worker.min.js 109 KB",
             "Tiềm năng lớn nhất: chỉ cần giữ biến thể lõi phù hợp với nền tảng "
             "đích thay vì cả 8 biến thể"],
            ["wasm/gs", "15 MB",
             "gs.wasm 14,8 MB, gs.js 37 KB",
             "Có thể loại bỏ nếu không dùng chuyển PDF/A và chuyển phông thành "
             "đường nét"],
            ["wasm/cpdf", "6 MB",
             "Bốn biến thể coherentpdf (bản trình duyệt và bản Node, mỗi bản có "
             "phiên bản thường và rút gọn)",
             "Có thể chỉ giữ biến thể rút gọn dùng cho trình duyệt, tiết kiệm "
             "khoảng 4,7 MB"],
            ["public/qpdf.wasm", "1,3 MB",
             "Mô-đun mã hoá và giải mã",
             "Không nên loại: phục vụ nhóm chức năng bảo mật cốt lõi"],
            ["public/coherentpdf.browser.min.js", "1,3 MB",
             "Bản sao dùng cho luồng chính",
             "Trùng lặp với wasm/cpdf; có thể hợp nhất"],
        ],
        widths=[4, 2, 6.5, 5],
        font_size=10,
    )
    r.p(
        "Phân tích trên cho thấy hai điểm tối ưu rõ rệt nhất. Điểm thứ nhất là "
        "thư mục lõi của động cơ nhận dạng ký tự với 44 megabyte cho tám biến "
        "thể. Tám biến thể này khác nhau ở việc có dùng tập lệnh SIMD hay không "
        "và có dùng mô hình LSTM hay không; động cơ chọn biến thể phù hợp ở "
        "thời điểm chạy tuỳ theo năng lực của môi trường. Với một gói cài đặt "
        "nhắm tới nền tảng cụ thể, việc giữ đủ tám biến thể là dư thừa."
    )
    r.p(
        "Điểm thứ hai là sự trùng lặp của CoherentPDF: thư viện xuất hiện ở cả "
        "thư mục tài nguyên WebAssembly và thư mục tài nguyên công khai, ở "
        "nhiều biến thể. Việc hợp nhất và chỉ giữ biến thể rút gọn dùng cho "
        "trình duyệt có thể tiết kiệm khoảng 6 megabyte."
    )
    r.p(
        "Cần lưu ý rằng dung lượng gói cài đặt cuối cùng lớn hơn 121 megabyte, "
        "vì còn phải cộng thêm gói JavaScript của ứng dụng, tài nguyên 21 ngôn "
        "ngữ, phông chữ, trình xem PDF nhúng và nhị phân Rust. Tài liệu kỹ "
        "thuật của dự án ước tính tổng dung lượng khoảng 250 đến 300 megabyte; "
        "con số này chưa được xác nhận bằng đo trực tiếp trong khuôn khổ đề tài "
        "vì ứng dụng chưa được biên dịch."
    )

    r.h3("4.2. Phương pháp đo hiệu năng đề xuất")
    r.p(
        "Vì các số liệu hiệu năng chưa được thu thập, mục này trình bày phương "
        "pháp đo đủ chi tiết để có thể thực hiện lại một cách nhất quán. Bảng "
        "4.7 đề xuất bộ chỉ số cùng cách đo và ngưỡng chấp nhận."
    )
    r.table(
        "Bảng 4.7. Bộ chỉ số hiệu năng đề xuất và phương pháp đo",
        ["Chỉ số", "Cách đo", "Bộ dữ liệu", "Ngưỡng chấp nhận đề xuất"],
        [
            ["Thời gian khởi động ứng dụng",
             "Từ lúc kích hoạt biểu tượng tới lúc lưới thẻ công cụ hiển thị đầy "
             "đủ; đo bằng đồng hồ bấm giờ, lặp 5 lần lấy trung vị",
             "Không cần dữ liệu", "Dưới 5 giây trên máy cấu hình phổ thông"],
            ["Thời gian ghép tệp",
             "Từ lúc bấm nút xử lý tới lúc hộp thoại lưu xuất hiện",
             "3 tệp × 10 trang; 3 tệp × 100 trang; 10 tệp × 50 trang",
             "Tăng gần tuyến tính theo tổng số trang"],
            ["Thời gian kết xuất ảnh thu nhỏ",
             "Từ lúc nạp tệp tới lúc lô ảnh thu nhỏ đầu tiên hiển thị",
             "Tệp 20, 100 và 500 trang",
             "Lô đầu tiên dưới 2 giây, không phụ thuộc tổng số trang nhờ nạp "
             "lười"],
            ["Thời gian nén",
             "Đo riêng cho từng chiến lược và từng mức",
             "Tệp 10 MB nhiều ảnh; tệp 50 MB",
             "Ghi nhận cùng tỉ lệ giảm dung lượng để đánh giá đánh đổi"],
            ["Thời gian nhận dạng ký tự",
             "Đo tổng thời gian và thời gian trung bình mỗi trang",
             "Tệp quét 5, 20 và 50 trang ở 200 và 300 DPI",
             "Ghi nhận riêng cho từng độ phân giải để định lượng ảnh hưởng của "
             "tham số này"],
            ["Thời gian khởi tạo mô-đun nặng",
             "Đo riêng lần gọi đầu tiên và các lần gọi sau",
             "Một thao tác dùng PyMuPDF, một thao tác dùng Ghostscript",
             "Lần gọi thứ hai phải nhanh hơn đáng kể, xác nhận cơ chế giữ thể "
             "hiện đơn nhất"],
            ["Bộ nhớ đỉnh",
             "Quan sát mức sử dụng bộ nhớ của tiến trình bằng công cụ hệ điều "
             "hành, ghi giá trị lớn nhất trong suốt thao tác",
             "Tệp 100 trang và 500 trang cho cùng một thao tác",
             "Không tăng tuyến tính theo số trang, xác nhận cơ chế dọn dẹp định "
             "kỳ"],
            ["Bộ nhớ sau nhiều thao tác liên tiếp",
             "Thực hiện 20 thao tác mã hoá liên tiếp, ghi mức bộ nhớ sau mỗi "
             "thao tác",
             "Cùng một tệp lặp lại",
             "Mức bộ nhớ ổn định, xác nhận cơ chế xoá tệp trong hệ tệp ảo"],
            ["Khả năng phản hồi của giao diện",
             "Trong khi thao tác dài đang chạy, thử cuộn trang và mở trình đơn",
             "Nhận dạng ký tự 50 trang",
             "Giao diện phản hồi được; chỉ báo tải cập nhật theo từng trang"],
        ],
        widths=[3.5, 5.5, 4, 5],
        font_size=10,
    )
    r.p(
        "Ba nguyên tắc cần tuân thủ khi thực hiện đo. Thứ nhất, mọi phép đo "
        "phải lặp lại ít nhất ba lần và lấy trung vị, vì môi trường WebView "
        "chịu ảnh hưởng của biên dịch tức thời và của bộ đệm hệ thống. Thứ hai, "
        "phải ghi rõ cấu hình máy đo — bộ xử lý, dung lượng bộ nhớ, hệ điều "
        "hành và phiên bản WebView — vì kết quả không có ý nghĩa nếu tách khỏi "
        "ngữ cảnh này. Thứ ba, phép đo phải lặp lại trên cả ba hệ điều hành, vì "
        "ba bộ máy WebView có đặc tính hiệu năng khác nhau."
    )
    r.p(
        "Ba nhóm chỉ số trong bảng có giá trị chẩn đoán thiết kế đặc biệt cao. "
        "Nhóm thứ nhất là thời gian khởi tạo mô-đun nặng ở lần gọi đầu so với "
        "các lần sau: nếu hai giá trị này gần nhau, cơ chế giữ thể hiện đơn "
        "nhất đã không hoạt động. Nhóm thứ hai là bộ nhớ đỉnh theo số trang: "
        "nếu tăng tuyến tính, cơ chế dọn dẹp định kỳ có vấn đề. Nhóm thứ ba là "
        "bộ nhớ sau nhiều thao tác liên tiếp: nếu tăng dần, việc xoá tệp trong "
        "hệ tệp ảo đã bị bỏ sót ở đâu đó."
    )

    r.h3("4.3. Đánh giá độ ổn định và quản lý tài nguyên qua phân tích mã")
    r.p(
        "Trong khi chờ số liệu đo trực tiếp, có thể đánh giá sơ bộ về độ ổn "
        "định và quản lý tài nguyên thông qua phân tích mã nguồn. Cách đánh giá "
        "này không thay thế được đo đạc nhưng cho phép xác định trước những "
        "điểm có nguy cơ cao và những điểm đã được xử lý cẩn thận."
    )
    r.p(
        "Về phía tích cực, phân tích mã cho thấy bảy cơ chế quản lý tài nguyên "
        "đã được áp dụng nhất quán như đã trình bày ở mục 4.1 của Chương 3. "
        "Đáng ghi nhận nhất là ba điểm. Thứ nhất, việc xoá tệp trong hệ tệp ảo "
        "được đặt trong khối bảo đảm thực thi với khối bắt lỗi riêng cho từng "
        "đường dẫn, xử lý đúng cả trường hợp tệp chưa được tạo. Thứ hai, cơ chế "
        "dọn dẹp định kỳ sau mỗi 25 trang trong vòng lặp nhận dạng ký tự cho "
        "thấy vấn đề tích luỹ bộ nhớ đã được nhận diện và xử lý chủ động. Thứ "
        "ba, việc giải phóng canvas bằng cách đặt kích thước về không được áp "
        "dụng ở cả bốn nơi có kết xuất, không bỏ sót."
    )
    r.p(
        "Về phía cần lưu ý, phân tích mã cũng chỉ ra ba điểm có nguy cơ. Điểm "
        "thứ nhất là việc sao chép mảng byte ở mỗi bước truyền dữ liệu trong "
        "luồng xử lý tự động: với đồ thị dài xử lý tệp lớn, lượng bộ nhớ tiêu "
        "thụ có thể tăng theo số nút. Đây là đánh đổi có chủ ý ưu tiên tính "
        "đúng đắn, nhưng cần được đo để biết ngưỡng thực tế."
    )
    r.p(
        "Điểm thứ hai là việc nạp đồng thời một tài liệu bằng hai thư viện "
        "trong một số công cụ — pdf.js để hiển thị và pdf-lib hoặc CoherentPDF "
        "để thao tác. Với tài liệu lớn, cách làm này nhân đôi lượng bộ nhớ giữ "
        "tài liệu. Điểm thứ ba là chiến lược nén kết xuất lại ảnh: dù canvas "
        "được giải phóng sau mỗi trang, các ảnh JPEG trung gian vẫn tích luỹ "
        "trong tài liệu đích cho tới khi lưu."
    )
    r.p(
        "Ba điểm trên đều là giả thuyết rút ra từ đọc mã, cần được xác nhận "
        "hoặc bác bỏ bằng phép đo bộ nhớ đỉnh theo Bảng 4.7. Việc nêu chúng ở "
        "đây có giá trị định hướng cho công việc đo đạc tiếp theo: người thực "
        "hiện biết trước cần chú ý vào đâu."
    )

    # ==================================================================
    r.h2("5. Nhận xét chung về kết quả thử nghiệm")

    r.h3("5.1. Kết quả đạt được")
    r.p(
        "Hình 4.6 trình bày khung tiêu chí đánh giá tổng thể với bốn nhóm, cùng "
        "phương pháp đo và trạng thái của từng nhóm."
    )
    r.figure(
        "fig_4_6_evaluation_criteria",
        "Hình 4.6. Khung tiêu chí đánh giá hệ thống và trạng thái thực hiện",
    )
    r.p(
        "Về tính đúng đắn chức năng, kết quả kiểm chứng được ở mức mã nguồn cho "
        "thấy toàn bộ 19 yêu cầu chức năng đã đặc tả ở Chương 2 đều có hiện "
        "thực tương ứng. Bộ kiểm thử tự động với 641 ca bao phủ tốt các hàm "
        "logic thuần tuý, đặc biệt là những điểm tinh tế như quy đổi toạ độ "
        "hOCR, cộng dồn góc xoay và phân tích chuỗi khoảng trang. Tuy nhiên "
        "tính đúng đắn ở mức tệp thật chưa được xác nhận do bộ kiểm thử chưa "
        "được thực thi và kiểm thử chức năng thủ công chưa được tiến hành."
    )
    r.p(
        "Về quyền riêng tư và bảo mật, đây là nhóm tiêu chí đạt kết quả rõ ràng "
        "nhất ở mức bằng chứng tĩnh. Kiểm chứng mức 1 xác nhận cả bảy biến cấu "
        "hình mô-đun đều trỏ về đường dẫn cục bộ, thư mục tài nguyên chứa đủ "
        "bốn mô-đun với tổng dung lượng 121 megabyte, và tệp khai báo quyền chỉ "
        "cấp bộ quyền lõi mặc định. Mười trong mười hai nhóm chức năng không có "
        "phụ thuộc mạng nào. Cơ chế danh sách máy chủ tin cậy và các lớp làm "
        "sạch dữ liệu đầu vào đã được hiện thực đầy đủ, với 22 ca kiểm thử tái "
        "hiện tấn công chèn mã."
    )
    r.p(
        "Về khả dụng và triển khai, hệ thống có quy trình biên dịch tự động cho "
        "ba hệ điều hành với bốn cấu hình, giao diện tiếng Việt đầy đủ với "
        "1.162 khoá dịch, cấu trúc điều hướng ba đường tiếp cận cho 127 công "
        "cụ, và cơ chế thông báo lỗi phân loại theo bốn nhóm nguyên nhân. Danh "
        "sách kiểm tra khói mười một mục đã được đặc tả sẵn sàng để thực hiện."
    )
    r.p(
        "Về hiệu năng và tài nguyên, chỉ có nhóm chỉ số dung lượng tài nguyên "
        "được đo trực tiếp với kết quả trình bày ở mục 4.1. Các chỉ số về thời "
        "gian xử lý và mức tiêu thụ bộ nhớ chưa được đo."
    )
    r.p(
        "Bảng 4.8 tổng hợp mức độ đạt được của từng nhóm tiêu chí, phân biệt rõ "
        "ba trạng thái: đã kiểm chứng bằng bằng chứng trực tiếp, đã hiện thực "
        "nhưng chưa kiểm chứng, và chưa đo."
    )
    r.table(
        "Bảng 4.8. Tổng hợp mức độ đạt được theo nhóm tiêu chí",
        ["Nhóm tiêu chí", "Đã kiểm chứng", "Đã hiện thực, chưa kiểm chứng",
         "Chưa đo"],
        [
            ["Tính đúng đắn chức năng",
             "Sự tồn tại của hiện thực cho 19 yêu cầu chức năng; cấu trúc 641 "
             "ca kiểm thử",
             "Tính đúng đắn của phép biến đổi trên tệp thật; kết quả chạy bộ "
             "kiểm thử",
             "—"],
            ["Quyền riêng tư và bảo mật",
             "Cấu hình trỏ mô-đun về cục bộ; khai báo quyền tối thiểu; sự tồn "
             "tại của các lớp làm sạch và cơ chế danh sách tin cậy",
             "Hành vi mạng thực tế khi chạy (kiểm chứng mức 2 và mức 3)",
             "—"],
            ["Hiệu năng và tài nguyên",
             "Dung lượng tài nguyên WebAssembly: 121 MB chia cho bốn mô-đun",
             "Sự tồn tại của bảy cơ chế quản lý bộ nhớ",
             "Thời gian xử lý; bộ nhớ đỉnh; thời gian khởi động; dung lượng gói "
             "cài đặt"],
            ["Khả dụng và triển khai",
             "Ma trận biên dịch bốn cấu hình; 1.162 khoá dịch tiếng Việt; cấu "
             "trúc điều hướng và cơ chế thông báo lỗi",
             "Trải nghiệm thực tế trên ba hệ điều hành; sự đồng nhất giữa ba bộ "
             "máy WebView",
             "—"],
        ],
        widths=[3, 5, 5, 3.5],
        font_size=10,
    )

    r.h3("5.2. Hạn chế và nguyên nhân")
    r.p(
        "Hạn chế lớn nhất của phần thử nghiệm là việc chưa thực hiện được ba "
        "trong bốn tầng kiểm thử đã đề ra. Nguyên nhân trực tiếp là điều kiện "
        "môi trường đã nêu ở mục 1.1: máy chủ phân tích không có giao diện đồ "
        "hoạ, dung lượng đĩa trống và bộ nhớ khả dụng không đủ cho việc cài đặt "
        "cây phụ thuộc và biên dịch, và phiên bản Node.js thấp hơn yêu cầu của "
        "dự án. Đây là hạn chế về điều kiện thực hiện chứ không phải hạn chế "
        "của bản thân hệ thống, nhưng nó làm giảm đáng kể giá trị kết luận của "
        "Chương 4."
    )
    r.p(
        "Hạn chế thứ hai nằm ở chính bộ kiểm thử tự động. Việc chạy trên môi "
        "trường mô phỏng cây tài liệu thay vì trình duyệt thật khiến ba mảng "
        "quan trọng không thể kiểm thử: kết xuất trang ra canvas, thực thi "
        "mô-đun WebAssembly đầy đủ, và tương tác với tầng bản địa. Hệ quả là "
        "phần lớn khối lượng mã trong thư mục logic — 47.499 dòng — không được "
        "bao phủ trực tiếp bởi kiểm thử tự động."
    )
    r.p(
        "Hạn chế thứ ba là thiếu kiểm thử hồi quy bằng ảnh cho các phép biến "
        "đổi có tính trực quan. Với những thao tác như đóng dấu chìm, đánh số "
        "trang, dàn trang sách gấp hay gộp nhiều trang lên một tờ, việc kết quả "
        "có đúng hay không phụ thuộc vào vị trí và kích thước của các phần tử "
        "trên trang — thứ mà kiểm thử đơn vị thông thường không kiểm chứng "
        "được. Đáng chú ý là kho mã đã có sẵn thư viện so sánh ảnh trong danh "
        "sách phụ thuộc, cho thấy hướng này đã được nghĩ tới nhưng chưa triển "
        "khai thành bộ kiểm thử hồi quy."
    )
    r.p(
        "Hạn chế thứ tư liên quan tới việc kiểm thử đa nền tảng. Quy trình tích "
        "hợp liên tục hiện chỉ biên dịch và tải lên gói cài đặt, không chạy bất "
        "kỳ kiểm thử nào trên gói đã dựng. Điều đó có nghĩa là sự khác biệt "
        "giữa ba bộ máy WebView — vốn là một rủi ro đã được nhận diện từ Chương "
        "1 — hiện chưa có cơ chế phát hiện tự động."
    )
    r.p(
        "Hạn chế thứ năm là không có dữ liệu so sánh với các giải pháp khác. Để "
        "đánh giá đầy đủ giá trị của hệ thống, cần so sánh thời gian xử lý và "
        "chất lượng kết quả với ít nhất một phần mềm desktop thương mại và một "
        "dịch vụ trực tuyến phổ biến, trên cùng một bộ dữ liệu. Việc này chưa "
        "thực hiện được vì lý do tương tự."
    )
    r.p(
        "Cuối cùng, cần nhắc lại hai hạn chế đã nêu ở Chương 3 vì chúng ảnh "
        "hưởng trực tiếp tới khả năng đưa hệ thống vào sử dụng: gói cài đặt "
        "chưa được ký số nên hệ điều hành sẽ cảnh báo ở lần chạy đầu, và dung "
        "lượng gói cài đặt lớn do phải mang theo toàn bộ tài nguyên xử lý."
    )

    r.h3("5.3. Hướng hoàn thiện công tác thử nghiệm")
    r.p(
        "Trên cơ sở các hạn chế đã nêu, có thể xác định năm hướng hoàn thiện "
        "theo thứ tự ưu tiên."
    )
    r.p(
        "Hướng thứ nhất, có mức độ ưu tiên cao nhất và chi phí thấp nhất, là "
        "thực thi bộ kiểm thử tự động hiện có trên một máy đủ tài nguyên với "
        "Node.js phiên bản 20, thu thập kết quả chạy và báo cáo độ phủ. Việc "
        "này cho ngay một bức tranh định lượng về chất lượng mã và có thể hoàn "
        "thành trong thời gian ngắn."
    )
    r.p(
        "Hướng thứ hai là biên dịch gói cài đặt cho ít nhất một hệ điều hành và "
        "thực hiện đầy đủ danh sách kiểm tra khói mười một mục, kết hợp với "
        "kiểm chứng ngoại tuyến ở mức 2 và mức 3 theo Bảng 4.5. Đây là bước "
        "then chốt để xác nhận yêu cầu cốt lõi của hệ thống, và cũng là bước "
        "cung cấp các ảnh chụp màn hình còn thiếu cho báo cáo."
    )
    r.p(
        "Hướng thứ ba là bổ sung kiểm thử đầu cuối bằng công cụ điều khiển "
        "trình duyệt thật. Việc này cho phép kiểm thử các phép biến đổi PDF "
        "trên tệp thật, kiểm tra kết xuất canvas và bao phủ phần lớn khối lượng "
        "mã hiện chưa được kiểm thử. Có thể triển khai theo hướng chạy bản web "
        "trong trình duyệt không giao diện, để tận dụng lại phần lớn kịch bản "
        "cho cả hai bản dựng."
    )
    r.p(
        "Hướng thứ tư là xây dựng bộ kiểm thử hồi quy bằng so sánh ảnh cho các "
        "phép biến đổi trực quan. Cách làm là kết xuất trang kết quả thành ảnh, "
        "so sánh với ảnh chuẩn đã được kiểm tra thủ công, và báo lỗi khi mức "
        "khác biệt vượt ngưỡng. Thư viện so sánh ảnh đã có sẵn trong danh sách "
        "phụ thuộc nên chi phí triển khai không cao."
    )
    r.p(
        "Hướng thứ năm là mở rộng quy trình tích hợp liên tục để chạy kiểm thử "
        "khói trên gói đã dựng ở cả ba hệ điều hành, kèm đo tự động một số chỉ "
        "số hiệu năng cơ bản. Việc này cho phép phát hiện sớm sự khác biệt giữa "
        "các bộ máy WebView và phát hiện hồi quy về hiệu năng giữa các phiên "
        "bản."
    )

    # ==================================================================
    r.h2("Kết luận chương 4")
    r.p(
        "Chương 4 đã trình bày môi trường thử nghiệm gồm ba loại phục vụ ba mục "
        "đích, đề xuất bộ dữ liệu thử nghiệm gồm mười sáu nhóm được xây dựng "
        "trên cơ sở phân tích các nhánh xử lý trong mã nguồn, và phân tích cấu "
        "trúc bộ kiểm thử tự động hiện có với 641 ca trong 39 tệp phân bố theo "
        "sáu nhóm chức năng."
    )
    r.p(
        "Chương cũng đã đặc tả quy trình kiểm thử chức năng mười bước, mười lăm "
        "kịch bản kiểm thử tiêu biểu nhắm vào các điểm rủi ro đã nhận diện, và "
        "ba mức kiểm chứng khả năng hoạt động ngoại tuyến với giá trị bằng "
        "chứng khác nhau. Kết quả kiểm chứng ở mức 1 xác nhận cấu hình của hệ "
        "thống đáp ứng đúng thiết kế: mười trong mười hai nhóm chức năng không "
        "có phụ thuộc mạng nào."
    )
    r.p(
        "Về đánh giá tài nguyên, chương đã trình bày kết quả đo trực tiếp duy "
        "nhất của phần thử nghiệm: cấu thành 121 megabyte tài nguyên "
        "WebAssembly chia cho bốn mô-đun, kèm phân tích khả năng tối ưu cho "
        "từng thành phần, trong đó chỉ ra hai điểm tối ưu rõ rệt nhất là tám "
        "biến thể lõi nhận dạng ký tự và sự trùng lặp của thư viện CoherentPDF."
    )
    r.p(
        "Về hiệu năng, chương đã đề xuất bộ chín chỉ số kèm phương pháp đo, bộ "
        "dữ liệu tương ứng và ngưỡng chấp nhận, đồng thời chỉ ra ba nhóm chỉ số "
        "có giá trị chẩn đoán thiết kế cao. Phân tích mã nguồn cũng đã xác định "
        "trước ba điểm có nguy cơ về bộ nhớ cần được chú ý khi đo."
    )
    r.p(
        "Điểm cần nhấn mạnh trong kết luận chương này là ranh giới giữa những "
        "gì đã kiểm chứng được và những gì chưa. Ba trong bốn tầng kiểm thử "
        "chưa được thực hiện do điều kiện môi trường, và báo cáo đã nhất quán "
        "để trống các cột kết quả tương ứng thay vì điền số liệu ước lượng. "
        "Năm hướng hoàn thiện đã được đề xuất theo thứ tự ưu tiên, trong đó hai "
        "hướng đầu có chi phí thấp và có thể thực hiện ngay khi có máy đủ điều "
        "kiện."
    )

    # ==================================================================
    # KẾT LUẬN
    # ==================================================================
    r.h1("KẾT LUẬN")

    r.h2("1. Kết quả đạt được")
    r.p(
        "Đề tài đã hoàn thành mục tiêu tổng quát đặt ra: nghiên cứu, phân tích, "
        "thiết kế và hoàn thiện một ứng dụng desktop đa nền tảng cho phép thực "
        "hiện các thao tác xử lý tài liệu PDF và hình ảnh hoàn toàn trên máy "
        "người dùng. Kết quả đạt được có thể tổng hợp theo bốn phương diện."
    )
    r.p(
        "Về phương diện phân tích và thiết kế, đề tài đã hệ thống hoá cơ sở lý "
        "luận về định dạng PDF, về hai mô hình xử lý tài liệu, về công nghệ "
        "WebAssembly và về kiến trúc ứng dụng desktop lai, từ đó rút ra ba ràng "
        "buộc cứng chi phối toàn bộ thiết kế. Trên cơ sở đó, đề tài đã đặc tả "
        "19 yêu cầu chức năng và 19 yêu cầu phi chức năng, xây dựng mô hình ca "
        "sử dụng, thiết kế kiến trúc phân tầng sáu tầng với quan hệ phụ thuộc "
        "một chiều, kiến trúc thành phần được tái dựng từ quan hệ nhập mô-đun "
        "thực tế, kiến trúc triển khai ba giai đoạn, quy trình xử lý tài liệu "
        "chung mười sáu bước, mô hình dữ liệu trong bộ nhớ, cấu trúc điều hướng "
        "và mô hình năm lớp bảo vệ dữ liệu."
    )
    r.p(
        "Về phương diện hiện thực, hệ thống đã được xây dựng hoàn chỉnh với "
        "85.570 dòng mã TypeScript, 127 mục công cụ phân thành bảy nhóm chức "
        "năng, 131 điểm vào giao diện, 79 lớp nút cho tính năng luồng xử lý tự "
        "động và một vỏ ứng dụng bản địa viết bằng Rust ở quy mô tối thiểu. "
        "Mười thư viện xử lý tài liệu đã được tích hợp và phân bổ nhiệm vụ theo "
        "thế mạnh của từng thư viện. Toàn bộ 121 megabyte tài nguyên "
        "WebAssembly đã được tổ chức để đóng gói kèm ứng dụng, bảo đảm khả năng "
        "hoạt động ngoại tuyến."
    )
    r.p(
        "Về phương diện giải quyết các bài toán kỹ thuật cụ thể, đề tài đã xử "
        "lý được một số vấn đề đáng ghi nhận: cơ chế lưu tệp bản địa được thiết "
        "kế để không làm thay đổi hành vi của bản web dù được gọi từ khoảng 311 "
        "vị trí; logic chọn phông chữ theo hệ chữ trong chức năng nhận dạng ký "
        "tự; kỹ thuật dựng lớp văn bản vô hình khớp toạ độ, góc nghiêng và độ "
        "dốc đường cơ sở; bảy cơ chế quản lý dữ liệu tạm bảo đảm nguyên tắc "
        "không ghi tệp ra đĩa; năm cơ chế suy giảm nhẹ nhàng khi gặp trở ngại; "
        "và cơ chế danh sách máy chủ tin cậy kiểm soát nguồn mã thực thi."
    )
    r.p(
        "Về phương diện tài liệu kỹ thuật, đề tài đã tái dựng và để lại 28 sơ "
        "đồ kiến trúc, quy trình và biểu đồ tuần tự, mỗi sơ đồ được lưu ở cả "
        "dạng vector để in ấn và dạng có thể chỉnh sửa, kèm bảng chỉ mục ghi rõ "
        "nguồn bằng chứng trong mã nguồn của từng hình. Đây là phần tài liệu "
        "thường thiếu ở các dự án phần mềm và có giá trị lâu dài cho việc bảo "
        "trì cũng như phát triển tiếp hệ thống."
    )

    r.h2("2. Hạn chế")
    r.p(
        "Hạn chế thứ nhất và cũng là hạn chế ảnh hưởng nhiều nhất tới giá trị "
        "kết luận của đề tài là việc chưa thực hiện được phần lớn công tác thử "
        "nghiệm thực tế. Bộ kiểm thử tự động chưa được thực thi, ứng dụng chưa "
        "được biên dịch và chạy, các số liệu về thời gian xử lý và mức tiêu thụ "
        "bộ nhớ chưa được đo, và các ảnh chụp giao diện chưa được thu thập. "
        "Nguyên nhân là điều kiện tài nguyên của môi trường thực hiện đề tài. "
        "Báo cáo đã xử lý hạn chế này bằng cách nêu rõ ranh giới giữa nội dung "
        "đã kiểm chứng và nội dung chưa kiểm chứng, tuyệt đối không đưa ra số "
        "liệu ước lượng."
    )
    r.p(
        "Hạn chế thứ hai thuộc về bản thân hệ thống: dung lượng gói cài đặt lớn "
        "do phải mang theo toàn bộ tài nguyên xử lý. Đây là cái giá trực tiếp "
        "và không thể tránh khỏi của yêu cầu hoạt động hoàn toàn ngoại tuyến, "
        "nhưng phân tích ở Chương 4 cho thấy vẫn còn dư địa tối ưu đáng kể, đặc "
        "biệt ở tám biến thể lõi của động cơ nhận dạng ký tự."
    )
    r.p(
        "Hạn chế thứ ba là các gói cài đặt chưa được ký số và chưa qua công "
        "chứng, khiến cơ chế bảo vệ của macOS và Windows cảnh báo ở lần chạy "
        "đầu tiên. Đây là rào cản thực tế đối với việc phân phối rộng rãi và "
        "cần được khắc phục bằng việc bổ sung chứng thư ký mã vào quy trình "
        "biên dịch."
    )
    r.p(
        "Hạn chế thứ tư là hai tính năng vẫn phụ thuộc mạng theo thiết kế: đóng "
        "dấu thời gian tin cậy và tải phông chữ theo yêu cầu cho một số ngôn "
        "ngữ. Tính năng thứ nhất về bản chất không thể thực hiện cục bộ vì dấu "
        "thời gian phải do một bên thứ ba tin cậy cấp. Tính năng thứ hai có thể "
        "khắc phục bằng cách đóng gói thêm phông chữ, nhưng sẽ làm tăng dung "
        "lượng gói cài đặt."
    )
    r.p(
        "Hạn chế thứ năm là phạm vi bao phủ của kiểm thử tự động. Do chạy trên "
        "môi trường mô phỏng cây tài liệu, bộ kiểm thử không kiểm chứng được "
        "các phép biến đổi PDF trên tệp thật, không kiểm chứng được phần kết "
        "xuất và không kiểm chứng được tương tác với tầng bản địa. Hệ quả là "
        "phần lớn khối lượng mã nghiệp vụ chưa được bao phủ trực tiếp."
    )
    r.p(
        "Hạn chế thứ sáu là sự khác biệt tiềm tàng giữa ba bộ máy WebView. Do "
        "ứng dụng dùng thành phần hiển thị của hệ điều hành thay vì đóng gói "
        "một bộ máy riêng, kết quả kết xuất và một số hành vi có thể khác nhau "
        "giữa ba nền tảng. Hiện chưa có cơ chế phát hiện tự động sự khác biệt "
        "này."
    )
    r.p(
        "Hạn chế thứ bảy mang tính chức năng: hệ thống chưa hỗ trợ chỉnh sửa "
        "trực tiếp nội dung văn bản có sẵn trong tệp PDF theo kiểu trình soạn "
        "thảo. Đây là một nhu cầu thực tế đáng kể, nhưng cũng là bài toán khó "
        "nhất trong xử lý PDF vì lý do đã phân tích ở Chương 1: định dạng PDF "
        "không lưu giữ cấu trúc logic của văn bản."
    )

    r.h2("3. Hướng phát triển")
    r.p(
        "Hướng phát triển trước mắt, có mức ưu tiên cao nhất, là hoàn thành "
        "công tác thử nghiệm theo năm hướng đã đề xuất ở mục 5.3 của Chương 4: "
        "thực thi bộ kiểm thử tự động và thu thập báo cáo độ phủ; biên dịch gói "
        "cài đặt và thực hiện danh sách kiểm tra khói cùng kiểm chứng ngoại "
        "tuyến ở mức 2 và mức 3; bổ sung kiểm thử đầu cuối bằng trình duyệt "
        "thật; xây dựng bộ kiểm thử hồi quy bằng so sánh ảnh; và mở rộng quy "
        "trình tích hợp liên tục để chạy kiểm thử trên gói đã dựng ở cả ba hệ "
        "điều hành."
    )
    r.p(
        "Hướng phát triển thứ hai là tối ưu dung lượng gói cài đặt. Biện pháp "
        "cụ thể gồm: chỉ giữ biến thể lõi nhận dạng ký tự phù hợp với nền tảng "
        "đích thay vì cả tám biến thể; hợp nhất các bản sao trùng lặp của thư "
        "viện CoherentPDF; và cung cấp cấu hình biên dịch cho phép loại bỏ "
        "những mô-đun không cần thiết với từng ngữ cảnh triển khai. Ba biện "
        "pháp này có thể giảm đáng kể dung lượng mà không ảnh hưởng tới chức "
        "năng cốt lõi."
    )
    r.p(
        "Hướng phát triển thứ ba là bổ sung ký số và công chứng cho các gói cài "
        "đặt, kết hợp với xây dựng quy trình phát hành tự động có kèm tệp kiểm "
        "tra tính toàn vẹn. Việc này không chỉ loại bỏ cảnh báo của hệ điều "
        "hành mà còn cung cấp cho người dùng một cách kiểm chứng rằng gói họ "
        "tải về đúng là gói do dự án phát hành."
    )
    r.p(
        "Hướng phát triển thứ tư là mở rộng khả năng hoạt động ngoại tuyến hoàn "
        "toàn cho chức năng nhận dạng ký tự đa ngôn ngữ, bằng cách cung cấp cơ "
        "chế tải và cài đặt gói ngôn ngữ ngay trong ứng dụng, hoặc cung cấp các "
        "bản dựng theo vùng ngôn ngữ. Với người dùng Việt Nam, việc đóng gói "
        "sẵn dữ liệu ngôn ngữ tiếng Việt cùng phông chữ tương ứng là một cải "
        "tiến có giá trị thực tế cao."
    )
    r.p(
        "Hướng phát triển thứ năm là bổ sung xử lý theo lô ở mức ứng dụng: cho "
        "phép người dùng chọn một thư mục và áp dụng cùng một thao tác cho toàn "
        "bộ tệp trong thư mục đó. Tính năng luồng xử lý tự động đã cung cấp nền "
        "tảng cho việc này, nhưng cần bổ sung khả năng đọc thư mục ở tầng bản "
        "địa — một thay đổi cần cân nhắc kỹ vì nó mở rộng bề mặt quyền của tầng "
        "bản địa."
    )
    r.p(
        "Hướng phát triển thứ sáu là cải thiện trải nghiệm với tài liệu rất "
        "lớn. Các biện pháp gồm: xử lý theo luồng thay vì nạp toàn bộ tệp vào "
        "bộ nhớ ở những thao tác cho phép; bổ sung khả năng huỷ giữa chừng cho "
        "các thao tác kéo dài; và hiển thị ước lượng thời gian còn lại dựa trên "
        "tiến độ thực tế."
    )
    r.p(
        "Hướng phát triển thứ bảy, có tính dài hạn, là bổ sung khả năng chỉnh "
        "sửa nội dung văn bản trong tài liệu PDF. Đây là bài toán khó nhưng có "
        "giá trị sử dụng cao. Một hướng tiếp cận khả thi là giới hạn phạm vi ở "
        "những tài liệu có cấu trúc đơn giản và cung cấp cơ chế xem trước rõ "
        "ràng để người dùng kiểm soát kết quả, thay vì cố gắng xử lý mọi trường "
        "hợp."
    )
    r.p(
        "Cuối cùng, ở mức định hướng chung, mô hình kiến trúc mà đề tài xây "
        "dựng — đưa toàn bộ năng lực xử lý vào máy khách bằng WebAssembly, giữ "
        "tầng bản địa ở quy mô tối thiểu, và bảo đảm khả năng hoạt động ngoại "
        "tuyến bằng cách đóng gói đầy đủ tài nguyên — có thể áp dụng lại cho "
        "những lớp bài toán khác có cùng đặc điểm về yêu cầu bảo vệ dữ liệu. "
        "Việc tổng kết mô hình này thành một khuôn mẫu kiến trúc có thể tái sử "
        "dụng là một hướng nghiên cứu đáng theo đuổi."
    )

    # ==================================================================
    r.h1("TÀI LIỆU THAM KHẢO")
    r.p(
        "Danh mục dưới đây gồm các nguồn được sử dụng trực tiếp trong quá trình "
        "phân tích mã nguồn, tái dựng kiến trúc và biên soạn báo cáo."
    )
    refs = [
        "ISO 32000-2:2020, Document management — Portable document format — "
        "Part 2: PDF 2.0, International Organization for Standardization, 2020.",
        "Adobe Systems Incorporated, PDF Reference, sixth edition: Adobe "
        "Portable Document Format version 1.7, Adobe Systems, 2006.",
        "World Wide Web Consortium, WebAssembly Core Specification, W3C "
        "Recommendation, https://www.w3.org/TR/wasm-core-2/.",
        "Tauri Working Group, Tauri v2 Documentation — Architecture, Commands, "
        "Capabilities and Permissions, https://v2.tauri.app/.",
        "Kho mã nguồn dự án: PDF Toolkit Desktop, "
        "https://github.com/imtoiteu/PDFToolkitDesktop, phiên bản 2.8.5.",
        "Tài liệu nội bộ dự án: DESKTOP.md — Desktop App (Tauri): Architecture, "
        "Commands, Offline Verification, Known Limitations, Smoke Test "
        "Checklist.",
        "Tài liệu nội bộ dự án: README.md — Features, Tools Supported, WASM "
        "Configuration, Air-Gapped Deployment, Security Features.",
        "Dự án BentoPDF (thượng nguồn), https://github.com/alam00000/bentopdf, "
        "giấy phép AGPL-3.0.",
        "pdf-lib — Create and modify PDF documents in any JavaScript "
        "environment, https://pdf-lib.js.org/.",
        "Mozilla Foundation, PDF.js — A general-purpose, web standards-based "
        "platform for parsing and rendering PDFs, "
        "https://mozilla.github.io/pdf.js/.",
        "qpdf — A content-preserving PDF document transformer, "
        "https://qpdf.readthedocs.io/.",
        "Coherent Graphics Ltd., CoherentPDF Command Line Tools and JavaScript "
        "API, https://www.coherentpdf.com/.",
        "Artifex Software, MuPDF and PyMuPDF Documentation, "
        "https://pymupdf.readthedocs.io/.",
        "Artifex Software, Ghostscript Documentation, "
        "https://ghostscript.readthedocs.io/.",
        "Pyodide — Python distribution for the browser and Node.js based on "
        "WebAssembly, https://pyodide.org/.",
        "Tesseract.js — Pure JavaScript OCR for more than 100 languages, "
        "https://tesseract.projectnaptha.com/.",
        "R. Smith, “An Overview of the Tesseract OCR Engine”, Proceedings of "
        "the Ninth International Conference on Document Analysis and "
        "Recognition (ICDAR), 2007, pp. 629–633.",
        "T. Breuel, The hOCR Embedded OCR Workflow and Output Format "
        "Specification, https://github.com/kba/hocr-spec.",
        "C. Adams, P. Cain, D. Pinkas, R. Zuccherato, RFC 3161 — Internet X.509 "
        "Public Key Infrastructure Time-Stamp Protocol (TSP), IETF, 2001.",
        "D. Cooper et al., RFC 5280 — Internet X.509 Public Key Infrastructure "
        "Certificate and CRL Profile, IETF, 2008.",
        "RSA Laboratories, PKCS #12: Personal Information Exchange Syntax "
        "Standard, version 1.1 (RFC 7292), IETF, 2014.",
        "OWASP Foundation, OWASP Cheat Sheet Series — Cross Site Scripting "
        "Prevention, https://cheatsheetseries.owasp.org/.",
        "DOMPurify — DOM-only, super-fast, uber-tolerant XSS sanitizer, "
        "https://github.com/cure53/DOMPurify.",
        "Mozilla Developer Network, Cross-Origin Isolation, SharedArrayBuffer "
        "and the COOP/COEP headers, https://developer.mozilla.org/.",
        "Vite — Next Generation Frontend Tooling, https://vite.dev/.",
        "Vitest — A Vite-native testing framework, https://vitest.dev/.",
        "Rete.js — JavaScript framework for visual programming, "
        "https://retejs.org/.",
        "GitHub, CodeQL Documentation — Security queries for JavaScript and "
        "TypeScript, https://codeql.github.com/.",
    ]
    for i, ref in enumerate(refs):
        p = r.doc.add_paragraph(style="GachDau")
        p.paragraph_format.left_indent = None
        p.add_run("[%d]  %s" % (i + 1, ref))
