# -*- coding: utf-8 -*-
"""Chương 2 — Phân tích và thiết kế hệ thống."""


def build(r):
    r.h1("CHƯƠNG 2. PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG")

    # ==================================================================
    r.h2("1. Phân tích bài toán")

    r.h3("1.1. Đặt vấn đề và mục tiêu xây dựng hệ thống")
    r.p(
        "Bài toán đặt ra cho hệ thống có thể phát biểu ngắn gọn như sau: xây "
        "dựng một ứng dụng cài đặt trên máy tính cá nhân, cung cấp đủ rộng các "
        "thao tác xử lý tài liệu PDF và hình ảnh cho công việc hằng ngày, sao "
        "cho trong suốt quá trình sử dụng không có bất kỳ byte nội dung tài "
        "liệu nào rời khỏi máy người dùng, và sao cho ứng dụng vẫn hoạt động "
        "đầy đủ khi máy không có kết nối mạng."
    )
    r.p(
        "Phát biểu này chứa ba ràng buộc cứng có ảnh hưởng quyết định tới toàn "
        "bộ thiết kế. Ràng buộc thứ nhất là “không truyền tài liệu ra ngoài”: "
        "nó loại bỏ hoàn toàn khả năng đặt bất kỳ thành phần xử lý nào ở phía "
        "máy chủ, kéo theo việc mọi thư viện xử lý phải chạy được trong môi "
        "trường máy khách. Ràng buộc thứ hai là “hoạt động khi không có mạng”: "
        "nó loại bỏ khả năng nạp mô-đun xử lý từ mạng phân phối nội dung khi "
        "chạy, buộc toàn bộ tài nguyên phải được đóng gói sẵn. Ràng buộc thứ ba "
        "là “đủ rộng cho công việc hằng ngày”: nó buộc hệ thống phải có số "
        "lượng công cụ lớn, từ đó buộc kiến trúc phải có tính khuôn mẫu cao."
    )
    r.p(
        "Bên cạnh ba ràng buộc cứng, bài toán còn có một số mục tiêu mềm. Ứng "
        "dụng cần có cảm giác của một phần mềm bản địa chứ không phải một trang "
        "web đóng khung: hộp thoại chọn và lưu tệp phải là hộp thoại của hệ "
        "điều hành, người dùng phải tự chọn được nơi lưu kết quả thay vì bị "
        "buộc vào thư mục Tải xuống. Giao diện cần có tiếng Việt đầy đủ và đặt "
        "tiếng Việt làm ngôn ngữ mặc định. Ứng dụng cần chạy trên cả ba hệ điều "
        "hành phổ biến từ một mã nguồn duy nhất để chi phí bảo trì không nhân "
        "lên ba lần."
    )
    r.p(
        "Từ ba ràng buộc cứng, có thể suy ra ngay một số kết luận thiết kế "
        "quan trọng trước khi đi vào chi tiết. Thứ nhất, hệ thống không có tài "
        "khoản người dùng, không có phân quyền, không có cơ sở dữ liệu và không "
        "có nhật ký tập trung — không phải vì bỏ sót mà vì những thành phần đó "
        "chỉ có ý nghĩa khi tồn tại máy chủ. Thứ hai, mọi trạng thái của ứng "
        "dụng đều là trạng thái phiên, mất đi khi đóng cửa sổ, ngoại trừ một "
        "lượng rất nhỏ tuỳ chọn giao diện. Thứ ba, ranh giới bảo mật quan trọng "
        "nhất của hệ thống không nằm giữa người dùng và máy chủ mà nằm giữa "
        "tầng giao diện chạy trong WebView và tầng vỏ bản địa có quyền truy cập "
        "hệ tệp."
    )

    r.h3("1.2. Phạm vi chức năng của hệ thống")
    r.p(
        "Phạm vi chức năng được xác định trên cơ sở đối chiếu sáu nhóm mục đích "
        "công việc đã phân tích ở Chương 1 với các công cụ thực sự được khai "
        "báo trong tệp cấu hình danh mục của hệ thống. Danh mục này tổ chức các "
        "công cụ thành bảy nhóm hiển thị, mỗi nhóm tương ứng với một mục trên "
        "thanh bên của màn hình làm việc. Bảng 2.1 tổng hợp bảy nhóm cùng số "
        "lượng công cụ và các thao tác tiêu biểu của từng nhóm."
    )
    r.table(
        "Bảng 2.1. Bảy nhóm công cụ và phạm vi thao tác của từng nhóm",
        ["Nhóm công cụ", "Số mục", "Thao tác tiêu biểu"],
        [
            ["Công cụ phổ biến", "12",
             "Trình dựng luồng xử lý, công cụ đa năng, ghép, tách, nén, soạn "
             "thảo, ảnh sang PDF, ký, cắt lề, trích trang, nhân bản và sắp xếp, "
             "xoá trang"],
            ["Chỉnh sửa và chú thích", "20",
             "Soạn thảo và chú thích, bookmark, mục lục, số trang, nhãn trang, "
             "đánh số Bates, đóng dấu chìm, đầu/chân trang, đảo màu, hiệu ứng "
             "bản quét, hiệu chỉnh màu, màu nền, màu chữ, ký tay, con dấu ảnh, "
             "gỡ chú thích, cắt lề, điền biểu mẫu, tạo biểu mẫu, gỡ trang trắng"],
            ["Chuyển đổi sang PDF", "33",
             "Ảnh (JPG, PNG, WebP, SVG, BMP, HEIC, TIFF, PSD), văn bản, "
             "Markdown, JSON, XML, CSV, RTF, tài liệu văn phòng (Word, Excel, "
             "PowerPoint, ODT, ODS, ODP, ODG, WPD, WPS, PUB, VSD, Pages), sách "
             "điện tử (EPUB, MOBI, FB2, CBZ), XPS, thư điện tử"],
            ["Chuyển đổi từ PDF", "16",
             "PDF sang JPG, PNG, WebP, BMP, TIFF, CBZ, SVG, CSV, Excel, Word, "
             "JSON, Markdown, văn bản; chuyển sang thang xám; trích ảnh; chuẩn "
             "bị tài liệu cho mô hình ngôn ngữ"],
            ["Tổ chức và quản lý", "27",
             "Nhận dạng ký tự quang học, ghép, ghép xen kẽ, nhân bản và sắp "
             "xếp, chồng tài liệu, tệp đính kèm, công cụ đa năng, lớp nội dung, "
             "trích bảng, tách, chia trang, trích trang, xoá trang, chèn trang "
             "trắng, đảo thứ tự, xoay, gộp nhiều trang lên một tờ, dàn trang "
             "sách gấp, gộp thành một trang dài, xem và sửa siêu dữ liệu, đóng "
             "gói ZIP, so sánh hai tài liệu, chia trang khổ lớn"],
            ["Tối ưu và sửa chữa", "10",
             "Nén, chuyển PDF/A, chuẩn hoá khổ trang, tuyến tính hoá, phân tích "
             "kích thước trang, gỡ hạn chế, sửa tệp hỏng, kết xuất thành ảnh, "
             "khử nghiêng, chuyển phông thành đường nét"],
            ["Bảo mật tài liệu", "9",
             "Mã hoá, làm sạch, giải mã, làm phẳng, gỡ siêu dữ liệu, đặt quyền "
             "sử dụng, ký số, kiểm tra chữ ký, đóng dấu thời gian"],
        ],
        widths=[3, 1.2, 9],
        font_size=11,
    )
    r.p(
        "Tổng cộng có 127 mục công cụ được khai báo trong danh mục, trong đó "
        "một số công cụ xuất hiện ở nhiều nhóm vì phục vụ nhiều mục đích khác "
        "nhau; hệ thống khử trùng lặp theo định danh khi dựng mục “Tất cả công "
        "cụ”. Về mặt tệp, hệ thống có 117 trang công cụ trong thư mục trang "
        "riêng cùng 14 trang gốc gồm trang chủ, bốn trang nhóm chủ đề và các "
        "trang thông tin, tổng cộng 131 điểm vào được khai báo trong cấu hình "
        "biên dịch."
    )
    r.p(
        "Cần nêu rõ những gì nằm ngoài phạm vi. Hệ thống không chỉnh sửa trực "
        "tiếp nội dung văn bản có sẵn trong tệp PDF theo kiểu trình soạn thảo "
        "văn bản — đây là tính năng nằm trong lộ trình phát triển của dự án "
        "nhưng chưa được hiện thực hoá. Hệ thống không đồng bộ tài liệu giữa "
        "các máy, không có kho lưu trữ, không có lịch sử xử lý lâu dài. Hệ "
        "thống cũng không cung cấp tính năng cộng tác nhiều người trên cùng một "
        "tài liệu. Tất cả những giới hạn này là hệ quả trực tiếp và có ý thức "
        "của ràng buộc “không có máy chủ”."
    )

    r.h3("1.3. Người dùng và ranh giới trách nhiệm")
    r.p(
        "Hệ thống chỉ có một nhóm người dùng duy nhất. Người dùng cài đặt ứng "
        "dụng trên máy của mình, mở tệp từ hệ thống tệp cục bộ, chọn thao tác, "
        "nhập tham số và lưu kết quả. Không tồn tại vai trò quản trị viên, "
        "không có cơ chế đăng nhập, không có phân quyền chức năng. Quyền truy "
        "cập tệp của người dùng chính là quyền của tài khoản hệ điều hành đang "
        "chạy ứng dụng — hệ thống không bổ sung cũng không thu hẹp quyền đó."
    )
    r.p(
        "Điểm này khác biệt căn bản so với các hệ thống xử lý tài liệu tập "
        "trung và cần được nêu rõ vì nó ảnh hưởng tới cách đọc phần thiết kế "
        "bảo mật. Trong hệ thống tập trung, bảo mật xoay quanh việc xác thực "
        "danh tính và kiểm soát ai được làm gì với tài liệu nào. Trong hệ thống "
        "này, bảo mật xoay quanh việc bảo đảm dữ liệu không rời khỏi máy, bảo "
        "đảm mã thực thi đến từ nguồn tin cậy, và bảo đảm dữ liệu trung gian "
        "được dọn sạch."
    )
    r.p(
        "Về ranh giới trách nhiệm, hệ thống chịu trách nhiệm cho những gì diễn "
        "ra bên trong tiến trình ứng dụng: tính đúng đắn của phép biến đổi, "
        "việc không phát sinh kết nối ngoài ý muốn, việc dọn dẹp dữ liệu trung "
        "gian, việc thông báo lỗi rõ ràng. Hệ thống không chịu trách nhiệm cho "
        "an toàn của chính máy tính người dùng, cho việc tệp kết quả được lưu ở "
        "đâu sau khi người dùng chọn, hay cho việc người dùng chia sẻ tệp đó "
        "cho ai. Ranh giới này cần được nêu trong tài liệu hướng dẫn để người "
        "dùng có kỳ vọng đúng."
    )
    r.p(
        "Ngoài người dùng, hệ thống tương tác với ba tác nhân phụ. Hệ điều hành "
        "cung cấp WebView để kết xuất giao diện và hộp thoại để chọn cũng như "
        "lưu tệp. Hệ thống tệp cục bộ là nơi đọc tệp nguồn và ghi tệp kết quả. "
        "Máy chủ cấp dấu thời gian là tác nhân bên ngoài duy nhất, chỉ tham gia "
        "khi người dùng chủ động sử dụng tính năng đóng dấu thời gian cho chữ "
        "ký số."
    )

    # ==================================================================
    r.h2("2. Phân tích yêu cầu hệ thống")

    r.h3("2.1. Yêu cầu chức năng")
    r.p(
        "Yêu cầu chức năng được đặc tả theo tám nhóm, mỗi nhóm tương ứng với "
        "một mảng năng lực của hệ thống. Bảng 2.2 trình bày các yêu cầu này "
        "kèm mức độ ưu tiên và ghi chú về mức độ hiện thực hoá đã được kiểm "
        "chứng trong mã nguồn."
    )
    r.table(
        "Bảng 2.2. Đặc tả yêu cầu chức năng của hệ thống",
        ["Mã", "Yêu cầu chức năng", "Mức độ", "Trạng thái hiện thực"],
        [
            ["CN-01",
             "Nạp tệp đầu vào qua hộp thoại chọn tệp của hệ điều hành và qua "
             "thao tác kéo–thả vào vùng nhận tệp; lọc theo kiểu MIME và phần "
             "mở rộng; cho phép nạp nhiều tệp với các công cụ đa tệp",
             "Bắt buộc", "Đã hiện thực ở mọi trang công cụ"],
            ["CN-02",
             "Phát hiện tệp có mật khẩu, hỏi mật khẩu theo từng tệp hoặc theo "
             "lô, ghi nhớ mật khẩu trong phiên và giải mã trước khi xử lý",
             "Bắt buộc", "Đã hiện thực trong password-prompt.ts và "
             "pdf-decrypt.ts"],
            ["CN-03",
             "Hiển thị thông tin tệp đã nạp: tên, dung lượng, số trang, ảnh thu "
             "nhỏ của từng trang, cho phép xoá tệp khỏi danh sách",
             "Bắt buộc", "Đã hiện thực; ảnh thu nhỏ được kết xuất theo lô và "
             "nạp lười"],
            ["CN-04",
             "Nhóm tổ chức trang: ghép nhiều tệp, ghép xen kẽ, tách, chia "
             "trang, trích trang, xoá trang, chèn trang trắng, đảo thứ tự, "
             "xoay theo góc chuẩn và góc tuỳ ý, gộp nhiều trang lên một tờ, "
             "dàn trang sách gấp, gộp thành một trang dài, chia trang khổ lớn",
             "Bắt buộc", "Đã hiện thực; 27 công cụ trong nhóm Tổ chức và quản lý"],
            ["CN-05",
             "Nhóm chỉnh sửa: đóng dấu chìm bằng chữ và bằng ảnh, đánh số "
             "trang, nhãn trang, đánh số Bates, đầu và chân trang, cắt lề, "
             "chú thích và làm nổi bật, ký tay, con dấu ảnh, che nội dung vĩnh "
             "viễn, hiệu chỉnh màu, hiệu ứng bản quét, bookmark và mục lục",
             "Bắt buộc", "Đã hiện thực; 20 công cụ trong nhóm Chỉnh sửa"],
            ["CN-06",
             "Nhóm chuyển đổi sang PDF từ ảnh, văn bản thuần, Markdown, CSV, "
             "JSON, XML, tài liệu văn phòng, sách điện tử, XPS và thư điện tử",
             "Bắt buộc", "Đã hiện thực; 33 công cụ"],
            ["CN-07",
             "Nhóm chuyển đổi từ PDF sang ảnh nhiều định dạng, SVG, văn bản, "
             "Markdown, JSON, CSV, Excel, Word, CBZ và trích ảnh, trích bảng",
             "Bắt buộc", "Đã hiện thực; 16 công cụ"],
            ["CN-08",
             "Nén tài liệu theo hai chiến lược: giữ nguyên lớp văn bản và kết "
             "xuất lại thành ảnh; mỗi chiến lược có bốn mức và cho phép tuỳ "
             "chỉnh tham số",
             "Bắt buộc", "Đã hiện thực trong compress.ts và compress-pdf-page.ts"],
            ["CN-09",
             "Mã hoá tài liệu bằng AES-256 với mật khẩu người dùng và mật khẩu "
             "chủ sở hữu; đặt các hạn chế in, sao chép, chỉnh sửa; gỡ mật khẩu; "
             "gỡ hạn chế",
             "Bắt buộc", "Đã hiện thực trên nền qpdf-wasm"],
            ["CN-10",
             "Làm sạch tài liệu: gỡ siêu dữ liệu, chú thích, mã kịch bản, tệp "
             "nhúng, lớp nội dung, liên kết, cây cấu trúc; làm phẳng biểu mẫu "
             "và chú thích",
             "Bắt buộc", "Đã hiện thực trong sanitize.ts với mười tuỳ chọn độc "
             "lập"],
            ["CN-11",
             "Ký số bằng chứng thư X.509 từ tệp PFX hoặc PEM; đóng dấu thời "
             "gian theo RFC 3161 với danh sách máy chủ định sẵn; kiểm tra chữ "
             "ký và hiển thị thông tin chứng thư",
             "Bắt buộc", "Đã hiện thực; khoá riêng chỉ tồn tại trong bộ nhớ"],
            ["CN-12",
             "Nhận dạng ký tự quang học, sinh lớp văn bản ẩn đặt đúng vị trí "
             "trên ảnh gốc, hỗ trợ chọn ngôn ngữ, độ phân giải, nhị phân hoá, "
             "danh sách ký tự cho phép và chế độ phân đoạn trang",
             "Bắt buộc", "Đã hiện thực trên nền Tesseract.js; dữ liệu tiếng Anh "
             "đóng gói sẵn"],
            ["CN-13",
             "Xây dựng luồng xử lý tự động bằng trình soạn thảo đồ thị trực "
             "quan, cho phép nối các nút xử lý thành chuỗi và thực thi theo thứ "
             "tự phụ thuộc",
             "Nên có", "Đã hiện thực; 79 lớp nút xử lý"],
            ["CN-14",
             "So sánh hai tài liệu và xuất báo cáo khác biệt",
             "Nên có", "Đã hiện thực; xử lý trong Web Worker riêng"],
            ["CN-15",
             "Lưu kết quả bằng hộp thoại lưu tệp của hệ điều hành, cho phép "
             "người dùng chọn vị trí và tên tệp; xử lý đúng trường hợp người "
             "dùng huỷ hộp thoại",
             "Bắt buộc", "Đã hiện thực qua lệnh save_file của tầng Rust"],
            ["CN-16",
             "Chuyển đổi ngôn ngữ giao diện ngay trong ứng dụng; ghi nhớ lựa "
             "chọn giữa các lần chạy; mặc định tiếng Việt ở lần chạy đầu",
             "Bắt buộc", "Đã hiện thực; 21 ngôn ngữ"],
            ["CN-17",
             "Cho phép người dùng cấu hình nguồn nạp các mô-đun xử lý và kiểm "
             "tra tính khả dụng của nguồn đã cấu hình",
             "Nên có", "Đã hiện thực trong trang cấu hình mô-đun"],
            ["CN-18",
             "Cho phép người triển khai vô hiệu hoá một số công cụ theo cấu "
             "hình khi biên dịch hoặc khi chạy",
             "Có thể có", "Đã hiện thực qua biến DISABLE_TOOLS và tệp "
             "config.json"],
            ["CN-19",
             "Cung cấp phím tắt cho các thao tác thường dùng và cho phép người "
             "dùng đặt lại phím tắt",
             "Có thể có", "Đã hiện thực trong shortcuts.ts"],
        ],
        widths=[1.2, 7, 1.6, 5],
        font_size=10,
    )

    r.h3("2.2. Yêu cầu phi chức năng")
    r.p(
        "Yêu cầu phi chức năng của hệ thống có một đặc điểm khác thường: yêu "
        "cầu quan trọng nhất — quyền riêng tư — không phải là một thuộc tính "
        "chất lượng có thể cải thiện dần mà là một thuộc tính nhị phân của kiến "
        "trúc. Hoặc hệ thống truyền tài liệu ra ngoài, hoặc không. Vì vậy nhóm "
        "yêu cầu này được đặt lên đầu và được đặc tả theo cách có thể kiểm "
        "chứng được."
    )
    r.p("Nhóm yêu cầu về quyền riêng tư và bảo mật gồm các điểm sau:")
    r.bullets([
        "PC-01. Trong toàn bộ vòng đời của một thao tác xử lý, không có yêu cầu "
        "mạng nào mang theo nội dung tài liệu hoặc siêu dữ liệu của tài liệu. "
        "Yêu cầu này phải kiểm chứng được bằng cách quan sát tab Network của "
        "công cụ phát triển hoặc bằng cách ngắt kết nối mạng.",
        "PC-02. Toàn bộ thao tác lõi phải hoạt động khi máy không có kết nối "
        "mạng. Chỉ hai tính năng được phép phụ thuộc mạng là đóng dấu thời gian "
        "và tải phông chữ theo yêu cầu; cả hai phải là tuỳ chọn do người dùng "
        "chủ động kích hoạt và phải được nêu rõ trong tài liệu.",
        "PC-03. Không ghi tệp tạm ra đĩa trong quá trình xử lý. Mọi dữ liệu "
        "trung gian chỉ tồn tại trong bộ nhớ tiến trình và phải được giải phóng "
        "tường minh khi không còn dùng, kể cả trên nhánh xử lý lỗi.",
        "PC-04. Mật khẩu tài liệu và khoá riêng của chứng thư số không được ghi "
        "vào bộ nhớ bền vững dưới bất kỳ hình thức nào và chỉ tồn tại trong "
        "phạm vi phiên làm việc.",
        "PC-05. Tầng giao diện không được có quyền truy cập trực tiếp hệ tệp. "
        "Mọi thao tác ghi tệp phải đi qua một lệnh bản địa duy nhất được khai "
        "báo tường minh.",
        "PC-06. Mã thực thi chỉ được nạp từ những nguồn nằm trong danh sách máy "
        "chủ tin cậy; địa chỉ do người dùng cấu hình phải được kiểm tra và loại "
        "bỏ nếu không thuộc danh sách.",
        "PC-07. Mọi nội dung do tệp đầu vào cung cấp — tên tệp, siêu dữ liệu, "
        "nội dung HTML trong thư điện tử, nội dung Markdown — phải được làm "
        "sạch trước khi hiển thị trong giao diện.",
    ])
    r.p("Nhóm yêu cầu về hiệu năng và tài nguyên gồm:")
    r.bullets([
        "PC-08. Thao tác trên cấu trúc trang với tài liệu cỡ vài chục trang "
        "phải hoàn thành trong thời gian đủ ngắn để người dùng chờ trực tiếp mà "
        "không cần chuyển sang việc khác.",
        "PC-09. Với các thao tác kéo dài, giao diện phải giữ được khả năng phản "
        "hồi và phải hiển thị trạng thái tiến trình theo từng bước cụ thể thay "
        "vì một vòng quay không xác định.",
        "PC-10. Mức tiêu thụ bộ nhớ không được tăng tuyến tính theo số trang "
        "của tài liệu; các thao tác duyệt nhiều trang phải có điểm giải phóng "
        "định kỳ.",
        "PC-11. Việc khởi tạo các mô-đun xử lý nặng phải được thực hiện một lần "
        "và tái sử dụng trong suốt phiên, tránh khởi tạo lại cho mỗi thao tác.",
    ])
    r.p("Nhóm yêu cầu về khả dụng và trải nghiệm gồm:")
    r.bullets([
        "PC-12. Giao diện phải sử dụng tiếng Việt làm ngôn ngữ mặc định ở lần "
        "chạy đầu tiên và cho phép chuyển đổi ngôn ngữ ngay trong ứng dụng mà "
        "không cần khởi động lại.",
        "PC-13. Mọi công cụ phải có cấu trúc giao diện đồng nhất: khu vực nạp "
        "tệp, bảng tham số, nút xử lý, hộp thoại thông báo, đường quay lại danh "
        "mục công cụ.",
        "PC-14. Thông báo lỗi phải nêu được nguyên nhân ở mức người dùng hiểu "
        "được và, khi có thể, nêu hướng khắc phục; không hiển thị nguyên văn "
        "thông điệp lỗi kỹ thuật của thư viện.",
        "PC-15. Người dùng phải chọn được vị trí lưu tệp kết quả; việc huỷ hộp "
        "thoại lưu không được coi là lỗi và không được để lại tệp dở dang.",
    ])
    r.p("Nhóm yêu cầu về khả năng bảo trì và triển khai gồm:")
    r.bullets([
        "PC-16. Các công cụ phải tuân theo một khuôn mẫu chung về cấu trúc "
        "trang và cấu trúc mô-đun nghiệp vụ, để việc thêm công cụ mới không làm "
        "tăng độ phức tạp của hệ thống.",
        "PC-17. Hệ thống phải biên dịch được cho macOS, Windows và Linux từ một "
        "mã nguồn duy nhất, với quy trình tự động hoá trên máy chạy hệ điều "
        "hành tương ứng.",
        "PC-18. Việc bổ sung bản dựng desktop không được làm thay đổi hành vi "
        "của bản dựng web và bản dựng cho mạng nội bộ.",
        "PC-19. Mã nguồn phải được kiểm tra bằng công cụ phân tích tĩnh có luật "
        "về an toàn, và phụ thuộc phải được quét lỗ hổng định kỳ.",
    ])
    r.p(
        "Đặc điểm chung của các yêu cầu trên là phần lớn có thể kiểm chứng "
        "được bằng quan sát trực tiếp hoặc bằng đọc cấu hình, thay vì phải suy "
        "luận. Đây là chủ ý thiết kế: với một hệ thống mà giá trị cốt lõi là "
        "sự tin cậy về dữ liệu, khả năng kiểm chứng quan trọng không kém khả "
        "năng thực hiện."
    )

    r.h3("2.3. Mô hình ca sử dụng của hệ thống")
    r.p(
        "Do hệ thống chỉ có một nhóm người dùng và không có phân quyền, mô hình "
        "ca sử dụng tương đối phẳng: mọi ca sử dụng đều thuộc về cùng một tác "
        "nhân chính. Hình 2.1 trình bày biểu đồ ca sử dụng tổng quát, trong đó "
        "các ca sử dụng được gộp theo nhóm chức năng thay vì liệt kê từng công "
        "cụ, bởi 127 công cụ đều chia sẻ chung một khuôn mẫu tương tác."
    )
    r.figure(
        "fig_2_1_use_case",
        "Hình 2.1. Biểu đồ ca sử dụng tổng quát của hệ thống PDF Toolkit "
        "Desktop",
    )
    r.p(
        "Biểu đồ cho thấy tác nhân chính là Người dùng, kết nối tới mười một "
        "nhóm ca sử dụng nằm trong ranh giới hệ thống. Hai tác nhân phụ nằm "
        "ngoài ranh giới: Hệ thống tệp cục bộ tham gia vào ca “Nạp tệp đầu vào” "
        "theo hướng đọc và ca “Lưu kết quả” theo hướng ghi; Máy chủ TSA chỉ "
        "tham gia vào ca “Ký số và kiểm tra chữ ký số” với quan hệ tuỳ chọn, "
        "được vẽ bằng nét đứt để nhấn mạnh rằng nhánh này không bắt buộc."
    )
    r.p(
        "Điểm quan trọng nhất cần đọc từ biểu đồ này là những gì không có mặt. "
        "Không có tác nhân quản trị viên, không có ca sử dụng đăng nhập, không "
        "có ca sử dụng quản lý người dùng, không có ca sử dụng tra cứu lịch sử "
        "xử lý, và không có tác nhân máy chủ ứng dụng. Đây không phải là sự "
        "thiếu sót trong phân tích mà là hệ quả trực tiếp của kiến trúc không "
        "máy chủ đã trình bày ở mục 1.1: những ca sử dụng đó chỉ có ý nghĩa khi "
        "tồn tại một thành phần tập trung cần được kiểm soát truy cập."
    )
    r.p(
        "Ba ca sử dụng đáng chú ý về mặt thiết kế. Ca “Nạp tệp đầu vào” là "
        "điểm vào chung của mọi luồng xử lý và là nơi diễn ra bước phát hiện "
        "tài liệu có mật khẩu; mọi công cụ đều đi qua ca này. Ca “Lưu kết quả "
        "bằng hộp thoại của hệ điều hành” là điểm ra chung và là ca sử dụng duy "
        "nhất chạm tới tầng bản địa. Ca “Xây dựng luồng xử lý tự động” khác "
        "biệt về bản chất so với các ca còn lại: thay vì thực hiện một thao tác "
        "trên một tài liệu, nó cho phép người dùng định nghĩa một chuỗi thao "
        "tác và thực thi chuỗi đó, do đó nó tái sử dụng gần như toàn bộ năng "
        "lực của các ca sử dụng khác."
    )
    r.p(
        "Ca “Thiết lập ngôn ngữ và nguồn mô-đun WASM” gộp các thao tác cấu "
        "hình. Ngôn ngữ giao diện được chuyển đổi ngay tại chỗ và ghi nhớ giữa "
        "các lần chạy. Nguồn mô-đun xử lý có thể được người dùng thay đổi trong "
        "trang cấu hình riêng, phục vụ trường hợp triển khai đặc thù; tuy nhiên "
        "địa chỉ nhập vào phải vượt qua kiểm tra danh sách máy chủ tin cậy như "
        "đã nêu ở yêu cầu PC-06."
    )

    # ==================================================================
    r.h2("3. Thiết kế kiến trúc hệ thống")

    r.h3("3.1. Biểu đồ ngữ cảnh hệ thống")
    r.p(
        "Biểu đồ ngữ cảnh xác định ranh giới của hệ thống và mọi thực thể mà hệ "
        "thống trao đổi dữ liệu. Với một hệ thống thông thường, biểu đồ này "
        "thường có nhiều luồng dữ liệu ra vào. Với PDF Toolkit Desktop, giá trị "
        "chính của biểu đồ nằm ở chỗ nó cho thấy số luồng ra ngoài ít đến mức "
        "nào. Hình 2.2 trình bày biểu đồ ngữ cảnh của hệ thống."
    )
    r.figure(
        "fig_2_2_context",
        "Hình 2.2. Biểu đồ ngữ cảnh của hệ thống PDF Toolkit Desktop",
    )
    r.p(
        "Ở trung tâm là ứng dụng, gồm vỏ Tauri và WebView. Người dùng trao đổi "
        "trực tiếp hai chiều: đưa vào thao tác và tham số, nhận về kết quả và "
        "thông báo. Hệ điều hành nằm phía trên, cung cấp WebView để kết xuất "
        "giao diện, cung cấp hộp thoại chọn tệp khi người dùng bấm vào vùng nạp "
        "tệp, và nhận yêu cầu hiển thị hộp thoại lưu khi ứng dụng có kết quả. "
        "Hệ thống tệp cục bộ nằm phía dưới; đáng chú ý là ứng dụng không truy "
        "cập trực tiếp hệ tệp mà luôn thông qua hộp thoại của hệ điều hành."
    )
    r.p(
        "Bên trái là kho mô-đun WebAssembly được đóng gói kèm ứng dụng, dung "
        "lượng 121 MB. Đây là nguồn cung cấp năng lực xử lý và nằm hoàn toàn "
        "bên trong gói cài đặt, nên mũi tên nạp mô-đun không vượt qua ranh giới "
        "máy người dùng."
    )
    r.p(
        "Bên phải là ba thực thể bên ngoài, tất cả đều được vẽ bằng nét đứt để "
        "biểu thị tính không bắt buộc hoặc không sử dụng. Máy chủ TSA được liên "
        "hệ khi và chỉ khi người dùng chọn đóng dấu thời gian cho chữ ký số; hệ "
        "thống có sẵn danh sách năm nhà cung cấp thông dụng để người dùng chọn. "
        "Nguồn phông chữ CJK và Noto được liên hệ khi người dùng thực hiện nhận "
        "dạng ký tự cho những ngôn ngữ mà phông tương ứng chưa được đóng gói "
        "sẵn. Mạng phân phối nội dung jsDelivr xuất hiện trong biểu đồ nhưng "
        "không có mũi tên trao đổi dữ liệu: nó chỉ được bản web sử dụng, còn "
        "bản desktop đã trỏ toàn bộ đường dẫn mô-đun về thư mục cục bộ."
    )
    r.p(
        "So sánh biểu đồ này với biểu đồ ngữ cảnh của một dịch vụ xử lý PDF "
        "trực tuyến làm nổi bật sự khác biệt về mô hình: ở đó, luồng dữ liệu "
        "chính là luồng tệp đi từ máy người dùng lên máy chủ và quay về; ở đây, "
        "luồng đó không tồn tại. Toàn bộ đường đi của tài liệu nằm gọn trong "
        "ranh giới máy người dùng."
    )

    r.h3("3.2. Kiến trúc phân tầng tổng thể")
    r.p(
        "Hệ thống được tổ chức thành sáu tầng với quan hệ phụ thuộc một chiều "
        "từ trên xuống. Nguyên tắc phân tầng ở đây khác với kiến trúc ba tầng "
        "quen thuộc của ứng dụng web, bởi không có tầng nào nằm trên mạng. "
        "Thay vào đó, các tầng được phân chia theo môi trường thực thi và theo "
        "mức độ đặc quyền. Hình 2.3 trình bày kiến trúc tổng thể."
    )
    r.figure(
        "fig_2_3_layered_architecture",
        "Hình 2.3. Kiến trúc phân tầng tổng thể của hệ thống",
    )
    r.p(
        "Tầng trên cùng là vỏ ứng dụng bản địa viết bằng Rust trên nền Tauri "
        "phiên bản 2. Tầng này có bốn thành phần: điểm vào tiến trình, lệnh lưu "
        "tệp, trình cắm hộp thoại và tệp khai báo quyền. Điều đáng chú ý là quy "
        "mô rất nhỏ của tầng này: toàn bộ mã Rust của dự án chỉ khoảng năm mươi "
        "dòng, trong đó phần thân của lệnh lưu tệp chiếm khoảng một nửa. Đây là "
        "hệ quả có chủ ý của nguyên tắc tối thiểu hoá bề mặt bản địa — càng ít "
        "mã bản địa thì càng ít khả năng phát sinh lỗ hổng có đặc quyền cao."
    )
    r.p(
        "Tầng thứ hai là WebView của hệ điều hành. Tầng này không do dự án viết "
        "nhưng là một phần thiết yếu của kiến trúc và có ba hiện thực khác nhau "
        "tuỳ hệ điều hành. Cấu hình quan trọng nhất ở tầng này là hai tiêu đề "
        "cách ly nguồn gốc được đặt trong tệp cấu hình Tauri, nhờ đó "
        "SharedArrayBuffer khả dụng và các mô-đun WebAssembly đa luồng chạy "
        "được."
    )
    r.p(
        "Tầng thứ ba là tầng giao diện, gồm 131 trang HTML, các phần giao diện "
        "dùng chung, kiểu trình bày bằng Tailwind, và ba mô-đun TypeScript cốt "
        "lõi: mô-đun chính dựng thanh bên và lưới thẻ công cụ, mô-đun giao diện "
        "cung cấp các thành phần dùng chung như chỉ báo tải và hộp thoại thông "
        "báo, và mô-đun quốc tế hoá. Tầng này chịu trách nhiệm về mọi thứ người "
        "dùng nhìn thấy nhưng không chứa logic xử lý tài liệu."
    )
    r.p(
        "Tầng thứ tư là tầng điều phối nghiệp vụ, tầng lớn nhất của hệ thống "
        "với 132 mô-đun trong thư mục logic, tương đương hơn bốn mươi bảy nghìn "
        "dòng mã. Mỗi mô-đun tương ứng với một công cụ và chịu trách nhiệm về "
        "toàn bộ vòng đời của công cụ đó: đăng ký sự kiện, kiểm tra đầu vào, "
        "gọi thư viện xử lý, đóng gói kết quả, dọn dẹp. Cùng tầng này còn có "
        "mô-đun luồng xử lý tự động, mô-đun so sánh tài liệu và mô-đun trạng "
        "thái phiên làm việc."
    )
    r.p(
        "Tầng thứ năm là tầng tiện ích với 43 mô-đun, cung cấp những năng lực "
        "dùng chung mà nhiều công cụ cùng cần: quản lý nguồn mô-đun xử lý, hàm "
        "lưu tệp, hàm phân tích khoảng trang, cơ chế hỏi mật khẩu và giải mã, "
        "cấu hình động cơ nhận dạng ký tự, nạp phông chữ theo ngôn ngữ. Việc "
        "tách riêng tầng này là điều kiện để bảo đảm yêu cầu PC-16 về tính "
        "khuôn mẫu."
    )
    r.p(
        "Tầng dưới cùng là tầng động cơ xử lý, gồm các thư viện JavaScript và "
        "WebAssembly đã liệt kê ở Bảng 1.1, cùng với kho tài nguyên cục bộ. "
        "Tầng này không biết gì về giao diện và cũng không biết gì về nghiệp vụ "
        "của từng công cụ; nó chỉ cung cấp các phép biến đổi trên dữ liệu nhị "
        "phân."
    )
    r.p(
        "Quan hệ phụ thuộc giữa các tầng là một chiều: tầng trên gọi xuống tầng "
        "dưới, không có lời gọi ngược. Ngoại lệ duy nhất về mặt luồng điều "
        "khiển là lệnh lưu tệp: tầng tiện ích gọi lên tầng vỏ bản địa qua cơ "
        "chế truyền thông liên tiến trình. Đây là một ngoại lệ có ý thức và "
        "được cô lập trong đúng một hàm, sẽ được phân tích chi tiết ở Chương 3."
    )

    r.h3("3.3. Kiến trúc thành phần")
    r.p(
        "Nếu kiến trúc phân tầng cho thấy hệ thống được chia theo chiều dọc như "
        "thế nào thì kiến trúc thành phần cho thấy các mô-đun cụ thể phụ thuộc "
        "lẫn nhau ra sao. Hình 2.4 trình bày sơ đồ thành phần được tái dựng "
        "bằng cách đọc các câu lệnh nhập mô-đun trong mã nguồn."
    )
    r.figure(
        "fig_2_4_component_architecture",
        "Hình 2.4. Kiến trúc thành phần và quan hệ phụ thuộc giữa các mô-đun",
    )
    r.p(
        "Nhóm điểm vào và khung giao diện gồm trang HTML công cụ, mô-đun chính "
        "và mô-đun giao diện. Trang HTML là điểm vào thực sự của mỗi công cụ: "
        "trình biên dịch được cấu hình với 131 điểm vào riêng biệt, nên khi "
        "người dùng mở một công cụ, chỉ mã của công cụ đó cùng các phụ thuộc "
        "của nó được tải. Mô-đun chính chỉ được nạp ở trang chủ để dựng thanh "
        "bên và lưới thẻ công cụ."
    )
    r.p(
        "Nhóm cấu hình và quốc tế hoá gồm ba thành phần. Tệp danh mục công cụ "
        "khai báo bảy nhóm và 127 mục, mỗi mục gồm đường dẫn, tên, biểu tượng "
        "và mô tả ngắn; định danh của mỗi công cụ được suy ra từ tên tệp HTML "
        "chứ không phải từ nhãn hiển thị, nhờ đó việc dịch giao diện không làm "
        "thay đổi định danh. Tệp phân loại kiểu nạp tệp chia các công cụ thành "
        "ba nhóm theo cách chúng nhận đầu vào: công cụ nạp một tệp PDF và cần "
        "hiển thị trang, công cụ đơn giản chỉ cần tệp, và công cụ nhận nhiều "
        "tệp. Mô-đun quốc tế hoá cùng thư mục tài nguyên ngôn ngữ chứa 21 ngôn "
        "ngữ; riêng bản tiếng Việt có 272 khoá cho giao diện chung và 890 khoá "
        "cho phần mô tả công cụ."
    )
    r.p(
        "Nhóm trạng thái và nhập liệu gồm mô-đun trạng thái phiên với năm "
        "trường, mô-đun xử lý tệp đầu vào và mô-đun quản lý danh sách công cụ "
        "bị vô hiệu hoá. Cần lưu ý rằng nhiều công cụ không dùng trạng thái "
        "dùng chung mà giữ trạng thái cục bộ riêng trong mô-đun của mình; đây "
        "là dấu vết của quá trình phát triển tăng dần và là một điểm có thể "
        "chuẩn hoá thêm trong tương lai."
    )
    r.p(
        "Tầng nghiệp vụ gồm bốn khối. Khối lớn nhất là thư mục logic với 132 "
        "mô-đun. Khối luồng xử lý tự động gồm bộ thực thi, trình soạn thảo, cơ "
        "chế lưu trữ đồ thị và 79 lớp nút; điểm quan trọng là các nút này gọi "
        "lại chính các hàm tiện ích mà các công cụ độc lập sử dụng, nhờ đó "
        "không có hiện tượng hiện thực hai lần cùng một phép biến đổi. Khối so "
        "sánh tài liệu có bộ máy riêng chạy trong Web Worker. Khối Web Worker "
        "gồm tám tệp trong thư mục công khai, xử lý những thao tác nặng như "
        "ghép tệp, quản lý tệp đính kèm, chuyển đổi JSON và sinh mục lục."
    )
    r.p(
        "Tầng tiện ích cung cấp ba nhóm năng lực then chốt được đánh dấu trong "
        "sơ đồ. Mô-đun quản lý nguồn mô-đun WebAssembly quyết định địa chỉ nạp "
        "và thực thi việc kiểm tra danh sách máy chủ tin cậy. Mô-đun trợ giúp "
        "chứa hàm lưu tệp dùng chung cho toàn hệ thống cùng thể hiện đơn nhất "
        "của qpdf. Cặp mô-đun hỏi mật khẩu và giải mã xử lý tài liệu có bảo vệ."
    )
    r.p(
        "Tầng dưới cùng của sơ đồ cho thấy bảy động cơ xử lý và kho tài nguyên "
        "cục bộ. Các mũi tên từ tầng tiện ích xuống tầng động cơ thể hiện đúng "
        "quan hệ trong mã: mô-đun trợ giúp khởi tạo qpdf, còn mô-đun quản lý "
        "nguồn cung cấp địa chỉ cho ba mô-đun được cấu hình bên ngoài là "
        "CoherentPDF, PyMuPDF và Ghostscript."
    )

    r.h3("3.4. Kiến trúc triển khai")
    r.p(
        "Kiến trúc triển khai mô tả hệ thống tồn tại ở đâu và dưới hình thức "
        "nào trong ba giai đoạn: phát triển, đóng gói và vận hành. Hình 2.5 "
        "trình bày ba giai đoạn này."
    )
    r.figure(
        "fig_2_5_deployment",
        "Hình 2.5. Kiến trúc triển khai của hệ thống qua ba giai đoạn",
    )
    r.p(
        "Trên máy phát triển, mã nguồn TypeScript được biên dịch bởi Vite ở chế "
        "độ dành riêng cho bản desktop, sinh ra thư mục kết quả chứa HTML, "
        "JavaScript, CSS và tài nguyên ngôn ngữ. Một kịch bản Node riêng sao "
        "chép toàn bộ thư mục mô-đun WebAssembly vào thư mục kết quả. Sau đó "
        "Cargo biên dịch phần Rust và nhúng thư mục kết quả vào nhị phân."
    )
    r.p(
        "Vì gói cài đặt cho macOS và Windows không thể biên dịch chéo từ Linux, "
        "dự án sử dụng ma trận tích hợp liên tục với bốn cấu hình chạy trên máy "
        "chủ tương ứng: macOS cho kiến trúc ARM64, macOS cho kiến trúc x86-64, "
        "Windows và Ubuntu. Mỗi cấu hình sinh ra gói cài đặt theo định dạng bản "
        "địa của hệ điều hành đó và tải lên làm hiện vật của quy trình."
    )
    r.p(
        "Trên máy người dùng cuối, gói cài đặt được cài đặt như một phần mềm "
        "thông thường. Khi chạy, tiến trình bản địa khởi tạo cửa sổ với kích "
        "thước mặc định 1280×860 điểm ảnh và kích thước tối thiểu 800×600, sau "
        "đó nạp giao diện vào WebView với hai tiêu đề cách ly nguồn gốc đã đặt "
        "sẵn. Tài nguyên giao diện và mô-đun xử lý được phục vụ từ bên trong "
        "nhị phân qua giao thức nội bộ của Tauri. Khi người dùng lưu kết quả, "
        "tiến trình bản địa ghi tệp ra hệ thống tệp qua hộp thoại của hệ điều "
        "hành."
    )
    r.p(
        "Khối nét đứt ở góc dưới bên phải thể hiện phần mạng: đây là thành phần "
        "duy nhất nằm ngoài máy người dùng và chỉ được chạm tới khi người dùng "
        "dùng tính năng đóng dấu thời gian hoặc tải phông chữ theo yêu cầu. "
        "Trong mọi trường hợp còn lại, đường biên của hệ thống trùng với đường "
        "biên của máy người dùng."
    )

    # ==================================================================
    r.h2("4. Thiết kế quy trình xử lý tài liệu")

    r.h3("4.1. Quy trình xử lý tổng quát")
    r.p(
        "Mặc dù có 127 công cụ với chức năng rất khác nhau, tất cả đều đi theo "
        "cùng một quy trình mười sáu bước. Việc nhận diện và chuẩn hoá quy "
        "trình chung này là quyết định thiết kế quan trọng nhất về mặt bảo trì: "
        "nó cho phép mỗi công cụ mới chỉ phải hiện thực phần khác biệt thay vì "
        "viết lại toàn bộ vòng đời. Hình 2.6 trình bày lưu đồ quy trình tổng "
        "quát."
    )
    r.figure(
        "fig_2_6_processing_pipeline",
        "Hình 2.6. Quy trình xử lý tài liệu tổng quát của hệ thống",
    )
    r.p(
        "Quy trình bắt đầu khi người dùng chọn công cụ, sau đó nạp tệp bằng một "
        "trong hai đường: hộp thoại chọn tệp hoặc kéo–thả vào vùng nhận tệp. "
        "Trong cả hai trường hợp, bước tiếp theo là lọc tệp theo kiểu MIME hoặc "
        "phần mở rộng — chẳng hạn công cụ ghép chỉ chấp nhận tệp có kiểu "
        "application/pdf hoặc có phần mở rộng .pdf — rồi đưa các tệp hợp lệ vào "
        "danh sách trạng thái."
    )
    r.p(
        "Điểm quyết định đầu tiên là kiểm tra tài liệu có mã hoá hay không. "
        "Nếu có, hệ thống gọi hàm giải mã theo lô: hàm này hiển thị hộp thoại "
        "nhập mật khẩu, ghi nhớ mật khẩu đã nhập trong phạm vi phiên để không "
        "phải hỏi lại cho các tệp cùng mật khẩu, và thử giải mã lần lượt bằng "
        "CoherentPDF rồi PyMuPDF. Cơ chế thử tuần tự này quan trọng vì hai thư "
        "viện xử lý được những biến thể mã hoá khác nhau; một tài liệu mà thư "
        "viện thứ nhất từ chối vẫn có cơ hội được thư viện thứ hai mở."
    )
    r.p(
        "Sau khi tài liệu đã sẵn sàng, hệ thống nạp tài liệu bằng hai thư viện "
        "phục vụ hai mục đích khác nhau: pdf.js để kết xuất và đếm trang phục "
        "vụ hiển thị, pdf-lib hoặc CoherentPDF để thao tác cấu trúc. Giao diện "
        "hiển thị bản xem trước, số trang và mở bảng tham số. Người dùng nhập "
        "tham số rồi bấm nút xử lý, kích hoạt chỉ báo tải."
    )
    r.p(
        "Điểm quyết định thứ hai là kiểm tra công cụ có cần mô-đun "
        "WebAssembly bên ngoài hay không. Với các công cụ dùng CoherentPDF, "
        "PyMuPDF hoặc Ghostscript, hệ thống gọi hàm kiểm tra tính khả dụng "
        "trước khi bắt đầu xử lý. Nếu mô-đun chưa được cấu hình, một hộp thoại "
        "chuyên biệt liệt kê những tính năng phụ thuộc mô-đun đó và dẫn người "
        "dùng tới trang cấu hình, thay vì để thao tác thất bại với một thông "
        "điệp lỗi khó hiểu."
    )
    r.p(
        "Bước thực thi diễn ra trên luồng chính hoặc trong Web Worker tuỳ theo "
        "khối lượng tính toán. Nếu thành công, kết quả được đóng gói thành đối "
        "tượng nhị phân với kiểu MIME phù hợp, rồi chuyển cho hàm lưu tệp dùng "
        "chung. Hàm này phát hiện môi trường Tauri và gọi lệnh bản địa để hiển "
        "thị hộp thoại lưu. Sau khi tệp được ghi, hệ thống hiển thị thông báo "
        "thành công và đặt lại trạng thái, giải phóng bộ nhớ."
    )
    r.p(
        "Nhánh lỗi được thiết kế để luôn quay về trạng thái sử dụng được: hộp "
        "thoại thông báo lỗi được hiển thị, chi tiết kỹ thuật được ghi vào nhật "
        "ký của công cụ phát triển, hệ tệp ảo của mô-đun WebAssembly được dọn "
        "sạch, Web Worker được kết thúc nếu đang chạy, và người dùng có thể thử "
        "lại ngay mà không cần khởi động lại ứng dụng."
    )
    r.p(
        "Một điểm cần nhấn mạnh về quy trình này là toàn bộ dữ liệu trung gian "
        "chỉ tồn tại trong bộ nhớ tiến trình. Không có bước nào ghi tệp tạm ra "
        "đĩa. Lần duy nhất hệ thống chạm tới hệ thống tệp theo hướng ghi là "
        "bước áp chót, khi người dùng đã chọn vị trí lưu."
    )

    r.h3("4.2. Cơ chế điều phối động cơ xử lý")
    r.p(
        "Như đã phân tích ở Chương 1, không có thư viện đơn lẻ nào phủ hết nhu "
        "cầu, nên hệ thống phải phân bổ thao tác cho nhiều động cơ khác nhau. "
        "Việc phân bổ này không được thực hiện bằng một bộ định tuyến động ở "
        "thời gian chạy mà được cố định trong mã của từng mô-đun nghiệp vụ: "
        "mỗi công cụ biết trước nó dùng thư viện nào. Cách làm này đơn giản và "
        "dễ dự đoán, đổi lại việc thay thế một thư viện đòi hỏi sửa mã. Hình "
        "2.7 tổng hợp bản đồ phân bổ thao tác cho từng động cơ."
    )
    r.figure(
        "fig_2_7_engine_routing",
        "Hình 2.7. Bản đồ phân bổ thao tác cho các động cơ xử lý",
    )
    r.p(
        "pdf-lib đảm nhiệm phần lớn thao tác thuộc mức can thiệp thứ nhất và "
        "thứ hai đã định nghĩa ở Chương 1: xoay, xoá, trích trang, đóng dấu "
        "chìm, đánh số trang, đầu và chân trang, gộp nhiều trang lên một tờ, "
        "làm phẳng, chuẩn hoá khổ giấy. Thư viện này thuần JavaScript nên nhẹ "
        "và không cần khởi tạo, phù hợp với các thao tác thường dùng. Kèm theo "
        "fontkit, nó cũng đảm nhiệm việc nhúng phông chữ và vẽ lớp văn bản cho "
        "kết quả nhận dạng ký tự."
    )
    r.p(
        "pdf.js chịu trách nhiệm mọi việc liên quan tới kết xuất: sinh ảnh thu "
        "nhỏ, hiển thị bản xem trước, chuyển trang thành ảnh, tạo hiệu ứng bản "
        "quét. Thư viện này cũng là nơi phát hiện tài liệu có mật khẩu, thông "
        "qua ngoại lệ chuyên biệt mà nó ném ra khi gặp tệp mã hoá."
    )
    r.p(
        "qpdf được dùng cho toàn bộ nhóm thao tác mật mã và cấu trúc mức thấp: "
        "mã hoá AES-256, giải mã, đặt quyền sử dụng, tuyến tính hoá và sửa lỗi "
        "tệp. Lý do chọn qpdf cho nhóm này là thư viện có hiện thực đầy đủ và "
        "được kiểm chứng của các cơ chế mã hoá trong đặc tả PDF."
    )
    r.p(
        "CoherentPDF phụ trách những thao tác cấu trúc mà pdf-lib xử lý chưa "
        "tốt: ghép tệp có giữ nhãn trang, tách theo bookmark, sinh mục lục, "
        "chuyển đổi hai chiều giữa PDF và JSON, quản lý tệp đính kèm. Việc chọn "
        "CoherentPDF làm động cơ ghép chính, thay vì dùng pdf-lib vốn cũng ghép "
        "được, xuất phát từ yêu cầu bảo toàn bookmark và nhãn trang của tài "
        "liệu nguồn."
    )
    r.p(
        "PyMuPDF chạy trên nền Pyodide đảm nhiệm nhóm thao tác nặng nhất về mặt "
        "phân tích nội dung: nén ảnh nhúng, chuyển PDF sang văn bản, Markdown, "
        "SVG và DOCX, trích ảnh và bảng, chuyển sách điện tử sang PDF, khử "
        "nghiêng trang quét. Việc gói này mang theo cả numpy và OpenCV giải "
        "thích vì sao nó là mô-đun nặng nhất và cũng là mô-đun có khả năng xử "
        "lý ảnh mạnh nhất trong hệ thống."
    )
    r.p(
        "Nhóm động cơ thứ hai gồm Ghostscript cho chuyển đổi PDF/A và chuyển "
        "phông thành đường nét, Tesseract.js cho nhận dạng ký tự, wasm-vips "
        "cùng các thư viện ảnh chuyên biệt cho việc giải mã định dạng ảnh ngoài "
        "luồng phổ thông, LibreOffice-WASM cho chuyển đổi tài liệu văn phòng, "
        "và cặp zgapdfsigner cùng node-forge cho ký số."
    )
    r.p(
        "Phía dưới sơ đồ là cổng kiểm tra chung. Ba mô-đun được cấu hình bên "
        "ngoài — CoherentPDF, PyMuPDF và Ghostscript — đều đi qua hàm kiểm tra "
        "tính khả dụng trước khi được sử dụng. Thiết kế này bảo đảm rằng khi "
        "một mô-đun thiếu, người dùng nhận được thông điệp có ý nghĩa kèm hướng "
        "dẫn thay vì một lỗi kỹ thuật."
    )

    r.h3("4.3. Biểu đồ tuần tự thao tác ghép tài liệu")
    r.p(
        "Thao tác ghép được chọn làm ví dụ chi tiết vì nó đi qua gần như toàn "
        "bộ các cơ chế đặc trưng của hệ thống: nạp nhiều tệp, xử lý tài liệu có "
        "mật khẩu, kết xuất bản xem trước, sắp xếp bằng kéo–thả, chuyển tính "
        "toán vào Web Worker, gọi mô-đun WebAssembly và lưu tệp qua tầng bản "
        "địa. Hình 2.8 trình bày biểu đồ tuần tự đầy đủ của thao tác này."
    )
    r.figure(
        "fig_2_8_sequence_merge",
        "Hình 2.8. Biểu đồ tuần tự quá trình ghép nhiều tài liệu PDF",
    )
    r.p(
        "Ba thông điệp đầu tiên xử lý phần đầu vào. Sau khi người dùng chọn "
        "hoặc kéo–thả các tệp, mô-đun nghiệp vụ gọi hàm giải mã theo lô. Hàm "
        "này duyệt danh sách tệp, phát hiện những tệp cần mật khẩu và hiển thị "
        "một hộp thoại duy nhất cho toàn bộ danh sách thay vì hỏi từng tệp một, "
        "kèm chỉ báo tiến độ. Danh sách trả về là danh sách tệp đã ở dạng có "
        "thể xử lý."
    )
    r.p(
        "Thông điệp thứ tư là một lời gọi nội bộ: mô-đun nghiệp vụ nạp từng tệp "
        "bằng pdf.js để lấy số trang và giữ lại bộ đệm nhị phân của tệp gốc. "
        "Cần lưu ý chi tiết kỹ thuật ở đây — bộ đệm được sao chép trước khi "
        "truyền cho pdf.js, bởi thư viện này chiếm quyền sở hữu bộ đệm mà nó "
        "nhận; nếu không sao chép, bộ đệm gốc sẽ trở nên không dùng được ở bước "
        "sau."
    )
    r.p(
        "Thông điệp thứ năm và thứ sáu thể hiện phần tương tác. Công cụ ghép có "
        "hai chế độ: chế độ tệp cho phép sắp xếp thứ tự các tệp và nhập khoảng "
        "trang cho từng tệp; chế độ trang kết xuất ảnh thu nhỏ của mọi trang "
        "trong mọi tệp và cho phép sắp xếp ở mức từng trang. Cả hai chế độ đều "
        "dùng thư viện kéo–thả. Việc kết xuất ảnh thu nhỏ được thực hiện theo "
        "lô tám trang một lần với cơ chế nạp lười, nhằm tránh chiếm dụng luồng "
        "chính quá lâu khi tài liệu có nhiều trang."
    )
    r.p(
        "Thông điệp thứ bảy là bước chuẩn bị công việc. Ở chế độ tệp, mỗi tệp "
        "sinh ra một công việc với kiểu khoảng là toàn bộ hoặc theo chuỗi "
        "khoảng do người dùng nhập. Ở chế độ trang, hệ thống thực hiện một bước "
        "tối ưu đáng chú ý: duyệt danh sách trang đã sắp xếp và gộp các trang "
        "liên tiếp cùng thuộc một tệp thành một công việc dạng khoảng, thay vì "
        "sinh ra một công việc cho mỗi trang. Với tài liệu nhiều trang, bước "
        "gộp này giảm đáng kể số lệnh mà thư viện xử lý phải thực hiện."
    )
    r.p(
        "Thông điệp thứ tám chuyển toàn bộ công việc sang Web Worker. Điểm quan "
        "trọng là danh sách bộ đệm nhị phân được truyền theo cơ chế chuyển "
        "quyền sở hữu: dữ liệu không bị sao chép mà được chuyển hẳn sang luồng "
        "worker. Với các tệp cỡ hàng chục megabyte, cơ chế này là khác biệt "
        "giữa việc dùng một lần bộ nhớ và dùng gấp đôi."
    )
    r.p(
        "Bên trong worker, thông điệp thứ chín và thứ mười thực hiện phần xử lý "
        "thật. Worker nạp CoherentPDF bằng lệnh nhập kịch bản đồng bộ, dựng "
        "từng tài liệu từ bộ nhớ, chuyển mỗi công việc thành một khoảng trang "
        "tương ứng, rồi gọi hàm ghép. Với chuỗi khoảng do người dùng nhập, "
        "worker gọi hàm kiểm tra tính hợp lệ trước khi phân tích; nếu chuỗi "
        "không hợp lệ, nó lặng lẽ dùng toàn bộ trang thay vì báo lỗi — một "
        "quyết định thiên về khả năng hoàn thành công việc."
    )
    r.p(
        "Sau khi có kết quả, worker giải phóng tường minh mọi tài liệu "
        "CoherentPDF đã nạp bằng hàm huỷ của thư viện. Đây là bước bắt buộc đã "
        "phân tích ở mục 1.4: bộ nhớ WebAssembly không được thu gom tự động. "
        "Kết quả được gửi ngược về luồng chính, cũng theo cơ chế chuyển quyền "
        "sở hữu."
    )
    r.p(
        "Ba thông điệp cuối xử lý phần đầu ra. Luồng chính đóng gói kết quả "
        "thành đối tượng nhị phân, gọi hàm lưu tệp dùng chung; hàm này phát "
        "hiện môi trường Tauri và chuyển sang lệnh bản địa, nhận về kết quả cho "
        "biết người dùng đã lưu hay đã huỷ; cuối cùng hộp thoại thành công được "
        "hiển thị kèm hàm gọi lại để đặt lại trạng thái."
    )

    r.h3("4.4. Biểu đồ tuần tự thao tác mã hoá tài liệu")
    r.p(
        "Thao tác mã hoá được chọn làm ví dụ thứ hai vì nó minh hoạ khuôn mẫu "
        "làm việc với mô-đun WebAssembly dạng chương trình dòng lệnh — khuôn "
        "mẫu rất khác so với khuôn mẫu thư viện của CoherentPDF. Hình 2.9 "
        "trình bày biểu đồ tuần tự của thao tác này."
    )
    r.figure(
        "fig_2_9_sequence_encrypt",
        "Hình 2.9. Biểu đồ tuần tự quá trình mã hoá tài liệu PDF",
    )
    r.p(
        "Sau khi người dùng chọn tệp và nhập mật khẩu, mô-đun nghiệp vụ kiểm "
        "tra điều kiện bắt buộc: mật khẩu người dùng không được để trống. Nếu "
        "người dùng chỉ nhập mật khẩu người dùng mà không nhập mật khẩu chủ sở "
        "hữu, hệ thống dùng chính mật khẩu đó cho cả hai vai trò nhưng không "
        "áp dụng hạn chế nào, đồng thời thông báo rõ điều này trong hộp thoại "
        "thành công. Đây là hành vi đúng theo đặc tả: khi hai mật khẩu trùng "
        "nhau, việc đặt hạn chế không có ý nghĩa bảo vệ vì người mở tài liệu "
        "cũng chính là người có quyền chủ sở hữu."
    )
    r.p(
        "Khi người dùng nhập mật khẩu chủ sở hữu riêng, hệ thống bổ sung tám "
        "cờ hạn chế vào tham số dòng lệnh: cấm chỉnh sửa, cấm trích xuất nội "
        "dung, cấm in, cấm truy cập hỗ trợ tiếp cận, cấm chú thích, cấm lắp "
        "ghép trang, cấm điền biểu mẫu và cấm các thay đổi khác."
    )
    r.p(
        "Thông điệp thứ tư tới thứ sáu thể hiện cơ chế khởi tạo một lần. Hàm "
        "khởi tạo qpdf giữ một thể hiện đơn nhất ở phạm vi mô-đun; lần gọi đầu "
        "tiên tạo mô-đun WebAssembly và trỏ nó tới tệp nhị phân trong thư mục "
        "công khai, các lần gọi sau trả về ngay thể hiện đã có. Trong quá trình "
        "khởi tạo, chỉ báo tải được hiển thị với thông điệp riêng, và nếu khởi "
        "tạo thất bại, người dùng nhận được hộp thoại lỗi đề nghị tải lại thay "
        "vì một lỗi không rõ nguyên nhân."
    )
    r.p(
        "Từ thông điệp thứ bảy trở đi là khuôn mẫu hệ tệp ảo đặc trưng của "
        "Emscripten: ghi dữ liệu vào một đường dẫn ảo, gọi hàm chính với danh "
        "sách tham số dòng lệnh, đọc kết quả từ một đường dẫn ảo khác. Trước "
        "khi đóng gói kết quả, hệ thống kiểm tra tệp ra có rỗng hay không, bởi "
        "qpdf có thể kết thúc mà không sinh ra dữ liệu trong một số trường hợp "
        "lỗi không ném ngoại lệ."
    )
    r.p(
        "Thông điệp thứ mười hai là bước quan trọng nhất về mặt quản lý tài "
        "nguyên và cũng là điểm dễ bỏ sót nhất: xoá cả tệp vào và tệp ra khỏi "
        "hệ tệp ảo. Bước này nằm trong khối bảo đảm thực thi, nên nó chạy cả "
        "khi qpdf ném ngoại lệ. Nếu thiếu bước này, mỗi lần mã hoá sẽ để lại "
        "hai bản sao tài liệu trong bộ nhớ của mô-đun, và sau vài chục thao tác "
        "mô-đun sẽ cạn bộ nhớ."
    )

    r.h3("4.5. Thiết kế luồng xử lý tự động")
    r.p(
        "Tính năng luồng xử lý tự động cho phép người dùng dựng một đồ thị các "
        "nút xử lý và thực thi toàn bộ chuỗi trong một lần, thay vì lặp lại "
        "thủ công từng thao tác trên từng tệp. Đây là tính năng phức tạp nhất "
        "về mặt thiết kế trong hệ thống, và cũng là nơi thể hiện rõ nhất giá "
        "trị của việc tách riêng tầng tiện ích. Hình 2.10 trình bày mô hình "
        "thực thi của tính năng này."
    )
    r.figure(
        "fig_2_10_workflow_engine",
        "Hình 2.10. Mô hình thực thi của luồng xử lý tự động",
    )
    r.p(
        "Phần soạn thảo dựa trên thư viện đồ thị Rete cùng các trình cắm cho "
        "vùng làm việc, kết nối và kết xuất. Có 79 lớp nút được đăng ký trong "
        "một sổ đăng ký tập trung, chia thành sáu nhóm: nút đầu vào, nhóm chỉnh "
        "sửa và chú thích, nhóm tổ chức và quản lý, nhóm tối ưu và sửa chữa, "
        "nhóm bảo mật, và nút đầu ra. Đồ thị người dùng dựng được có thể lưu và "
        "nạp lại dưới dạng JSON kèm số hiệu phiên bản định dạng."
    )
    r.p(
        "Bộ thực thi hoạt động theo bốn bước. Bước thứ nhất xác định các nút "
        "cuối, tức những nút không có kết nối đầu ra; nếu không tìm được nút "
        "nào, hệ thống báo lỗi ngay vì đồ thị không có điểm kết thúc. Bước thứ "
        "hai duyệt ngược theo chiều rộng từ mỗi nút cuối để thu thập tập nút "
        "thực sự tham gia vào luồng — nhờ đó những nút người dùng đã đặt lên "
        "vùng làm việc nhưng chưa nối vào đâu sẽ không được thực thi."
    )
    r.p(
        "Bước thứ ba sắp xếp tô-pô tập nút theo thuật toán Kahn. Nếu số nút sắp "
        "xếp được nhỏ hơn số nút trong tập, tức tồn tại chu trình, hệ thống ném "
        "lỗi chuyên biệt về phụ thuộc vòng. Bước thứ tư thực thi tuần tự theo "
        "thứ tự đã sắp xếp, mỗi nút cập nhật trạng thái hiển thị của mình qua "
        "bốn giá trị: chờ, đang chạy, hoàn thành, lỗi."
    )
    r.p(
        "Một ràng buộc nghiệp vụ đáng chú ý được kiểm tra trước khi thực thi: "
        "nút mã hoá chỉ được phép nối tới nút thuộc nhóm đầu ra. Lý do là sau "
        "khi tài liệu đã được mã hoá, mọi phép biến đổi tiếp theo sẽ thất bại "
        "hoặc cho kết quả sai vì các thư viện xử lý không mở được tài liệu. "
        "Thay vì để người dùng phát hiện điều này khi luồng đã chạy được nửa "
        "chừng, hệ thống kiểm tra ngay từ đầu và báo lỗi kèm tên nút vi phạm."
    )
    r.p(
        "Về xử lý lỗi, khi một nút thất bại, bộ thực thi đánh dấu nút đó là lỗi "
        "và đưa mọi nút đang ở trạng thái đang chạy về trạng thái chờ, sau đó "
        "ném ngoại lệ có kèm tên nút. Cách làm này giúp người dùng nhìn ngay "
        "được vị trí hỏng trên đồ thị thay vì phải đối chiếu thông điệp lỗi với "
        "cấu trúc luồng."
    )
    r.p(
        "Điểm thiết kế quan trọng nhất của tính năng này là các nút không hiện "
        "thực lại phép biến đổi mà gọi lại chính các hàm tiện ích được các công "
        "cụ độc lập sử dụng. Chẳng hạn nút ghép gọi cùng một hàm ghép trên nền "
        "CoherentPDF mà trang công cụ ghép sử dụng. Nhờ đó, một sửa lỗi trong "
        "hàm tiện ích có hiệu lực đồng thời ở cả hai nơi, và không tồn tại nguy "
        "cơ hai hiện thực của cùng một phép biến đổi phân kỳ theo thời gian."
    )

    # ==================================================================
    r.h2("5. Thiết kế dữ liệu")

    r.h3("5.1. Mô hình dữ liệu trong bộ nhớ")
    r.p(
        "Hệ thống không có cơ sở dữ liệu, không có lược đồ quan hệ và không có "
        "thực thể bền vững nào ngoài một lượng rất nhỏ tuỳ chọn giao diện. Vì "
        "vậy phần thiết kế dữ liệu ở đây không mô tả bảng và khoá ngoại mà mô "
        "tả các cấu trúc dữ liệu tồn tại trong bộ nhớ tiến trình cùng vòng đời "
        "của chúng. Hình 2.11 trình bày mô hình này."
    )
    r.figure(
        "fig_2_11_data_model",
        "Hình 2.11. Mô hình dữ liệu trong bộ nhớ và dữ liệu cấu hình bền vững",
    )
    r.p(
        "Ở tầng cao nhất là ba kiểu dữ liệu được định nghĩa cho luồng xử lý tự "
        "động. Kiểu tài liệu PDF chứa bốn trường: định danh kiểu, đối tượng tài "
        "liệu của pdf-lib, mảng byte và tên tệp. Việc mang theo cả đối tượng "
        "tài liệu lẫn mảng byte là có chủ ý: một số nút thao tác trên đối tượng "
        "tài liệu, một số nút cần chuỗi byte thô để đưa vào mô-đun WebAssembly. "
        "Kiểu ảnh chứa đối tượng nhị phân và tên tệp. Kiểu nhiều tài liệu chứa "
        "một mảng các tài liệu PDF, phục vụ các nút xử lý theo lô."
    )
    r.p(
        "Một chi tiết quan trọng về ngữ nghĩa: khi dữ liệu được truyền giữa các "
        "nút, mảng byte được sao chép chứ không dùng chung tham chiếu. Điều này "
        "bảo đảm một nút không vô tình sửa dữ liệu mà nút khác đang dùng, đổi "
        "lại chi phí bộ nhớ cao hơn. Với đồ thị dài xử lý tệp lớn, đây là một "
        "điểm cần cân nhắc khi tối ưu về sau."
    )
    r.p(
        "Ở tầng giữa bên trái là trạng thái phiên dùng chung với năm trường: "
        "công cụ đang hoạt động, danh sách tệp đã nạp, tài liệu PDF hiện tại, "
        "danh sách trang và địa chỉ tài liệu đang xem. Trạng thái này được đặt "
        "lại hoàn toàn khi chuyển công cụ hoặc khi hoàn tất một thao tác. Cần "
        "lưu ý rằng không phải mọi công cụ đều dùng trạng thái này; nhiều mô-đun "
        "giữ trạng thái riêng phù hợp với nhu cầu của mình."
    )
    r.p(
        "Ở tầng giữa bên phải là dữ liệu bền vững duy nhất của hệ thống, lưu "
        "trong bộ nhớ cục bộ của WebView. Có ba nhóm: mã ngôn ngữ giao diện, "
        "cấu hình địa chỉ mô-đun xử lý, và các phím tắt do người dùng đặt lại. "
        "Điều quan trọng cần nhấn mạnh là danh sách này không chứa nội dung tài "
        "liệu, không chứa tên tệp đã xử lý, không chứa mật khẩu và không chứa "
        "bất kỳ dấu vết nào về công việc người dùng đã làm."
    )
    r.p(
        "Ở tầng dưới cùng là vùng dữ liệu tạm — phần chiếm nhiều bộ nhớ nhất và "
        "cần được quản lý cẩn thận nhất. Vùng này gồm bộ đệm nhị phân của tệp "
        "gốc, canvas kết xuất trang, hệ tệp ảo của qpdf và Ghostscript, hệ tệp "
        "ảo của Pyodide, và đối tượng nhị phân kết quả trước khi lưu. Toàn bộ "
        "vùng này bị huỷ khi đóng cửa sổ ứng dụng, và các cơ chế giải phóng chủ "
        "động trong quá trình chạy sẽ được trình bày ở mục 5.3 cũng như ở "
        "Chương 3."
    )

    r.h3("5.2. Dữ liệu cấu hình và cơ chế tuỳ biến khi triển khai")
    r.p(
        "Ngoài dữ liệu người dùng, hệ thống có một tập dữ liệu cấu hình phục vụ "
        "việc tuỳ biến khi triển khai. Tập này gồm ba mức với thời điểm áp dụng "
        "khác nhau, được tổng hợp trong Bảng 2.3."
    )
    r.table(
        "Bảng 2.3. Ba mức cấu hình của hệ thống",
        ["Mức", "Cơ chế", "Thời điểm áp dụng", "Nội dung cấu hình được"],
        [
            ["Biên dịch",
             "Biến môi trường tiền tố VITE_ và tệp .env theo chế độ dựng",
             "Khi chạy lệnh biên dịch",
             "Địa chỉ các mô-đun WebAssembly, địa chỉ tài nguyên nhận dạng ký "
             "tự, ngôn ngữ mặc định, tên và biểu trưng thương hiệu, dòng chân "
             "trang"],
            ["Biên dịch",
             "Biến DISABLE_TOOLS được nhúng thành hằng số khi dựng",
             "Khi chạy lệnh biên dịch",
             "Danh sách định danh công cụ bị loại khỏi danh mục"],
            ["Chạy",
             "Tệp config.json đặt cạnh tài nguyên ứng dụng",
             "Khi ứng dụng khởi động",
             "Danh sách công cụ bị vô hiệu hoá bổ sung và danh sách nhóm chức "
             "năng bị ẩn trong trình soạn thảo"],
            ["Chạy",
             "Bộ nhớ cục bộ của WebView",
             "Khi người dùng thay đổi trong giao diện",
             "Ngôn ngữ giao diện, địa chỉ mô-đun xử lý do người dùng đặt, phím "
             "tắt tuỳ chỉnh"],
        ],
        widths=[1.6, 4, 3, 7],
        font_size=11,
    )
    r.p(
        "Cơ chế vô hiệu hoá công cụ đáng được nói thêm vì nó phục vụ một nhu "
        "cầu triển khai thực tế. Một tổ chức có thể muốn ẩn những công cụ không "
        "phù hợp với quy định nội bộ, chẳng hạn ẩn công cụ gỡ hạn chế hoặc gỡ "
        "mật khẩu. Hệ thống hỗ trợ điều này ở cả hai mức: khi biên dịch để tạo "
        "bản dựng riêng, và khi chạy để điều chỉnh mà không cần dựng lại. Khi "
        "một công cụ bị vô hiệu hoá, nó biến mất khỏi danh mục và trang tương "
        "ứng cũng hiển thị thông báo không khả dụng nếu người dùng truy cập "
        "trực tiếp."
    )
    r.p(
        "Việc tải tệp cấu hình khi chạy được thực hiện thận trọng: hệ thống "
        "kiểm tra mã trạng thái phản hồi, kiểm tra kiểu nội dung phải là JSON, "
        "và bọc toàn bộ trong khối bắt lỗi. Nếu tệp không tồn tại hoặc không "
        "hợp lệ, ứng dụng tiếp tục chạy với cấu hình mặc định thay vì dừng. Đây "
        "là lựa chọn đúng cho một ứng dụng desktop, nơi tệp cấu hình là tuỳ "
        "chọn chứ không bắt buộc."
    )

    r.h3("5.3. Vòng đời dữ liệu và nguyên tắc không ghi tệp tạm")
    r.p(
        "Nguyên tắc “không ghi tệp tạm ra đĩa” đã nêu ở yêu cầu PC-03 có ý "
        "nghĩa quan trọng hơn vẻ ngoài của nó. Trong mô hình xử lý phía máy "
        "chủ, tệp tạm là nơi dữ liệu tồn tại lâu nhất và cũng là nơi dễ rò rỉ "
        "nhất: chúng có thể bị sao lưu, bị đọc bởi tiến trình khác, hoặc còn "
        "lại sau khi ứng dụng bị kết thúc bất thường. Loại bỏ hoàn toàn tệp tạm "
        "vì vậy là một biện pháp bảo vệ có giá trị thực chất."
    )
    r.p(
        "Để thực hiện nguyên tắc này, hệ thống dựa vào ba cơ chế. Thứ nhất, các "
        "thư viện JavaScript thuần như pdf-lib và pdf.js vốn làm việc trực tiếp "
        "trên mảng byte trong bộ nhớ, không có khái niệm tệp. Thứ hai, các "
        "mô-đun WebAssembly được biên dịch bằng Emscripten sử dụng hệ tệp ảo "
        "nằm hoàn toàn trong bộ nhớ, nên khi mã thư viện gọi hàm ghi tệp, dữ "
        "liệu vẫn không chạm tới đĩa. Thứ ba, kết quả cuối cùng được giữ dưới "
        "dạng đối tượng nhị phân trong bộ nhớ cho tới khi người dùng chọn vị "
        "trí lưu."
    )
    r.p(
        "Đổi lại, hệ thống phải chịu trách nhiệm giải phóng bộ nhớ một cách "
        "tường minh ở nhiều điểm. Vòng đời điển hình của một thao tác gồm năm "
        "giai đoạn giải phóng: xoá tệp khỏi hệ tệp ảo sau khi đọc kết quả, đặt "
        "kích thước canvas về không sau khi kết xuất xong, gọi hàm huỷ tài liệu "
        "của thư viện WebAssembly, kết thúc Web Worker sau khi nhận kết quả, và "
        "thu hồi địa chỉ đối tượng tạm sau khi tải xuống. Chi tiết từng cơ chế "
        "sẽ được trình bày ở mục 4.1 của Chương 3."
    )
    r.p(
        "Cần nêu một giới hạn của thiết kế này để tránh hiểu nhầm. Việc không "
        "ghi tệp tạm bảo đảm dữ liệu không tồn tại trên đĩa dưới dạng tệp, "
        "nhưng không loại trừ khả năng hệ điều hành hoán đổi vùng nhớ của tiến "
        "trình ra bộ nhớ ảo trên đĩa khi bộ nhớ vật lý cạn kiệt. Đây là hành vi "
        "nằm ngoài tầm kiểm soát của ứng dụng ở tầng người dùng; trong các môi "
        "trường có yêu cầu bảo mật đặc biệt cao, biện pháp bổ sung phải đến từ "
        "cấu hình hệ điều hành, chẳng hạn mã hoá toàn bộ ổ đĩa hoặc vô hiệu hoá "
        "phân vùng hoán đổi."
    )

    # ==================================================================
    r.h2("6. Thiết kế giao diện hệ thống")

    r.h3("6.1. Cấu trúc điều hướng")
    r.p(
        "Với 127 mục công cụ, thách thức lớn nhất về giao diện không phải là "
        "trình bày từng công cụ mà là giúp người dùng tìm được công cụ cần "
        "dùng. Thiết kế điều hướng của hệ thống giải quyết vấn đề này bằng mô "
        "hình không gian làm việc có thanh bên, kết hợp ba đường tiếp cận song "
        "song. Hình 2.12 trình bày cấu trúc điều hướng tổng thể."
    )
    r.figure(
        "fig_2_12_navigation",
        "Hình 2.12. Cấu trúc điều hướng của giao diện người dùng",
    )
    r.p(
        "Đường tiếp cận thứ nhất là duyệt theo nhóm. Thanh bên bên trái liệt kê "
        "bảy nhóm công cụ kèm số lượng công cụ trong mỗi nhóm, cộng thêm một "
        "mục tổng hợp tất cả công cụ đã khử trùng lặp. Khi người dùng chọn một "
        "nhóm, vùng nội dung bên phải hiển thị lưới thẻ công cụ của nhóm đó "
        "kèm tiêu đề và mô tả nhóm. Nhóm công cụ phổ biến được chọn mặc định "
        "khi mở ứng dụng."
    )
    r.p(
        "Đường tiếp cận thứ hai là tìm kiếm. Ô tìm kiếm lọc trên toàn bộ tập "
        "công cụ, không giới hạn trong nhóm đang xem, và tìm cả trên tên lẫn "
        "mô tả ngắn. Việc chọn một nhóm ở thanh bên sẽ xoá nội dung ô tìm kiếm "
        "để hai cơ chế không xung đột với nhau."
    )
    r.p(
        "Đường tiếp cận thứ ba là các trang nhóm chủ đề. Ngoài trang chủ, hệ "
        "thống có bốn trang tập hợp theo chủ đề — chuyển đổi, soạn thảo, bảo "
        "mật, ghép và tách — cùng trang liệt kê toàn bộ công cụ. Những trang "
        "này chủ yếu phục vụ bản web nhưng vẫn hiện diện trong bản desktop và "
        "cung cấp thêm một lối vào cho người dùng đã quen với cách phân loại "
        "theo chủ đề."
    )
    r.p(
        "Từ thẻ công cụ, người dùng chuyển sang trang công cụ độc lập. Mỗi "
        "trang có cùng năm khu vực theo thứ tự cố định: khu vực nạp tệp, bảng "
        "tham số, khu vực xem trước và sắp xếp, nút xử lý kèm chỉ báo tiến "
        "trình, và cuối cùng là hộp thoại lưu của hệ điều hành. Tính nhất quán "
        "này là yêu cầu PC-13 và có giá trị thực tế lớn: người dùng học một lần "
        "và áp dụng cho mọi công cụ."
    )
    r.p(
        "Bốn loại hộp thoại phủ lên trang công cụ khi cần: hộp thoại thông báo "
        "dùng chung cho cả thành công và lỗi, hộp thoại nhập mật khẩu ở hai "
        "biến thể đơn lẻ và theo lô, hộp thoại yêu cầu cấu hình mô-đun, và hộp "
        "thoại cài đặt kèm phím tắt. Việc gom mọi thông báo vào một cơ chế duy "
        "nhất giúp hành vi nhất quán và giảm đáng kể lượng mã trùng lặp."
    )

    r.h3("6.2. Khuôn mẫu giao diện công cụ và nguyên tắc phản hồi")
    r.p(
        "Mỗi trang công cụ được xây dựng theo một khuôn mẫu HTML chung, trong "
        "đó các thành phần dùng chung như thanh điều hướng, chân trang, hộp "
        "thoại thông báo và hộp thoại cài đặt được chèn vào bằng cơ chế mảnh "
        "giao diện ở thời điểm biên dịch. Nhờ vậy, một thay đổi ở thanh điều "
        "hướng có hiệu lực đồng thời trên toàn bộ 131 trang mà không cần sửa "
        "từng tệp."
    )
    r.p(
        "Các định danh phần tử cũng được chuẩn hoá: vùng nhận tệp, ô nhập tệp, "
        "vùng hiển thị tệp đã chọn, bảng tham số, nút xử lý, hộp thoại tải và "
        "nút quay lại danh mục đều dùng chung một bộ định danh trên mọi trang. "
        "Sự chuẩn hoá này cho phép mô-đun nghiệp vụ của mọi công cụ dùng chung "
        "một cách truy xuất phần tử, và là điều kiện để bộ kiểm thử tự động có "
        "thể mô phỏng tương tác một cách nhất quán."
    )
    r.p(
        "Về nguyên tắc phản hồi, hệ thống tuân thủ ba quy tắc. Thứ nhất, mọi "
        "thao tác kéo dài phải hiển thị chỉ báo tải với văn bản mô tả bước đang "
        "thực hiện, không chỉ một vòng quay chung chung; chẳng hạn thao tác mã "
        "hoá lần lượt hiển thị “đang khởi tạo mã hoá”, “đang đọc tệp PDF”, "
        "“đang mã hoá bằng AES-256” và “đang chuẩn bị tải xuống”. Thứ hai, mọi "
        "kết thúc — thành công hay lỗi — đều phải đóng chỉ báo tải và hiển thị "
        "một hộp thoại rõ ràng. Thứ ba, hộp thoại thành công có thể mang theo "
        "một hàm gọi lại để đặt lại trạng thái, nhờ đó người dùng bấm xác nhận "
        "là giao diện trở về trạng thái sẵn sàng cho công việc tiếp theo."
    )
    r.p(
        "Một chi tiết kỹ thuật nhỏ nhưng quan trọng trong hiện thực hộp thoại "
        "thông báo: trước mỗi lần hiển thị, nút xác nhận được nhân bản và thay "
        "thế phần tử cũ. Kỹ thuật này loại bỏ toàn bộ trình xử lý sự kiện đã "
        "gắn từ những lần hiển thị trước, tránh tình trạng một lần bấm kích "
        "hoạt nhiều hàm gọi lại tích luỹ qua nhiều thao tác."
    )

    r.h3("6.3. Thiết kế đa ngữ")
    r.p(
        "Hệ thống hỗ trợ 21 ngôn ngữ giao diện, trong đó tiếng Việt là ngôn ngữ "
        "mặc định ở lần chạy đầu tiên. Thiết kế đa ngữ dựa trên thư viện i18next "
        "với hai không gian tên: một cho giao diện chung và một cho phần mô tả "
        "công cụ. Bản tiếng Việt có 272 khoá trong không gian tên chung và 890 "
        "khoá trong không gian tên công cụ."
    )
    r.p(
        "Cơ chế xác định ngôn ngữ áp dụng thứ tự ưu tiên năm mức: tiền tố ngôn "
        "ngữ trong đường dẫn, giá trị đã lưu trong bộ nhớ cục bộ, danh sách "
        "ngôn ngữ ưa thích của trình duyệt, ngôn ngữ mặc định đặt khi biên "
        "dịch, và cuối cùng là tiếng Anh. Riêng với bản desktop, mô-đun khởi "
        "tạo ghi sẵn mã tiếng Việt vào bộ nhớ cục bộ nếu chưa có giá trị nào, "
        "nên mức thứ hai luôn khớp ở lần chạy đầu."
    )
    r.p(
        "Nguyên tắc thiết kế quan trọng nhất của phần đa ngữ là tách biệt hoàn "
        "toàn giữa định danh và nhãn hiển thị. Danh mục công cụ dùng tên nội bộ "
        "cố định bằng tiếng Anh làm khoá, còn nhãn hiển thị được tra cứu qua "
        "bảng ánh xạ khoá dịch. Nhờ đó, việc đổi ngôn ngữ không làm thay đổi "
        "định danh công cụ, không ảnh hưởng tới cấu hình vô hiệu hoá công cụ và "
        "không phá vỡ các liên kết nội bộ."
    )
    r.p(
        "Một khác biệt quan trọng giữa bản web và bản desktop nằm ở cách xử lý "
        "liên kết. Bản web sinh sẵn một thư mục trang riêng cho mỗi ngôn ngữ ở "
        "thời điểm biên dịch và viết lại mọi liên kết nội bộ để thêm tiền tố "
        "ngôn ngữ, phục vụ mục tiêu tối ưu hoá công cụ tìm kiếm. Bản desktop "
        "không sinh những trang đó và dùng cơ chế đổi ngôn ngữ tại chỗ. Nếu áp "
        "dụng nhầm cơ chế viết lại liên kết cho bản desktop, mọi liên kết sẽ "
        "trỏ tới trang không tồn tại — đây chính là một lỗi thực tế đã xảy ra "
        "và được khắc phục, sẽ được phân tích chi tiết ở Chương 3."
    )

    # ==================================================================
    r.h2("7. Thiết kế bảo mật và an toàn thông tin")

    r.h3("7.1. Mô hình các lớp bảo vệ dữ liệu")
    r.p(
        "Thiết kế bảo mật của hệ thống được tổ chức thành năm lớp đồng tâm, "
        "trong đó lớp ngoài cùng mang tính kiến trúc và các lớp trong dần mang "
        "tính kỹ thuật cụ thể. Cách tổ chức này phản ánh đúng thứ tự hiệu lực: "
        "lớp ngoài loại bỏ cả một họ mối đe doạ, các lớp trong xử lý những mối "
        "đe doạ còn lại. Hình 2.13 trình bày mô hình này."
    )
    r.figure(
        "fig_2_13_security_layers",
        "Hình 2.13. Mô hình năm lớp bảo vệ dữ liệu của hệ thống",
    )
    r.p(
        "Lớp thứ nhất là lớp kiến trúc: hệ thống không tải tệp lên mạng. Đây là "
        "lớp có hiệu lực mạnh nhất vì nó loại bỏ toàn bộ họ mối đe doạ liên "
        "quan tới truyền và lưu trữ dữ liệu ở bên thứ ba — nghe lén đường "
        "truyền, rò rỉ từ kho lưu trữ, truy cập trái phép của nhân viên nhà "
        "cung cấp, lộ dữ liệu từ bản sao lưu. Không có biện pháp kỹ thuật nào "
        "ở các lớp trong đạt được hiệu quả tương đương."
    )
    r.p(
        "Lớp thứ hai là cách ly tiến trình của vỏ Tauri. Tệp khai báo quyền chỉ "
        "cấp cho cửa sổ chính đúng bộ quyền lõi mặc định, không có quyền hệ tệp "
        "và không có quyền hộp thoại. Hệ quả là ngay cả khi mã giao diện bị "
        "chèn mã độc, mã đó cũng không thể đọc hay ghi tệp tuỳ ý; nó chỉ có thể "
        "gọi đúng một lệnh được khai báo, và lệnh đó bắt buộc phải mở hộp thoại "
        "cho người dùng xác nhận vị trí lưu. Đây là ứng dụng cụ thể của nguyên "
        "tắc đặc quyền tối thiểu."
    )
    r.p(
        "Lớp thứ ba kiểm soát nguồn mã thực thi. Mô-đun quản lý nguồn "
        "WebAssembly duy trì một tập máy chủ tin cậy được xây dựng từ ba nguồn: "
        "tên miền của chính ứng dụng, các địa chỉ mặc định biên dịch sẵn, và "
        "các địa chỉ do người dùng chủ động thêm vào. Mọi địa chỉ đọc từ bộ nhớ "
        "cục bộ đều được đối chiếu với tập này; địa chỉ không thuộc tập sẽ bị "
        "loại bỏ, ghi cảnh báo và xoá khỏi bộ nhớ cục bộ để không tái xuất "
        "hiện."
    )
    r.p(
        "Lớp thứ tư vệ sinh dữ liệu đầu vào. Mọi nội dung do tệp cung cấp mà có "
        "khả năng được hiển thị dưới dạng HTML đều đi qua bộ lọc: nội dung "
        "Markdown chuyển thành HTML được làm sạch bằng DOMPurify; nội dung HTML "
        "trong thư điện tử đi qua một hàm chuyên biệt loại bỏ thẻ kịch bản, thẻ "
        "khung nhúng, thuộc tính kiểu và các điểm ảnh theo dõi; tên tệp và siêu "
        "dữ liệu được thoát ký tự trước khi chèn vào giao diện. Cùng lớp này "
        "còn có các mô-đun làm sạch tài liệu và che nội dung vĩnh viễn."
    )
    r.p(
        "Lớp thứ năm, trong cùng, là các cơ chế mật mã áp dụng lên chính tài "
        "liệu: mã hoá AES-256 với hai loại mật khẩu và các cờ hạn chế, ký số "
        "bằng chứng thư X.509 với khoá riêng chỉ tồn tại trong bộ nhớ, và đóng "
        "dấu thời gian theo RFC 3161."
    )
    r.p(
        "Bao trùm cả năm lớp là một nguyên tắc âm: hệ thống không có tài khoản, "
        "không có phiên đăng nhập, không có nhật ký phía máy chủ và không gửi "
        "dữ liệu đo đạc. Mỗi thành phần không tồn tại là một bề mặt tấn công "
        "không tồn tại."
    )

    r.h3("7.2. Kiểm soát nguồn mã thực thi và cách ly nguồn gốc")
    r.p(
        "Mục này phân tích sâu hơn lớp bảo vệ thứ ba, bởi đây là lớp có thiết "
        "kế tinh tế nhất và cũng dễ bị hiểu sai nhất. Vấn đề đặt ra như sau: hệ "
        "thống cần cho phép người triển khai trỏ các mô-đun xử lý về máy chủ "
        "nội bộ của họ, nhưng khả năng cấu hình đó chính là một kênh tấn công "
        "tiềm tàng, vì địa chỉ được lưu trong bộ nhớ cục bộ của WebView và có "
        "thể bị thay đổi."
    )
    r.p(
        "Giải pháp gồm ba thành phần. Thứ nhất, tập máy chủ tin cậy được khởi "
        "tạo ngay khi mô-đun được nạp, từ tên miền hiện tại của ứng dụng và từ "
        "các địa chỉ mặc định. Thứ hai, mỗi lần đọc cấu hình từ bộ nhớ cục bộ, "
        "hệ thống trích tên miền của từng địa chỉ và đối chiếu với tập tin cậy; "
        "địa chỉ không khớp bị loại, đồng thời cấu hình đã lọc được ghi đè trở "
        "lại bộ nhớ cục bộ. Thứ ba, khi người dùng chủ động đặt một địa chỉ mới "
        "qua giao diện, tên miền của địa chỉ đó được thêm vào tập tin cậy — hành "
        "vi này hợp lý vì đó là hành động có chủ ý của người dùng, khác hẳn với "
        "một giá trị xuất hiện âm thầm trong bộ nhớ cục bộ."
    )
    r.p(
        "Bổ sung cho cơ chế trên là chức năng kiểm tra tính khả dụng của địa "
        "chỉ. Khi người dùng nhập một địa chỉ, hệ thống kiểm tra giao thức phải "
        "là HTTP hoặc HTTPS, thử tải một tệp đặc trưng của mô-đun tương ứng với "
        "thời hạn chờ mười giây, kiểm tra mã trạng thái và kiểm tra kiểu nội "
        "dung trả về. Việc phản hồi lỗi cụ thể — không tìm thấy tệp, lỗi cấu "
        "hình chia sẻ tài nguyên, kiểu nội dung không đúng — giúp người triển "
        "khai chẩn đoán nhanh thay vì phải đoán."
    )
    r.p(
        "Về cách ly nguồn gốc, tệp cấu hình Tauri đặt hai tiêu đề bắt buộc cho "
        "giao thức phục vụ tài nguyên nội bộ. Hai tiêu đề này không phải tuỳ "
        "chọn về hiệu năng mà là điều kiện tiên quyết để một số mô-đun "
        "WebAssembly hoạt động. Việc gỡ bỏ chúng sẽ khiến các mô-đun cần đa "
        "luồng thất bại với thông điệp khó chẩn đoán — đây là một điểm được ghi "
        "chú rõ trong tài liệu kỹ thuật của dự án."
    )
    r.p(
        "Cuối cùng, trình phục vụ ngoại tuyến của bản web được vô hiệu hoá "
        "trong bản desktop. Lý do là ứng dụng đã hoàn toàn cục bộ nên một tầng "
        "bộ nhớ đệm bổ sung không mang lại lợi ích, trong khi lại có thể che "
        "khuất tài nguyên đã đóng gói và gây khó khăn khi chẩn đoán sự cố."
    )

    r.h3("7.3. Bảo vệ tài liệu bằng mật mã và giới hạn của cơ chế")
    r.p(
        "Hệ thống cung cấp ba nhóm cơ chế mật mã trên tài liệu. Nhóm thứ nhất "
        "là mã hoá nội dung: người dùng đặt mật khẩu người dùng để giới hạn "
        "quyền mở tài liệu, và tuỳ chọn đặt mật khẩu chủ sở hữu riêng để áp "
        "dụng các hạn chế thao tác. Thuật toán được cố định ở AES-256, mức mạnh "
        "nhất mà đặc tả PDF hỗ trợ."
    )
    r.p(
        "Nhóm thứ hai là chữ ký số. Hệ thống chấp nhận chứng thư ở ba dạng: tệp "
        "PKCS#12 kèm mật khẩu, cặp tệp chứng thư và khoá riêng ở định dạng PEM, "
        "và tệp PEM gộp cả hai. Với khoá riêng đã mã hoá, hệ thống giải mã bằng "
        "mật khẩu người dùng cung cấp. Toàn bộ quá trình phân tích chứng thư và "
        "ký diễn ra trong bộ nhớ của tiến trình; khoá riêng không được ghi ra "
        "đâu và không được gửi đi."
    )
    r.p(
        "Nhóm thứ ba là đóng dấu thời gian tin cậy theo RFC 3161. Hệ thống cung "
        "cấp sẵn danh sách năm nhà cung cấp thông dụng để người dùng chọn. Một "
        "chi tiết đáng chú ý là một số nhà cung cấp chỉ có điểm cuối HTTP; điều "
        "này được ghi chú rõ trong mã nguồn kèm lý giải: dấu thời gian theo RFC "
        "3161 được ký ở tầng ứng dụng nên tính toàn vẹn của nó không phụ thuộc "
        "duy nhất vào tầng vận chuyển."
    )
    r.p(
        "Cần nêu rõ ba giới hạn của các cơ chế trên để tránh kỳ vọng sai. Giới "
        "hạn thứ nhất: mã hoá PDF chỉ mạnh bằng mật khẩu người dùng đặt; một "
        "mật khẩu ngắn hoặc dễ đoán sẽ vô hiệu hoá toàn bộ giá trị của AES-256. "
        "Hệ thống hiện chưa có cơ chế đánh giá độ mạnh mật khẩu và đây là một "
        "điểm nên bổ sung."
    )
    r.p(
        "Giới hạn thứ hai: các cờ hạn chế in, sao chép và chỉnh sửa chỉ có hiệu "
        "lực khi trình đọc PDF tôn trọng chúng. Đặc tả không có cơ chế cưỡng "
        "chế kỹ thuật cho các cờ này, và bản thân hệ thống cũng cung cấp công "
        "cụ gỡ hạn chế. Vì vậy cần hiểu các cờ này là chỉ dẫn về ý định của tác "
        "giả chứ không phải biện pháp bảo vệ thực sự."
    )
    r.p(
        "Giới hạn thứ ba liên quan tới tính năng ký số với chứng thư cần tải "
        "chuỗi chứng thư từ bên ngoài. Do nhiều máy chủ của cơ quan cấp chứng "
        "thư không hỗ trợ chia sẻ tài nguyên nguồn gốc chéo, thư viện ký cần "
        "một máy chủ trung chuyển. Hệ thống hỗ trợ cấu hình máy chủ trung "
        "chuyển kèm cơ chế ký yêu cầu bằng mã xác thực thông điệp; tuy nhiên mã "
        "nguồn ghi chú rất thẳng thắn rằng bí mật dùng để ký nằm trong mã phía "
        "máy khách nên chỉ có tác dụng ngăn lạm dụng tình cờ, không có tác dụng "
        "trước kẻ tấn công có chủ đích. Đây là một đánh đổi được nêu rõ chứ "
        "không được che giấu, và với chứng thư tự ký hoặc chứng thư không cần "
        "tải chuỗi thì vấn đề này không phát sinh."
    )

    # ==================================================================
    r.h2("Kết luận chương 2")
    r.p(
        "Chương 2 đã chuyển các phân tích lý luận và thực tiễn của Chương 1 "
        "thành một thiết kế cụ thể. Xuất phát từ ba ràng buộc cứng — không "
        "truyền tài liệu ra ngoài, hoạt động khi không có mạng, và đủ rộng cho "
        "công việc hằng ngày — chương đã suy ra một loạt kết luận thiết kế "
        "mang tính bắt buộc: không có tài khoản và phân quyền, mọi trạng thái "
        "là trạng thái phiên, và ranh giới bảo mật quan trọng nhất nằm giữa "
        "tầng giao diện và tầng vỏ bản địa."
    )
    r.p(
        "Về phân tích yêu cầu, chương đã đặc tả 19 yêu cầu chức năng kèm trạng "
        "thái hiện thực đã kiểm chứng trong mã nguồn, và 19 yêu cầu phi chức "
        "năng chia thành bốn nhóm. Điểm đáng chú ý của tập yêu cầu phi chức "
        "năng là phần lớn được viết theo cách có thể kiểm chứng bằng quan sát "
        "trực tiếp, phù hợp với đặc thù của một hệ thống mà giá trị cốt lõi là "
        "sự tin cậy về dữ liệu."
    )
    r.p(
        "Về kiến trúc, chương đã trình bày mô hình phân tầng sáu tầng với quan "
        "hệ phụ thuộc một chiều, trong đó tầng vỏ bản địa được giữ ở quy mô tối "
        "thiểu theo nguyên tắc thu hẹp bề mặt đặc quyền. Kiến trúc thành phần "
        "được tái dựng từ quan hệ nhập mô-đun thực tế, và kiến trúc triển khai "
        "mô tả đầy đủ ba giai đoạn phát triển, đóng gói và vận hành."
    )
    r.p(
        "Về quy trình xử lý, chương đã nhận diện một quy trình chung mười sáu "
        "bước áp dụng cho toàn bộ 127 công cụ, phân tích bản đồ phân bổ thao "
        "tác cho từng động cơ xử lý, và trình bày chi tiết hai biểu đồ tuần tự "
        "đại diện cho hai khuôn mẫu tích hợp khác nhau: khuôn mẫu thư viện "
        "trong Web Worker và khuôn mẫu chương trình dòng lệnh trên hệ tệp ảo. "
        "Mô hình thực thi của luồng xử lý tự động cũng được phân tích, làm rõ "
        "giá trị của việc tái sử dụng tầng tiện ích."
    )
    r.p(
        "Về dữ liệu, giao diện và bảo mật, chương đã mô tả mô hình dữ liệu "
        "trong bộ nhớ cùng ba mức cấu hình, cấu trúc điều hướng ba đường tiếp "
        "cận, khuôn mẫu giao diện công cụ, thiết kế đa ngữ, và mô hình năm lớp "
        "bảo vệ dữ liệu. Chương cũng đã nêu thẳng thắn ba giới hạn của các cơ "
        "chế mật mã và một giới hạn của nguyên tắc không ghi tệp tạm, nhằm bảo "
        "đảm người đọc có kỳ vọng đúng về năng lực thực tế của hệ thống. Toàn "
        "bộ thiết kế này được hiện thực hoá như thế nào là nội dung của "
        "Chương 3."
    )
