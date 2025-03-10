import streamlit as st
import pandas as pd
from database import (
    get_san_pham, get_loai_san_pham, get_nha_cung_cap, get_khach_hang, get_nhan_vien, get_hoa_don, get_phieu_nhap,
    them_san_pham, xoa_san_pham, sua_san_pham,
    them_nha_cung_cap, xoa_nha_cung_cap, sua_nha_cung_cap,
    them_khach_hang, xoa_khach_hang, sua_khach_hang,
    them_nhan_vien, xoa_nhan_vien, sua_nhan_vien,
    them_hoa_don, xoa_hoa_don, sua_hoa_don,
    them_phieu_nhap, xoa_phieu_nhap, sua_phieu_nhap
)

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
    min_price, max_price = st.slider("💰 Lọc theo giá", min_value=0, max_value=500000, value=(0, 500000))
    
    # Lọc dữ liệu
    filtered_products = [
        product for product in san_pham
        if (search_query.lower() in product[1].lower()) and  # product[1] là tên sản phẩm
           (min_price <= product[4] <= max_price)           # product[4] là giá sản phẩm
    ]
    
    # Hiển thị dữ liệu đã lọc
    st.dataframe(pd.DataFrame(filtered_products, columns=["ID_SP", "TEN_SP", "ID_LOAI", "ID_NCC", "GIA"]))

    # Form thêm sản phẩm
    with st.form("Thêm sản phẩm"):
        st.write("### Thêm sản phẩm mới")
        ten_sp = st.text_input("Tên sản phẩm")
        id_loai = st.number_input("ID Loại sản phẩm", min_value=1)
        id_ncc = st.number_input("ID Nhà cung cấp", min_value=1)
        gia = st.number_input("Giá", min_value=0)
        if st.form_submit_button("Thêm"):
            them_san_pham(ten_sp, id_loai, id_ncc, gia)
            st.success("Thêm sản phẩm thành công!")
            st.experimental_rerun()
    
    # Form xóa sản phẩm
    with st.form("Xóa sản phẩm"):
        st.write("### Xóa sản phẩm")
        id_sp_xoa = st.number_input("ID Sản phẩm cần xóa", min_value=1)
        if st.form_submit_button("Xóa"):
            xoa_san_pham(id_sp_xoa)
            st.success("Xóa sản phẩm thành công!")
            st.experimental_rerun()
    
    # Form sửa thông tin sản phẩm
    with st.form("Sửa sản phẩm"):
        st.write("### Sửa thông tin sản phẩm")
        id_sp_sua = st.number_input("ID Sản phẩm cần sửa", min_value=1)
        ten_sp_moi = st.text_input("Tên sản phẩm mới")
        id_loai_moi = st.number_input("ID Loại sản phẩm mới", min_value=1)
        id_ncc_moi = st.number_input("ID Nhà cung cấp mới", min_value=1)
        gia_moi = st.number_input("Giá mới", min_value=0)
        if st.form_submit_button("Sửa"):
            sua_san_pham(id_sp_sua, ten_sp_moi, id_loai_moi, id_ncc_moi, gia_moi)
            st.success("Sửa thông tin sản phẩm thành công!")
            st.experimental_rerun()

# Quản lý Nhà Cung Cấp
elif page == "🏭 Quản lý Nhà Cung Cấp":
    st.subheader("🏭 Quản lý Nhà Cung Cấp")
    nha_cung_cap = get_nha_cung_cap()
    df_nha_cung_cap = pd.DataFrame(nha_cung_cap, columns=["ID_NCC", "TEN_NCC", "SDT_NCC"])
    st.dataframe(df_nha_cung_cap)
    
    # Form thêm nhà cung cấp
    with st.form("Thêm nhà cung cấp"):
        st.write("### Thêm nhà cung cấp mới")
        ten_ncc = st.text_input("Tên nhà cung cấp")
        sdt_ncc = st.text_input("Số điện thoại")
        if st.form_submit_button("Thêm"):
            them_nha_cung_cap(ten_ncc, sdt_ncc)
            st.success("Thêm nhà cung cấp thành công!")
            st.experimental_rerun()
    
    # Form xóa nhà cung cấp
    with st.form("Xóa nhà cung cấp"):
        st.write("### Xóa nhà cung cấp")
        id_ncc_xoa = st.number_input("ID Nhà cung cấp cần xóa", min_value=1)
        if st.form_submit_button("Xóa"):
            xoa_nha_cung_cap(id_ncc_xoa)
            st.success("Xóa nhà cung cấp thành công!")
            st.experimental_rerun()
    
    # Form sửa thông tin nhà cung cấp
    with st.form("Sửa nhà cung cấp"):
        st.write("### Sửa thông tin nhà cung cấp")
        id_ncc_sua = st.number_input("ID Nhà cung cấp cần sửa", min_value=1)
        ten_ncc_moi = st.text_input("Tên nhà cung cấp mới")
        sdt_ncc_moi = st.text_input("Số điện thoại mới")
        if st.form_submit_button("Sửa"):
            sua_nha_cung_cap(id_ncc_sua, ten_ncc_moi, sdt_ncc_moi)
            st.success("Sửa thông tin nhà cung cấp thành công!")
            st.experimental_rerun()

