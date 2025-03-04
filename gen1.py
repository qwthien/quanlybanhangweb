import firebirdsql
from faker import Faker
import random
from datetime import datetime, timedelta

# Khởi tạo Faker với ngôn ngữ tiếng Việt
fake = Faker('vi_VN')

# Thông tin kết nối Firebird
DATABASE_PATH = "C:/FirebirdData/QLBH1.FDB"  # Thay bằng đường dẫn đầy đủ đến file QLBH1.FDB
USER = "SYSDBA"  # Thay bằng tên người dùng Firebird của bạn (e.g., "SYSDBA")
PASSWORD = "123"  # Thay bằng mật khẩu của bạn (e.g., "masterkey")
HOST = "localhost"  # Hoặc địa chỉ máy chủ Firebird nếu không chạy cục bộ
PORT = 3050  # Cổng mặc định của Firebird

# Hàm tạo kết nối đến Firebird
def get_firebird_connection():
    try:
        conn = firebirdsql.connect(
            host=HOST,
            database=DATABASE_PATH,
            user=USER,
            password=PASSWORD,
            port=PORT,
            charset='UTF8'  # Đảm bảo sử dụng UTF-8 để xử lý ký tự Unicode
        )
        return conn
    except firebirdsql.Error as e:
        print(f"Error connecting to Firebird: {e}")
        return None

# Hàm sinh và chèn dữ liệu trực tiếp vào Firebird
def generate_and_insert_data():
    conn = get_firebird_connection()
    if conn is None:
        return

    cursor = conn.cursor()

    # Danh sách tên sản phẩm giả lập
    products = ['Sữa tươi', 'Bánh mì', 'Nước ngọt', 'Gạo', 'Trứng gà', 'Thịt bò', 'Cá hồi', 'Rau củ', 'Trái cây', 'Đồ uống']
    
    # Danh sách loại sản phẩm
    product_types = ['Thực phẩm', 'Đồ uống', 'Hàng tiêu dùng', 'Sản phẩm tươi sống']
    
    # Danh sách các vai trò tài khoản
    roles = ['Quản lý', 'Nhân viên bán hàng', 'Kế toán', 'Kho']

    # 1. Chèn dữ liệu cho TAI_KHOAN (100 dòng)
    tai_khoan_data = []
    for i in range(1, 101):
        username = f"user{i}"
        password = fake.password(length=10)
        role = random.choice(roles)
        tai_khoan_data.append((i, username, password, role))  # ID_TK, TEN_DANG_NHAP, MAT_KHAU, MAT_KHAU_VARCHAR
    
    cursor.executemany('''
        INSERT INTO TAI_KHOAN (ID_TK, TEN_DANG_NHAP, MAT_KHAU, MAT_KHAU_VARCHAR) 
        VALUES (?, ?, ?, ?)
    ''', tai_khoan_data)

    # 2. Chèn dữ liệu cho NHAN_VIEN (100 dòng, liên kết với TAI_KHOAN)
    nhan_vien_data = []
    for i in range(1, 101):
        id_tk = i
        ten_nv = fake.name()
        sdt_nv = fake.phone_number()
        nhan_vien_data.append((i, ten_nv, sdt_nv, id_tk))  # ID_NV, TEN_NV, SDT_NV, ID_TK
    
    cursor.executemany('''
        INSERT INTO NHAN_VIEN (ID_NV, TEN_NV, SDT_NV, ID_TK) 
        VALUES (?, ?, ?, ?)
    ''', nhan_vien_data)

    # 3. Chèn dữ liệu cho NHA_CUNG_CAP (100 dòng)
    nha_cung_cap_data = []
    for i in range(1, 101):
        ten_ncc = fake.company()
        sdt_ncc = fake.phone_number()
        nha_cung_cap_data.append((i, ten_ncc, sdt_ncc))  # ID_NCC, TEN_NCC, SDT_NCC
    
    cursor.executemany('''
        INSERT INTO NHA_CUNG_CAP (ID_NCC, TEN_NCC, SDT_NCC) 
        VALUES (?, ?, ?)
    ''', nha_cung_cap_data)

    # 4. Chèn dữ liệu cho LOAI_SAN_PHAM (100 dòng)
    loai_san_pham_data = []
    for i in range(1, 101):
        ten_loai = random.choice(product_types)
        mo_ta = f"Mô tả cho {ten_loai}"
        loai_san_pham_data.append((i, ten_loai, mo_ta))  # ID_LOAI, TEN_LOAI, MO_TA
    
    cursor.executemany('''
        INSERT INTO LOAI_SAN_PHAM (ID_LOAI, TEN_LOAI, MO_TA) 
        VALUES (?, ?, ?)
    ''', loai_san_pham_data)

    # 5. Chèn dữ liệu cho CHI_TIET_PHIEU_NHAP (100 dòng, liên kết với NHAN_VIEN và NHA_CUNG_CAP)
    start_date = datetime(2024, 1, 1)
    chi_tiet_phieu_nhap_data = []
    for i in range(1, 101):
        id_pn = i
        id_nv = random.randint(1, 100)  # Liên kết với NHAN_VIEN
        id_ncc = random.randint(1, 100)  # Liên kết với NHA_CUNG_CAP
        ngay_nhap = start_date + timedelta(days=random.randint(0, 425))  # Từ 2024-01-01 đến 2025-02-25
        tong_tien = round(random.uniform(100000, 5000000), 2)  # Số tiền ngẫu nhiên
        chi_tiet_phieu_nhap_data.append((id_pn, id_nv, id_ncc, ngay_nhap, tong_tien))  # ID_PN, ID_NV, ID_NCC, NGAY_NHAP, TONG_TIEN
    
    cursor.executemany('''
        INSERT INTO CHI_TIET_PHIEU_NHAP (ID_PN, ID_NV, ID_NCC, NGAY_NHAP, TONG_TIEN) 
        VALUES (?, ?, ?, ?, ?)
    ''', chi_tiet_phieu_nhap_data)

    # 6. Chèn dữ liệu cho CHI_TIET_HOA_DON (100 dòng, liên kết với NHAN_VIEN và LOAI_SAN_PHAM)
    chi_tiet_hoa_don_data = []
    for i in range(1, 101):
        id_cthd = i
        id_nv = random.randint(1, 100)  # Liên kết với NHAN_VIEN
        id_sp = random.randint(1, 100)  # Liên kết với LOAI_SAN_PHAM
        so_luong = random.randint(1, 100)
        don_gia = round(random.uniform(5000, 500000), 2)
        tong_tien = round(so_luong * don_gia, 2)
        chi_tiet_hoa_don_data.append((id_cthd, id_nv, id_sp, so_luong, don_gia, tong_tien))  # ID_CTHD, ID_NV, ID_SP, SO_LUONG, DON_GIA, TONG_TIEN
    
    cursor.executemany('''
        INSERT INTO CHI_TIET_HOA_DON (ID_CTHD, ID_NV, ID_SP, SO_LUONG, DON_GIA, TONG_TIEN) 
        VALUES (?, ?, ?, ?, ?, ?)
    ''', chi_tiet_hoa_don_data)

    # Commit và đóng kết nối
    conn.commit()
    cursor.close()
    conn.close()
    print("Dữ liệu đã được chèn trực tiếp vào file QLBH1.FDB thành công!")

if __name__ == "__main__":
    generate_and_insert_data()