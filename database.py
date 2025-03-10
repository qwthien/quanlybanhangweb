import fdb

# Cấu hình kết nối với cơ sở dữ liệu Firebird
DB_CONFIG = {
    "dsn": r"localhost:C:\FirebirdData\QLBH1.FDB",  # Đảm bảo đường dẫn đúng
    "user": "sysdba",
    "password": "123",
    "charset": "UTF8"
}

def get_connection():
    """Tạo kết nối đến Firebird"""
    return fdb.connect(**DB_CONFIG)

# Các hàm truy vấn dữ liệu

def get_san_pham():
    """Lấy danh sách sản phẩm"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM SAN_PHAM")
    result = cur.fetchall()
    conn.close()
    return result

def get_loai_san_pham():
    """Lấy danh sách loại sản phẩm"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM LOAI_SAN_PHAM")
    result = cur.fetchall()
    conn.close()
    return result

def get_nha_cung_cap():
    """Lấy danh sách nhà cung cấp"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM NHA_CUNG_CAP")
    result = cur.fetchall()
    conn.close()
    return result

def get_khach_hang():
    """Lấy danh sách khách hàng"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM KHACH_HANG")
    result = cur.fetchall()
    conn.close()
    return result

def get_nhan_vien():
    """Lấy danh sách nhân viên"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM NHAN_VIEN")
    result = cur.fetchall()
    conn.close()
    return result

def get_hoa_don():
    """Lấy danh sách hóa đơn"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM HOA_DON")
    result = cur.fetchall()
    conn.close()
    return result

def get_phieu_nhap():
    """Lấy danh sách phiếu nhập"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM PHIEU_NHAP")
    result = cur.fetchall()
    conn.close()
    return result

# Các hàm thêm, xóa, sửa

def them_san_pham(ten_sp, id_loai, id_ncc, gia):
    """Thêm sản phẩm mới vào cơ sở dữ liệu"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO SAN_PHAM (TEN_SP, ID_LOAI, ID_NCC, GIA) VALUES (?, ?, ?, ?)",
                (ten_sp, id_loai, id_ncc, gia))
    conn.commit()
    conn.close()

def xoa_san_pham(id_sp):
    """Xóa sản phẩm khỏi cơ sở dữ liệu"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM SAN_PHAM WHERE ID_SP = ?", (id_sp,))
    conn.commit()
    conn.close()

def sua_san_pham(id_sp, ten_sp, id_loai, id_ncc, gia):
    """Cập nhật thông tin sản phẩm"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE SAN_PHAM SET TEN_SP = ?, ID_LOAI = ?, ID_NCC = ?, GIA = ? WHERE ID_SP = ?",
                (ten_sp, id_loai, id_ncc, gia, id_sp))
    conn.commit()
    conn.close()

def them_loai_san_pham(ten_loai):
    """Thêm loại sản phẩm mới vào cơ sở dữ liệu"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO LOAI_SAN_PHAM (TEN_LOAI) VALUES (?)", (ten_loai,))
    conn.commit()
    conn.close()

def xoa_loai_san_pham(id_loai):
    """Xóa loại sản phẩm khỏi cơ sở dữ liệu"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM LOAI_SAN_PHAM WHERE ID_LOAI = ?", (id_loai,))
    conn.commit()
    conn.close()

def sua_loai_san_pham(id_loai, ten_loai):
    """Cập nhật thông tin loại sản phẩm"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE LOAI_SAN_PHAM SET TEN_LOAI = ? WHERE ID_LOAI = ?", (ten_loai, id_loai))
    conn.commit()
    conn.close()

def them_nha_cung_cap(ten_ncc, sdt_ncc, dia_chi):
    """Thêm nhà cung cấp mới vào cơ sở dữ liệu"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO NHA_CUNG_CAP (TEN_NCC, SDT_NCC, DIA_CHI) VALUES (?, ?, ?)",
                (ten_ncc, sdt_ncc, dia_chi))
    conn.commit()
    conn.close()

def xoa_nha_cung_cap(id_ncc):
    """Xóa nhà cung cấp khỏi cơ sở dữ liệu"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM NHA_CUNG_CAP WHERE ID_NCC = ?", (id_ncc,))
    conn.commit()
    conn.close()

def sua_nha_cung_cap(id_ncc, ten_ncc, sdt_ncc, dia_chi):
    """Cập nhật thông tin nhà cung cấp"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE NHA_CUNG_CAP SET TEN_NCC = ?, SDT_NCC = ?, DIA_CHI = ? WHERE ID_NCC = ?",
                (ten_ncc, sdt_ncc, dia_chi, id_ncc))
    conn.commit()
    conn.close()

