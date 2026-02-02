import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Moumitar Rannaghar | Bengali Home Food",
    page_icon="🍛",
    layout="wide"
)

# Read HTML file
html_file = Path("moumitar-rannaghar.html")
html_content = html_file.read_text(encoding="utf-8")

# Render HTML
st.components.v1.html(
    html_content,
    height=3000,
    scrolling=True
)
