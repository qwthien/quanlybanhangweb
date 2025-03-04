import fdb

DB_CONFIG = {
    "dsn": r"localhost:C:\FirebirdData\QLBH1.FDB",
    "user": "sysdba",
    "password": "123",
    "charset": "UTF8"
}

def get_connection():
    """Tạo kết nối đến Firebird"""
    return fdb.connect(**DB_CONFIG)

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