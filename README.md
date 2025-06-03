# Image Integrity Checker

## 1. Bài 1: Băm dữ liệu văn bản bằng SHA-256 và SHA-512

**Mô tả:**  
Chương trình cho phép nhập dữ liệu gốc và dữ liệu đã sửa, sau đó tính toán và hiển thị giá trị băm SHA-256 và SHA-512 cho từng dữ liệu. Qua đó, bạn có thể kiểm tra sự thay đổi của dữ liệu thông qua giá trị băm.

**Cách sử dụng:**
1. Mở terminal/cmd, di chuyển đến thư mục chứa file `b1.py`.
2. Chạy lệnh:
   ```
   python b1.py
   ```
3. Nhập dữ liệu gốc và dữ liệu đã sửa theo hướng dẫn trên màn hình.
4. So sánh giá trị băm để kiểm tra tính toàn vẹn dữ liệu.

---

## 2. Bài 2: Kiểm tra tính toàn vẹn file ảnh bằng SHA-512

**Mô tả:**  
Chương trình tính giá trị băm SHA-512 của một file ảnh (ví dụ: `1.jpg`). Giá trị băm này giúp kiểm tra tính toàn vẹn của file ảnh, phát hiện thay đổi hoặc hỏng file.

**Cách sử dụng:**
1. Đảm bảo file ảnh (ví dụ: `1.jpg`) nằm cùng thư mục với file `b2.py`.
2. Mở terminal/cmd, di chuyển đến thư mục chứa file `b2.py`.
3. Chạy lệnh:
   ```
   python b2.py
   ```
4. Chương trình sẽ hiển thị giá trị SHA-512 của file ảnh. Nếu file không tồn tại, sẽ có thông báo lỗi.

---

## Ứng dụng

- Kiểm tra tính toàn vẹn dữ liệu văn bản và file ảnh.
- Phát hiện thay đổi, chỉnh sửa hoặc hỏng dữ liệu thông qua giá trị băm.

---

## Yêu cầu

- Python 3.x
- Thư viện chuẩn `hashlib` (có sẵn trong Python)

---

## Liên hệ

Mọi thắc mắc vui lòng liên hệ qua sansieuga02@gmail.com hoặc GitHub.
[Dương Huy Hoàng - CNTT17-07]
