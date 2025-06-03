import hashlib
import os

def get_file_sha512(filepath):
    """Tính giá trị băm SHA-512 của file."""
    sha512 = hashlib.sha512()
    try:
        with open(filepath, "rb") as f:
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break
                sha512.update(chunk)
        return sha512.hexdigest()
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{filepath}'.")
        return None
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        return None

if __name__ == "__main__":
    file_path = "1.jpg"  # Đường dẫn file ảnh

    if not os.path.isfile(file_path):
        print(f"File '{file_path}' không tồn tại.")
    else:
        hash_value = get_file_sha512(file_path)
        if hash_value:
            print(f"Giá trị SHA-512 của file '{file_path}':\n{hash_value}")
        else:
            print("Không thể tính giá trị SHA-512 cho file này.")