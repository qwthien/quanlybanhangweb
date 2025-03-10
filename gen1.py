import random
from datetime import datetime, timedelta
from faker import Faker

# Khởi tạo Faker với ngôn ngữ tiếng Việt
fake = Faker('vi_VN')

# Danh sách tên sản phẩm giả lập
products = ['Sữa tươi', 'Bánh mì', 'Nước ngọt', 'Gạo', 'Trứng gà', 'Thịt bò', 'Cá hồi', 'Rau củ', 'Trái cây', 'Đồ uống']
    
# Danh sách loại sản phẩm
product_types = ['Thực phẩm', 'Đồ uống', 'Hàng tiêu dùng', 'Sản phẩm tươi sống']
    
# Danh sách các vai trò tài khoản
roles = ['Quản lý', 'Nhân viên bán hàng', 'Kế toán', 'Kho']

# Hàm sinh dữ liệu và ghi vào file .txt
def generate_insert_queries():
    # Mở file .txt để ghi
    with open("insert_queries.txt", "w", encoding="utf-8") as file:
        
        # 1. Chèn dữ liệu cho TAI_KHOAN (100 dòng)
        for i in range(1, 101):
            username = f"user{i}"
            password = fake.password(length=10)
            role = random.choice(roles)
            file.write(f"INSERT INTO TAI_KHOAN (TEN_DANG_NHAP, MAT_KHAU, TEN_DANG_NHAP) VALUES ('{username}', '{password}', '{role}');\n")

        # 2. Chèn dữ liệu cho LOAI_SAN_PHAM (100 dòng)
        for i in range(1, 101):
            ten_loai = random.choice(product_types)
            mo_ta = f"Mô tả cho {ten_loai}"
            file.write(f"INSERT INTO LOAI_SAN_PHAM (TEN_LOAI, MO_TA) VALUES ('{ten_loai}', '{mo_ta}');\n")

        # 3. Chèn dữ liệu cho NHA_CUNG_CAP (100 dòng)
        for i in range(1, 101):
            ten_ncc = fake.company()
            sdt_ncc = fake.phone_number()
            file.write(f"INSERT INTO NHA_CUNG_CAP (TEN_NCC, SDT_NCC) VALUES ('{ten_ncc}', '{sdt_ncc}');\n")

        # 4. Chèn dữ liệu cho NHAN_VIEN (100 dòng, liên kết với TAI_KHOAN)
        for i in range(1, 101):
            id_tk = i
            ten_nv = fake.name()
            sdt_nv = fake.phone_number()
            file.write(f"INSERT INTO NHAN_VIEN (TEN_NV, SDT_NV, ID_TK) VALUES ('{ten_nv}', '{sdt_nv}', {id_tk});\n")

        # 5. Chèn dữ liệu cho SAN_PHAM (100 dòng, liên kết với LOAI_SAN_PHAM)
        for i in range(1, 101):
            ten_sp = random.choice(products)
            gia_sp = round(random.uniform(10000, 100000), 2)
            id_loai = random.randint(1, 100)  # Liên kết với LOAI_SAN_PHAM
            file.write(f"INSERT INTO SAN_PHAM (TEN_SP, GIA, ID_LOAI) VALUES ('{ten_sp}', {gia_sp}, {id_loai});\n")

        # 6. Chèn dữ liệu cho PHIEU_NHAP (100 dòng, liên kết với NHAN_VIEN và NHA_CUNG_CAP)
        start_date = datetime(2024, 1, 1)
        for i in range(1, 101):
            id_nv = random.randint(1, 100)  # Liên kết với NHAN_VIEN
            id_ncc = random.randint(1, 100)  # Liên kết với NHA_CUNG_CAP
            ngay_nhap = start_date + timedelta(days=random.randint(0, 425))  # Từ 2024-01-01 đến 2025-02-25
            tong_tien = round(random.uniform(100000, 5000000), 2)  # Số tiền ngẫu nhiên
            file.write(f"INSERT INTO PHIEU_NHAP (ID_NV, ID_NCC, NGAY_NHAP, TONG_TIEN) VALUES ({id_nv}, {id_ncc}, '{ngay_nhap.strftime('%Y-%m-%d')}', {tong_tien});\n")

        # 7. Chèn dữ liệu cho HOA_DON (100 dòng, liên kết với KHACH_HANG)
        for i in range(1, 101):
            id_kh = random.randint(1, 100)  # Liên kết với KHACH_HANG
            ngay_lap = start_date + timedelta(days=random.randint(0, 425))  # Từ 2024-01-01 đến 2025-02-25
            tong_tien = round(random.uniform(100000, 5000000), 2)  # Số tiền ngẫu nhiên
            file.write(f"INSERT INTO HOA_DON (ID_KH, NGAY_LAP, TONG_TIEN) VALUES ({id_kh}, '{ngay_lap.strftime('%Y-%m-%d')}', {tong_tien});\n")

        # 8. Chèn dữ liệu cho CHI_TIET_HOA_DON (100 dòng, liên kết với HOA_DON và SAN_PHAM)
        for i in range(1, 101):
            id_hd = random.randint(1, 100)  # Liên kết với HOA_DON
            id_sp = random.randint(1, 100)  # Liên kết với SAN_PHAM
            so_luong = random.randint(1, 100)
            don_gia = round(random.uniform(5000, 500000), 2)
            tong_tien = round(so_luong * don_gia, 2)
            file.write(f"INSERT INTO CHI_TIET_HOA_DON (ID_HD, ID_SP, SO_LUONG, DON_GIA, TONG_TIEN) VALUES ({id_hd}, {id_sp}, {so_luong}, {don_gia}, {tong_tien});\n")

        # 9. Chèn dữ liệu cho CHI_TIET_PHIEU_NHAP (100 dòng, liên kết với PHIEU_NHAP và SAN_PHAM)
        for i in range(1, 101):
            id_pn = random.randint(1, 100)  # Liên kết với PHIEU_NHAP
            id_sp = random.randint(1, 100)  # Liên kết với SAN_PHAM
            so_luong = random.randint(1, 100)
            don_gia = round(random.uniform(5000, 500000), 2)
            tong_tien = round(so_luong * don_gia, 2)
            file.write(f"INSERT INTO CHI_TIET_PHIEU_NHAP (ID_PN, ID_SP, SO_LUONG, DON_GIA, TONG_TIEN) VALUES ({id_pn}, {id_sp}, {so_luong}, {don_gia}, {tong_tien});\n")

        # 10. Chèn dữ liệu vào bảng `products` và `product_types`
        # Dữ liệu bảng `products` (Sản phẩm)
        for product in products:
            file.write(f"INSERT INTO PRODUCTS (PRODUCT_NAME) VALUES ('{product}');\n")

        # Dữ liệu bảng `product_types` (Loại sản phẩm)
        for product_type in product_types:
            file.write(f"INSERT INTO PRODUCT_TYPES (TYPE_NAME) VALUES ('{product_type}');\n")

        # Dữ liệu bảng `roles` (Vai trò tài khoản)
        for role in roles:
            file.write(f"INSERT INTO ROLES (ROLE_NAME) VALUES ('{role}');\n")

    print("Dữ liệu đã được ghi vào file insert_queries.txt thành công!")

if __name__ == "__main__":
    generate_insert_queries()
