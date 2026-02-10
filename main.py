import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide")

st.title("Preview Home - Karya Reksa")

html_path = Path("Frontend/Home/index.html")

if html_path.exists():
    html = html_path.read_text(encoding="utf-8")
    st.components.v1.html(html, height=900, scrolling=True)
else:
    st.error("Home index.html belum ditemukan")
