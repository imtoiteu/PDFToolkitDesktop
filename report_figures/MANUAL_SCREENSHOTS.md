# MANUAL SCREENSHOTS — danh sách ảnh cần chụp thủ công

Báo cáo `BAO_CAO_DE_TAI_PDFTOOLKIT_DESKTOP.docx` hiện có **11 khung giữ chỗ** cho ảnh chụp giao diện. Các ảnh này không thể chụp tự động trên máy chủ phân tích vì máy không có giao diện đồ hoạ và không đủ tài nguyên để biên dịch ứng dụng (chi tiết ở Bảng 4.1 của báo cáo).

## Chuẩn bị chung

1. Dùng máy có giao diện đồ hoạ, cài **Node.js ≥ 20** và **Rust ≥ 1.77.2**.
2. Cài phụ thuộc hệ thống theo nền tảng (xem `DESKTOP.md`).
3. Chạy `npm install`, sau đó `npm run tauri:dev` để chạy bản phát triển, hoặc `npm run tauri:build` rồi cài đặt gói sinh ra.
4. Đặt ngôn ngữ giao diện là **tiếng Việt** trước khi chụp, để ảnh khớp với nội dung báo cáo.
5. Chuẩn bị sẵn bộ tệp mẫu theo Bảng 4.2 của báo cáo.
6. Chụp ở độ phân giải tối thiểu **1600 × 1000** để chữ trong ảnh còn đọc được khi in, lưu ở định dạng **PNG**.
7. Đặt tệp ảnh vào thư mục `report_figures/screenshots/` theo đúng tên gợi ý ở từng mục dưới đây.

## Danh sách ảnh cần chụp

### Hình 3.3

**Chú thích trong báo cáo:** Hình 3.3. Màn hình làm việc chính của PDF Toolkit Desktop

**Tên tệp gợi ý:** `screenshots/hinh_3_3.png`

**Nội dung cần thể hiện:** Toàn bộ cửa sổ ứng dụng ở trạng thái vừa khởi động, hiển thị thanh bên danh mục bên trái và lưới thẻ công cụ của nhóm “Công cụ phổ biến”.

**Các bước thực hiện:**

1. Khởi chạy ứng dụng đã đóng gói (hoặc chạy lệnh npm run tauri:dev).
2. Chờ giao diện nạp xong, xác nhận ngôn ngữ đang là tiếng Việt.
3. Không mở công cụ nào, giữ nguyên nhóm mặc định “Công cụ phổ biến”.
4. Chụp toàn bộ cửa sổ ứng dụng kèm thanh tiêu đề của hệ điều hành để thấy rõ đây là ứng dụng bản địa chứ không phải tab trình duyệt.

### Hình 3.4

**Chú thích trong báo cáo:** Hình 3.4. Thanh bên danh mục và chức năng tìm kiếm công cụ

**Tên tệp gợi ý:** `screenshots/hinh_3_4.png`

**Nội dung cần thể hiện:** Ảnh ghép hai trạng thái: (a) thanh bên với bảy nhóm và số lượng công cụ của từng nhóm; (b) kết quả lọc sau khi gõ một từ khoá vào ô tìm kiếm.

**Các bước thực hiện:**

1. Chụp ảnh thứ nhất: cận cảnh thanh bên, thấy rõ tên bảy nhóm kèm số đếm và nhóm đang được chọn.
2. Gõ từ khoá “ghép” (hoặc “merge”) vào ô tìm kiếm ở đầu vùng nội dung.
3. Chụp ảnh thứ hai: lưới thẻ công cụ đã được lọc theo từ khoá.
4. Ghép hai ảnh nằm ngang, đặt nhãn (a) và (b) bên dưới mỗi ảnh.

### Hình 3.10

**Chú thích trong báo cáo:** Hình 3.10. Giao diện trình dựng luồng xử lý tự động

**Tên tệp gợi ý:** `screenshots/hinh_3_10.png`

**Nội dung cần thể hiện:** Vùng làm việc của trình dựng luồng với một đồ thị hoàn chỉnh gồm ít nhất bốn nút được nối thành chuỗi, thể hiện rõ các cổng vào/ra và đường kết nối.

**Các bước thực hiện:**

1. Mở công cụ “PDF Workflow Builder” từ nhóm Công cụ phổ biến.
2. Kéo vào vùng làm việc các nút: PDF Input → Merge → Watermark → Download PDF.
3. Nối các nút thành chuỗi và nạp hai tệp PDF mẫu vào nút đầu vào.
4. Chạy luồng và chụp màn hình ở thời điểm một nút đang ở trạng thái “đang chạy” để thấy chỉ báo trạng thái trên nút.
5. Chụp toàn bộ cửa sổ ứng dụng.

### Hình 3.14