# Quản lý Khách Hàng
elif page == "👥 Quản lý Khách Hàng":
    st.subheader("👥 Quản lý Khách Hàng")
    khach_hang = get_khach_hang()
    df_khach_hang = pd.DataFrame(khach_hang, columns=["ID_KH", "TEN_KH", "SDT_KH", "DIA_CHI"])
    st.dataframe(df_khach_hang)
    
    # Form thêm khách hàng
    with st.form("Thêm khách hàng"):
        st.write("### Thêm khách hàng mới")
        ten_kh = st.text_input("Tên khách hàng")
        sdt_kh = st.text_input("Số điện thoại")
        dia_chi = st.text_input("Địa chỉ")
        if st.form_submit_button("Thêm"):
            them_khach_hang(ten_kh, sdt_kh, dia_chi)
            st.success("Thêm khách hàng thành công!")
            st.experimental_rerun()
    
    # Form xóa khách hàng
    with st.form("Xóa khách hàng"):
        st.write("### Xóa khách hàng")
        id_kh_xoa = st.number_input("ID Khách hàng cần xóa", min_value=1)
        if st.form_submit_button("Xóa"):
            xoa_khach_hang(id_kh_xoa)
            st.success("Xóa khách hàng thành công!")
            st.experimental_rerun()
    
    # Form sửa thông tin khách hàng
    with st.form("Sửa khách hàng"):
        st.write("### Sửa thông tin khách hàng")
        id_kh_sua = st.number_input("ID Khách hàng cần sửa", min_value=1)
        ten_kh_moi = st.text_input("Tên khách hàng mới")
        sdt_kh_moi = st.text_input("Số điện thoại mới")
        dia_chi_moi = st.text_input("Địa chỉ mới")
        if st.form_submit_button("Sửa"):
            sua_khach_hang(id_kh_sua, ten_kh_moi, sdt_kh_moi, dia_chi_moi)
            st.success("Sửa thông tin khách hàng thành công!")
            st.experimental_rerun()

# Quản lý Nhân Viên
elif page == "👨‍💼 Quản lý Nhân Viên":
    st.subheader("👨‍💼 Quản lý Nhân Viên")
    nhan_vien = get_nhan_vien()
    df_nhan_vien = pd.DataFrame(nhan_vien, columns=["ID_NV", "TEN_NV", "SDT_NV", "ID_TK"])
    st.dataframe(df_nhan_vien)
    
    # Form thêm nhân viên
    with st.form("Thêm nhân viên"):
        st.write("### Thêm nhân viên mới")
        ten_nv = st.text_input("Tên nhân viên")
        sdt_nv = st.text_input("Số điện thoại")
        id_tk = st.number_input("ID Tài khoản", min_value=1)
        if st.form_submit_button("Thêm"):
            them_nhan_vien(ten_nv, sdt_nv, id_tk)
            st.success("Thêm nhân viên thành công!")
            st.experimental_rerun()
    
    # Form xóa nhân viên
    with st.form("Xóa nhân viên"):
        st.write("### Xóa nhân viên")
        id_nv_xoa = st.number_input("ID Nhân viên cần xóa", min_value=1)
        if st.form_submit_button("Xóa"):
            xoa_nhan_vien(id_nv_xoa)
            st.success("Xóa nhân viên thành công!")
            st.experimental_rerun()
    
    # Form sửa thông tin nhân viên
    with st.form("Sửa nhân viên"):
        st.write("### Sửa thông tin nhân viên")
        id_nv_sua = st.number_input("ID Nhân viên cần sửa", min_value=1)
        ten_nv_moi = st.text_input("Tên nhân viên mới")
        sdt_nv_moi = st.text_input("Số điện thoại mới")
        id_tk_moi = st.number_input("ID Tài khoản mới", min_value=1)
        if st.form_submit_button("Sửa"):
            sua_nhan_vien(id_nv_sua, ten_nv_moi, sdt_nv_moi, id_tk_moi)
            st.success("Sửa thông tin nhân viên thành công!")
            st.experimental_rerun()

