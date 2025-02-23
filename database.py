import fdb

DB_CONFIG = {
    "dsn": "localhost:C:/firebird/warehouse.fdb",  # Đường dẫn database
    "user": "sysdba",
    "password": "masterkey",
    "charset": "UTF8"
}

def get_connection():
    """Tạo kết nối đến Firebird"""
    return fdb.connect(**DB_CONFIG)

def get_products():
    """Truy vấn danh sách sản phẩm"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, quantity, price FROM products")
    products = [{"ID": row[0], "Tên": row[1], "Số lượng": row[2], "Giá": row[3]} for row in cur.fetchall()]
    conn.close()
    return products