**Chú thích trong báo cáo:** Hình 3.14. Giao diện công cụ ghép tài liệu ở hai chế độ làm việc

**Tên tệp gợi ý:** `screenshots/hinh_3_14.png`

**Nội dung cần thể hiện:** Ảnh ghép hai trạng thái của công cụ Merge PDF: (a) chế độ tệp với danh sách tệp có thể kéo thả và ô nhập khoảng trang; (b) chế độ trang với lưới ảnh thu nhỏ của tất cả các trang.

**Các bước thực hiện:**

1. Mở công cụ “Merge PDF”.
2. Nạp ba tệp PDF mẫu có số trang khác nhau (ví dụ 3, 5 và 2 trang).
3. Chụp ảnh thứ nhất ở chế độ tệp, thấy rõ tay cầm kéo thả, ô nhập khoảng trang và tổng số trang của từng tệp.
4. Chuyển sang chế độ trang bằng nút chuyển chế độ.
5. Chờ ảnh thu nhỏ kết xuất xong, kéo một trang sang vị trí khác.
6. Chụp ảnh thứ hai ở chế độ trang.
7. Ghép hai ảnh theo chiều dọc, đặt nhãn (a) và (b).

### Hình 3.15

**Chú thích trong báo cáo:** Hình 3.15. Giao diện công cụ tách và tổ chức lại trang

**Tên tệp gợi ý:** `screenshots/hinh_3_15.png`

**Nội dung cần thể hiện:** Giao diện công cụ Split PDF hoặc PDF Multi Tool với một tài liệu đã nạp, hiển thị lưới ảnh thu nhỏ và các tuỳ chọn tách.

**Các bước thực hiện:**

1. Mở công cụ “Split PDF” (hoặc “PDF Multi Tool”).
2. Nạp một tệp PDF có ít nhất 8 trang.
3. Nhập một chuỗi khoảng trang, ví dụ 1-3, 5, 7-8.
4. Chụp toàn bộ cửa sổ trước khi bấm nút xử lý, thấy rõ ảnh thu nhỏ và bảng tham số.

### Hình 3.16

**Chú thích trong báo cáo:** Hình 3.16. Giao diện công cụ nén tài liệu và kết quả so sánh dung lượng

**Tên tệp gợi ý:** `screenshots/hinh_3_16.png`

**Nội dung cần thể hiện:** Giao diện công cụ Compress PDF thể hiện lựa chọn chiến lược nén, bốn mức nén, các tham số tuỳ chỉnh và khu vực hiển thị dung lượng trước — sau khi nén.

**Các bước thực hiện:**

1. Mở công cụ “Compress PDF”.
2. Nạp một tệp PDF có nhiều ảnh, dung lượng ít nhất 5 MB.
3. Chọn chiến lược nén và mức “balanced”, mở phần tuỳ chỉnh tham số.
4. Chạy thao tác nén tới khi hoàn tất.
5. Chụp màn hình ở trạng thái đã có kết quả, thấy rõ dung lượng trước và sau cùng tỉ lệ giảm.

### Hình 3.17

**Chú thích trong báo cáo:** Hình 3.17. Giao diện chức năng mã hoá và giải mã tài liệu

**Tên tệp gợi ý:** `screenshots/hinh_3_17.png`

**Nội dung cần thể hiện:** Ảnh ghép hai trạng thái: (a) giao diện Encrypt PDF với hai ô nhập mật khẩu người dùng và mật khẩu chủ sở hữu; (b) hộp thoại yêu cầu nhập mật khẩu khi nạp một tệp đã mã hoá.

**Các bước thực hiện:**

1. Mở công cụ “Encrypt PDF”, nạp một tệp PDF thường.
2. Nhập mật khẩu người dùng và mật khẩu chủ sở hữu khác nhau.
3. Chụp ảnh thứ nhất trước khi bấm nút xử lý.
4. Thực hiện mã hoá và lưu tệp kết quả.
5. Mở công cụ “Decrypt PDF” và nạp chính tệp vừa mã hoá.
6. Chụp ảnh thứ hai khi hộp thoại nhập mật khẩu hiện lên.
7. Ghép hai ảnh nằm ngang, đặt nhãn (a) và (b).

### Hình 3.18

**Chú thích trong báo cáo:** Hình 3.18. Giao diện chức năng nhận dạng ký tự quang học

**Tên tệp gợi ý:** `screenshots/hinh_3_18.png`

**Nội dung cần thể hiện:** Giao diện công cụ OCR PDF thể hiện các tham số (ngôn ngữ, độ phân giải, nhị phân hoá, chế độ phân đoạn trang) và chỉ báo tiến trình đang xử lý theo từng trang.

**Các bước thực hiện:**

