import streamlit as st
from database import get_products

st.title("📦 Quản lý kho hàng")

# Hiển thị danh sách sản phẩm
st.subheader("📋 Danh sách sản phẩm")
products = get_products()
st.table(products)
