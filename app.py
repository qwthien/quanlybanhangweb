import streamlit as st
import pandas as pd
from database import get_san_pham, get_loai_san_pham, get_nha_cung_cap, get_khach_hang, get_nhan_vien, get_hoa_don, get_phieu_nhap

# Cấu hình trang
st.set_page_config(page_title="Quản lý Bán Hàng", layout="wide")

# Sidebar - Thanh điều hướng
with st.sidebar:
    st.image("https://www.svgrepo.com/show/354197/warehouse.svg", width=100)
    st.title("📦 Quản lý Bán Hàng")
    page = st.radio("Chọn chức năng", [
        "🏠 Trang chính",
        "📦 Quản lý Sản phẩm",
        "🏭 Quản lý Nhà Cung Cấp",
        "👥 Quản lý Khách Hàng",
        "👨‍💼 Quản lý Nhân Viên",
        "🧾 Quản lý Hóa Đơn",
        "📥 Quản lý Phiếu Nhập"
    ])

# Trang chính
if page == "🏠 Trang chính":
    st.subheader("🏠 Trang chính")
    st.write("Chào mừng bạn đến với hệ thống quản lý bán hàng!")

# Quản lý Sản phẩm
elif page == "📦 Quản lý Sản phẩm":
    st.subheader("📦 Quản lý Sản phẩm")
    san_pham = get_san_pham()
    df_san_pham = pd.DataFrame(san_pham, columns=["ID_SP", "TEN_SP", "ID_LOAI", "ID_NCC", "GIA"])
    
    # Thanh tìm kiếm
    search_query = st.text_input("🔍 Tìm kiếm sản phẩm", "")
    
    # Bộ lọc giá
    min_price, max_price = st.slider("💰 Lọc theo giá", min_value=0, max_value=20000000, value=(0, 20000000))
    
    # Lọc dữ liệu
    filtered_products = [
        product for product in san_pham
        if (search_query.lower() in product[1].lower()) and  # product[1] là tên sản phẩm
           (min_price <= product[4] <= max_price)           # product[4] là giá sản phẩm
    ]
    
    # Hiển thị dữ liệu đã lọc
    st.dataframe(pd.DataFrame(filtered_products, columns=["ID_SP", "TEN_SP", "ID_LOAI", "ID_NCC", "GIA"]))

# Quản lý Nhà Cung Cấp
elif page == "🏭 Quản lý Nhà Cung Cấp":
    st.subheader("🏭 Quản lý Nhà Cung Cấp")
    nha_cung_cap = get_nha_cung_cap()
    df_nha_cung_cap = pd.DataFrame(nha_cung_cap, columns=["ID_NCC", "TEN_NCC", "SDT_NCC"])
    st.dataframe(df_nha_cung_cap)

# Quản lý Khách Hàng
elif page == "👥 Quản lý Khách Hàng":
    st.subheader("👥 Quản lý Khách Hàng")
    khach_hang = get_khach_hang()
    df_khach_hang = pd.DataFrame(khach_hang, columns=["ID_KH", "TEN_KH", "SDT_KH", "DIA_CHI"])
    st.dataframe(df_khach_hang)

# Quản lý Nhân Viên
elif page == "👨‍💼 Quản lý Nhân Viên":
    st.subheader("👨‍💼 Quản lý Nhân Viên")
    nhan_vien = get_nhan_vien()
    df_nhan_vien = pd.DataFrame(nhan_vien, columns=["ID_NV", "TEN_NV", "SDT_NV", "ID_TK"])
    st.dataframe(df_nhan_vien)

# Quản lý Hóa Đơn
elif page == "🧾 Quản lý Hóa Đơn":
    st.subheader("🧾 Quản lý Hóa Đơn")
    hoa_don = get_hoa_don()
    df_hoa_don = pd.DataFrame(hoa_don, columns=["ID_HD", "NGAY_LAP", "ID_NV", "ID_KH", "TONG_TIEN"])
    st.dataframe(df_hoa_don)

# Quản lý Phiếu Nhập
elif page == "📥 Quản lý Phiếu Nhập":
    st.subheader("📥 Quản lý Phiếu Nhập")
    phieu_nhap = get_phieu_nhap()
    df_phieu_nhap = pd.DataFrame(phieu_nhap, columns=["ID_PN", "NGAY_NHAP", "ID_NV", "ID_NCC", "TONG_TIEN"])
    st.dataframe(df_phieu_nhap)