1. Mở công cụ “OCR PDF”.
2. Nạp một tệp PDF quét (ảnh, không có lớp văn bản) khoảng 3–5 trang.
3. Chọn ngôn ngữ “eng”, bật tuỳ chọn nhị phân hoá.
4. Bấm nút xử lý và chụp màn hình khi chỉ báo tải đang hiển thị dòng “Processing page x of y”.
5. Sau khi hoàn tất, mở tệp kết quả và chụp thêm ảnh minh hoạ việc chọn và sao chép được văn bản trên trang ảnh (tuỳ chọn).

### Hình 3.19

**Chú thích trong báo cáo:** Hình 3.19. Hộp thoại lưu tệp bản địa của hệ điều hành

**Tên tệp gợi ý:** `screenshots/hinh_3_19.png`

**Nội dung cần thể hiện:** Hộp thoại “Save As” của hệ điều hành do lệnh save_file mở, hiển thị tên tệp gợi ý do ứng dụng đặt sẵn.

**Các bước thực hiện:**

1. Thực hiện bất kỳ thao tác nào tạo ra tệp kết quả, ví dụ ghép hai tệp PDF.
2. Khi hộp thoại lưu của hệ điều hành hiện ra, KHÔNG bấm lưu ngay.
3. Chụp toàn màn hình để thấy rõ hộp thoại là hộp thoại bản địa của hệ điều hành, có tên tệp gợi ý (ví dụ merged.pdf).
4. Ghi rõ trong chú thích ảnh tên hệ điều hành đã dùng để chụp.

### Hình 3.20

**Chú thích trong báo cáo:** Hình 3.20. Trang cấu hình nguồn mô-đun xử lý và bộ chọn ngôn ngữ

**Tên tệp gợi ý:** `screenshots/hinh_3_20.png`

**Nội dung cần thể hiện:** Ảnh ghép hai trạng thái: (a) trang cấu hình mô-đun WASM với ba mục PyMuPDF, Ghostscript và CoherentPDF cùng nút kiểm tra; (b) bộ chọn ngôn ngữ trên thanh điều hướng đang mở.

**Các bước thực hiện:**

1. Mở trang cấu hình mô-đun (wasm-settings) từ trình đơn cài đặt.
2. Chụp ảnh thứ nhất, thấy rõ ba mục mô-đun và trạng thái đã cấu hình.
3. Quay lại trang chủ, bấm vào bộ chọn ngôn ngữ trên thanh điều hướng.
4. Chụp ảnh thứ hai khi danh sách ngôn ngữ đang mở, thấy rõ tiếng Việt đang được chọn.
5. Ghép hai ảnh nằm ngang, đặt nhãn (a) và (b).

### Hình 4.4

**Chú thích trong báo cáo:** Hình 4.4. Kiểm chứng khả năng hoạt động ngoại tuyến qua tab mạng của công cụ phát triển

**Tên tệp gợi ý:** `screenshots/hinh_4_4.png`

**Nội dung cần thể hiện:** Cửa sổ ứng dụng đặt cạnh bảng công cụ phát triển đang mở tab Network, sau khi đã thực hiện xong một thao tác lõi, cho thấy không có yêu cầu nào tới máy chủ bên ngoài.

**Các bước thực hiện:**

1. Chạy ứng dụng ở chế độ phát triển (npm run tauri:dev) để mở được công cụ phát triển của WebView.
2. Bấm chuột phải trong cửa sổ ứng dụng và chọn Inspect, chuyển sang tab Network.
3. Xoá danh sách yêu cầu hiện có, sau đó thực hiện một thao tác lõi (ví dụ Merge PDF hoặc Compress PDF).
4. Chờ thao tác hoàn tất, KHÔNG lọc danh sách yêu cầu.
5. Chụp toàn màn hình, bảo đảm nhìn rõ toàn bộ danh sách yêu cầu và thấy rằng không có mục nào trỏ tới cdn.jsdelivr.net hay bất kỳ máy chủ từ xa nào.
6. Lặp lại quy trình sau khi ngắt kết nối mạng và chụp thêm một ảnh cho thấy thao tác vẫn hoàn thành.

## Cách chèn ảnh vào báo cáo

Có hai cách. Cách thủ công: mở tệp Word, tìm khung màu cam có dòng `[CHỖ DÀNH CHO ẢNH CHỤP MÀN HÌNH – Hình x.y]`, xoá khung đó và chèn ảnh vào đúng vị trí, giữ nguyên dòng chú thích bên dưới.

Cách tự động: đặt các tệp ảnh vào `report_figures/screenshots/` theo đúng tên gợi ý, sau đó sửa lời gọi `r.placeholder(...)` tương ứng trong `report_figures/tools/content_c.py` và `content_d.py` thành `r.screenshot("hinh_x_y.png", "<chú thích>")` rồi chạy lại `python3 make_report.py`.

