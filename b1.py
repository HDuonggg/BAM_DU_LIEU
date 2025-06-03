import hashlib

def hash_sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

def hash_sha512(data):
    return hashlib.sha512(data.encode()).hexdigest()

if __name__ == "__main__":
    # Nhập dữ liệu gốc
    original = input("Nhập dữ liệu gốc: ")
    print("Dữ liệu gốc:", original)
    print("SHA-256:", hash_sha256(original))
    print("SHA-512:", hash_sha512(original))

    # Nhập dữ liệu đã sửa
    modified = input("\nNhập dữ liệu đã sửa: ")
    print("\nDữ liệu đã sửa:", modified)
    print("SHA-256:", hash_sha256(modified))
    print("SHA-512:", hash_sha512(modified))