def them_khach_hang(ten_kh, sdt_kh, dia_chi):
    """Thêm khách hàng mới vào cơ sở dữ liệu"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO KHACH_HANG (TEN_KH, SDT_KH, DIA_CHI) VALUES (?, ?, ?)",
                (ten_kh, sdt_kh, dia_chi))
    conn.commit()
    conn.close()

def xoa_khach_hang(id_kh):
    """Xóa khách hàng khỏi cơ sở dữ liệu"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM KHACH_HANG WHERE ID_KH = ?", (id_kh,))
    conn.commit()
    conn.close()

def sua_khach_hang(id_kh, ten_kh, sdt_kh, dia_chi):
    """Cập nhật thông tin khách hàng"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE KHACH_HANG SET TEN_KH = ?, SDT_KH = ?, DIA_CHI = ? WHERE ID_KH = ?",
                (ten_kh, sdt_kh, dia_chi, id_kh))
    conn.commit()
    conn.close()

def them_nhan_vien(ten_nv, sdt_nv, id_tk):
    """Thêm nhân viên mới vào cơ sở dữ liệu"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO NHAN_VIEN (TEN_NV, SDT_NV, ID_TK) VALUES (?, ?, ?)",
                (ten_nv, sdt_nv, id_tk))
    conn.commit()
    conn.close()

def xoa_nhan_vien(id_nv):
    """Xóa nhân viên khỏi cơ sở dữ liệu"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM NHAN_VIEN WHERE ID_NV = ?", (id_nv,))
    conn.commit()
    conn.close()

def sua_nhan_vien(id_nv, ten_nv, sdt_nv, id_tk):
    """Cập nhật thông tin nhân viên"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE NHAN_VIEN SET TEN_NV = ?, SDT_NV = ?, ID_TK = ? WHERE ID_NV = ?",
                (ten_nv, sdt_nv, id_tk, id_nv))
    conn.commit()
    conn.close()

def them_hoa_don(ngay_lap, id_nv, id_kh, tong_tien):
    """Thêm hóa đơn mới vào cơ sở dữ liệu"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO HOA_DON (NGAY_LAP, ID_NV, ID_KH, TONG_TIEN) VALUES (?, ?, ?, ?)",
                (ngay_lap, id_nv, id_kh, tong_tien))
    conn.commit()
    conn.close()

def xoa_hoa_don(id_hd):
    """Xóa hóa đơn khỏi cơ sở dữ liệu"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM HOA_DON WHERE ID_HD = ?", (id_hd,))
    conn.commit()
    conn.close()

def sua_hoa_don(id_hd, ngay_lap, id_nv, id_kh, tong_tien):
    """Cập nhật thông tin hóa đơn"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE HOA_DON SET NGAY_LAP = ?, ID_NV = ?, ID_KH = ?, TONG_TIEN = ? WHERE ID_HD = ?",
                (ngay_lap, id_nv, id_kh, tong_tien, id_hd))
    conn.commit()
    conn.close()

def them_phieu_nhap(ngay_nhap, id_nv, id_ncc, tong_tien):
    """Thêm phiếu nhập mới vào cơ sở dữ liệu"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO PHIEU_NHAP (NGAY_NHAP, ID_NV, ID_NCC, TONG_TIEN) VALUES (?, ?, ?, ?)",
                (ngay_nhap, id_nv, id_ncc, tong_tien))
    conn.commit()
    conn.close()

def xoa_phieu_nhap(id_pn):
    """Xóa phiếu nhập khỏi cơ sở dữ liệu"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM PHIEU_NHAP WHERE ID_PN = ?", (id_pn,))
    conn.commit()
    conn.close()

def sua_phieu_nhap(id_pn, ngay_nhap, id_nv, id_ncc, tong_tien):
    """Cập nhật thông tin phiếu nhập"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE PHIEU_NHAP SET NGAY_NHAP = ?, ID_NV = ?, ID_NCC = ?, TONG_TIEN = ? WHERE ID_PN = ?",
                (ngay_nhap, id_nv, id_ncc, tong_tien, id_pn))
    conn.commit()
    conn.close()
