import streamlit as st
import pandas as pd
import plotly.express as px
import io
from database import get_products

# Cấu hình trang
st.set_page_config(page_title="Quản lý Kho Hàng", layout="wide")

# Sidebar - Thanh điều hướng
with st.sidebar:
    st.image("https://www.svgrepo.com/show/354197/warehouse.svg", width=100)
    st.title("📦 Quản lý Kho Hàng")
    page = st.radio("Chọn chức năng", ["🏠 Trang chính", "📊 Báo cáo", "📂 Xuất dữ liệu"])

# Lấy dữ liệu từ cơ sở dữ liệu
products = get_products()

# Trang chính
if page == "🏠 Trang chính":
    st.subheader("📋 Danh sách Sản phẩm")

    # Thanh tìm kiếm
    search_query = st.text_input("🔍 Tìm kiếm sản phẩm", "")

    # Bộ lọc giá & số lượng
    min_price, max_price = st.slider("💰 Lọc theo giá", min_value=0, max_value=20000000, value=(0, 20000000))
    min_qty, max_qty = st.slider("📦 Lọc theo số lượng", min_value=0, max_value=100, value=(0, 100))

    # Lọc dữ liệu
    filtered_products = [
        product for product in products
        if (search_query.lower() in product["Tên"].lower()) and
           (min_price <= product["Giá bán"] <= max_price) and
           (min_qty <= product.get("Số lượng", 0) <= max_qty)
    ]

    # Hiển thị bảng dữ liệu
    st.dataframe(filtered_products)

# Báo cáo
elif page == "📊 Báo cáo":
    st.subheader("📊 Thống kê hàng tồn kho")

    # Tạo DataFrame tạm thời để vẽ biểu đồ
    df_report = pd.DataFrame({
        "Tên": [product["Tên"] for product in products],
        "Số lượng": [product.get("Số lượng", 0) for product in products],
        "Tổng giá trị": [product["Giá bán"] * product.get("Số lượng", 1) for product in products]
    })

    # Biểu đồ số lượng hàng tồn
    fig_qty = px.bar(df_report, x="Tên", y="Số lượng", title="📦 Số lượng tồn kho", color="Số lượng")
    st.plotly_chart(fig_qty, use_container_width=True)

    # Biểu đồ giá trị kho
    fig_value = px.pie(df_report, names="Tên", values="Tổng giá trị", title="💰 Tổng giá trị kho")
    st.plotly_chart(fig_value, use_container_width=True)

# Xuất dữ liệu
elif page == "📂 Xuất dữ liệu":
    st.subheader("📂 Xuất dữ liệu kho hàng")

    # Chuyển danh sách sản phẩm thành DataFrame
    df_export = pd.DataFrame(products)

    # Xuất ra CSV
    csv = df_export.to_csv(index=False).encode('utf-8')
    st.download_button(label="📥 Tải xuống CSV", data=csv, file_name="danh_sach_san_pham.csv", mime="text/csv")

    # Xuất ra Excel
    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
        df_export.to_excel(writer, index=False, sheet_name="KhoHang")
    excel_buffer.seek(0)

    st.download_button(label="📥 Tải xuống Excel", data=excel_buffer, file_name="danh_sach_san_pham.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")