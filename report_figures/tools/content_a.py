# -*- coding: utf-8 -*-
"""Phần đầu báo cáo: bìa trong, chữ viết tắt, mở đầu và Chương 1."""


def build(r):
    # ==================================================================
    # MỤC LỤC
    # ==================================================================
    r.h1("MỤC LỤC", page_break=False)
    r.toc_field()

    # ==================================================================
    # DANH MỤC CHỮ VIẾT TẮT
    # ==================================================================
    r.h1("DANH MỤC CHỮ VIẾT TẮT VÀ THUẬT NGỮ")
    r.table(
        "Bảng 0.1. Danh mục chữ viết tắt và thuật ngữ sử dụng trong báo cáo",
        ["Ký hiệu", "Nguyên nghĩa", "Giải thích ngắn gọn"],
        [
            ["AES", "Advanced Encryption Standard",
             "Chuẩn mã hoá đối xứng; PDF Toolkit dùng AES-256 khi đặt mật khẩu "
             "cho tài liệu"],
            ["AGPL", "GNU Affero General Public License",
             "Giấy phép nguồn mở áp dụng cho mã nguồn dự án và cho ba thư viện "
             "xử lý được cấu hình sẵn"],
            ["API", "Application Programming Interface",
             "Giao diện lập trình; trong báo cáo chủ yếu chỉ giao diện giữa các "
             "mô-đun trong cùng tiến trình"],
            ["CBZ", "Comic Book ZIP",
             "Định dạng lưu truyện tranh dưới dạng kho nén chứa ảnh theo thứ tự"],
            ["CDN", "Content Delivery Network",
             "Mạng phân phối nội dung; bản web tải mô-đun WASM từ CDN, bản "
             "desktop thì không"],
            ["COOP / COEP", "Cross-Origin Opener/Embedder Policy",
             "Hai tiêu đề HTTP bắt buộc để bật SharedArrayBuffer cho mô-đun "
             "WebAssembly đa luồng"],
            ["CPDF", "CoherentPDF",
             "Thư viện xử lý PDF viết bằng OCaml, biên dịch sang JavaScript, "
             "dùng cho ghép tệp và tệp đính kèm"],
            ["CSV", "Comma-Separated Values",
             "Định dạng bảng dữ liệu dạng văn bản thuần"],
            ["DPI", "Dots Per Inch",
             "Mật độ điểm ảnh trên một inch, tham số then chốt khi lấy mẫu lại "
             "ảnh trong quá trình nén"],
            ["hOCR", "HTML-based OCR format",
             "Định dạng HTML mô tả vị trí, kích thước và độ tin cậy của từng từ "
             "mà bộ nhận dạng trả về"],
            ["IPC", "Inter-Process Communication",
             "Cơ chế trao đổi dữ liệu giữa WebView và tiến trình Rust trong "
             "khung nền Tauri"],
            ["JS", "JavaScript",
             "Ngôn ngữ lập trình chạy trong WebView"],
            ["MEMFS", "In-memory File System",
             "Hệ tệp ảo trong bộ nhớ do Emscripten cung cấp cho mô-đun "
             "WebAssembly"],
            ["OCR", "Optical Character Recognition",
             "Nhận dạng ký tự quang học, biến ảnh chụp văn bản thành văn bản "
             "có thể tìm kiếm"],
            ["OEM", "OCR Engine Mode",
             "Chế độ động cơ nhận dạng của Tesseract; hệ thống sử dụng chế độ 1 "
             "(LSTM)"],
            ["PDF", "Portable Document Format",
             "Định dạng tài liệu điện tử do Adobe công bố, hiện là chuẩn "
             "ISO 32000"],
            ["PDF/A", "PDF for Archive",
             "Biến thể PDF dùng cho lưu trữ dài hạn, yêu cầu nhúng đầy đủ phông "
             "và không gian màu"],
            ["PFX / PKCS#12", "Personal Information Exchange",
             "Định dạng đóng gói chứng thư số kèm khoá riêng, dùng khi ký số"],
            ["PSM", "Page Segmentation Mode",
             "Chế độ phân đoạn trang của Tesseract, quyết định cách bộ nhận "
             "dạng tách dòng và khối văn bản"],
            ["TSA", "Time Stamping Authority",
             "Cơ quan cấp dấu thời gian tin cậy theo RFC 3161"],
            ["UI", "User Interface", "Giao diện người dùng"],
            ["WASM", "WebAssembly",
             "Định dạng mã nhị phân chạy trong môi trường web với tốc độ gần "
             "mã máy"],
            ["XFA", "XML Forms Architecture",
             "Kiến trúc biểu mẫu dựa trên XML từng được dùng trong một số biểu "
             "mẫu PDF"],
            ["XSS", "Cross-Site Scripting",
             "Lỗ hổng cho phép chèn và thực thi mã kịch bản trong ngữ cảnh "
             "trang hiển thị"],
        ],
        widths=[2, 4, 8],
        font_size=11,
    )

    # ==================================================================
    # MỞ ĐẦU
    # ==================================================================
    r.h1("MỞ ĐẦU")

    r.h2("1. Tính cấp thiết của đề tài")
    r.p(
        "Tài liệu điện tử ở định dạng PDF hiện diện trong hầu hết mọi hoạt động "
        "hành chính, đào tạo, nghiên cứu và sản xuất. Một quyết định hành chính "
        "được ban hành dưới dạng PDF, một bài giảng được đóng gói thành PDF, "
        "một hợp đồng được ký số trên nền PDF, một hồ sơ bệnh án hay một bản vẽ "
        "kỹ thuật cũng được lưu trữ và trao đổi dưới cùng định dạng đó. Sự phổ "
        "biến này bắt nguồn từ một đặc tính then chốt của PDF: tài liệu được "
        "hiển thị giống hệt nhau trên mọi thiết bị, mọi hệ điều hành, không phụ "
        "thuộc vào phần mềm soạn thảo đã tạo ra nó. Chính đặc tính đó cũng khiến "
        "PDF trở thành định dạng khó thao tác nhất trong nhóm tài liệu văn "
        "phòng: cấu trúc bên trong tệp được tổ chức theo hướng phục vụ việc "
        "kết xuất chính xác chứ không phải phục vụ việc chỉnh sửa."
    )
    r.p(
        "Hệ quả trực tiếp là người dùng thường xuyên phải nhờ tới công cụ "
        "chuyên dụng cho những nhu cầu tưởng chừng rất đơn giản: ghép hai bản "
        "quét thành một hồ sơ, tách một phụ lục ra khỏi tài liệu chính, xoay "
        "lại những trang bị quét ngược, giảm dung lượng một tập tin quá lớn để "
        "gửi qua thư điện tử, đặt mật khẩu cho một văn bản nội bộ, hoặc biến "
        "một bản quét thành tài liệu có thể tìm kiếm được bằng nhận dạng ký tự "
        "quang học. Trong thực tế, phần lớn người dùng giải quyết những nhu cầu "
        "này bằng các dịch vụ trực tuyến miễn phí. Thao tác rất thuận tiện: mở "
        "trình duyệt, kéo tệp vào trang web, chờ vài giây rồi tải kết quả về."
    )
    r.p(
        "Sự thuận tiện ấy đi kèm một cái giá thường bị bỏ qua. Khi tệp được kéo "
        "vào một dịch vụ trực tuyến, toàn bộ nội dung tài liệu đã rời khỏi máy "
        "người dùng và nằm trên hạ tầng của một bên thứ ba. Với tài liệu chứa "
        "thông tin cá nhân, thông tin nội bộ, số liệu chưa công bố, dữ liệu hợp "
        "đồng hoặc tài liệu có yêu cầu bảo mật, hành vi tải lên đơn giản này đã "
        "là một sự cố lộ lọt thông tin, bất kể nhà cung cấp dịch vụ có cam kết "
        "xoá tệp sau vài giờ hay không. Bên cạnh đó, các dịch vụ miễn phí "
        "thường đặt giới hạn về dung lượng tệp, số lần xử lý trong ngày và số "
        "tệp mỗi lần, đồng thời không hoạt động khi máy tính không có kết nối "
        "Internet — điều rất thường gặp trong các môi trường làm việc có kiểm "
        "soát mạng chặt chẽ hoặc mạng nội bộ tách biệt."
    )
    r.p(
        "Ở chiều ngược lại, các phần mềm xử lý PDF cài đặt trên máy tính giải "
        "quyết được vấn đề riêng tư nhưng lại đặt ra rào cản khác. Những bộ "
        "phần mềm thương mại đầy đủ tính năng có chi phí bản quyền đáng kể và "
        "thường được cấp phép theo từng máy hoặc theo thuê bao. Các công cụ "
        "miễn phí thì thường chỉ giải quyết một nhóm thao tác hẹp, buộc người "
        "dùng phải cài đặt và ghi nhớ nhiều phần mềm khác nhau, mỗi phần mềm "
        "một giao diện, một quy ước và một mức độ tin cậy riêng. Việc cài đặt "
        "nhiều phần mềm nhỏ từ nhiều nguồn khác nhau lại làm phát sinh rủi ro "
        "về an toàn phần mềm."
    )
    r.p(
        "Từ khoảng năm 2017 trở lại đây, sự trưởng thành của WebAssembly đã mở "
        "ra một hướng tiếp cận thứ ba. Các thư viện xử lý tài liệu vốn được "
        "viết bằng C, C++ hoặc OCaml và chỉ chạy được trên máy chủ — qpdf, "
        "Ghostscript, MuPDF, Tesseract, CoherentPDF — nay có thể được biên dịch "
        "sang WebAssembly và thực thi ngay trong môi trường của một trình duyệt "
        "hoặc một WebView, với tốc độ đủ tốt cho công việc thực tế. Điều này "
        "cho phép xây dựng những ứng dụng có đầy đủ năng lực xử lý tài liệu "
        "nhưng không cần bất kỳ máy chủ xử lý nào phía sau: tệp không rời khỏi "
        "máy người dùng, không tồn tại đường truyền để nghe lén, không tồn tại "
        "kho lưu trữ trung gian để rò rỉ."
    )
    r.p(
        "Kết hợp hướng tiếp cận đó với một khung nền ứng dụng desktop lai — cụ "
        "thể là Tauri, sử dụng WebView sẵn có của hệ điều hành thay vì đóng gói "
        "một trình duyệt riêng — ta thu được một loại phần mềm có đặc điểm rất "
        "phù hợp với bài toán đặt ra: giao diện hiện đại và dễ phát triển như "
        "một ứng dụng web, nhưng chạy như một ứng dụng bản địa, có hộp thoại hệ "
        "thống, có quyền truy cập tệp theo đúng cơ chế của hệ điều hành, và "
        "quan trọng nhất là hoạt động đầy đủ khi hoàn toàn không có mạng."
    )
    r.p(
        "Đề tài “Xây dựng ứng dụng desktop xử lý tài liệu PDF hoạt động hoàn "
        "toàn cục bộ — PDF Toolkit Desktop” được thực hiện theo hướng này. Hệ "
        "thống được xây dựng nhằm cung cấp một bộ công cụ xử lý tài liệu PDF và "
        "hình ảnh đủ rộng cho công việc hằng ngày, chạy trên cả ba hệ điều hành "
        "phổ biến, không yêu cầu tài khoản, không có giới hạn số lần sử dụng, "
        "không gửi bất kỳ tệp nào ra ngoài, và có giao diện tiếng Việt đầy đủ. "
        "Tính cấp thiết của đề tài vì vậy không nằm ở việc tạo ra một tính năng "
        "chưa từng có, mà ở việc tổ chức lại một tập hợp năng lực xử lý đã tồn "
        "tại thành một sản phẩm mà người dùng có thể tin cậy về mặt dữ liệu."
    )

    r.h2("2. Mục tiêu nghiên cứu")
    r.p(
        "Mục tiêu tổng quát của đề tài là nghiên cứu, phân tích, thiết kế và "
        "hoàn thiện một ứng dụng desktop đa nền tảng cho phép thực hiện các "
        "thao tác xử lý tài liệu PDF và hình ảnh hoàn toàn trên máy người dùng, "
        "bảo đảm không có dữ liệu tài liệu nào được truyền ra khỏi thiết bị "
        "trong quá trình xử lý."
    )
    r.p("Các mục tiêu cụ thể bao gồm:")
    r.bullets([
        "Phân tích đặc điểm của bài toán xử lý tài liệu PDF phía máy khách, "
        "xác định nhóm thao tác cần hỗ trợ và ràng buộc kỹ thuật của từng nhóm;",
        "Nghiên cứu khả năng và giới hạn của việc đưa các thư viện xử lý tài "
        "liệu vào môi trường WebAssembly, từ đó xác định thư viện phù hợp cho "
        "từng nhóm thao tác;",
        "Thiết kế kiến trúc hệ thống theo mô hình phân tầng, trong đó tầng vỏ "
        "native chỉ đảm nhiệm những việc mà môi trường web không làm được, còn "
        "toàn bộ logic xử lý nằm trong tầng web dùng chung;",
        "Hiện thực hoá đầy đủ các nhóm chức năng đã thiết kế, bao gồm tổ chức "
        "trang, chỉnh sửa, chuyển đổi định dạng, nén, bảo mật, ký số, nhận dạng "
        "ký tự quang học và xây dựng luồng xử lý tự động;",
        "Thiết kế cơ chế lưu tệp sử dụng hộp thoại của hệ điều hành, thay cho "
        "cơ chế tải xuống của trình duyệt, để trải nghiệm giống một ứng dụng "
        "bản địa;",
        "Bảo đảm ứng dụng chạy được hoàn toàn ngoại tuyến bằng cách đóng gói "
        "sẵn toàn bộ mô-đun WebAssembly và dữ liệu ngôn ngữ cần thiết;",
        "Xây dựng giao diện đa ngữ với tiếng Việt là ngôn ngữ mặc định, phù hợp "
        "với người dùng trong nước;",
        "Xác lập phương pháp kiểm thử và đánh giá, đồng thời chỉ rõ những nội "
        "dung đã kiểm chứng được và những nội dung còn phải tiếp tục đo đạc.",
    ])

    r.h2("3. Nhiệm vụ nghiên cứu")
    r.p(
        "Để đạt được các mục tiêu trên, đề tài xác định các nhiệm vụ nghiên cứu "
        "theo trình tự sau. Thứ nhất, hệ thống hoá cơ sở lý luận về định dạng "
        "PDF, về các mô hình xử lý tài liệu và về công nghệ WebAssembly, làm "
        "nền tảng cho các quyết định thiết kế ở chương sau. Thứ hai, khảo sát "
        "thực tiễn sử dụng công cụ xử lý PDF hiện nay, phân tích ưu nhược điểm "
        "của từng nhóm giải pháp và rút ra yêu cầu cho hệ thống cần xây dựng. "
        "Thứ ba, phân tích yêu cầu chức năng và phi chức năng, mô hình hoá ca "
        "sử dụng, thiết kế kiến trúc tổng thể, kiến trúc thành phần, kiến trúc "
        "triển khai, quy trình xử lý tài liệu, mô hình dữ liệu, cấu trúc giao "
        "diện và các lớp bảo vệ dữ liệu."
    )
    r.p(
        "Thứ tư, hiện thực hoá hệ thống: xây dựng khung giao diện đa trang, xây "
        "dựng các mô-đun nghiệp vụ tương ứng với từng công cụ, tích hợp các thư "
        "viện xử lý dưới dạng WebAssembly, xây dựng vỏ ứng dụng native bằng "
        "Rust và Tauri, xây dựng cơ chế lưu tệp bản địa, tổ chức tài nguyên "
        "ngoại tuyến và thiết lập quy trình biên dịch, đóng gói cho ba hệ điều "
        "hành. Thứ năm, xây dựng bộ kiểm thử tự động cho các phần logic thuần "
        "tuý, thiết lập quy trình phân tích tĩnh và quét bảo mật, đặc tả quy "
        "trình kiểm thử chức năng thủ công và phương pháp đo hiệu năng. Cuối "
        "cùng, tổng hợp kết quả, đánh giá mức độ đáp ứng các yêu cầu đã đặt ra, "
        "chỉ rõ hạn chế và đề xuất hướng phát triển tiếp theo."
    )

    r.h2("4. Đối tượng nghiên cứu")
    r.p(
        "Đối tượng nghiên cứu của đề tài là ứng dụng desktop PDF Toolkit "
        "Desktop cùng toàn bộ mã nguồn, cấu hình biên dịch, tài nguyên đi kèm "
        "và quy trình đóng gói của nó. Cụ thể hơn, đối tượng nghiên cứu bao gồm "
        "kiến trúc phân tầng của ứng dụng, cơ chế tích hợp các thư viện xử lý "
        "tài liệu dưới dạng WebAssembly, cơ chế trao đổi giữa tầng giao diện "
        "chạy trong WebView và tầng vỏ native viết bằng Rust, mô hình dữ liệu "
        "trong bộ nhớ, cơ chế quản lý vòng đời dữ liệu tạm, các lớp bảo vệ dữ "
        "liệu và cơ chế quốc tế hoá giao diện."
    )
    r.p(
        "Bên cạnh đó, đề tài cũng nghiên cứu đặc điểm và giới hạn của các thư "
        "viện xử lý tài liệu được tích hợp, bởi lẽ những giới hạn đó quyết định "
        "trực tiếp phạm vi chức năng mà hệ thống có thể cung cấp. Việc lựa chọn "
        "thư viện nào cho thao tác nào, tại sao một thao tác lại phải thực hiện "
        "trong Web Worker còn thao tác khác thì không, tại sao một số tính năng "
        "buộc phải chấp nhận phụ thuộc mạng — tất cả đều là nội dung nghiên cứu "
        "của đề tài."
    )

    r.h2("5. Phạm vi nghiên cứu")
    r.p(
        "Về phạm vi nội dung, đề tài tập trung vào bản dựng desktop của hệ "
        "thống. Kho mã nguồn còn chứa cấu hình cho bản triển khai web tĩnh và "
        "bản đóng gói bằng Docker phục vụ mạng nội bộ; những phần này chỉ được "
        "nhắc tới ở mức cần thiết để làm rõ sự khác biệt của bản desktop, "
        "không phải là đối tượng phân tích chính. Tương tự, hệ thống tài liệu "
        "hướng dẫn xây dựng bằng VitePress và các quy trình tích hợp liên tục "
        "phục vụ bản web chỉ được đề cập khi liên quan trực tiếp tới chất lượng "
        "hoặc quy trình phát hành của bản desktop."
    )
    r.p(
        "Về phạm vi chức năng, đề tài chỉ mô tả và đánh giá những chức năng có "
        "bằng chứng trong mã nguồn. Những tính năng được nêu trong phần lộ "
        "trình phát triển của dự án nhưng chưa được hiện thực hoá không được "
        "tính vào phạm vi. Về phạm vi thời gian, phân tích được thực hiện trên "
        "trạng thái kho mã tại phiên bản 2.8.5, ứng với nhánh chính của kho "
        "PDFToolkitDesktop."
    )
    r.p(
        "Về phạm vi thực nghiệm, cần nói rõ ngay từ đầu: môi trường máy chủ "
        "dùng để phân tích mã nguồn trong khuôn khổ đề tài không có giao diện "
        "đồ hoạ và không đủ tài nguyên đĩa cũng như bộ nhớ để cài đặt toàn bộ "
        "phụ thuộc và biên dịch ứng dụng. Do đó các số đo về thời gian xử lý, "
        "mức tiêu thụ bộ nhớ và ảnh chụp giao diện thực tế chưa được thu thập. "
        "Báo cáo trình bày đầy đủ phương pháp đo và tiêu chí đánh giá, đồng "
        "thời đánh dấu rõ ràng những nội dung chưa có số liệu, tuyệt đối không "
        "đưa ra con số ước lượng thay thế."
    )

    r.h2("6. Phương pháp nghiên cứu")
    r.p(
        "Đề tài sử dụng phối hợp bốn nhóm phương pháp. Phương pháp nghiên cứu "
        "tài liệu được dùng để hệ thống hoá cơ sở lý luận về định dạng PDF, về "
        "WebAssembly, về kiến trúc ứng dụng desktop lai và về các nguyên tắc "
        "bảo vệ dữ liệu; nguồn tài liệu gồm đặc tả kỹ thuật, tài liệu chính "
        "thức của các thư viện được tích hợp và tài liệu nội bộ của dự án."
    )
    r.p(
        "Phương pháp phân tích mã nguồn giữ vai trò trung tâm. Toàn bộ kiến "
        "trúc, luồng xử lý và cơ chế được mô tả trong báo cáo đều được tái dựng "
        "bằng cách đọc trực tiếp mã nguồn: lần theo chuỗi lời gọi hàm, đối "
        "chiếu các câu lệnh nhập mô-đun để xác định quan hệ phụ thuộc, đọc tệp "
        "cấu hình biên dịch để xác định ranh giới tiến trình và tài nguyên đóng "
        "gói. Nguyên tắc được tuân thủ xuyên suốt là không mô tả một thành phần "
        "kiến trúc nào mà mã nguồn không hiện thực."
    )
    r.p(
        "Phương pháp mô hình hoá được dùng để chuyển kết quả phân tích thành "
        "các biểu đồ ca sử dụng, biểu đồ ngữ cảnh, biểu đồ thành phần, biểu đồ "
        "tuần tự, lưu đồ xử lý và sơ đồ kiến trúc triển khai. Mỗi biểu đồ trong "
        "báo cáo đều gắn với một hoặc một số tệp mã nguồn cụ thể và được lưu "
        "kèm ở dạng có thể chỉnh sửa để tiện cập nhật khi mã nguồn thay đổi."
    )
    r.p(
        "Phương pháp thực nghiệm và kiểm thử được dùng ở hai mức. Ở mức tự "
        "động, dự án có sẵn một bộ kiểm thử đơn vị viết bằng Vitest chạy trong "
        "môi trường jsdom, cùng với cấu hình phân tích tĩnh và quét bảo mật "
        "trong quy trình tích hợp liên tục; báo cáo phân tích cấu trúc và mức "
        "độ bao phủ của bộ kiểm thử này. Ở mức thủ công, báo cáo đặc tả quy "
        "trình kiểm thử chức năng và phương pháp đo hiệu năng để có thể thực "
        "hiện trên máy có giao diện đồ hoạ."
    )

    r.h2("7. Đóng góp của đề tài")
    r.p(
        "Về mặt lý luận, đề tài hệ thống hoá một mô hình kiến trúc cho lớp ứng "
        "dụng xử lý tài liệu chạy hoàn toàn cục bộ, trong đó ranh giới trách "
        "nhiệm giữa tầng vỏ native và tầng web được xác định theo nguyên tắc "
        "tối thiểu hoá bề mặt native. Mô hình này có thể áp dụng lại cho những "
        "bài toán khác có cùng đặc điểm: cần năng lực xử lý mạnh, cần bảo vệ dữ "
        "liệu tuyệt đối và cần chạy trên nhiều hệ điều hành với một mã nguồn "
        "duy nhất."
    )
    r.p(
        "Về mặt thực tiễn, đề tài tạo ra một sản phẩm phần mềm hoàn chỉnh, có "
        "thể biên dịch thành gói cài đặt cho macOS, Windows và Linux, cung cấp "
        "hơn một trăm công cụ xử lý tài liệu, có giao diện tiếng Việt mặc định "
        "và hoạt động đầy đủ khi không có mạng. Sản phẩm này có thể sử dụng "
        "trực tiếp trong các môi trường có yêu cầu không đưa tài liệu ra khỏi "
        "máy trạm."
    )
    r.p(
        "Về mặt tài liệu kỹ thuật, đề tài để lại một bộ sơ đồ kiến trúc được "
        "tái dựng từ mã nguồn, lưu ở cả dạng vector để in ấn và dạng có thể "
        "chỉnh sửa, kèm theo bảng chỉ mục ghi rõ nguồn bằng chứng của từng hình "
        "vẽ. Đây là phần thường thiếu ở các dự án phần mềm nguồn mở và có giá "
        "trị cho việc tiếp nhận, bảo trì cũng như phát triển tiếp hệ thống."
    )

    r.h2("8. Kết cấu đề tài")
    r.p(
        "Ngoài phần mở đầu, kết luận và danh mục tài liệu tham khảo, nội dung "
        "báo cáo được trình bày trong bốn chương."
    )
    r.p(
        "Chương 1 trình bày cơ sở khoa học và thực tiễn của đề tài, gồm tổng "
        "quan về định dạng PDF và các nhóm thao tác xử lý tài liệu, so sánh mô "
        "hình xử lý phía máy chủ với mô hình xử lý phía máy khách, giới thiệu "
        "công nghệ WebAssembly và kiến trúc ứng dụng desktop lai, đồng thời "
        "khảo sát thực trạng sử dụng công cụ xử lý PDF hiện nay cùng các căn cứ "
        "về giấy phép và an toàn thông tin."
    )
    r.p(
        "Chương 2 phân tích bài toán và thiết kế hệ thống: xác định phạm vi "
        "chức năng, đặc tả yêu cầu chức năng và phi chức năng, mô hình hoá ca "
        "sử dụng, thiết kế kiến trúc tổng thể và kiến trúc thành phần, thiết kế "
        "quy trình xử lý tài liệu, mô hình dữ liệu, cấu trúc giao diện và các "
        "lớp bảo vệ dữ liệu."
    )
    r.p(
        "Chương 3 trình bày quá trình xây dựng và triển khai hệ thống: môi "
        "trường phát triển, cấu trúc mã nguồn, khuôn mẫu hiện thực một công cụ, "
        "cách tích hợp từng thư viện xử lý, cơ chế lưu tệp bản địa, cơ chế đa "
        "ngữ, cách quản lý dữ liệu tạm và bộ nhớ, cách xử lý lỗi, cùng quy "
        "trình biên dịch và đóng gói cho ba hệ điều hành."
    )
    r.p(
        "Chương 4 trình bày thử nghiệm và đánh giá hệ thống: môi trường thử "
        "nghiệm, cấu trúc bộ kiểm thử tự động, quy trình kiểm thử chức năng, "
        "kiểm chứng khả năng chạy ngoại tuyến, phân tích cấu thành dung lượng "
        "tài nguyên và khung tiêu chí đánh giá, kèm theo phần nhận xét về kết "
        "quả đạt được cũng như những hạn chế còn tồn tại."
    )

    # ==================================================================
    # CHƯƠNG 1
    # ==================================================================
    r.h1("CHƯƠNG 1\nCƠ SỞ KHOA HỌC VÀ THỰC TIỄN")

    r.h2("1. Cơ sở lý luận")

    r.h3("1.1. Tổng quan về định dạng PDF và bài toán xử lý tài liệu số")
    r.p(
        "PDF ra đời đầu những năm 1990 với mục tiêu duy nhất là bảo đảm một "
        "tài liệu được in ra hoặc hiển thị giống hệt nhau ở mọi nơi. Để đạt "
        "được điều đó, tệp PDF không lưu tài liệu theo cách một trình soạn thảo "
        "văn bản lưu: nó không có khái niệm “đoạn văn”, “câu” hay “bảng” theo "
        "nghĩa cấu trúc. Thay vào đó, mỗi trang là một chuỗi lệnh vẽ mô tả việc "
        "đặt một chuỗi ký tự tại một toạ độ với một phông chữ và cỡ chữ nhất "
        "định, vẽ một đường thẳng, tô một hình chữ nhật, hay đặt một ảnh vào "
        "một vùng. Khái niệm gần nhất với cấu trúc là cây đối tượng của tài "
        "liệu và, nếu tác giả có chủ ý, cây thẻ cấu trúc phục vụ khả năng tiếp "
        "cận."
    )
    r.p(
        "Về mặt tổ chức tệp, PDF là một đồ thị các đối tượng được đánh số, "
        "gồm từ điển, mảng, chuỗi, số, luồng dữ liệu nhị phân và tham chiếu "
        "chéo. Bảng tham chiếu chéo đặt ở cuối tệp cho phép trình đọc nhảy "
        "thẳng tới đối tượng cần thiết mà không phải đọc toàn bộ tệp. Cấu trúc "
        "này giải thích nhiều đặc điểm mà người phát triển công cụ xử lý PDF "
        "phải đối mặt: một tệp có thể chứa nhiều phiên bản chồng lên nhau do "
        "được cập nhật tăng dần; một trang có thể tham chiếu tới tài nguyên "
        "dùng chung với trang khác; xoá một trang không đồng nghĩa với việc "
        "giải phóng dữ liệu mà trang đó dùng; và nội dung “đã xoá” trên giao "
        "diện có thể vẫn còn nguyên trong tệp nếu công cụ chỉ vẽ đè lên."
    )
    r.p(
        "Từ góc nhìn kỹ thuật, các thao tác xử lý PDF có thể chia thành ba mức "
        "độ can thiệp khác nhau. Mức thứ nhất là thao tác trên cấu trúc trang: "
        "ghép, tách, sắp xếp, xoay, xoá, trích trang. Những thao tác này chỉ "
        "cần đọc và ghi lại cây trang cùng các tham chiếu liên quan, không đụng "
        "tới nội dung bên trong trang, vì vậy nhanh và an toàn nhất. Mức thứ "
        "hai là thao tác bổ sung nội dung lên trang có sẵn: đóng dấu chìm, "
        "đánh số trang, thêm đầu trang và chân trang, thêm chú thích, thêm chữ "
        "ký hình ảnh. Ở mức này công cụ phải hiểu hệ toạ độ của trang, hộp "
        "MediaBox và CropBox, góc xoay đã đặt cho trang, đồng thời phải nhúng "
        "được phông chữ cho văn bản mới."
    )
    r.p(
        "Mức thứ ba là thao tác biến đổi sâu nội dung: nén ảnh nhúng, chuyển "
        "phông thành đường nét vector, chuyển đổi sang PDF/A, trích xuất văn "
        "bản và bảng, kết xuất trang thành ảnh, che thông tin vĩnh viễn. Đây là "
        "nhóm khó nhất, đòi hỏi phải phân tích được luồng nội dung của trang, "
        "hiểu được từ điển tài nguyên, xử lý được các bộ mã hoá luồng khác nhau "
        "và, trong nhiều trường hợp, phải kết xuất lại trang. Đó cũng là lý do "
        "vì sao không có một thư viện đơn lẻ nào phủ được toàn bộ ba mức, và vì "
        "sao một hệ thống xử lý PDF hoàn chỉnh luôn phải tích hợp nhiều thư "
        "viện với thế mạnh khác nhau."
    )
    r.p(
        "Bên cạnh ba mức trên còn có nhóm thao tác về an ninh tài liệu. PDF hỗ "
        "trợ mã hoá nội dung với hai loại mật khẩu: mật khẩu người dùng dùng để "
        "mở tài liệu và mật khẩu chủ sở hữu dùng để gỡ bỏ các hạn chế thao tác "
        "như in, sao chép, chỉnh sửa. Đặc tả cũng hỗ trợ chữ ký số theo chuẩn "
        "PKCS#7 nhúng trực tiếp trong tệp, cho phép xác minh tính toàn vẹn của "
        "tài liệu và danh tính người ký, kèm khả năng gắn dấu thời gian tin cậy "
        "theo RFC 3161. Việc hiện thực đúng các cơ chế này đòi hỏi phải thao "
        "tác ở mức byte của tệp, bởi phần chữ ký phải bao trùm toàn bộ nội dung "
        "trừ chính vùng chứa chữ ký."
    )

    r.h3("1.2. Phân nhóm thao tác xử lý tài liệu trong thực tế sử dụng")
    r.p(
        "Nếu mục 1.1 phân nhóm theo mức độ can thiệp kỹ thuật thì từ góc nhìn "
        "người dùng, các thao tác lại được nhóm theo mục đích công việc. Cách "
        "phân nhóm này quan trọng vì nó quyết định cách tổ chức giao diện. Khảo "
        "sát các công cụ phổ biến cho thấy có sáu nhóm mục đích tương đối ổn "
        "định."
    )
    r.p(
        "Nhóm thứ nhất là tổ chức và quản lý tài liệu: ghép nhiều tệp thành "
        "một, tách một tệp thành nhiều phần, sắp xếp lại thứ tự trang, nhân "
        "bản trang, xoá trang thừa, đảo ngược thứ tự, xoay trang bị quét lệch "
        "hướng, chia một trang khổ lớn thành nhiều trang nhỏ hoặc gộp nhiều "
        "trang lên một tờ để tiết kiệm giấy khi in. Đây là nhóm được dùng nhiều "
        "nhất và cũng là nhóm mà người dùng kỳ vọng phải nhanh."
    )
    r.p(
        "Nhóm thứ hai là chỉnh sửa và chú thích: thêm chữ ký, đóng dấu chìm để "
        "khẳng định bản quyền hoặc đánh dấu trạng thái tài liệu, đánh số trang, "
        "thêm đầu trang chân trang, làm nổi bật đoạn văn, thêm ghi chú, che "
        "thông tin nhạy cảm, cắt bớt lề, tạo và điền biểu mẫu. Nhóm này đòi hỏi "
        "giao diện tương tác trực quan hơn hẳn nhóm thứ nhất."
    )
    r.p(
        "Nhóm thứ ba là chuyển đổi định dạng theo hai chiều. Chiều vào gồm việc "
        "tạo PDF từ ảnh, từ tài liệu văn phòng, từ văn bản thuần, từ Markdown, "
        "từ bảng tính, từ sách điện tử, từ thư điện tử. Chiều ra gồm việc rút "
        "trích nội dung PDF thành ảnh, thành văn bản, thành bảng, thành tài "
        "liệu soạn thảo được. Chiều ra khó hơn chiều vào rất nhiều, bởi như đã "
        "phân tích ở mục 1.1, PDF không lưu giữ cấu trúc logic của tài liệu."
    )
    r.p(
        "Nhóm thứ tư là tối ưu hoá: giảm dung lượng tệp, chuẩn hoá khổ trang, "
        "tuyến tính hoá tệp để mở nhanh trên web, sửa chữa tệp hỏng, chuyển "
        "sang định dạng lưu trữ dài hạn. Nhóm thứ năm là bảo mật: đặt và gỡ mật "
        "khẩu, thay đổi quyền sử dụng, gỡ bỏ siêu dữ liệu, làm sạch tài liệu "
        "khỏi mã kịch bản và tệp nhúng, ký số và kiểm tra chữ ký. Nhóm thứ sáu, "
        "xuất hiện gần đây và ngày càng quan trọng, là nhận dạng ký tự quang "
        "học để biến tài liệu quét thành tài liệu tìm kiếm được."
    )
    r.p(
        "Một hệ thống muốn thay thế được thói quen dùng dịch vụ trực tuyến phải "
        "phủ được cả sáu nhóm ở mức đủ dùng, chứ không thể chỉ mạnh ở một vài "
        "nhóm. Đây là ràng buộc quan trọng đối với thiết kế: số lượng công cụ "
        "lớn buộc kiến trúc phải có tính khuôn mẫu cao, nếu không chi phí bảo "
        "trì sẽ tăng theo cấp số nhân."
    )

    r.h3("1.3. Mô hình xử lý phía máy chủ và mô hình xử lý phía máy khách")
    r.p(
        "Trong mô hình xử lý phía máy chủ — mô hình mà hầu hết dịch vụ trực "
        "tuyến đang dùng — trình duyệt chỉ đóng vai trò thu thập tệp và tham "
        "số rồi gửi lên máy chủ. Máy chủ nhận tệp, lưu tạm vào đĩa hoặc kho đối "
        "tượng, gọi các công cụ dòng lệnh để xử lý, sinh tệp kết quả rồi trả về "
        "một liên kết tải xuống. Mô hình này có ưu điểm rõ ràng: năng lực xử lý "
        "không bị giới hạn bởi máy người dùng, dễ dùng các thư viện gốc mạnh "
        "nhất, dễ mở rộng theo chiều ngang, và cùng một dịch vụ phục vụ được "
        "mọi thiết bị kể cả điện thoại yếu."
    )
    r.p(
        "Nhược điểm của mô hình này nằm ở chính hành vi trung tâm của nó là "
        "chuyển tệp lên máy chủ. Từ thời điểm tệp rời khỏi máy người dùng, nhà "
        "cung cấp dịch vụ trở thành một bên nắm giữ dữ liệu, và người dùng chỉ "
        "còn có thể tin vào cam kết chính sách chứ không thể tự kiểm chứng. Tệp "
        "tồn tại trên đĩa máy chủ trong một khoảng thời gian nhất định, có thể "
        "được ghi vào bản sao lưu, có thể xuất hiện trong nhật ký hệ thống, có "
        "thể bị lộ nếu máy chủ bị xâm nhập. Thêm vào đó, mô hình này đặt ra chi "
        "phí vận hành tỉ lệ thuận với lượng sử dụng, dẫn tới các giới hạn về "
        "dung lượng và số lần dùng, và hoàn toàn không hoạt động khi không có "
        "kết nối."
    )
    r.p(
        "Mô hình xử lý phía máy khách đảo ngược cách bố trí. Toàn bộ mã xử lý "
        "được tải về máy người dùng một lần, sau đó tệp được đọc, biến đổi và "
        "ghi ra hoàn toàn trong tiến trình cục bộ. Không có yêu cầu mạng nào "
        "mang theo nội dung tài liệu. Ưu điểm là tính riêng tư mang tính cấu "
        "trúc chứ không phải tính riêng tư dựa trên cam kết: người dùng có thể "
        "tự kiểm chứng bằng cách ngắt mạng và quan sát rằng ứng dụng vẫn hoạt "
        "động bình thường. Chi phí vận hành gần như bằng không vì không có máy "
        "chủ xử lý, do đó không cần đặt giới hạn sử dụng."
    )
    r.p(
        "Đổi lại, mô hình này phải chấp nhận ba ràng buộc. Thứ nhất, năng lực "
        "xử lý bị giới hạn bởi máy người dùng, đặc biệt là bộ nhớ khả dụng của "
        "môi trường thực thi. Thứ hai, khối lượng mã và tài nguyên phải tải về "
        "hoặc đóng gói theo ứng dụng là rất lớn, vì các thư viện xử lý tài liệu "
        "vốn nặng. Thứ ba, mã xử lý nằm trong tay người dùng, nên mọi bí mật "
        "nhúng trong mã đều không còn là bí mật — điều này ảnh hưởng tới cách "
        "thiết kế những tính năng cần truy cập dịch vụ bên ngoài. Ba ràng buộc "
        "này định hình phần lớn các quyết định kỹ thuật được trình bày ở "
        "Chương 2 và Chương 3."
    )

    r.h3("1.4. WebAssembly và việc đưa thư viện xử lý tài liệu vào máy khách")
    r.p(
        "WebAssembly là định dạng chỉ thị nhị phân dành cho một máy ảo dạng "
        "ngăn xếp, được thiết kế làm đích biên dịch cho các ngôn ngữ như C, "
        "C++, Rust, OCaml hay Go. Mã WebAssembly được nạp và biên dịch nhanh, "
        "chạy trong hộp cát với tốc độ tiệm cận mã máy, và có mô hình bộ nhớ "
        "tuyến tính rõ ràng. Chính hai đặc điểm — hiệu năng cao và cách ly "
        "chặt — khiến WebAssembly trở thành nền tảng khả thi để đưa các thư "
        "viện xử lý tài liệu vốn chỉ chạy trên máy chủ vào môi trường máy "
        "khách."
    )
    r.p(
        "Việc chuyển một thư viện gốc sang WebAssembly thường được thực hiện "
        "bằng bộ công cụ Emscripten. Bộ công cụ này không chỉ biên dịch mã máy "
        "mà còn mô phỏng những thứ mà thư viện gốc trông đợi ở hệ điều hành, "
        "quan trọng nhất là hệ tệp. Emscripten cung cấp một hệ tệp ảo trong bộ "
        "nhớ, thường gọi là MEMFS, cho phép chương trình gọi các hàm mở, đọc, "
        "ghi tệp như bình thường trong khi thực tế mọi thứ chỉ nằm trong bộ nhớ "
        "của tiến trình. Khuôn mẫu sử dụng vì vậy rất đặc trưng: ghi dữ liệu "
        "đầu vào vào một đường dẫn ảo, gọi hàm chính của chương trình với tham "
        "số dòng lệnh, rồi đọc kết quả từ một đường dẫn ảo khác."
    )
    r.p(
        "Khuôn mẫu này có một hệ quả quan trọng về quản lý tài nguyên: hệ tệp "
        "ảo không được thu gom tự động. Nếu chương trình gọi liên tiếp nhiều "
        "thao tác mà không xoá tệp ảo cũ, bộ nhớ của mô-đun sẽ tăng dần cho tới "
        "khi vượt giới hạn. Tương tự, các thư viện cấp phát đối tượng trong bộ "
        "nhớ tuyến tính của WebAssembly thường yêu cầu giải phóng tường minh "
        "bằng một hàm huỷ do chính thư viện cung cấp. Đây là điểm khác biệt lớn "
        "so với lập trình JavaScript thông thường và là nguồn gốc của nhiều lỗi "
        "rò rỉ bộ nhớ trong các ứng dụng dạng này."
    )
    r.p(
        "Một số mô-đun WebAssembly cần đa luồng để đạt hiệu năng chấp nhận "
        "được. Đa luồng trong môi trường web dựa trên đối tượng "
        "SharedArrayBuffer, và vì lý do an toàn trước các tấn công kênh phụ, "
        "trình duyệt chỉ cho phép sử dụng đối tượng này khi trang được đặt "
        "trong trạng thái cách ly nguồn gốc chéo. Trạng thái đó yêu cầu máy chủ "
        "gửi kèm hai tiêu đề Cross-Origin-Opener-Policy và "
        "Cross-Origin-Embedder-Policy với giá trị phù hợp. Với ứng dụng "
        "desktop, hai tiêu đề này phải được khung nền đặt cho giao thức phục vụ "
        "tài nguyên nội bộ."
    )
    r.p(
        "Một hướng phát triển đáng chú ý là việc đưa cả một môi trường thực thi "
        "ngôn ngữ bậc cao vào WebAssembly. Pyodide là ví dụ tiêu biểu: nó biên "
        "dịch trình thông dịch CPython cùng thư viện chuẩn sang WebAssembly, "
        "kèm cơ chế nạp các gói mở rộng đã được biên dịch sẵn dưới dạng bánh xe "
        "nhị phân. Nhờ đó, những thư viện xử lý tài liệu và xử lý ảnh mạnh của "
        "hệ sinh thái Python có thể chạy trong môi trường máy khách. Cái giá "
        "phải trả là dung lượng: một môi trường như vậy dễ dàng chiếm hàng chục "
        "megabyte, và thời gian khởi tạo lần đầu đáng kể, buộc ứng dụng phải "
        "lưu lại thể hiện đã khởi tạo để tái sử dụng."
    )
    r.p(
        "Cuối cùng, cần lưu ý rằng WebAssembly chạy trên luồng chính sẽ làm "
        "đóng băng giao diện trong suốt thời gian tính toán. Với các thao tác "
        "kéo dài, giải pháp là chuyển việc tính toán vào Web Worker — một luồng "
        "thực thi riêng, giao tiếp với luồng chính bằng cơ chế truyền thông "
        "điệp. Khi truyền dữ liệu lớn giữa hai luồng, việc chuyển quyền sở hữu "
        "bộ đệm thay vì sao chép là bắt buộc nếu không muốn nhân đôi bộ nhớ "
        "tiêu thụ."
    )

    r.h3("1.5. Kiến trúc ứng dụng desktop lai và khung nền Tauri")
    r.p(
        "Ứng dụng desktop lai là loại ứng dụng có giao diện xây dựng bằng công "
        "nghệ web nhưng được đóng gói và phân phối như phần mềm cài đặt thông "
        "thường. Kiến trúc chung gồm hai phần: một tiến trình bản địa quản lý "
        "cửa sổ, vòng đời ứng dụng và các quyền hệ thống; và một thành phần "
        "hiển thị web chịu trách nhiệm kết xuất giao diện. Hai phần trao đổi "
        "với nhau qua một kênh truyền thông liên tiến trình."
    )
    r.p(
        "Có hai trường phái hiện thực. Trường phái thứ nhất, tiêu biểu là "
        "Electron, đóng gói kèm một bản Chromium và một môi trường Node.js đầy "
        "đủ. Ưu điểm là hành vi kết xuất hoàn toàn đồng nhất trên mọi hệ điều "
        "hành và lập trình viên có ngay toàn bộ năng lực của Node.js. Nhược "
        "điểm là dung lượng gói cài đặt rất lớn, tiêu thụ bộ nhớ cao và bề mặt "
        "tấn công rộng do mã giao diện có thể chạm tới các API hệ thống."
    )
    r.p(
        "Trường phái thứ hai, tiêu biểu là Tauri, sử dụng thành phần WebView "
        "sẵn có của hệ điều hành: WebKitGTK trên Linux, WKWebView trên macOS và "
        "WebView2 trên Windows. Tiến trình bản địa được viết bằng Rust và chỉ "
        "phơi bày ra cho tầng web đúng những lệnh mà lập trình viên khai báo "
        "tường minh. Ưu điểm là phần lõi nhị phân rất nhỏ, tiêu thụ tài nguyên "
        "thấp, và mô hình quyền theo nguyên tắc đặc quyền tối thiểu: nếu một "
        "khả năng không được khai báo trong tệp mô tả quyền thì tầng web không "
        "thể gọi tới, kể cả khi mã giao diện bị chèn mã độc. Nhược điểm là hành "
        "vi kết xuất có thể khác biệt nhỏ giữa các hệ điều hành do dùng ba bộ "
        "máy trình duyệt khác nhau, và việc biên dịch gói cài đặt cho mỗi hệ "
        "điều hành phải thực hiện trên chính hệ điều hành đó."
    )
    r.p(
        "Đối với bài toán của đề tài, trường phái thứ hai phù hợp hơn hẳn vì ba "
        "lý do. Thứ nhất, ứng dụng đã phải đóng gói kèm hơn một trăm megabyte "
        "mô-đun WebAssembly, nên việc thêm hàng trăm megabyte cho một bản "
        "Chromium riêng là không hợp lý. Thứ hai, và quan trọng hơn, đề tài đặt "
        "yêu cầu cao về bảo vệ dữ liệu; mô hình quyền theo khai báo cho phép "
        "chứng minh bằng cấu hình rằng tầng giao diện không có quyền truy cập "
        "hệ tệp. Thứ ba, toàn bộ logic xử lý đã chạy được trong môi trường web "
        "nên không cần tới năng lực của Node.js ở phía bản địa; tiến trình bản "
        "địa chỉ còn nhiệm vụ mở cửa sổ và hiển thị hộp thoại lưu tệp."
    )

    r.h3("1.6. Bảo vệ dữ liệu và an toàn thông tin trong xử lý tài liệu cục bộ")
    r.p(
        "Khi hệ thống không có máy chủ, mô hình mối đe doạ thay đổi căn bản. "
        "Những rủi ro quen thuộc của ứng dụng web — chiếm quyền phiên làm việc, "
        "chèn câu lệnh cơ sở dữ liệu, leo thang đặc quyền trên máy chủ, lộ dữ "
        "liệu từ bản sao lưu — đều không còn ý nghĩa vì không tồn tại thành "
        "phần tương ứng. Bù lại, xuất hiện những rủi ro khác cần được xử lý "
        "một cách có hệ thống."
    )
    r.p(
        "Rủi ro thứ nhất là nội dung độc hại nằm trong chính tài liệu đầu vào. "
        "Tài liệu do người dùng mở có thể chứa mã kịch bản, tên tệp được dựng "
        "cố ý để chèn mã, siêu dữ liệu chứa chuỗi tấn công, hoặc nội dung "
        "Markdown và HTML được nhúng. Nếu ứng dụng hiển thị những nội dung này "
        "bằng cách gán trực tiếp vào cây tài liệu của giao diện, mã độc sẽ được "
        "thực thi trong ngữ cảnh của ứng dụng. Trong một ứng dụng desktop lai, "
        "hậu quả nghiêm trọng hơn ứng dụng web thông thường vì ngữ cảnh đó có "
        "thể gọi tới các lệnh bản địa được khai báo. Biện pháp phòng ngừa gồm "
        "hai lớp: làm sạch mọi nội dung do tệp cung cấp trước khi hiển thị, và "
        "giới hạn tối đa số lệnh bản địa được phơi bày."
    )
    r.p(
        "Rủi ro thứ hai là nguồn gốc của mã thực thi. Một ứng dụng xử lý tài "
        "liệu phía máy khách phải nạp nhiều mô-đun WebAssembly kích thước lớn. "
        "Nếu địa chỉ nạp các mô-đun này có thể bị thay đổi — chẳng hạn thông "
        "qua một giá trị cấu hình lưu trong bộ nhớ cục bộ của trình duyệt — thì "
        "kẻ tấn công có thể khiến ứng dụng nạp và thực thi mã tuỳ ý. Biện pháp "
        "phòng ngừa là duy trì danh sách máy chủ tin cậy và từ chối mọi địa chỉ "
        "nằm ngoài danh sách đó, đồng thời chủ động loại bỏ các giá trị đáng "
        "ngờ đã được lưu từ trước."
    )
    r.p(
        "Rủi ro thứ ba là dữ liệu còn sót lại. Trong quá trình xử lý, tài liệu "
        "tồn tại ở nhiều dạng trung gian: bộ đệm nhị phân, ảnh kết xuất trên "
        "canvas, tệp trong hệ tệp ảo của mô-đun WebAssembly, đối tượng tài liệu "
        "trong bộ nhớ của thư viện. Nếu những dạng trung gian này không được "
        "giải phóng đúng lúc, chúng vừa gây tiêu tốn bộ nhớ vừa kéo dài thời "
        "gian nội dung nhạy cảm nằm trong không gian địa chỉ của tiến trình. "
        "Nguyên tắc thiết kế cần tuân thủ là: không ghi tệp tạm ra đĩa, và giải "
        "phóng tường minh mọi vùng dữ liệu trung gian ngay khi không còn dùng "
        "tới, kể cả trên nhánh xử lý lỗi."
    )
    r.p(
        "Rủi ro thứ tư liên quan tới các tính năng buộc phải kết nối mạng. Ký "
        "số với dấu thời gian tin cậy đòi hỏi liên hệ với một máy chủ cấp dấu "
        "thời gian; một số chứng thư số yêu cầu tải chuỗi chứng thư từ địa chỉ "
        "ghi trong phần mở rộng của chứng thư. Nguyên tắc xử lý là cô lập: các "
        "tính năng này phải là tuỳ chọn, chỉ chạy khi người dùng chủ động kích "
        "hoạt, và phải được nêu rõ trong tài liệu để người dùng biết chính xác "
        "khi nào ứng dụng chạm tới mạng. Ngoài ra, cần lưu ý rằng khoá riêng "
        "dùng để ký chỉ được phép tồn tại trong bộ nhớ của tiến trình và không "
        "bao giờ được gửi đi."
    )
    r.p(
        "Cuối cùng, cần phân biệt rõ giữa che giấu và xoá bỏ. Khi người dùng "
        "yêu cầu che một đoạn thông tin nhạy cảm, nếu công cụ chỉ vẽ một hình "
        "chữ nhật đen lên trên thì văn bản gốc vẫn còn trong luồng nội dung và "
        "có thể được trích ra bằng bất kỳ công cụ nào. Việc che thông tin đúng "
        "cách phải loại bỏ dữ liệu khỏi tệp. Tương tự, việc gỡ siêu dữ liệu "
        "phải xử lý cả từ điển thông tin tài liệu lẫn luồng siêu dữ liệu XMP, "
        "và việc làm sạch tài liệu phải tính tới mã kịch bản, tệp nhúng, chú "
        "thích, liên kết và cây cấu trúc."
    )

    r.h2("2. Cơ sở thực tiễn")

    r.h3("2.1. Thực trạng sử dụng công cụ xử lý PDF và rủi ro đi kèm")
    r.p(
        "Trong thực tế công tác hiện nay, nhu cầu xử lý tài liệu PDF phát sinh "
        "hằng ngày ở hầu hết vị trí công việc. Cán bộ văn phòng ghép các bản "
        "quét thành hồ sơ hoàn chỉnh, tách phụ lục để gửi riêng cho từng bộ "
        "phận, giảm dung lượng tệp để gửi qua hệ thống thư điện tử có giới hạn "
        "kích thước. Giảng viên và nghiên cứu viên chuyển đổi tài liệu giữa các "
        "định dạng, trích xuất bảng số liệu, đánh số trang cho bản thảo, gộp "
        "các chương thành một tài liệu thống nhất. Bộ phận pháp chế và nhân sự "
        "đặt mật khẩu cho tài liệu nội bộ, che thông tin cá nhân trước khi công "
        "bố, ký số văn bản điện tử."
    )
    r.p(
        "Khảo sát cách thức thực hiện những công việc này cho thấy ba nhóm "
        "hành vi phổ biến. Nhóm thứ nhất sử dụng dịch vụ trực tuyến miễn phí — "
        "cách làm nhanh nhất, không cần cài đặt, nhưng đồng nghĩa với việc đưa "
        "tài liệu ra khỏi tổ chức. Nhóm thứ hai sử dụng phần mềm thương mại "
        "được cấp phép, an toàn về mặt dữ liệu nhưng chi phí cao và thường chỉ "
        "được trang bị cho một số máy nhất định, dẫn tới hiện tượng dồn việc "
        "vào những máy đó. Nhóm thứ ba sử dụng tổ hợp nhiều công cụ miễn phí "
        "nhỏ lẻ, mỗi công cụ cho một việc, gây khó khăn cho việc chuẩn hoá và "
        "hỗ trợ kỹ thuật."
    )
    r.p(
        "Rủi ro lớn nhất nằm ở nhóm hành vi thứ nhất, và điểm đáng chú ý là "
        "phần lớn người dùng không nhận thức được rằng hành vi kéo tệp vào một "
        "trang web đã là hành vi truyền dữ liệu ra ngoài. Đối với tài liệu chứa "
        "thông tin cá nhân, số liệu chưa công bố, nội dung hợp đồng hoặc tài "
        "liệu có yêu cầu bảo mật, hậu quả có thể rất nghiêm trọng và thường chỉ "
        "được phát hiện muộn. Ngay cả khi nhà cung cấp dịch vụ tuân thủ đúng "
        "cam kết xoá tệp, việc dữ liệu đã đi qua một hạ tầng không thuộc quyền "
        "kiểm soát của tổ chức đã đủ để vi phạm nhiều quy định nội bộ."
    )
    r.p(
        "Bên cạnh rủi ro về dữ liệu, các dịch vụ trực tuyến còn tạo ra ba bất "
        "tiện thực tế. Thứ nhất là giới hạn sử dụng: dung lượng tệp tối đa, số "
        "lần xử lý mỗi ngày, số tệp mỗi lần thao tác. Thứ hai là sự phụ thuộc "
        "vào chất lượng đường truyền: với tệp hàng trăm megabyte, thời gian tải "
        "lên và tải xuống thường vượt xa thời gian xử lý thực sự. Thứ ba là "
        "tính không sẵn sàng: khi mạng gián đoạn hoặc khi làm việc trong môi "
        "trường mạng tách biệt, người dùng hoàn toàn không thể thực hiện được "
        "những thao tác đơn giản nhất."
    )

    r.h3("2.2. Nhu cầu xử lý tài liệu trong môi trường hạn chế kết nối")
    r.p(
        "Một bộ phận đáng kể môi trường làm việc có yêu cầu hạn chế hoặc kiểm "
        "soát chặt kết nối ra ngoài. Đó có thể là mạng nội bộ tách biệt hoàn "
        "toàn, mạng có kiểm soát luồng ra qua tường lửa và danh sách cho phép, "
        "hoặc chính sách nội bộ cấm sử dụng dịch vụ đám mây cho tài liệu công "
        "việc. Trong những môi trường như vậy, mọi giải pháp dựa trên dịch vụ "
        "trực tuyến đều bị loại bỏ ngay từ đầu, và nhu cầu về một công cụ xử lý "
        "tài liệu chạy hoàn toàn cục bộ trở nên bức thiết."
    )
    r.p(
        "Yêu cầu “chạy hoàn toàn cục bộ” trong bối cảnh này cần được hiểu "
        "nghiêm ngặt. Không chỉ là việc phần mềm được cài trên máy, mà là việc "
        "phần mềm không phát sinh bất kỳ yêu cầu mạng nào trong quá trình sử "
        "dụng bình thường. Nhiều phần mềm hiện nay tuy cài trên máy nhưng vẫn "
        "tải tài nguyên từ mạng phân phối nội dung khi khởi động, gửi dữ liệu "
        "đo đạc sử dụng, hoặc kiểm tra bản quyền trực tuyến — tất cả đều là "
        "những hành vi không chấp nhận được trong môi trường tách biệt. Vì vậy "
        "khả năng kiểm chứng độc lập, chẳng hạn bằng cách ngắt mạng hoặc quan "
        "sát nhật ký kết nối, là một yêu cầu chức năng thực sự chứ không phải "
        "một điểm cộng."
    )
    r.p(
        "Từ yêu cầu này phát sinh một ràng buộc kỹ thuật rất cụ thể: toàn bộ "
        "tài nguyên mà phần mềm cần trong quá trình chạy — mã xử lý, mô-đun "
        "WebAssembly, dữ liệu ngôn ngữ cho nhận dạng ký tự, phông chữ, tài "
        "nguyên giao diện — phải được đóng gói sẵn trong gói cài đặt. Điều này "
        "làm dung lượng gói cài đặt tăng lên đáng kể, và đây là một sự đánh đổi "
        "có ý thức: chấp nhận gói cài đặt lớn để đổi lấy khả năng hoạt động độc "
        "lập hoàn toàn."
    )

    r.h3("2.3. Khó khăn khi xây dựng công cụ xử lý PDF chạy cục bộ")
    r.p(
        "Xây dựng một hệ thống xử lý PDF phía máy khách gặp một số khó khăn đặc "
        "thù mà mô hình máy chủ không có. Khó khăn thứ nhất là sự phân tán của "
        "năng lực xử lý. Như đã phân tích ở mục 1.1, không tồn tại một thư viện "
        "duy nhất phủ được toàn bộ nhu cầu. Thư viện thao tác cấu trúc trang "
        "thường không xử lý được nội dung; thư viện kết xuất thường không sửa "
        "được cấu trúc; thư viện mã hoá thường không hiểu bố cục. Hệ thống vì "
        "vậy buộc phải tích hợp nhiều thư viện và phải có cơ chế điều phối để "
        "chọn đúng thư viện cho từng thao tác, đồng thời phải xử lý được trường "
        "hợp một thư viện thất bại và cần chuyển sang thư viện khác."
    )
    r.p(
        "Khó khăn thứ hai là quản lý bộ nhớ. Môi trường thực thi web có giới "
        "hạn bộ nhớ chặt hơn tiến trình bản địa, trong khi tài liệu PDF có thể "
        "rất lớn. Việc kết xuất một trang khổ A0 ở độ phân giải cao có thể sinh "
        "ra một canvas chiếm hàng trăm megabyte. Việc nạp một tài liệu năm trăm "
        "trang vào cả pdf.js lẫn pdf-lib đồng thời sẽ nhân đôi lượng bộ nhớ "
        "tiêu thụ. Vì vậy, mỗi thao tác phải được thiết kế với ý thức rõ ràng "
        "về vòng đời của từng vùng dữ liệu, và phải có điểm giải phóng tường "
        "minh."
    )
    r.p(
        "Khó khăn thứ ba là trải nghiệm người dùng trong các thao tác kéo dài. "
        "Nhận dạng ký tự quang học trên một tài liệu vài chục trang có thể mất "
        "nhiều phút. Nếu tính toán chạy trên luồng chính, giao diện sẽ đóng "
        "băng và người dùng sẽ nghĩ ứng dụng bị treo. Giải pháp gồm hai phần: "
        "chuyển tính toán nặng vào luồng riêng khi có thể, và luôn cập nhật "
        "trạng thái tiến trình cho người dùng thấy công việc vẫn đang tiến "
        "triển."
    )
    r.p(
        "Khó khăn thứ tư là số lượng công cụ. Một hệ thống muốn thay thế được "
        "thói quen dùng dịch vụ trực tuyến phải có hơn một trăm công cụ. Nếu "
        "mỗi công cụ được viết theo một cách riêng, chi phí bảo trì sẽ vượt quá "
        "khả năng của đội phát triển. Vì vậy tính khuôn mẫu của kiến trúc — một "
        "khuôn mẫu chung cho trang giao diện, một khuôn mẫu chung cho mô-đun "
        "nghiệp vụ, một tập tiện ích dùng chung — trở thành yếu tố quyết định "
        "khả năng tồn tại lâu dài của hệ thống."
    )
    r.p(
        "Khó khăn thứ năm là sự khác biệt giữa các bộ máy trình duyệt. Vì ứng "
        "dụng dùng WebView của hệ điều hành, cùng một đoạn mã có thể cho kết "
        "quả kết xuất hơi khác nhau trên WebKitGTK, WKWebView và WebView2. Sự "
        "khác biệt thường nhỏ và nằm ở phần hiển thị, nhưng cũng có trường hợp "
        "ảnh hưởng tới chức năng, chẳng hạn khả năng hỗ trợ một định dạng ảnh "
        "hoặc một tính năng canvas. Điều này đòi hỏi phải kiểm thử trên cả ba "
        "hệ điều hành trước khi phát hành."
    )

    r.h3("2.4. Công nghệ và thư viện sử dụng trong xây dựng hệ thống")
    r.p(
        "Trên cơ sở phân tích ở các mục trên, hệ thống được xây dựng với tập "
        "công nghệ sau. Tầng giao diện dùng TypeScript biên dịch bằng Vite, "
        "tạo kiểu bằng Tailwind CSS, tổ chức theo mô hình đa trang trong đó mỗi "
        "công cụ là một trang HTML độc lập kèm một mô-đun nghiệp vụ riêng. Việc "
        "chọn mô hình đa trang thay vì ứng dụng một trang là một quyết định có "
        "chủ ý: nó cho phép mỗi công cụ chỉ tải đúng phần mã và thư viện mà nó "
        "cần, thay vì buộc người dùng tải toàn bộ hơn một trăm công cụ chỉ để "
        "dùng một thao tác ghép tệp."
    )
    r.p(
        "Tầng vỏ bản địa dùng Tauri phiên bản 2 với mã Rust. Tiến trình bản địa "
        "chỉ đảm nhiệm hai việc: tạo cửa sổ ứng dụng với các tiêu đề cách ly "
        "nguồn gốc cần thiết, và cung cấp đúng một lệnh cho tầng web để hiển "
        "thị hộp thoại lưu tệp của hệ điều hành rồi ghi dữ liệu ra đường dẫn "
        "người dùng chọn. Tầng xử lý tài liệu là tập hợp các thư viện JavaScript "
        "và WebAssembly, được trình bày tóm tắt trong Bảng 1.1."
    )
    r.table(
        "Bảng 1.1. Các thư viện xử lý tài liệu được tích hợp và vai trò của "
        "từng thư viện",
        ["Thư viện", "Dạng", "Vai trò trong hệ thống"],
        [
            ["pdf-lib (kèm @pdf-lib/fontkit)", "JavaScript",
             "Đọc và ghi cấu trúc PDF: xoay, xoá, trích trang, đóng dấu chìm, "
             "đánh số trang, đầu/chân trang, gộp trang, làm phẳng biểu mẫu, "
             "nhúng phông và vẽ lớp văn bản cho kết quả OCR"],
            ["pdf.js (pdfjs-dist)", "JavaScript",
             "Kết xuất trang ra canvas phục vụ xem trước, sinh ảnh thu nhỏ, "
             "chuyển PDF sang ảnh, trích văn bản và phát hiện tài liệu có mật "
             "khẩu"],
            ["qpdf (qpdf-wasm)", "WebAssembly",
             "Mã hoá AES-256, giải mã, đặt quyền sử dụng, tuyến tính hoá và "
             "sửa chữa tệp"],
            ["CoherentPDF", "JavaScript sinh từ OCaml",
             "Ghép tệp có giữ nhãn trang, tách theo bookmark, sinh mục lục, "
             "chuyển đổi PDF ↔ JSON, quản lý tệp đính kèm và bookmark"],
            ["PyMuPDF trên nền Pyodide", "WebAssembly",
             "Nén ảnh nhúng, chuyển PDF sang văn bản/Markdown/SVG/DOCX, trích "
             "ảnh và bảng, chuyển sách điện tử sang PDF, khử nghiêng trang quét"],
            ["Ghostscript", "WebAssembly",
             "Chuyển đổi sang PDF/A và chuyển phông chữ thành đường nét vector"],
            ["Tesseract.js", "WebAssembly",
             "Nhận dạng ký tự quang học, trả về văn bản và dữ liệu hOCR chứa "
             "toạ độ từng từ"],
            ["wasm-vips, heic2any, utif, tiff", "JS + WebAssembly",
             "Giải mã và biến đổi các định dạng ảnh ngoài luồng phổ thông như "
             "HEIC, TIFF, PSD"],
            ["LibreOffice-WASM", "WebAssembly",
             "Chuyển tài liệu văn phòng (DOCX, XLSX, PPTX, ODF, RTF, WPD, WPS, "
             "PUB, VSD) sang PDF"],
            ["zgapdfsigner, node-forge", "JavaScript",
             "Ký số theo chuẩn X.509 từ chứng thư PFX hoặc PEM, đóng dấu thời "
             "gian theo RFC 3161 và kiểm tra chữ ký"],
            ["PDFKit, jsPDF, jspdf-autotable", "JavaScript",
             "Sinh tài liệu PDF mới từ văn bản, Markdown, CSV, JSON và XML"],
            ["EmbedPDF (pdfium)", "WebAssembly",
             "Trình xem và chú thích tài liệu tích hợp trong công cụ soạn thảo"],
            ["Rete.js và các trình cắm", "JavaScript",
             "Trình soạn thảo đồ thị trực quan cho tính năng xây dựng luồng xử "
             "lý tự động"],
            ["DOMPurify", "JavaScript",
             "Làm sạch nội dung HTML do tệp cung cấp trước khi hiển thị"],
        ],
        widths=[4, 3, 9],
        font_size=11,
    )
    r.p(
        "Danh sách trên cho thấy rõ tính phân tán của năng lực xử lý đã nêu ở "
        "mục 2.3: bốn thư viện khác nhau cùng thao tác trên tệp PDF nhưng ở "
        "những khía cạnh không giao nhau, và việc chọn thư viện nào cho thao "
        "tác nào là một quyết định thiết kế được trình bày chi tiết ở Chương 2."
    )

    r.h3("2.5. Căn cứ về giấy phép và yêu cầu tuân thủ")
    r.p(
        "Hệ thống được phát triển trên cơ sở dự án nguồn mở BentoPDF, được cấp "
        "phép theo AGPL-3.0. Bản desktop bổ sung phần vỏ ứng dụng bằng Tauri, "
        "cấu trúc giao diện dạng không gian làm việc có thanh bên, cơ chế đa "
        "ngữ với tiếng Việt mặc định và toàn bộ hạ tầng đóng gói ngoại tuyến. "
        "Việc kế thừa một dự án nguồn mở kèm theo nghĩa vụ tuân thủ giấy phép: "
        "giữ nguyên thông tin ghi công của tác giả gốc, công bố mã nguồn của "
        "bản phái sinh theo cùng điều khoản, và không được đổi sang giấy phép "
        "hạn chế hơn."
    )
    r.p(
        "Một điểm cần lưu ý về mặt giấy phép là ba thư viện xử lý quan trọng — "
        "PyMuPDF, Ghostscript và CoherentPDF — đều được cấp phép AGPL-3.0. Kho "
        "mã nguồn không nhúng trực tiếp mã của các thư viện này mà cấu hình sẵn "
        "địa chỉ nạp chúng; bản web nạp từ mạng phân phối nội dung, còn bản "
        "desktop đóng gói bản sao cục bộ để chạy ngoại tuyến. Cách tổ chức này "
        "giúp phân tách rõ ràng ranh giới giấy phép và cho phép người triển "
        "khai lựa chọn nguồn cung cấp phù hợp với chính sách của mình."
    )
    r.p(
        "Về yêu cầu tuân thủ trong sử dụng, do hệ thống không thu thập, không "
        "truyền và không lưu trữ dữ liệu người dùng ở bất kỳ máy chủ nào, phần "
        "lớn nghĩa vụ liên quan tới bảo vệ dữ liệu cá nhân được đáp ứng một "
        "cách tự nhiên bởi chính kiến trúc. Không tồn tại cơ sở dữ liệu chứa "
        "thông tin người dùng, không tồn tại nhật ký truy cập phía máy chủ, "
        "không tồn tại cơ chế theo dõi hành vi. Điều này đơn giản hoá đáng kể "
        "việc đưa hệ thống vào sử dụng trong các tổ chức có quy định nghiêm "
        "ngặt về dữ liệu."
    )
    r.p(
        "Tuy nhiên, cần nêu rõ hai điểm mà người triển khai phải lưu ý. Thứ "
        "nhất, hai tính năng tuỳ chọn có phát sinh kết nối ra ngoài là đóng dấu "
        "thời gian tin cậy và tải phông chữ theo yêu cầu; tổ chức có chính sách "
        "mạng nghiêm ngặt cần biết trước điều này để quyết định có cho phép hay "
        "không. Thứ hai, các gói cài đặt hiện chưa được ký số, nên hệ điều hành "
        "sẽ cảnh báo ở lần chạy đầu tiên; việc bổ sung chứng thư ký mã là một "
        "yêu cầu cần thực hiện trước khi phân phối rộng rãi."
    )

    r.h2("Kết luận chương 1")
    r.p(
        "Chương 1 đã hệ thống hoá cơ sở khoa học và thực tiễn làm nền cho các "
        "quyết định thiết kế ở những chương sau. Về mặt lý luận, chương đã phân "
        "tích đặc điểm cấu trúc của định dạng PDF và chỉ ra rằng chính cách tổ "
        "chức hướng kết xuất của định dạng này là nguyên nhân khiến các thao "
        "tác xử lý phải chia thành ba mức can thiệp với độ khó rất khác nhau, "
        "và khiến không một thư viện đơn lẻ nào phủ được toàn bộ nhu cầu."
    )
    r.p(
        "Chương cũng đã so sánh hai mô hình xử lý tài liệu và làm rõ rằng ưu "
        "thế của mô hình phía máy khách không nằm ở hiệu năng mà nằm ở tính "
        "riêng tư mang tính cấu trúc: người dùng có thể tự kiểm chứng thay vì "
        "phải tin vào cam kết. Đổi lại, mô hình này phải chấp nhận ba ràng buộc "
        "về bộ nhớ, về dung lượng tài nguyên và về việc mã xử lý nằm trong tay "
        "người dùng — ba ràng buộc định hình toàn bộ thiết kế được trình bày ở "
        "Chương 2."
    )
    r.p(
        "Về công nghệ nền, chương đã phân tích khả năng và giới hạn của "
        "WebAssembly trong việc đưa thư viện xử lý tài liệu vào máy khách, đặc "
        "biệt là khuôn mẫu hệ tệp ảo, yêu cầu giải phóng bộ nhớ tường minh và "
        "điều kiện cách ly nguồn gốc để bật đa luồng. Chương cũng đã so sánh "
        "hai trường phái ứng dụng desktop lai và lập luận vì sao mô hình dùng "
        "WebView hệ thống với mô hình quyền theo khai báo phù hợp hơn với bài "
        "toán đặt ra."
    )
    r.p(
        "Về mặt thực tiễn, chương đã khảo sát thực trạng sử dụng công cụ xử lý "
        "PDF hiện nay, chỉ ra ba nhóm hành vi phổ biến cùng rủi ro và bất tiện "
        "của từng nhóm, phân tích nhu cầu trong môi trường hạn chế kết nối, "
        "liệt kê năm khó khăn đặc thù khi xây dựng công cụ xử lý PDF chạy cục "
        "bộ, giới thiệu tập thư viện được tích hợp và làm rõ các căn cứ về "
        "giấy phép cùng yêu cầu tuân thủ. Những nội dung này là đầu vào trực "
        "tiếp cho việc phân tích yêu cầu và thiết kế hệ thống ở Chương 2."
    )
