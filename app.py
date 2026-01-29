import streamlit as st

from ui.sidebar import render_sidebar
from ui.header import render_header
from ui.summary_view import render_summary
from ui.quiz_view import render_quiz
from core.processor import process_url


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="URL-Based Content Summarization & Quiz System",
    page_icon="📘",
    layout="wide"
)

# --------------------------------------------------
# Load External CSS
# --------------------------------------------------
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("styles/styles.css")

# --------------------------------------------------
# Main Container Wrapper (CRITICAL FOR UI)
# --------------------------------------------------
st.markdown('<div class="main">', unsafe_allow_html=True)

# --------------------------------------------------
# Sidebar (Controls)
# --------------------------------------------------
url, process_btn, font_size = render_sidebar()

# --------------------------------------------------
# Header Section
# --------------------------------------------------
render_header()

# --------------------------------------------------
# Processing Logic
# --------------------------------------------------
if process_btn:
    process_url(url)

# --------------------------------------------------
# Output Sections
# --------------------------------------------------
render_summary(font_size)
render_quiz()

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("""
<div class="footer">
    MCA Minor Project | URL-Based Content Summarization & Quiz Generation System
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Close Main Container
# --------------------------------------------------
st.markdown('</div>', unsafe_allow_html=True)
