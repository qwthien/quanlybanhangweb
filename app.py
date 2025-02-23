import streamlit as st
import pandas as pd
import plotly.express as px

# Cấu hình trang
st.set_page_config(page_title="Quản lý Kho Hàng", layout="wide")

# Sidebar - Thanh điều hướng
with st.sidebar:
    st.image("https://www.svgrepo.com/show/354197/warehouse.svg", width=100)
    st.title("📦 Quản lý Kho Hàng")
    page = st.radio("Chọn chức năng", ["🏠 Trang chính", "📊 Báo cáo", "📂 Xuất dữ liệu"])

# 🔹 Dữ liệu mẫu
mock_data = [
    {"ID": 1, "Tên": "Laptop Dell", "Số lượng": 20, "Giá": 15000000},
    {"ID": 2, "Tên": "Chuột Logitech", "Số lượng": 50, "Giá": 500000},
    {"ID": 3, "Tên": "Bàn phím cơ", "Số lượng": 30, "Giá": 1200000},
    {"ID": 4, "Tên": "Màn hình LG", "Số lượng": 15, "Giá": 4500000},
    {"ID": 5, "Tên": "Ổ cứng SSD", "Số lượng": 25, "Giá": 2200000},
]

df = pd.DataFrame(mock_data)

# Trang chính
if page == "🏠 Trang chính":
    st.subheader("📋 Danh sách Sản phẩm")

    # Thanh tìm kiếm
    search_query = st.text_input("🔍 Tìm kiếm sản phẩm", "")

    # Bộ lọc giá & số lượng
    min_price, max_price = st.slider("💰 Lọc theo giá", min_value=0, max_value=20000000, value=(0, 20000000))
    min_qty, max_qty = st.slider("📦 Lọc theo số lượng", min_value=0, max_value=100, value=(0, 100))

    # Lọc dữ liệu
    filtered_df = df[
        (df["Tên"].str.contains(search_query, case=False, na=False)) &
        (df["Giá"] >= min_price) & (df["Giá"] <= max_price) &
        (df["Số lượng"] >= min_qty) & (df["Số lượng"] <= max_qty)
    ]

    # Hiển thị bảng dữ liệu
    st.dataframe(filtered_df)

# Báo cáo
elif page == "📊 Báo cáo":
    st.subheader("📊 Thống kê hàng tồn kho")

    # Biểu đồ số lượng hàng tồn
    fig_qty = px.bar(df, x="Tên", y="Số lượng", title="📦 Số lượng tồn kho", color="Số lượng")
    st.plotly_chart(fig_qty, use_container_width=True)

    # Biểu đồ giá trị kho
    df["Tổng giá trị"] = df["Số lượng"] * df["Giá"]
    fig_value = px.pie(df, names="Tên", values="Tổng giá trị", title="💰 Tổng giá trị kho")
    st.plotly_chart(fig_value, use_container_width=True)

# Xuất dữ liệu
elif page == "📂 Xuất dữ liệu":
    st.subheader("📂 Xuất dữ liệu kho hàng")

    # Xuất ra CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(label="📥 Tải xuống CSV", data=csv, file_name="danh_sach_san_pham.csv", mime="text/csv")

    # Xuất ra Excel
    excel_buffer = pd.ExcelWriter("danh_sach_san_pham.xlsx", engine="xlsxwriter")
    df.to_excel(excel_buffer, index=False, sheet_name="KhoHang")
    excel_buffer.close()

    with open("danh_sach_san_pham.xlsx", "rb") as file:
        st.download_button(label="📥 Tải xuống Excel", data=file, file_name="danh_sach_san_pham.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