# Quản lý Hóa Đơn
elif page == "🧾 Quản lý Hóa Đơn":
    st.subheader("🧾 Quản lý Hóa Đơn")
    hoa_don = get_hoa_don()
    df_hoa_don = pd.DataFrame(hoa_don, columns=["ID_HD", "NGAY_LAP", "ID_NV", "ID_KH", "TONG_TIEN"])
    st.dataframe(df_hoa_don)
    
    # Form thêm hóa đơn
    with st.form("Thêm hóa đơn"):
        st.write("### Thêm hóa đơn mới")
        ngay_lap = st.date_input("Ngày lập")
        id_nv = st.number_input("ID Nhân viên", min_value=1)
        id_kh = st.number_input("ID Khách hàng", min_value=1)
        tong_tien = st.number_input("Tổng tiền", min_value=0)
        if st.form_submit_button("Thêm"):
            them_hoa_don(ngay_lap, id_nv, id_kh, tong_tien)
            st.success("Thêm hóa đơn thành công!")
            st.experimental_rerun()
    
    # Form xóa hóa đơn
    with st.form("Xóa hóa đơn"):
        st.write("### Xóa hóa đơn")
        id_hd_xoa = st.number_input("ID Hóa đơn cần xóa", min_value=1)
        if st.form_submit_button("Xóa"):
            xoa_hoa_don(id_hd_xoa)
            st.success("Xóa hóa đơn thành công!")
            st.experimental_rerun()
    
    # Form sửa thông tin hóa đơn
    with st.form("Sửa hóa đơn"):
        st.write("### Sửa thông tin hóa đơn")
        id_hd_sua = st.number_input("ID Hóa đơn cần sửa", min_value=1)
        ngay_lap_moi = st.date_input("Ngày lập mới")
        id_nv_moi = st.number_input("ID Nhân viên mới", min_value=1)
        id_kh_moi = st.number_input("ID Khách hàng mới", min_value=1)
        tong_tien_moi = st.number_input("Tổng tiền mới", min_value=0)
        if st.form_submit_button("Sửa"):
            sua_hoa_don(id_hd_sua, ngay_lap_moi, id_nv_moi, id_kh_moi, tong_tien_moi)
            st.success("Sửa thông tin hóa đơn thành công!")
            st.experimental_rerun()

# Quản lý Phiếu Nhập
elif page == "📥 Quản lý Phiếu Nhập":
    st.subheader("📥 Quản lý Phiếu Nhập")
    phieu_nhap = get_phieu_nhap()
    df_phieu_nhap = pd.DataFrame(phieu_nhap, columns=["ID_PN", "NGAY_NHAP", "ID_NV", "ID_NCC", "TONG_TIEN"])
    st.dataframe(df_phieu_nhap)
    
    # Form thêm phiếu nhập
    with st.form("Thêm phiếu nhập"):
        st.write("### Thêm phiếu nhập mới")
        ngay_nhap = st.date_input("Ngày nhập")
        id_nv = st.number_input("ID Nhân viên", min_value=1)
        id_ncc = st.number_input("ID Nhà cung cấp", min_value=1)
        tong_tien = st.number_input("Tổng tiền", min_value=0)
        if st.form_submit_button("Thêm"):
            them_phieu_nhap(ngay_nhap, id_nv, id_ncc, tong_tien)
            st.success("Thêm phiếu nhập thành công!")
            st.experimental_rerun()
    
    # Form xóa phiếu nhập
    with st.form("Xóa phiếu nhập"):
        st.write("### Xóa phiếu nhập")
        id_pn_xoa = st.number_input("ID Phiếu nhập cần xóa", min_value=1)
        if st.form_submit_button("Xóa"):
            xoa_phieu_nhap(id_pn_xoa)
            st.success("Xóa phiếu nhập thành công!")
            st.experimental_rerun()
    