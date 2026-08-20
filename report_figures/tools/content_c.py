# -*- coding: utf-8 -*-
"""Chương 3 — Xây dựng và triển khai hệ thống."""


def build(r):
    r.h1("CHƯƠNG 3. XÂY DỰNG VÀ TRIỂN KHAI HỆ THỐNG")

    # ==================================================================
    r.h2("1. Môi trường và công nghệ triển khai")

    r.h3("1.1. Môi trường phát triển và cấu trúc mã nguồn")
    r.p(
        "Môi trường phát triển của hệ thống gồm hai chuỗi công cụ độc lập chạy "
        "song song. Chuỗi thứ nhất phục vụ tầng web: Node.js phiên bản 20 trở "
        "lên, trình quản lý gói npm, trình biên dịch TypeScript, bộ dựng Vite "
        "và khung kiểm thử Vitest. Chuỗi thứ hai phục vụ tầng bản địa: trình "
        "biên dịch Rust từ phiên bản 1.77.2 trở lên cùng công cụ dòng lệnh của "
        "Tauri. Hai chuỗi này gặp nhau ở bước cuối, khi Cargo nhúng kết quả "
        "dựng của Vite vào nhị phân."
    )
    r.p(
        "Ngoài hai chuỗi công cụ trên, mỗi hệ điều hành đòi hỏi một tập phụ "
        "thuộc hệ thống riêng để biên dịch được thành phần WebView. Trên Linux "
        "cần các gói phát triển của WebKitGTK 4.1, libsoup 3.0, librsvg2, "
        "libappindicator3 và tiện ích patchelf. Trên Windows cần bộ công cụ "
        "biên dịch của Visual Studio với gói phát triển C++ cùng thời gian chạy "
        "WebView2. Trên macOS cần công cụ dòng lệnh của Xcode. Hình 3.1 trình "
        "bày cấu trúc mã nguồn và các thành phần môi trường."
    )
    r.figure(
        "fig_3_1_source_tree",
        "Hình 3.1. Cấu trúc mã nguồn và môi trường phát triển của hệ thống",
    )
    r.p(
        "Về khối lượng mã, thư mục logic là khối lớn nhất với 47.499 dòng "
        "TypeScript chia cho 132 mô-đun, trung bình khoảng 360 dòng cho mỗi "
        "công cụ. Thư mục tiện ích có 9.281 dòng chia cho 43 mô-đun. Thư mục "
        "luồng xử lý tự động có 8.484 dòng, phần lớn nằm ở 79 lớp nút. Thư mục "
        "so sánh tài liệu có 2.897 dòng. Thư mục kiểm thử có 9.208 dòng. Tổng "
        "cộng mã TypeScript của dự án khoảng 85.570 dòng. Phần HTML của các "
        "trang công cụ chiếm khoảng 59.236 dòng, chủ yếu là đánh dấu giao diện "
        "và thẻ siêu dữ liệu."
    )
    r.p(
        "Sự chênh lệch rất lớn giữa 85.570 dòng TypeScript và khoảng năm mươi "
        "dòng Rust là con số phản ánh rõ nhất triết lý kiến trúc đã trình bày "
        "ở Chương 2: tầng bản địa được giữ ở mức tối thiểu tuyệt đối, chỉ đảm "
        "nhiệm những việc mà môi trường web không thể làm."
    )
    r.p(
        "Thư mục cấu hình chứa một số tệp đáng chú ý. Tệp cấu hình Vite dài 802 "
        "dòng, phần lớn là danh sách 131 điểm vào HTML được khai báo tường "
        "minh, cùng bốn trình cắm tuỳ chỉnh xử lý định tuyến theo ngôn ngữ, làm "
        "phẳng đường dẫn trang, viết lại đường dẫn tài nguyên và sao chép tệp "
        "tĩnh. Tệp cấu hình ESLint bật hai bộ luật an toàn. Thư mục kịch bản "
        "chứa 13 kịch bản Node phục vụ các bước dựng phụ trợ. Thư mục quy trình "
        "tích hợp liên tục chứa 9 quy trình."
    )

    r.h3("1.2. Công nghệ xây dựng tầng giao diện")
    r.p(
        "Tầng giao diện được xây dựng theo mô hình đa trang thay vì mô hình ứng "
        "dụng một trang. Quyết định này có ba lý do kỹ thuật. Thứ nhất, với hơn "
        "một trăm công cụ, một ứng dụng một trang buộc phải tải toàn bộ mã của "
        "mọi công cụ hoặc phải xây dựng cơ chế tách gói phức tạp; mô hình đa "
        "trang giải quyết vấn đề này một cách tự nhiên vì mỗi trang là một điểm "
        "vào riêng và bộ dựng tự động chỉ gói những phụ thuộc mà trang đó cần."
    )
    r.p(
        "Thứ hai, mỗi công cụ có bảng tham số rất khác nhau; việc dựng bảng "
        "tham số động trong một ứng dụng một trang sẽ dẫn tới hoặc một hệ thống "
        "mô tả biểu mẫu phức tạp, hoặc một khối điều kiện khổng lồ. Mô hình đa "
        "trang cho phép mỗi công cụ khai báo giao diện của mình bằng HTML tĩnh. "
        "Thứ ba, mô hình đa trang cho phép cùng một mã nguồn phục vụ được cả "
        "bản web tối ưu cho công cụ tìm kiếm và bản desktop, vì mỗi công cụ có "
        "một địa chỉ riêng."
    )
    r.p(
        "Về xử lý kiểu trình bày, hệ thống dùng Tailwind CSS phiên bản 4 qua "
        "trình cắm Vite chính thức, kết hợp với một số tệp CSS riêng cho những "
        "thành phần phức tạp như trình soạn thảo bookmark và trình soạn thảo "
        "Markdown. Các phần giao diện dùng chung được chèn bằng trình cắm "
        "Handlebars ở thời điểm biên dịch, với ngữ cảnh gồm đường dẫn gốc, cờ "
        "chế độ đơn giản, tên và biểu trưng thương hiệu, dòng chân trang và số "
        "hiệu phiên bản."
    )
    r.p(
        "Một điểm kỹ thuật đáng lưu ý là việc bổ sung các gói mô phỏng API của "
        "Node.js cho môi trường trình duyệt. Cấu hình Vite khai báo mô phỏng "
        "cho năm mô-đun: buffer, stream, util, zlib và process, đồng thời bật "
        "biến toàn cục Buffer và process. Lý do là một số thư viện xử lý tài "
        "liệu — đáng kể nhất là PDFKit và các thư viện liên quan tới nén — được "
        "viết cho môi trường Node.js và trông đợi những API này tồn tại."
    )
    r.p(
        "Về đóng gói kết quả, bản web sinh thêm bản nén Brotli và gzip cho mọi "
        "tệp lớn hơn 1 KB, phục vụ việc phục vụ tĩnh hiệu quả. Bản desktop bỏ "
        "qua bước này vì tài nguyên được phục vụ trực tiếp bởi vỏ Tauri, nên "
        "các tệp nén chỉ làm tăng gấp đôi dung lượng gói cài đặt mà không mang "
        "lại lợi ích. Đây là một trong ba điểm khác biệt duy nhất giữa hai chế "
        "độ dựng, được kiểm soát bằng một biến kiểm tra chế độ trong cấu hình."
    )

    r.h3("1.3. Xây dựng tầng vỏ bản địa")
    r.p(
        "Tầng vỏ bản địa được hiện thực trong hai tệp Rust. Tệp điểm vào chỉ "
        "chứa bốn dòng thực chất: một chỉ thị biên dịch có điều kiện để không "
        "hiện cửa sổ console trên Windows ở bản phát hành, và một lời gọi tới "
        "hàm khởi chạy trong thư viện. Tệp thư viện chứa hàm khởi chạy và một "
        "lệnh duy nhất được phơi bày cho tầng web."
    )
    r.p(
        "Hàm khởi chạy dựng đối tượng ứng dụng Tauri, đăng ký trình cắm hộp "
        "thoại, đăng ký danh sách lệnh chỉ gồm một phần tử, và chạy vòng lặp sự "
        "kiện. Cấu hình cửa sổ nằm trong tệp cấu hình JSON: nhãn cửa sổ, tiêu "
        "đề hiển thị, kích thước mặc định 1280×860 và kích thước tối thiểu "
        "800×600, cho phép thay đổi kích thước, không mở toàn màn hình."
    )
    r.p(
        "Phần đáng chú ý nhất trong cấu hình là khối bảo mật. Trường chính sách "
        "bảo mật nội dung được đặt là rỗng, nghĩa là không áp dụng chính sách "
        "bổ sung ngoài mặc định của Tauri; hai tiêu đề cách ly nguồn gốc được "
        "đặt tường minh. Tệp khai báo quyền chỉ liệt kê một quyền duy nhất là "
        "bộ quyền lõi mặc định, kèm một ghi chú giải thích rằng hộp thoại lưu "
        "được điều khiển hoàn toàn từ phía Rust nên tầng web không cần bất kỳ "
        "quyền hệ tệp hay quyền hộp thoại nào."
    )
    r.p(
        "Cấu hình biên dịch Rust cho bản phát hành được tối ưu theo hướng giảm "
        "kích thước nhị phân: bật tối ưu hoá liên kết thời gian, đặt số đơn vị "
        "sinh mã về một, chọn mức tối ưu ưu tiên kích thước, chuyển hành vi khi "
        "hoảng loạn sang huỷ tiến trình thay vì tháo dỡ ngăn xếp, và loại bỏ "
        "thông tin gỡ lỗi. Tổ hợp này cho nhị phân nhỏ nhất có thể, phù hợp với "
        "thực tế rằng phần lớn dung lượng gói cài đặt đến từ tài nguyên "
        "WebAssembly chứ không từ mã Rust."
    )

    # ==================================================================
    r.h2("2. Xây dựng các thành phần chính của hệ thống")

    r.h3("2.1. Khuôn mẫu hiện thực một công cụ")
    r.p(
        "Với 127 công cụ, khả năng duy trì hệ thống phụ thuộc hoàn toàn vào "
        "tính khuôn mẫu. Sau khi khảo sát mã nguồn của nhiều mô-đun nghiệp vụ "
        "thuộc các nhóm khác nhau, có thể rút ra một khuôn mẫu ba bước áp dụng "
        "gần như thống nhất. Hình 3.2 trình bày khuôn mẫu này."
    )
    r.figure(
        "fig_3_2_tool_template",
        "Hình 3.2. Khuôn mẫu hiện thực một công cụ trong hệ thống",
    )
    r.p(
        "Bước thứ nhất là trang HTML tĩnh. Mỗi trang gồm phần đầu chứa thẻ siêu "
        "dữ liệu phục vụ tối ưu hoá công cụ tìm kiếm, phần thân chứa thanh điều "
        "hướng và chân trang được chèn từ mảnh giao diện dùng chung, nút quay "
        "lại danh mục, tiêu đề và mô tả công cụ, vùng nhận tệp kèm ô nhập tệp "
        "ẩn, khu vực hiển thị tệp đã chọn, bảng tham số riêng của công cụ, nút "
        "xử lý, và cuối cùng là hộp thoại tải cùng hộp thoại thông báo."
    )
    r.p(
        "Mọi nhãn văn bản trong trang đều mang thuộc tính khoá dịch theo dạng "
        "không gian tên và đường dẫn khoá. Nhờ đó hàm áp dụng bản dịch có thể "
        "duyệt toàn bộ cây tài liệu và thay thế nội dung mà không cần biết "
        "trước cấu trúc của từng trang."
    )
    r.p(
        "Bước thứ hai là mô-đun nghiệp vụ tương ứng, đặt trong thư mục logic "
        "với tên theo quy ước gồm tên công cụ và hậu tố chỉ vai trò. Mô-đun này "
        "có cấu trúc gồm năm phần: khối đăng ký sự kiện chạy khi cây tài liệu "
        "sẵn sàng, hàm xử lý tệp được chọn, hàm cập nhật giao diện, hàm thực "
        "thi phép biến đổi, và hàm đặt lại trạng thái."
    )
    r.p(
        "Khối đăng ký sự kiện gắn trình xử lý cho bốn nguồn sự kiện: thay đổi "
        "của ô nhập tệp, ba sự kiện kéo–thả trên vùng nhận tệp, lần bấm nút xử "
        "lý và lần bấm nút quay lại. Một chi tiết nhỏ nhưng quan trọng xuất "
        "hiện ở hầu hết các mô-đun: trình xử lý sự kiện bấm trên ô nhập tệp xoá "
        "giá trị hiện tại của ô trước khi hộp thoại mở, để người dùng chọn lại "
        "đúng tệp vừa chọn vẫn kích hoạt được sự kiện thay đổi."
    )
    r.p(
        "Hàm xử lý tệp được chọn thực hiện việc lọc. Với công cụ chỉ nhận PDF, "
        "điều kiện lọc kiểm tra kiểu MIME hoặc phần mở rộng viết thường. Với "
        "công cụ nhận ảnh, hệ thống có một mô-đun tiện ích riêng định nghĩa "
        "danh sách phần mở rộng và chuỗi thuộc tính chấp nhận, bảo đảm tính "
        "nhất quán giữa các công cụ ảnh khác nhau."
    )
    r.p(
        "Hàm cập nhật giao diện dựng danh sách tệp đã chọn kèm tên, dung lượng "
        "đã định dạng và nút xoá, đồng thời bỏ ẩn bảng tham số. Một nguyên tắc "
        "an toàn được tuân thủ nhất quán ở đây: nội dung do tệp cung cấp, đặc "
        "biệt là tên tệp, luôn được gán qua thuộc tính nội dung văn bản chứ "
        "không qua thuộc tính HTML nội bộ, nhằm loại trừ khả năng chèn mã qua "
        "tên tệp được dựng cố ý."
    )
    r.p(
        "Bước thứ ba là gọi tiện ích dùng chung và động cơ xử lý. Chuỗi gọi "
        "điển hình gồm: giải mã tệp có mật khẩu nếu cần, nạp tài liệu, thực thi "
        "phép biến đổi bằng thư viện tương ứng, đóng gói kết quả thành đối "
        "tượng nhị phân với tên tệp đã khử trùng lặp, và gọi hàm lưu tệp dùng "
        "chung. Xuyên suốt chuỗi này, chỉ báo tải được cập nhật với văn bản mô "
        "tả bước đang thực hiện."
    )
    r.p(
        "Khuôn mẫu này không được cưỡng chế bằng một lớp cơ sở hay một giao "
        "diện bắt buộc mà được duy trì bằng quy ước. Cách làm này có ưu điểm là "
        "linh hoạt — những công cụ có nhu cầu đặc biệt như trình soạn thảo hay "
        "trình dựng luồng có thể đi chệch khỏi khuôn mẫu — nhưng cũng có nhược "
        "điểm là không có cơ chế bảo đảm tự động. Việc chuẩn hoá khuôn mẫu "
        "thành một trừu tượng dùng chung là một hướng cải tiến đáng cân nhắc."
    )

    r.h3("2.2. Xây dựng màn hình làm việc và cơ chế điều hướng")
    r.p(
        "Màn hình làm việc chính được dựng hoàn toàn bằng mã trong mô-đun chính "
        "thay vì viết sẵn trong HTML, bởi nội dung của nó phụ thuộc vào danh "
        "mục công cụ, vào cấu hình vô hiệu hoá và vào ngôn ngữ đang chọn."
    )
    r.p(
        "Quá trình dựng gồm bốn bước. Bước thứ nhất lọc danh mục: mỗi nhóm được "
        "lọc bỏ những công cụ nằm trong danh sách vô hiệu hoá, và những nhóm "
        "trở nên rỗng sau khi lọc cũng bị loại khỏi thanh bên. Bước thứ hai "
        "dựng mục tổng hợp tất cả công cụ bằng cách duyệt mọi nhóm và thêm vào "
        "một tập theo định danh, nhờ đó những công cụ xuất hiện ở nhiều nhóm "
        "chỉ hiện một lần."
    )
    r.p(
        "Bước thứ ba dựng thanh bên: mỗi nhóm trở thành một nút gồm nhãn đã "
        "dịch và số lượng công cụ. Bước thứ tư dựng lưới thẻ công cụ cho nhóm "
        "đang chọn; mỗi thẻ gồm biểu tượng, tên đã dịch và mô tả ngắn đã dịch. "
        "Hệ thống hỗ trợ hai bộ biểu tượng và phân biệt chúng bằng tiền tố tên "
        "biểu tượng."
    )
    r.p(
        "Cơ chế dịch nhãn dựa trên hai bảng ánh xạ đặt trong mô-đun chính: một "
        "bảng ánh xạ tên nhóm sang khoá dịch và một bảng ánh xạ tên công cụ "
        "sang tiền tố khoá dịch. Cách làm này giữ cho tệp danh mục công cụ độc "
        "lập với hệ thống dịch, nhưng đổi lại đòi hỏi cập nhật hai nơi khi thêm "
        "công cụ mới."
    )
    r.p(
        "Về hành vi, việc chọn một nhóm sẽ xoá nội dung ô tìm kiếm và dựng lại "
        "lưới. Ngược lại, việc gõ vào ô tìm kiếm sẽ lọc trên toàn bộ tập công "
        "cụ. Trên màn hình hẹp, thanh bên chuyển thành trình đơn thu gọn do một "
        "mô-đun riêng quản lý."
    )
    r.placeholder(
        "Hình 3.3",
        "Hình 3.3. Màn hình làm việc chính của PDF Toolkit Desktop",
        "Toàn bộ cửa sổ ứng dụng ở trạng thái vừa khởi động, hiển thị thanh bên "
        "danh mục bên trái và lưới thẻ công cụ của nhóm “Công cụ phổ biến”.",
        [
            "Khởi chạy ứng dụng đã đóng gói (hoặc chạy lệnh npm run tauri:dev).",
            "Chờ giao diện nạp xong, xác nhận ngôn ngữ đang là tiếng Việt.",
            "Không mở công cụ nào, giữ nguyên nhóm mặc định “Công cụ phổ biến”.",
            "Chụp toàn bộ cửa sổ ứng dụng kèm thanh tiêu đề của hệ điều hành để "
            "thấy rõ đây là ứng dụng bản địa chứ không phải tab trình duyệt.",
        ],
    )
    r.placeholder(
        "Hình 3.4",
        "Hình 3.4. Thanh bên danh mục và chức năng tìm kiếm công cụ",
        "Ảnh ghép hai trạng thái: (a) thanh bên với bảy nhóm và số lượng công "
        "cụ của từng nhóm; (b) kết quả lọc sau khi gõ một từ khoá vào ô tìm "
        "kiếm.",
        [
            "Chụp ảnh thứ nhất: cận cảnh thanh bên, thấy rõ tên bảy nhóm kèm số "
            "đếm và nhóm đang được chọn.",
            "Gõ từ khoá “ghép” (hoặc “merge”) vào ô tìm kiếm ở đầu vùng nội "
            "dung.",
            "Chụp ảnh thứ hai: lưới thẻ công cụ đã được lọc theo từ khoá.",
            "Ghép hai ảnh nằm ngang, đặt nhãn (a) và (b) bên dưới mỗi ảnh.",
        ],
    )

    r.h3("2.3. Xây dựng cơ chế lưu tệp bản địa")
    r.p(
        "Cơ chế lưu tệp bản địa là điểm giao duy nhất giữa tầng web và tầng "
        "Rust, đồng thời là thay đổi có tác động rộng nhất khi bổ sung bản "
        "desktop: hàm lưu tệp dùng chung được gọi từ khoảng 311 vị trí trong "
        "mã nguồn. Chính vì độ phủ rộng đó mà thiết kế phải bảo đảm không làm "
        "thay đổi hành vi của bản web. Hình 3.5 trình bày cơ chế này."
    )
    r.figure(
        "fig_3_5_native_save",
        "Hình 3.5. Cơ chế lưu tệp bản địa qua lệnh save_file của tầng Rust",
    )
    r.p(
        "Giải pháp được chọn là phân nhánh ngay bên trong hàm lưu tệp dùng "
        "chung, dựa trên việc phát hiện môi trường thực thi. Hàm phát hiện kiểm "
        "tra sự tồn tại của hai biến toàn cục mà Tauri chèn vào mọi cửa sổ nó "
        "quản lý. Nếu không phát hiện được, hàm giữ nguyên hành vi cũ: tạo địa "
        "chỉ đối tượng tạm, tạo một thẻ liên kết có thuộc tính tải xuống, kích "
        "hoạt lần bấm bằng mã, gỡ thẻ khỏi cây tài liệu và thu hồi địa chỉ."
    )
    r.p(
        "Nếu phát hiện được môi trường Tauri, hàm chuyển sang nhánh bản địa: "
        "nạp động mô-đun lõi của Tauri, chuyển đối tượng nhị phân thành mảng "
        "byte, và gọi lệnh lưu tệp với hai tham số là tên tệp gợi ý và dữ liệu. "
        "Việc nạp động thay vì nhập tĩnh là một chi tiết có chủ ý: nó bảo đảm "
        "gói của bản web không kéo theo mã Tauri không cần thiết."
    )
    r.p(
        "Phía Rust, lệnh lưu tệp là một hàm bất đồng bộ nhận ba tham số: đối "
        "tượng ứng dụng, tên tệp và mảng byte. Hàm gọi trình cắm hộp thoại để "
        "mở hộp thoại lưu của hệ điều hành với tên tệp gợi ý đã đặt sẵn. Lời "
        "gọi này là lời gọi chặn, đưa hộp thoại lên luồng giao diện và chặn "
        "luồng công nhân cho tới khi người dùng quyết định."
    )
    r.p(
        "Kết quả trả về được xử lý theo ba trường hợp rõ ràng. Nếu người dùng "
        "chọn một đường dẫn, hàm chuyển đối tượng đường dẫn thành đường dẫn hệ "
        "tệp, ghi mảng byte ra và trả về giá trị đúng. Nếu người dùng huỷ hộp "
        "thoại, hàm trả về giá trị sai — đây là điểm thiết kế quan trọng: việc "
        "huỷ không được coi là lỗi, không sinh thông báo lỗi và không để lại "
        "tệp dở dang. Nếu việc ghi tệp thất bại thực sự, hàm trả về lỗi kèm "
        "thông điệp của hệ thống."
    )
    r.p(
        "Phía JavaScript, toàn bộ lời gọi được bọc trong khối bắt lỗi với một "
        "cơ chế dự phòng: nếu lời gọi lệnh bản địa ném ngoại lệ vì bất kỳ lý do "
        "gì, hàm ghi lỗi vào nhật ký rồi gọi lại nhánh tải xuống kiểu trình "
        "duyệt. Nguyên tắc đằng sau cơ chế này là kết quả xử lý không bao giờ "
        "được phép mất một cách âm thầm; thà người dùng nhận tệp ở thư mục tải "
        "xuống mặc định còn hơn không nhận được gì."
    )
    r.p(
        "Cần nêu một giới hạn của cơ chế: dữ liệu được truyền qua kênh liên "
        "tiến trình của Tauri dưới dạng mảng byte, nên với tệp kết quả cỡ vài "
        "trăm megabyte, thao tác lưu sẽ chậm hơn một chút so với tải xuống bằng "
        "đối tượng nhị phân trong trình duyệt. Đây là đánh đổi đã được ghi nhận "
        "trong tài liệu kỹ thuật của dự án."
    )

    r.h3("2.4. Xây dựng cơ chế đa ngữ và xử lý sự cố phát sinh")
    r.p(
        "Cơ chế đa ngữ là ví dụ điển hình cho thấy việc bổ sung một bản dựng "
        "mới có thể làm lộ ra những giả định ngầm trong mã hiện có. Hình 3.6 "
        "trình bày cơ chế đa ngữ cùng điểm khác biệt giữa hai bản dựng."
    )
    r.figure(
        "fig_3_6_i18n",
        "Hình 3.6. Cơ chế đa ngữ và điều kiện bảo vệ cho bản dựng desktop",
    )
    r.p(
        "Trình tự khởi động của hệ thống bắt đầu bằng việc kiểm tra bộ nhớ cục "
        "bộ: nếu chưa có giá trị ngôn ngữ nào được lưu, mô-đun chính ghi mã "
        "tiếng Việt vào. Đây là hiện thực cụ thể của yêu cầu PC-12 về ngôn ngữ "
        "mặc định. Sau đó hàm xác định ngôn ngữ chạy theo thứ tự ưu tiên năm "
        "mức đã trình bày ở Chương 2, và thư viện i18next được khởi tạo với "
        "phần phụ trợ tải tài nguyên qua HTTP."
    )
    r.p(
        "Sau khi khởi tạo, hàm áp dụng bản dịch duyệt toàn bộ cây tài liệu và "
        "thay thế nội dung của mọi phần tử mang thuộc tính khoá dịch. Bộ chọn "
        "ngôn ngữ được chèn vào thanh điều hướng, và việc đổi ngôn ngữ được "
        "thực hiện tại chỗ, không tải lại trang."
    )
    r.p(
        "Vấn đề nảy sinh ở hàm viết lại liên kết. Bản web bản phát hành sinh "
        "sẵn một thư mục trang riêng cho mỗi ngôn ngữ thông qua một kịch bản "
        "hậu xử lý, phục vụ mục tiêu tối ưu hoá công cụ tìm kiếm với thẻ ngôn "
        "ngữ thay thế và sơ đồ trang riêng. Để các trang đó liên kết đúng với "
        "nhau, hàm viết lại liên kết thêm tiền tố ngôn ngữ vào mọi liên kết nội "
        "bộ khi ngôn ngữ hiện tại không phải tiếng Anh."
    )
    r.p(
        "Điều kiện bảo vệ ban đầu chỉ loại trừ chế độ phát triển. Trong bản "
        "desktop đã dựng, chế độ phát triển tắt và ngôn ngữ mặc định là tiếng "
        "Việt, nên hàm viết lại liên kết chạy và biến mọi liên kết công cụ "
        "thành đường dẫn có tiền tố tiếng Việt. Nhưng gói desktop không hề chứa "
        "những trang có tiền tố đó. Hệ quả quan sát được rất khó chẩn đoán: các "
        "thẻ công cụ ở nhóm mặc định không phản hồi khi bấm ở lần tải đầu tiên, "
        "nhưng sau khi người dùng chuyển sang một nhóm khác thì mọi thẻ lại "
        "hoạt động bình thường — bởi việc chuyển nhóm dựng lại lưới thẻ với "
        "liên kết nguyên bản, còn hàm viết lại liên kết không chạy lại."
    )
    r.p(
        "Cách khắc phục là mở rộng điều kiện bảo vệ để nhận diện cả môi trường "
        "Tauri, thông qua hai dấu hiệu độc lập: chế độ dựng và các biến toàn "
        "cục do Tauri chèn. Việc dùng hai dấu hiệu thay vì một bảo đảm cơ chế "
        "hoạt động đúng cả khi chạy phát triển với cửa sổ Tauri và khi chạy bản "
        "đã dựng."
    )
    r.p(
        "Sự cố này minh hoạ một bài học thiết kế đáng ghi nhận: khi một mã "
        "nguồn phục vụ nhiều đích triển khai, những hành vi chỉ đúng cho một "
        "đích cần được bảo vệ bằng điều kiện mô tả trực tiếp đặc điểm của đích "
        "đó, chứ không nên dựa vào một điều kiện gián tiếp như cờ chế độ phát "
        "triển. Bài học này cũng lý giải vì sao thiết kế đã chọn giữ định danh "
        "công cụ độc lập với nhãn hiển thị: nhờ đó việc sửa lỗi chỉ cần thay "
        "đổi điều kiện bảo vệ, không phải đụng tới cấu trúc danh mục."
    )

    # ==================================================================
    r.h2("3. Xây dựng mô-đun xử lý tài liệu")

    r.h3("3.1. Tổ chức tài nguyên WebAssembly ngoại tuyến")
    r.p(
        "Yêu cầu PC-02 về khả năng hoạt động ngoại tuyến được hiện thực bằng "
        "một chuỗi cơ chế phối hợp từ thời điểm biên dịch tới thời điểm chạy. "
        "Hình 3.7 trình bày toàn bộ chuỗi này."
    )
    r.figure(
        "fig_3_7_wasm_resolution",
        "Hình 3.7. Cơ chế giải quyết nguồn mô-đun WebAssembly cho bản desktop",
    )
    r.p(
        "Ở thời điểm biên dịch, chế độ dựng dành cho desktop nạp một tệp môi "
        "trường riêng. Tệp này khai báo bảy biến trỏ toàn bộ mô-đun về đường "
        "dẫn tương đối trong gói ứng dụng: ba biến cho PyMuPDF, Ghostscript và "
        "CoherentPDF; bốn biến cho các thành phần của động cơ nhận dạng ký tự "
        "gồm tệp công nhân, thư mục lõi, thư mục dữ liệu ngôn ngữ và thư mục "
        "phông chữ. Bản web bỏ qua hoàn toàn tệp này."
    )
    r.p(
        "Ở thời điểm chạy, mô-đun quản lý nguồn áp dụng thứ tự ưu tiên ba mức: "
        "giá trị người dùng đặt trong bộ nhớ cục bộ, giá trị từ biến môi trường "
        "đã nhúng khi biên dịch, và cuối cùng là địa chỉ mạng phân phối nội "
        "dung mặc định. Với bản desktop, mức thứ hai luôn có giá trị nên mức "
        "thứ ba không bao giờ được dùng tới, trừ khi người dùng chủ động đặt "
        "một địa chỉ khác."
    )
    r.p(
        "Mỗi mô-đun có một bộ nạp chuyên biệt tuân theo cùng một khuôn mẫu: giữ "
        "một thể hiện đơn nhất và một lời hứa nạp dùng chung ở phạm vi mô-đun. "
        "Lời hứa nạp dùng chung giải quyết một vấn đề tinh tế: khi hai thao tác "
        "cùng yêu cầu một mô-đun gần như đồng thời, nếu chỉ kiểm tra thể hiện "
        "đã có thì cả hai đều thấy chưa có và cùng khởi tạo, dẫn tới nạp trùng. "
        "Việc lưu lại lời hứa khiến lời gọi thứ hai chờ trên chính lời hứa của "
        "lời gọi thứ nhất."
    )
    r.p(
        "Cách nạp khác nhau tuỳ mô-đun. CoherentPDF được nạp trên luồng chính "
        "bằng cách chèn một thẻ kịch bản vào phần đầu tài liệu và chờ sự kiện "
        "nạp xong; trong Web Worker, nó được nạp bằng lệnh nhập kịch bản đồng "
        "bộ. qpdf được khởi tạo bằng hàm tạo mô-đun với tuỳ chọn định vị tệp "
        "nhị phân. PyMuPDF được nạp qua bộ nạp riêng khởi tạo môi trường "
        "Pyodide rồi cài các gói Python cần thiết."
    )
    r.p(
        "Tài nguyên trên đĩa được đóng gói bởi một kịch bản Node thuần, chạy "
        "sau bước dựng giao diện. Kịch bản này kiểm tra sự tồn tại của cả thư "
        "mục nguồn lẫn thư mục đích trước khi sao chép, và đưa ra thông điệp "
        "lỗi có hướng dẫn cụ thể nếu thiếu. Việc dùng API hệ tệp của Node thay "
        "vì lệnh sao chép của trình vỏ là có chủ ý: cùng một kịch bản phải chạy "
        "được trên cả ba hệ điều hành trong ma trận tích hợp liên tục."
    )
    r.p(
        "Bảng 3.1 tổng hợp bằng chứng cụ thể về khả năng hoạt động ngoại tuyến "
        "của từng nhóm chức năng, dựa trên việc đối chiếu mã nguồn với cấu hình "
        "biên dịch."
    )
    r.table(
        "Bảng 3.1. Phụ thuộc mạng của từng nhóm chức năng trong bản desktop",
        ["Nhóm chức năng", "Nguồn tài nguyên khi chạy", "Phụ thuộc mạng"],
        [
            ["Tổ chức trang, chỉnh sửa, chú thích",
             "pdf-lib và pdf.js đóng gói trong gói JavaScript",
             "Không"],
            ["Ghép, tách theo bookmark, mục lục, tệp đính kèm",
             "CoherentPDF từ thư mục cục bộ /wasm/cpdf/",
             "Không"],
            ["Mã hoá, giải mã, đặt quyền, tuyến tính hoá, sửa tệp",
             "qpdf.wasm trong thư mục tài nguyên công khai",
             "Không"],
            ["Nén, chuyển đổi từ PDF, trích ảnh và bảng, khử nghiêng",
             "PyMuPDF trên nền Pyodide từ /wasm/pymupdf/",
             "Không"],
            ["Chuyển PDF/A, chuyển phông thành đường nét",
             "Ghostscript từ /wasm/gs/",
             "Không"],
            ["Nhận dạng ký tự tiếng Anh",
             "Lõi Tesseract và dữ liệu ngôn ngữ eng từ /wasm/ocr/",
             "Không"],
            ["Nhận dạng ký tự các ngôn ngữ khác",
             "Lõi cục bộ; dữ liệu ngôn ngữ cần bổ sung vào /wasm/ocr/lang-data",
             "Không, nếu đã bổ sung dữ liệu ngôn ngữ"],
            ["Nhận dạng ký tự cần phông CJK hoặc Noto mở rộng",
             "Phông tải theo yêu cầu từ nguồn cấu hình",
             "Có, khi phông chưa đóng gói"],
            ["Chuyển tài liệu văn phòng sang PDF",
             "LibreOffice-WASM trong thư mục tài nguyên công khai",
             "Không"],
            ["Ký số bằng chứng thư tự ký hoặc chứng thư đủ chuỗi",
             "zgapdfsigner và node-forge trong gói JavaScript",
             "Không"],
            ["Ký số cần tải chuỗi chứng thư từ bên ngoài",
             "Máy chủ của cơ quan cấp chứng thư qua máy chủ trung chuyển",
             "Có"],
            ["Đóng dấu thời gian RFC 3161",
             "Máy chủ TSA do người dùng chọn",
             "Có"],
        ],
        widths=[5, 6, 3.5],
        font_size=11,
    )

    r.h3("3.2. Hiện thực nhóm thao tác tổ chức trang")
    r.p(
        "Nhóm tổ chức trang là nhóm được dùng nhiều nhất và cũng là nhóm có "
        "hiện thực đa dạng nhất về mặt lựa chọn thư viện. Mục này phân tích "
        "chi tiết ba thao tác đại diện."
    )
    r.p(
        "Thao tác ghép được hiện thực trên nền CoherentPDF chạy trong Web "
        "Worker, theo đúng trình tự đã trình bày ở biểu đồ tuần tự Hình 2.8. "
        "Điểm đáng phân tích thêm là cấu trúc dữ liệu công việc được thiết kế "
        "để phục vụ cả hai chế độ ghép. Mỗi công việc gồm tên tệp và một trong "
        "bốn kiểu khoảng: toàn bộ, chuỗi khoảng do người dùng nhập, một trang "
        "đơn theo chỉ số, hoặc một khoảng liên tiếp theo cặp chỉ số đầu và "
        "cuối. Bốn kiểu này đủ để biểu diễn mọi tổ hợp mà giao diện cho phép."
    )
    r.p(
        "Thuật toán gộp trang liên tiếp trong chế độ ghép theo trang đáng được "
        "mô tả cụ thể. Sau khi người dùng sắp xếp xong, hệ thống thu được một "
        "danh sách phẳng gồm các cặp tên tệp và chỉ số trang theo đúng thứ tự "
        "hiển thị. Thuật toán duyệt danh sách này, với mỗi phần tử thì mở rộng "
        "về phía sau chừng nào phần tử kế tiếp còn cùng tệp và có chỉ số trang "
        "liền kề. Kết quả là một chuỗi công việc ngắn hơn nhiều so với danh "
        "sách trang gốc trong trường hợp phổ biến là người dùng chỉ đảo thứ tự "
        "một vài khối."
    )
    r.p(
        "Phía Web Worker, hàm ghép nạp từng tệp từ bộ nhớ, chuyển mỗi công việc "
        "thành một đối tượng khoảng của thư viện, rồi gọi hàm ghép nhận vào ba "
        "tham số: danh sách tài liệu, cờ giữ nhãn trang và danh sách khoảng "
        "tương ứng. Cờ giữ nhãn trang được điều khiển bằng một hộp kiểm trên "
        "giao diện, cho phép người dùng chọn giữ hệ thống đánh số riêng của "
        "từng tài liệu nguồn hay đánh số lại liên tục."
    )
    r.p(
        "Thao tác xoay minh hoạ một vấn đề tinh tế của định dạng PDF. Góc xoay "
        "của một trang là một thuộc tính của trang chứ không phải một phép biến "
        "đổi lên nội dung, và giá trị của nó có thể đã khác không từ trước. Vì "
        "vậy việc xoay thêm phải cộng dồn vào giá trị hiện có rồi lấy phần dư "
        "theo 360 độ, chứ không được đặt giá trị tuyệt đối. Hệ thống có hẳn hai "
        "mô-đun tiện ích riêng cho việc này, kèm 33 ca kiểm thử tự động, cho "
        "thấy đây là điểm đã từng gây lỗi trong thực tế."
    )
    r.p(
        "Thao tác trích và xoá trang dùng chung một cơ chế phân tích chuỗi "
        "khoảng. Hàm phân tích chấp nhận cú pháp danh sách phân tách bằng dấu "
        "phẩy, trong đó mỗi phần tử là một số trang hoặc một khoảng có dấu gạch "
        "nối. Hàm này có ba đặc điểm thiết kế đáng chú ý: chuỗi rỗng được hiểu "
        "là toàn bộ trang; phần tử không hợp lệ bị bỏ qua kèm cảnh báo trong "
        "nhật ký thay vì làm cả thao tác thất bại; và kết quả được đưa qua tập "
        "hợp rồi sắp xếp, nên các khoảng chồng lấn không sinh ra trang trùng."
    )

    r.h3("3.3. Hiện thực nhóm chuyển đổi định dạng")
    r.p(
        "Nhóm chuyển đổi có 49 công cụ chia hai chiều và là nhóm phụ thuộc "
        "nhiều thư viện bên ngoài nhất. Về chiều tạo PDF từ định dạng khác, hệ "
        "thống dùng ba con đường tuỳ theo nguồn."
    )
    r.p(
        "Con đường thứ nhất dành cho ảnh: ảnh được chuẩn hoá về dạng có thể "
        "nhúng, rồi nhúng vào tài liệu mới bằng pdf-lib. Bước chuẩn hoá là phần "
        "phức tạp nhất vì pdf-lib chỉ nhúng trực tiếp được hai định dạng là "
        "JPEG và PNG. Mọi định dạng khác — BMP, TIFF, PSD, HEIC, WebP, SVG — "
        "phải được giải mã trước, thông qua thư viện chuyên biệt hoặc thông qua "
        "canvas, rồi mã hoá lại. Hệ thống có một mô-đun tiện ích riêng cho bước "
        "này với 16 ca kiểm thử."
    )
    r.p(
        "Con đường thứ hai dành cho tài liệu văn phòng: tệp được đưa vào "
        "LibreOffice biên dịch sang WebAssembly, tận dụng bộ lọc nhập của "
        "LibreOffice vốn hỗ trợ rất nhiều định dạng, kể cả những định dạng cũ "
        "như WordPerfect, WPS Office, Microsoft Publisher và Visio. Đây là lý "
        "do vì sao hệ thống hỗ trợ được danh sách định dạng rộng bất thường ở "
        "nhóm này."
    )
    r.p(
        "Con đường thứ ba dành cho nội dung dạng văn bản có cấu trúc: văn bản "
        "thuần, Markdown, CSV, JSON và XML. Ở đây hệ thống không chuyển đổi mà "
        "sinh tài liệu mới bằng PDFKit hoặc jsPDF kèm trình cắm bảng. Với "
        "Markdown, chuỗi xử lý gồm phân tích bằng markdown-it với nhiều trình "
        "cắm mở rộng, kết xuất thành HTML, làm sạch bằng DOMPurify, rồi chuyển "
        "thành PDF. Hệ thống còn hỗ trợ kết xuất sơ đồ Mermaid nhúng trong "
        "Markdown; ảnh SVG do Mermaid sinh ra cũng được làm sạch trước khi "
        "nhúng, và có ba ca kiểm thử riêng cho đường xử lý này."
    )
    r.p(
        "Về chiều trích xuất từ PDF, phần lớn công cụ dựa vào PyMuPDF. Chuyển "
        "sang văn bản và Markdown dùng khả năng phân tích bố cục của thư viện; "
        "chuyển sang SVG dùng khả năng kết xuất vector; chuyển sang DOCX dùng "
        "gói pdf2docx đi kèm; trích bảng dùng thuật toán nhận diện bảng của thư "
        "viện. Riêng chuyển sang ảnh có hai đường: dùng PyMuPDF cho chất lượng "
        "cao, hoặc dùng pdf.js kết xuất ra canvas rồi xuất ảnh cho trường hợp "
        "không cần mô-đun nặng."
    )
    r.p(
        "Chuyển đổi sang CBZ và từ CBZ minh hoạ một chi tiết thú vị về siêu dữ "
        "liệu. Hệ thống không chỉ đóng gói ảnh vào kho nén mà còn sinh ba loại "
        "tệp siêu dữ liệu chuẩn của giới truyện tranh số, để các trình đọc "
        "chuyên dụng nhận diện đúng thông tin tập truyện. Mô-đun sinh siêu dữ "
        "liệu này có 39 ca kiểm thử — số ca nhiều thứ tư trong toàn bộ bộ kiểm "
        "thử, cho thấy mức độ chi tiết của đặc tả cần tuân thủ."
    )
    r.p(
        "Chuyển đổi thư điện tử sang PDF là một trường hợp đặc biệt về an toàn. "
        "Tệp thư có thể chứa HTML tuỳ ý, và hệ thống phải hiển thị nội dung đó. "
        "Hàm làm sạch chuyên biệt thực hiện nhiều bước: loại bỏ các thẻ nguy "
        "hiểm và thuộc tính kiểu bằng DOMPurify, giải mã các liên kết đã bị bọc "
        "bởi dịch vụ bảo vệ liên kết, cắt ngắn những liên kết quá dài, loại bỏ "
        "ảnh kích thước một điểm ảnh vốn dùng để theo dõi người nhận, chuyển "
        "cấu trúc bảng dùng cho dàn trang thành thẻ khối đơn giản, và giới hạn "
        "tổng kích thước HTML ở một trăm nghìn ký tự."
    )

    r.h3("3.4. Hiện thực nhóm nén và tối ưu hoá")
    r.p(
        "Nén tài liệu là một trong những thao tác được yêu cầu nhiều nhất, và "
        "cũng là thao tác có sự đánh đổi rõ rệt nhất giữa dung lượng và chất "
        "lượng. Hệ thống hiện thực hai chiến lược khác nhau về bản chất, để "
        "người dùng chọn theo mục đích. Hình 3.8 trình bày hai chiến lược này."
    )
    r.figure(
        "fig_3_8_compression",
        "Hình 3.8. Hai chiến lược nén tài liệu và tham số của từng chiến lược",
    )
    r.p(
        "Chiến lược thứ nhất giữ nguyên cấu trúc tài liệu và chỉ tối ưu các "
        "thành phần bên trong. Thao tác chính là lấy mẫu lại ảnh nhúng: những "
        "ảnh có mật độ điểm ảnh vượt một ngưỡng sẽ được hạ xuống mật độ đích, "
        "kèm mức nén JPEG tương ứng. Bốn mức được định nghĩa sẵn với các cặp "
        "tham số cụ thể, từ mức nhẹ giữ chất lượng 90 và mật độ đích 150 điểm "
        "trên inch, tới mức cực đại hạ chất lượng xuống 30 và mật độ đích 60."
    )
    r.p(
        "Một chi tiết hiện thực đáng chú ý: ngưỡng kích hoạt lấy mẫu lại luôn "
        "được điều chỉnh để lớn hơn mật độ đích ít nhất mười đơn vị. Điều này "
        "ngăn trường hợp người dùng tự đặt tham số khiến ngưỡng thấp hơn hoặc "
        "bằng mật độ đích, dẫn tới việc lấy mẫu lại những ảnh vốn đã ở đúng mật "
        "độ mong muốn và chỉ làm giảm chất lượng mà không giảm dung lượng."
    )
    r.p(
        "Ngoài lấy mẫu lại ảnh, chiến lược này còn gỡ siêu dữ liệu và ảnh thu "
        "nhỏ của trang, tạo tập con phông chữ để chỉ giữ những ký tự thực sự "
        "dùng, và lưu tài liệu với bốn tuỳ chọn tối ưu: mức thu gom rác cao "
        "nhất, nén luồng, làm sạch cấu trúc và dùng luồng đối tượng. Cơ chế dự "
        "phòng được cài đặt cho trường hợp việc xử lý ảnh thất bại: hệ thống "
        "thử lại với phần xử lý ảnh tắt và đánh dấu kết quả là đã dùng đường dự "
        "phòng, để giao diện có thể thông báo cho người dùng biết mức giảm dung "
        "lượng sẽ thấp hơn."
    )
    r.p(
        "Chiến lược thứ hai kết xuất lại toàn bộ tài liệu thành ảnh. Mỗi trang "
        "được kết xuất ra canvas với hệ số tỉ lệ đã định, chuyển thành ảnh JPEG "
        "với mức chất lượng tương ứng, rồi nhúng vào một tài liệu mới có kích "
        "thước trang bằng đúng kích thước canvas. Bốn mức cũng được định nghĩa "
        "sẵn, từ tỉ lệ 2,0 với chất lượng 0,85 tới tỉ lệ 1,0 với chất lượng "
        "0,25."
    )
    r.p(
        "Chiến lược này cho mức giảm dung lượng cao nhất với tài liệu có nhiều "
        "đồ hoạ vector phức tạp, nhưng có một hệ quả không thể đảo ngược: tài "
        "liệu kết quả trở thành một tập ảnh, mất hoàn toàn lớp văn bản. Không "
        "còn tìm kiếm được, không còn sao chép được, và các công cụ đọc màn "
        "hình không còn đọc được. Vì vậy giao diện phải nêu rõ hệ quả này để "
        "người dùng lựa chọn có ý thức."
    )
    r.p(
        "Về quản lý bộ nhớ, chiến lược thứ hai đặc biệt nhạy cảm vì mỗi trang "
        "sinh ra một canvas lớn. Hiện thực giải phóng canvas ngay sau khi xuất "
        "ảnh bằng cách đặt cả chiều rộng và chiều cao về không — một kỹ thuật "
        "buộc trình duyệt giải phóng bộ đệm điểm ảnh ngay lập tức thay vì chờ "
        "bộ thu gom rác."
    )

    r.h3("3.5. Hiện thực nhóm bảo mật tài liệu")
    r.p(
        "Nhóm bảo mật gồm chín công cụ, trong đó thao tác mã hoá đã được phân "
        "tích chi tiết qua biểu đồ tuần tự ở Chương 2. Mục này tập trung vào ba "
        "thao tác còn lại có hiện thực đáng chú ý."
    )
    r.p(
        "Thao tác giải mã minh hoạ cơ chế thử tuần tự nhiều động cơ. Hàm giải "
        "mã nhận vào mảng byte và mật khẩu, rồi thử lần lượt hai đường. Đường "
        "thứ nhất dùng CoherentPDF: thư viện được đặt ở chế độ xử lý chậm nhưng "
        "kỹ, tài liệu được dựng từ bộ nhớ với mật khẩu, và nếu tài liệu được "
        "báo là có mã hoá thì hàm thử gỡ mã hoá bằng mật khẩu người dùng, thất "
        "bại thì thử tiếp bằng mật khẩu chủ sở hữu. Đường thứ hai dùng PyMuPDF: "
        "tài liệu được mở, xác thực bằng mật khẩu, rồi lưu lại."
    )
    r.p(
        "Điểm thiết kế quan trọng là cách xử lý lỗi khi cả hai đường đều thất "
        "bại: hàm không ném lỗi của đường cuối cùng mà gom thông điệp lỗi của "
        "cả hai đường, mỗi thông điệp có tiền tố tên động cơ, rồi ném một lỗi "
        "tổng hợp. Nhờ đó khi chẩn đoán sự cố, người phát triển thấy được cả "
        "hai nguyên nhân thay vì chỉ nguyên nhân cuối."
    )
    r.p(
        "Thông điệp lỗi còn được chuẩn hoá trước khi hiển thị. CoherentPDF, do "
        "được sinh từ mã OCaml, trả về thông điệp có dạng bao bọc bởi tên kiểu "
        "ngoại lệ; các mô-đun khác trả về thông điệp có tiền tố cấp độ lỗi và "
        "tên hàm. Hàm chuẩn hoá dùng biểu thức chính quy để bóc lấy phần nội "
        "dung có ý nghĩa, nhờ đó người dùng nhận được câu ngắn gọn thay vì một "
        "chuỗi kỹ thuật khó hiểu."
    )
    r.p(
        "Cơ chế hỏi mật khẩu được xây dựng thành một mô-đun tiện ích riêng với "
        "hai chế độ. Chế độ đơn lẻ hỏi mật khẩu cho một tệp. Chế độ theo lô "
        "quét toàn bộ danh sách tệp, xác định những tệp cần mật khẩu và hiển "
        "thị một hộp thoại duy nhất liệt kê chúng kèm chỉ báo tiến độ giải mã. "
        "Cả hai chế độ đều dùng một biến nhớ mật khẩu ở phạm vi mô-đun: khi "
        "nhiều tệp dùng chung một mật khẩu — trường hợp rất phổ biến — người "
        "dùng chỉ phải nhập một lần. Mô-đun này có 33 ca kiểm thử tự động."
    )
    r.p(
        "Thao tác làm sạch tài liệu được hiện thực bằng pdf-lib ở mức thao tác "
        "trực tiếp trên từ điển đối tượng. Mười tuỳ chọn độc lập được cung cấp: "
        "làm phẳng biểu mẫu, gỡ siêu dữ liệu, gỡ chú thích, gỡ mã JavaScript, "
        "gỡ tệp nhúng, gỡ lớp nội dung, gỡ liên kết, gỡ cây cấu trúc, gỡ thông "
        "tin đánh dấu và gỡ phông chữ. Chín tuỳ chọn đầu được bật mặc định; "
        "riêng tuỳ chọn gỡ phông tắt mặc định vì nó có thể làm tài liệu hiển "
        "thị sai."
    )
    r.p(
        "Thao tác ký số được xây dựng quanh thư viện zgapdfsigner kết hợp với "
        "node-forge cho phần phân tích chứng thư. Ba dạng đầu vào được hỗ trợ: "
        "tệp PKCS#12, cặp tệp PEM riêng biệt, và tệp PEM gộp. Với cặp tệp PEM, "
        "hệ thống thực hiện một bước chuyển đổi trung gian thú vị: dựng một cấu "
        "trúc PKCS#12 trong bộ nhớ từ chứng thư và khoá, dùng mật khẩu do người "
        "dùng cung cấp hoặc một chuỗi ngẫu nhiên sinh bằng bộ sinh số ngẫu "
        "nhiên mật mã của trình duyệt. Bước này cần thiết vì thư viện ký chỉ "
        "nhận đầu vào ở dạng PKCS#12."
    )
    r.p(
        "Thao tác kiểm tra chữ ký được hiện thực trong một mô-đun dài hơn 800 "
        "dòng, thực hiện việc trích xuất phần chữ ký khỏi tệp, kiểm tra phạm vi "
        "byte được ký có bao trùm toàn bộ tài liệu hay không, xác minh chữ ký "
        "mật mã, và hiển thị thông tin chứng thư gồm chủ thể, tổ chức phát "
        "hành và thời hạn hiệu lực."
    )

    r.h3("3.6. Hiện thực chức năng nhận dạng ký tự quang học")
    r.p(
        "Nhận dạng ký tự là chức năng phức tạp nhất về mặt xử lý trong hệ "
        "thống, bởi nó phải kết hợp ba việc rất khác nhau: kết xuất ảnh, nhận "
        "dạng, và dựng lại lớp văn bản đặt đúng vị trí trên tài liệu gốc. Hình "
        "3.9 trình bày toàn bộ chuỗi xử lý."
    )
    r.figure(
        "fig_3_9_ocr_pipeline",
        "Hình 3.9. Chuỗi xử lý của chức năng nhận dạng ký tự quang học",
    )
    r.p(
        "Bước chuẩn bị đầu tiên là tạo công nhân nhận dạng với ngôn ngữ đã "
        "chọn và chế độ động cơ LSTM. Trước khi tạo, hệ thống kiểm tra ngôn ngữ "
        "yêu cầu có nằm trong danh sách khả dụng hay không. Việc xây dựng tuỳ "
        "chọn công nhân có một ràng buộc đáng chú ý: ba biến chỉ đường dẫn tệp "
        "công nhân, thư mục lõi và thư mục dữ liệu ngôn ngữ phải được đặt cùng "
        "nhau. Nếu chỉ đặt một hoặc hai, hàm ném lỗi nêu rõ biến nào còn thiếu "
        "thay vì để động cơ thất bại ở giữa chừng với thông điệp khó hiểu."
    )
    r.p(
        "Bước chuẩn bị thứ hai là chọn phông chữ. Đây là phần có logic tinh tế "
        "nhất trong toàn bộ chức năng. Hệ thống duy trì một bảng ánh xạ từ mã "
        "ngôn ngữ sang họ phông, và phân loại các ngôn ngữ thành ba nhóm: nhóm "
        "chữ Hán Nhật Hàn, nhóm chữ Ấn Độ, và nhóm ưu tiên gồm hai nhóm trên "
        "cộng với tiếng Ả Rập, tiếng Nga và tiếng Ukraina."
    )
    r.p(
        "Logic chọn phông hoạt động như sau: ngôn ngữ chính được chọn là ngôn "
        "ngữ đầu tiên thuộc nhóm ưu tiên trong danh sách người dùng chọn, hoặc "
        "ngôn ngữ đầu tiên nếu không có ngôn ngữ ưu tiên nào. Nếu ngôn ngữ "
        "chính thuộc nhóm ưu tiên, đồng thời danh sách có chứa ngôn ngữ dùng "
        "chữ Latin, và không có chữ Hán Nhật Hàn, và họ phông của hai bên khác "
        "nhau, thì hệ thống nhúng hai phông riêng biệt. Trong mọi trường hợp "
        "khác, một phông duy nhất được dùng cho cả hai vai trò."
    )
    r.p(
        "Lý do của logic này nằm ở đặc điểm của phông chữ Hán Nhật Hàn: các "
        "phông này thường đã bao gồm đầy đủ ký tự Latin, nên nhúng thêm một "
        "phông Latin riêng chỉ làm tăng dung lượng tệp kết quả một cách không "
        "cần thiết. Ngược lại, phông tiếng Ả Rập hoặc phông chữ Ấn Độ có thể "
        "không phủ đủ ký tự Latin, nên khi tài liệu trộn hai hệ chữ, việc nhúng "
        "hai phông là bắt buộc để không mất ký tự."
    )
    r.p(
        "Vòng lặp xử lý từng trang gồm năm bước. Trang được kết xuất ra canvas "
        "với hệ số tỉ lệ do người dùng chọn — đây là tham số quyết định cả chất "
        "lượng nhận dạng lẫn thời gian xử lý. Nếu người dùng bật tuỳ chọn nhị "
        "phân hoá, canvas được chuyển thành ảnh hai màu bằng cách tính độ sáng "
        "theo trọng số chuẩn của ba kênh màu rồi so với ngưỡng 128; kỹ thuật "
        "này thường cải thiện rõ rệt kết quả với bản quét mờ hoặc có nền màu."
    )
    r.p(
        "Bước nhận dạng được bọc trong một cơ chế hạn thời năm phút cho mỗi "
        "trang. Cơ chế này giải quyết một vấn đề thực tế: với trang có nhiễu "
        "nặng hoặc bố cục bất thường, động cơ nhận dạng có thể chạy rất lâu. "
        "Điểm thiết kế quan trọng là khi quá hạn, hệ thống không huỷ toàn bộ "
        "tài liệu mà ghi một cảnh báo cho trang đó và tiếp tục sang trang tiếp "
        "theo — trang bị bỏ qua vẫn xuất hiện trong kết quả nhưng không có lớp "
        "văn bản."
    )
    r.p(
        "Bước dựng lớp văn bản là phần kỹ thuật nhất. Kết quả hOCR được phân "
        "tích thành cấu trúc gồm dòng và từ, mỗi đơn vị có hộp bao, góc nghiêng "
        "và độ dốc đường cơ sở. Toạ độ được quy đổi từ điểm ảnh của canvas sang "
        "điểm PDF theo kích thước thật của trang. Trang gốc được sao chép sang "
        "tài liệu mới bằng pdf-lib — lưu ý là sao chép chứ không kết xuất lại, "
        "nên hình ảnh gốc được giữ nguyên hoàn toàn."
    )
    r.p(
        "Với mỗi từ, hệ thống tính vị trí, cỡ chữ và hệ số co ngang sao cho "
        "chuỗi văn bản khớp với hộp bao mà động cơ nhận dạng trả về, rồi vẽ "
        "chuỗi đó với độ mờ bằng không. Kết quả là lớp văn bản hoàn toàn vô "
        "hình nhưng có thể chọn, sao chép và tìm kiếm. Góc xoay của mỗi dòng "
        "được tính từ góc nghiêng cộng với arctang của độ dốc đường cơ sở, xử "
        "lý được cả trường hợp bản quét bị lệch nhẹ."
    )
    r.p(
        "Ba chi tiết bổ sung đáng ghi nhận. Thứ nhất, ký tự điều khiển và ký tự "
        "định dạng vô hình bị loại khỏi chuỗi trước khi vẽ, vì chúng có thể gây "
        "lỗi ở bước nhúng phông. Thứ hai, với dòng viết từ phải sang trái, thứ "
        "tự từ được đảo trước khi vẽ để thứ tự đọc trong lớp văn bản đúng với "
        "thứ tự ngữ nghĩa. Thứ ba, khi động cơ báo dòng cần chèn dấu cách giữa "
        "các từ, hệ thống vẽ thêm ký tự cách với hệ số co tính riêng, bảo đảm "
        "việc sao chép văn bản cho ra chuỗi có dấu cách đúng chỗ."
    )
    r.p(
        "Về quản lý bộ nhớ, chức năng này áp dụng bốn biện pháp: giải phóng "
        "canvas sau mỗi trang, gọi hàm dọn dẹp của đối tượng trang pdf.js trong "
        "khối bảo đảm thực thi, gọi hàm dọn dẹp của cả tài liệu sau mỗi 25 "
        "trang, và kết thúc công nhân nhận dạng trong khối bảo đảm thực thi ở "
        "cấp ngoài cùng. Biện pháp thứ ba đặc biệt quan trọng với tài liệu "
        "hàng trăm trang."
    )
    r.p(
        "Cuối cùng, kết quả trả về không chỉ gồm tài liệu và văn bản mà còn có "
        "một mảng cảnh báo phân thành bốn loại: quá hạn nhận dạng, lỗi nhận "
        "dạng, lỗi vẽ lớp văn bản và lỗi ở mức trang. Việc phân loại rõ ràng "
        "giúp người dùng biết chính xác trang nào có vấn đề và vấn đề thuộc "
        "loại gì, thay vì chỉ nhận một thông báo chung chung."
    )

    r.h3("3.7. Hiện thực luồng xử lý tự động")
    r.p(
        "Trình dựng luồng xử lý tự động được hiện thực trên nền thư viện đồ thị "
        "Rete với bốn trình cắm: trình cắm vùng làm việc, trình cắm kết nối, "
        "trình cắm kết xuất dựa trên Lit, và động cơ luồng dữ liệu. Mã của "
        "tính năng này chiếm 8.484 dòng, trong đó phần lớn nằm ở 79 lớp nút."
    )
    r.p(
        "Mỗi lớp nút kế thừa từ một lớp cơ sở chung, khai báo siêu dữ liệu gồm "
        "định danh, nhãn, nhóm chức năng, biểu tượng và mô tả; khai báo các "
        "cổng vào và cổng ra với kiểu dữ liệu tương ứng; khai báo các điều "
        "khiển nhập tham số; và hiện thực hàm sinh dữ liệu thực hiện phép biến "
        "đổi thực sự."
    )
    r.p(
        "Ba kiểu dữ liệu truyền giữa các nút đã được mô tả ở Chương 2. Để đơn "
        "giản hoá việc viết nút, hệ thống cung cấp ba hàm trợ giúp. Hàm thứ "
        "nhất trích một tài liệu đơn từ dữ liệu vào, tự động lấy phần tử đầu "
        "nếu đầu vào là danh sách nhiều tài liệu. Hàm thứ hai gom mọi tài liệu "
        "từ một mảng dữ liệu vào, làm phẳng các danh sách lồng nhau. Hàm thứ ba "
        "là hàm xử lý theo lô: nhận vào danh sách dữ liệu và một hàm biến đổi, "
        "trả về một tài liệu đơn nếu chỉ có một đầu vào hoặc một danh sách nếu "
        "có nhiều. Nhờ ba hàm này, phần lớn lớp nút chỉ cần vài chục dòng."
    )
    r.p(
        "Mọi hàm trợ giúp đều sao chép mảng byte khi truyền dữ liệu, bảo đảm "
        "một nút không sửa dữ liệu mà nút khác đang giữ tham chiếu. Đây là lựa "
        "chọn ưu tiên tính đúng đắn hơn hiệu năng, phù hợp với đặc điểm của "
        "tính năng là chạy theo lô chứ không tương tác thời gian thực."
    )
    r.p(
        "Đồ thị người dùng dựng được có thể lưu và nạp lại. Định dạng lưu là "
        "JSON gồm số hiệu phiên bản, danh sách nút với định danh, kiểu, vị trí "
        "và giá trị các điều khiển, cùng danh sách kết nối với định danh nút "
        "nguồn, cổng ra, nút đích và cổng vào. Việc mang theo số hiệu phiên bản "
        "cho phép xử lý tương thích ngược khi định dạng thay đổi."
    )
    r.p(
        "Về thông báo lỗi, tính năng có một mô-đun riêng quản lý các thông điệp "
        "lỗi đã dịch, với các khoá như luồng không có nút đầu ra, đồ thị có phụ "
        "thuộc vòng, nút không được nối tài liệu vào, hay mô-đun xử lý chưa "
        "được cấu hình. Việc tách riêng các thông điệp này bảo đảm tính năng "
        "hoạt động nhất quán với phần còn lại của giao diện về mặt ngôn ngữ."
    )
    r.placeholder(
        "Hình 3.10",
        "Hình 3.10. Giao diện trình dựng luồng xử lý tự động",
        "Vùng làm việc của trình dựng luồng với một đồ thị hoàn chỉnh gồm ít "
        "nhất bốn nút được nối thành chuỗi, thể hiện rõ các cổng vào/ra và "
        "đường kết nối.",
        [
            "Mở công cụ “PDF Workflow Builder” từ nhóm Công cụ phổ biến.",
            "Kéo vào vùng làm việc các nút: PDF Input → Merge → Watermark → "
            "Download PDF.",
            "Nối các nút thành chuỗi và nạp hai tệp PDF mẫu vào nút đầu vào.",
            "Chạy luồng và chụp màn hình ở thời điểm một nút đang ở trạng thái "
            "“đang chạy” để thấy chỉ báo trạng thái trên nút.",
            "Chụp toàn bộ cửa sổ ứng dụng.",
        ],
    )

    # ==================================================================
    r.h2("4. Triển khai và tối ưu hệ thống")

    r.h3("4.1. Quản lý dữ liệu tạm và bộ nhớ")
    r.p(
        "Như đã phân tích ở Chương 2, nguyên tắc không ghi tệp tạm chuyển toàn "
        "bộ gánh nặng quản lý sang bộ nhớ. Hình 3.11 tổng hợp bảy cơ chế quản lý "
        "dữ liệu tạm được áp dụng trong hệ thống cùng lý do và phạm vi của từng "
        "cơ chế."
    )
    r.figure(
        "fig_3_11_temp_data",
        "Hình 3.11. Các cơ chế quản lý dữ liệu tạm và bộ nhớ",
    )
    r.p(
        "Cơ chế thứ nhất áp dụng cho hệ tệp ảo của qpdf. Khuôn mẫu gồm ba bước "
        "ghi, gọi và đọc, kèm bước xoá bắt buộc trong khối bảo đảm thực thi. "
        "Bước xoá được bọc trong khối bắt lỗi riêng cho từng đường dẫn, vì "
        "trong một số nhánh lỗi tệp có thể chưa được tạo và lời gọi xoá sẽ ném "
        "ngoại lệ; việc để ngoại lệ đó lan ra sẽ che khuất lỗi gốc."
    )
    r.p(
        "Cơ chế thứ hai áp dụng cho Ghostscript theo cùng khuôn mẫu, kèm việc "
        "lưu thể hiện mô-đun trong một biến ở phạm vi mô-đun để tái sử dụng "
        "giữa các lần gọi. Cơ chế thứ ba áp dụng cho PyMuPDF: đối tượng tài "
        "liệu Python được đóng tường minh sau mỗi thao tác, và môi trường "
        "Pyodide được giữ lại vì chi phí khởi tạo rất cao."
    )
    r.p(
        "Cơ chế thứ tư là giải phóng canvas. Kỹ thuật đặt cả chiều rộng và "
        "chiều cao về không được áp dụng nhất quán ở bốn nơi: chức năng nhận "
        "dạng ký tự, chiến lược nén kết xuất lại, chuyển PDF sang ảnh, và sinh "
        "ảnh thu nhỏ. Lý do dùng kỹ thuật này thay vì chỉ bỏ tham chiếu là bộ "
        "đệm điểm ảnh của canvas nằm ngoài vùng nhớ mà bộ thu gom rác của "
        "JavaScript quản lý trực tiếp, nên việc bỏ tham chiếu không bảo đảm "
        "giải phóng ngay."
    )
    r.p(
        "Cơ chế thứ năm là giải phóng đối tượng CoherentPDF. Mọi tài liệu được "
        "nạp trong Web Worker ghép đều được huỷ tường minh bằng hàm huỷ của thư "
        "viện, cả tài liệu nguồn lẫn tài liệu kết quả. Đây là hệ quả trực tiếp "
        "của đặc điểm bộ nhớ WebAssembly đã phân tích ở Chương 1."
    )
    r.p(
        "Cơ chế thứ sáu là chuyển quyền sở hữu bộ đệm khi gửi dữ liệu sang Web "
        "Worker. Với tệp cỡ hàng chục megabyte, việc sao chép thay vì chuyển "
        "quyền sẽ nhân đôi lượng bộ nhớ trong suốt thời gian xử lý. Đổi lại, "
        "bộ đệm gốc trở nên không dùng được sau khi chuyển, nên mã gọi phải "
        "được viết với ý thức về điều này."
    )
    r.p(
        "Cơ chế thứ bảy là thu hồi địa chỉ đối tượng tạm. Mỗi lời gọi tạo địa "
        "chỉ đối tượng đều đi kèm một lời gọi thu hồi tương ứng, áp dụng ở "
        "nhánh tải xuống kiểu trình duyệt và ở các chức năng xem trước tài "
        "liệu."
    )
    r.p(
        "Ngoài bảy cơ chế trên, hệ thống còn áp dụng hai biện pháp ở mức tổ "
        "chức xử lý. Biện pháp thứ nhất là kết xuất theo lô với nạp lười: khi "
        "sinh ảnh thu nhỏ cho tài liệu nhiều trang, hệ thống xử lý tám trang "
        "mỗi lô và chỉ kết xuất những trang sắp lọt vào vùng nhìn thấy, với "
        "biên dự phòng 300 điểm ảnh. Biện pháp thứ hai là dọn dẹp định kỳ: "
        "trong vòng lặp nhận dạng ký tự, hàm dọn dẹp của tài liệu pdf.js được "
        "gọi sau mỗi 25 trang."
    )

    r.h3("4.2. Xử lý lỗi và phản hồi người dùng")
    r.p(
        "Chiến lược xử lý lỗi của hệ thống dựa trên bốn phân loại nguyên nhân, "
        "mỗi phân loại có cách phản hồi riêng. Hình 3.12 tổng hợp chiến lược "
        "này."
    )
    r.figure(
        "fig_3_12_error_handling",
        "Hình 3.12. Chiến lược xử lý lỗi và phản hồi cho người dùng",
    )
    r.p(
        "Phân loại thứ nhất là lỗi đầu vào: không có tệp, tệp sai định dạng, "
        "tham số bắt buộc để trống. Những lỗi này được phát hiện trước khi bắt "
        "đầu xử lý và được phản hồi bằng hộp thoại có tiêu đề mô tả đúng vấn "
        "đề. Nguyên tắc là phát hiện càng sớm càng tốt, tránh để người dùng chờ "
        "một thao tác chắc chắn sẽ thất bại."
    )
    r.p(
        "Phân loại thứ hai là tài liệu có mật khẩu. Đây không hẳn là lỗi mà là "
        "một trạng thái cần tương tác bổ sung. Hệ thống nhận biết trạng thái "
        "này qua ba dấu hiệu: ngoại lệ chuyên biệt do pdf.js ném, thông báo xác "
        "thực thất bại từ CoherentPDF, và cờ cần mật khẩu của PyMuPDF. Phản hồi "
        "là mở hộp thoại nhập mật khẩu chứ không phải thông báo lỗi."
    )
    r.p(
        "Phân loại thứ ba là thiếu mô-đun xử lý. Phản hồi được thiết kế đặc "
        "biệt kỹ: thay vì báo lỗi kỹ thuật, hệ thống mở một hộp thoại chuyên "
        "biệt nêu tên mô-đun bằng ngôn ngữ người dùng hiểu được, liệt kê bốn "
        "tính năng đầu tiên phụ thuộc mô-đun đó kèm số lượng tính năng còn lại, "
        "nhắc về giấy phép của mô-đun, và cung cấp nút dẫn thẳng tới trang cấu "
        "hình."
    )
    r.p(
        "Phân loại thứ tư là lỗi phát sinh trong quá trình xử lý: ngoại lệ từ "
        "thư viện, lỗi trong Web Worker, quá hạn nhận dạng. Mọi thao tác đều "
        "được bọc trong khối bắt lỗi, và mọi khối bắt lỗi đều làm ba việc theo "
        "thứ tự: đóng chỉ báo tải, ghi chi tiết kỹ thuật vào nhật ký, và hiển "
        "thị hộp thoại với thông điệp đã chuẩn hoá."
    )
    r.p(
        "Về ghi vết, hệ thống dùng nhật ký của công cụ phát triển với quy ước "
        "tiền tố theo mô-đun đặt trong dấu ngoặc vuông. Ba mức được sử dụng: "
        "mức thông tin cho các bước bình thường đáng ghi nhận, mức cảnh báo cho "
        "tình huống bất thường nhưng đã xử lý được, và mức lỗi cho ngoại lệ "
        "thực sự. Cần nhấn mạnh rằng toàn bộ nhật ký chỉ tồn tại trong phiên "
        "làm việc và không được gửi đi đâu."
    )
    r.p(
        "Điểm đáng chú ý nhất trong chiến lược xử lý lỗi là tập hợp các cơ chế "
        "suy giảm nhẹ nhàng. Hệ thống có ít nhất năm cơ chế loại này: giải mã "
        "thử tuần tự hai động cơ; nén thử có xử lý ảnh rồi không xử lý ảnh; nạp "
        "phông thất bại thì lùi về phông chuẩn có sẵn; lưu bản địa thất bại thì "
        "lùi về tải xuống kiểu trình duyệt; và nhận dạng quá hạn ở một trang "
        "không làm hỏng cả tài liệu. Triết lý chung là hoàn thành công việc ở "
        "mức tốt nhất có thể thay vì thất bại hoàn toàn khi gặp trở ngại."
    )

    r.h3("4.3. Quy trình biên dịch và đóng gói")
    r.p(
        "Quy trình biên dịch của bản desktop gồm sáu bước được móc nối tự động, "
        "khởi phát từ một lệnh duy nhất. Hình 3.13 trình bày toàn bộ quy trình "
        "cùng đầu ra của từng bước."
    )
    r.figure(
        "fig_3_13_build_pipeline",
        "Hình 3.13. Quy trình biên dịch và đóng gói ứng dụng desktop",
    )
    r.p(
        "Bước thứ nhất là lệnh dựng của Tauri. Lệnh này đọc tệp cấu hình và "
        "phát hiện khai báo lệnh chạy trước khi dựng, từ đó tự động kích hoạt "
        "bước thứ hai. Cơ chế móc nối này bảo đảm không thể quên bước chuẩn bị "
        "giao diện trước khi biên dịch phần bản địa."
    )
    r.p(
        "Bước thứ hai là lệnh dựng giao diện ở chế độ desktop. Chế độ này kích "
        "hoạt ba khác biệt so với bản web: nạp tệp môi trường riêng trỏ mô-đun "
        "về đường dẫn cục bộ, bỏ qua việc sinh bản nén Brotli và gzip, và kích "
        "hoạt bước sao chép tài nguyên WebAssembly."
    )
    r.p(
        "Bước thứ ba là biên dịch TypeScript và dựng gói với Vite. Đây là bước "
        "tốn thời gian nhất về phía giao diện do phải xử lý 131 điểm vào riêng "
        "biệt cùng toàn bộ cây phụ thuộc của chúng. Bước thứ tư sao chép 121 MB "
        "tài nguyên WebAssembly vào thư mục kết quả."
    )
    r.p(
        "Bước thứ năm là biên dịch phần Rust ở cấu hình phát hành với các tuỳ "
        "chọn tối ưu kích thước đã nêu. Bước thứ sáu đóng gói: Tauri nhúng toàn "
        "bộ thư mục kết quả vào nhị phân và sinh gói cài đặt theo định dạng bản "
        "địa của hệ điều hành đang chạy."
    )
    r.p(
        "Đầu ra gồm nhị phân thô cùng các gói cài đặt: định dạng AppImage và "
        "deb trên Linux, định dạng dmg cùng gói ứng dụng trên macOS, định dạng "
        "msi và trình cài đặt NSIS trên Windows. Bảng 3.2 tổng hợp các định "
        "dạng này."
    )
    r.table(
        "Bảng 3.2. Định dạng gói cài đặt và yêu cầu môi trường theo hệ điều hành",
        ["Hệ điều hành", "Thành phần WebView", "Định dạng gói", "Yêu cầu biên dịch"],
        [
            ["Linux (Ubuntu 22.04 trong CI)", "WebKitGTK 4.1",
             ".AppImage, .deb",
             "libwebkit2gtk-4.1-dev, libsoup-3.0-dev, librsvg2-dev, "
             "libappindicator3-dev, patchelf"],
            ["macOS (ARM64)", "WKWebView", ".dmg, .app",
             "Xcode Command Line Tools; đích aarch64-apple-darwin"],
            ["macOS (x86-64)", "WKWebView", ".dmg, .app",
             "Xcode Command Line Tools; đích x86_64-apple-darwin"],
            ["Windows", "WebView2", ".msi, .exe (NSIS)",
             "Visual Studio Build Tools với gói C++; WebView2 Runtime"],
        ],
        widths=[3.5, 2.5, 3, 7],
        font_size=11,
    )
    r.p(
        "Vì gói cài đặt cho macOS và Windows không thể biên dịch chéo từ Linux, "
        "dự án dùng một quy trình tích hợp liên tục với ma trận bốn cấu hình. "
        "Quy trình được kích hoạt thủ công hoặc bằng cách đẩy một thẻ phiên bản "
        "theo quy ước riêng cho bản desktop. Mỗi cấu hình cài phụ thuộc hệ "
        "thống tương ứng, thiết lập Node và Rust, dùng bộ đệm cho thư mục Cargo "
        "để rút ngắn thời gian, rồi gọi tác vụ dựng chính thức của Tauri."
    )
    r.p(
        "Hai hạn chế của quy trình đóng gói hiện tại cần được nêu rõ. Thứ nhất, "
        "các gói cài đặt chưa được ký số và chưa qua công chứng, nên cơ chế bảo "
        "vệ của macOS và Windows sẽ cảnh báo ở lần chạy đầu tiên; việc bổ sung "
        "chứng thư ký mã vào quy trình là yêu cầu bắt buộc trước khi phân phối "
        "rộng rãi. Thứ hai, dung lượng gói cài đặt ước tính khoảng 250 đến 300 "
        "megabyte, chủ yếu do 121 MB tài nguyên WebAssembly; đây là cái giá "
        "trực tiếp của yêu cầu hoạt động hoàn toàn ngoại tuyến."
    )

    r.h3("4.4. Hoàn thiện giao diện và trải nghiệm người dùng")
    r.p(
        "Phần hoàn thiện giao diện tập trung vào bốn khía cạnh. Khía cạnh thứ "
        "nhất là tính nhất quán: mọi trang công cụ dùng chung một bộ định danh "
        "phần tử, một cơ chế thông báo, một cơ chế chỉ báo tải và một đường "
        "quay lại danh mục. Khía cạnh thứ hai là khả năng thích ứng với kích "
        "thước cửa sổ: thanh bên chuyển thành trình đơn thu gọn trên cửa sổ "
        "hẹp, và lưới thẻ công cụ điều chỉnh số cột theo bề rộng khả dụng."
    )
    r.p(
        "Khía cạnh thứ ba là hỗ trợ thao tác bàn phím thông qua hệ thống phím "
        "tắt có thể tuỳ chỉnh. Khía cạnh thứ tư là ngôn ngữ: toàn bộ giao diện "
        "được dịch sang tiếng Việt với 1.162 khoá, bao gồm cả tên công cụ, mô "
        "tả ngắn, nhãn tham số và thông điệp lỗi."
    )
    r.p(
        "Các hình từ 3.14 tới 3.20 minh hoạ giao diện thực tế của những nhóm "
        "chức năng tiêu biểu. Do hạn chế về môi trường đã nêu ở phần phạm vi "
        "nghiên cứu, những ảnh chụp này cần được bổ sung thủ công trên máy có "
        "giao diện đồ hoạ; mỗi khung giữ chỗ dưới đây nêu rõ trạng thái ứng "
        "dụng và thao tác cần thực hiện để chụp."
    )
    r.placeholder(
        "Hình 3.14",
        "Hình 3.14. Giao diện công cụ ghép tài liệu ở hai chế độ làm việc",
        "Ảnh ghép hai trạng thái của công cụ Merge PDF: (a) chế độ tệp với danh "
        "sách tệp có thể kéo thả và ô nhập khoảng trang; (b) chế độ trang với "
        "lưới ảnh thu nhỏ của tất cả các trang.",
        [
            "Mở công cụ “Merge PDF”.",
            "Nạp ba tệp PDF mẫu có số trang khác nhau (ví dụ 3, 5 và 2 trang).",
            "Chụp ảnh thứ nhất ở chế độ tệp, thấy rõ tay cầm kéo thả, ô nhập "
            "khoảng trang và tổng số trang của từng tệp.",
            "Chuyển sang chế độ trang bằng nút chuyển chế độ.",
            "Chờ ảnh thu nhỏ kết xuất xong, kéo một trang sang vị trí khác.",
            "Chụp ảnh thứ hai ở chế độ trang.",
            "Ghép hai ảnh theo chiều dọc, đặt nhãn (a) và (b).",
        ],
    )
    r.placeholder(
        "Hình 3.15",
        "Hình 3.15. Giao diện công cụ tách và tổ chức lại trang",
        "Giao diện công cụ Split PDF hoặc PDF Multi Tool với một tài liệu đã "
        "nạp, hiển thị lưới ảnh thu nhỏ và các tuỳ chọn tách.",
        [
            "Mở công cụ “Split PDF” (hoặc “PDF Multi Tool”).",
            "Nạp một tệp PDF có ít nhất 8 trang.",
            "Nhập một chuỗi khoảng trang, ví dụ 1-3, 5, 7-8.",
            "Chụp toàn bộ cửa sổ trước khi bấm nút xử lý, thấy rõ ảnh thu nhỏ "
            "và bảng tham số.",
        ],
    )
    r.placeholder(
        "Hình 3.16",
        "Hình 3.16. Giao diện công cụ nén tài liệu và kết quả so sánh dung lượng",
        "Giao diện công cụ Compress PDF thể hiện lựa chọn chiến lược nén, bốn "
        "mức nén, các tham số tuỳ chỉnh và khu vực hiển thị dung lượng trước — "
        "sau khi nén.",
        [
            "Mở công cụ “Compress PDF”.",
            "Nạp một tệp PDF có nhiều ảnh, dung lượng ít nhất 5 MB.",
            "Chọn chiến lược nén và mức “balanced”, mở phần tuỳ chỉnh tham số.",
            "Chạy thao tác nén tới khi hoàn tất.",
            "Chụp màn hình ở trạng thái đã có kết quả, thấy rõ dung lượng trước "
            "và sau cùng tỉ lệ giảm.",
        ],
    )
    r.placeholder(
        "Hình 3.17",
        "Hình 3.17. Giao diện chức năng mã hoá và giải mã tài liệu",
        "Ảnh ghép hai trạng thái: (a) giao diện Encrypt PDF với hai ô nhập mật "
        "khẩu người dùng và mật khẩu chủ sở hữu; (b) hộp thoại yêu cầu nhập mật "
        "khẩu khi nạp một tệp đã mã hoá.",
        [
            "Mở công cụ “Encrypt PDF”, nạp một tệp PDF thường.",
            "Nhập mật khẩu người dùng và mật khẩu chủ sở hữu khác nhau.",
            "Chụp ảnh thứ nhất trước khi bấm nút xử lý.",
            "Thực hiện mã hoá và lưu tệp kết quả.",
            "Mở công cụ “Decrypt PDF” và nạp chính tệp vừa mã hoá.",
            "Chụp ảnh thứ hai khi hộp thoại nhập mật khẩu hiện lên.",
            "Ghép hai ảnh nằm ngang, đặt nhãn (a) và (b).",
        ],
    )
    r.placeholder(
        "Hình 3.18",
        "Hình 3.18. Giao diện chức năng nhận dạng ký tự quang học",
        "Giao diện công cụ OCR PDF thể hiện các tham số (ngôn ngữ, độ phân "
        "giải, nhị phân hoá, chế độ phân đoạn trang) và chỉ báo tiến trình đang "
        "xử lý theo từng trang.",
        [
            "Mở công cụ “OCR PDF”.",
            "Nạp một tệp PDF quét (ảnh, không có lớp văn bản) khoảng 3–5 trang.",
            "Chọn ngôn ngữ “eng”, bật tuỳ chọn nhị phân hoá.",
            "Bấm nút xử lý và chụp màn hình khi chỉ báo tải đang hiển thị dòng "
            "“Processing page x of y”.",
            "Sau khi hoàn tất, mở tệp kết quả và chụp thêm ảnh minh hoạ việc "
            "chọn và sao chép được văn bản trên trang ảnh (tuỳ chọn).",
        ],
    )
    r.placeholder(
        "Hình 3.19",
        "Hình 3.19. Hộp thoại lưu tệp bản địa của hệ điều hành",
        "Hộp thoại “Save As” của hệ điều hành do lệnh save_file mở, hiển thị "
        "tên tệp gợi ý do ứng dụng đặt sẵn.",
        [
            "Thực hiện bất kỳ thao tác nào tạo ra tệp kết quả, ví dụ ghép hai "
            "tệp PDF.",
            "Khi hộp thoại lưu của hệ điều hành hiện ra, KHÔNG bấm lưu ngay.",
            "Chụp toàn màn hình để thấy rõ hộp thoại là hộp thoại bản địa của "
            "hệ điều hành, có tên tệp gợi ý (ví dụ merged.pdf).",
            "Ghi rõ trong chú thích ảnh tên hệ điều hành đã dùng để chụp.",
        ],
    )
    r.placeholder(
        "Hình 3.20",
        "Hình 3.20. Trang cấu hình nguồn mô-đun xử lý và bộ chọn ngôn ngữ",
        "Ảnh ghép hai trạng thái: (a) trang cấu hình mô-đun WASM với ba mục "
        "PyMuPDF, Ghostscript và CoherentPDF cùng nút kiểm tra; (b) bộ chọn "
        "ngôn ngữ trên thanh điều hướng đang mở.",
        [
            "Mở trang cấu hình mô-đun (wasm-settings) từ trình đơn cài đặt.",
            "Chụp ảnh thứ nhất, thấy rõ ba mục mô-đun và trạng thái đã cấu hình.",
            "Quay lại trang chủ, bấm vào bộ chọn ngôn ngữ trên thanh điều hướng.",
            "Chụp ảnh thứ hai khi danh sách ngôn ngữ đang mở, thấy rõ tiếng Việt "
            "đang được chọn.",
            "Ghép hai ảnh nằm ngang, đặt nhãn (a) và (b).",
        ],
    )

    # ==================================================================
    r.h2("Kết luận chương 3")
    r.p(
        "Chương 3 đã trình bày quá trình hiện thực hoá thiết kế đã đề ra ở "
        "Chương 2. Về môi trường, hệ thống dùng hai chuỗi công cụ độc lập cho "
        "tầng web và tầng bản địa, gặp nhau ở bước đóng gói cuối cùng. Cấu trúc "
        "mã nguồn cho thấy rõ tỉ lệ đặc trưng của kiến trúc: 85.570 dòng "
        "TypeScript so với khoảng năm mươi dòng Rust, phản ánh đúng nguyên tắc "
        "tối thiểu hoá bề mặt bản địa."
    )
    r.p(
        "Về xây dựng các thành phần chính, chương đã phân tích khuôn mẫu ba "
        "bước áp dụng cho toàn bộ 127 công cụ, cơ chế dựng màn hình làm việc "
        "động theo danh mục và cấu hình, cơ chế lưu tệp bản địa với cơ chế dự "
        "phòng bảo đảm kết quả không bị mất, và cơ chế đa ngữ kèm phân tích một "
        "sự cố thực tế phát sinh khi bổ sung bản dựng mới. Sự cố này để lại một "
        "bài học đáng ghi nhận về việc bảo vệ hành vi theo đích triển khai bằng "
        "điều kiện trực tiếp thay vì điều kiện gián tiếp."
    )
    r.p(
        "Về xây dựng các mô-đun xử lý, chương đã trình bày cơ chế tổ chức tài "
        "nguyên WebAssembly ngoại tuyến với bằng chứng cụ thể cho từng nhóm "
        "chức năng, hiện thực của bốn nhóm thao tác tiêu biểu, và phân tích chi "
        "tiết chức năng nhận dạng ký tự — chức năng phức tạp nhất về mặt xử lý, "
        "với logic chọn phông theo hệ chữ, cơ chế hạn thời theo trang và kỹ "
        "thuật dựng lớp văn bản vô hình khớp toạ độ."
    )
    r.p(
        "Về triển khai và tối ưu, chương đã tổng hợp bảy cơ chế quản lý dữ liệu "
        "tạm cùng lý do của từng cơ chế, bốn phân loại lỗi cùng cách phản hồi "
        "tương ứng, năm cơ chế suy giảm nhẹ nhàng, và quy trình biên dịch sáu "
        "bước cho ba hệ điều hành. Hai hạn chế của quy trình đóng gói hiện tại "
        "— chưa ký số và dung lượng lớn — đã được nêu rõ cùng nguyên nhân."
    )
    r.p(
        "Phần hoàn thiện giao diện được minh hoạ bằng mười khung giữ chỗ ảnh "
        "chụp màn hình, mỗi khung nêu rõ trạng thái ứng dụng cần đạt tới và "
        "trình tự thao tác để chụp. Việc dùng khung giữ chỗ thay vì ảnh minh "
        "hoạ dựng sẵn là lựa chọn có ý thức nhằm bảo đảm tính trung thực của "
        "báo cáo. Nội dung thử nghiệm và đánh giá được trình bày ở Chương 4."
    )
