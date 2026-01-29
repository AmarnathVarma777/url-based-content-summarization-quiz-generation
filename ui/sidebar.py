import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.markdown("<p style='font-size:33px; font-weight:600;'>🚀LearnAssist AI</p>", unsafe_allow_html=True)
        st.markdown("## 📘 Control Panel")

        url = st.text_input(
            "🔗 Enter Content URL",
            placeholder="https://www.youtube.com/watch?v=..."
        )

        process_btn = st.button("🚀 Get Summary")

        st.markdown("---")
        st.markdown("### 🔠 Reading Settings")

        if "font_size" not in st.session_state:
            st.session_state.font_size = 15

        font_size = st.slider(
            "Summary Font Size",
            12, 22,
            st.session_state.font_size
        )

        st.session_state.font_size = font_size

        return url, process_btn, font_size
    
    
