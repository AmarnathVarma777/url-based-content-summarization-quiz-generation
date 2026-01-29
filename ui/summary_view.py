import streamlit as st

def render_summary(font_size):
    if "summary" not in st.session_state:
        return

    summary_text = st.session_state.summary

    if not isinstance(summary_text, str) or not summary_text.strip():
        st.warning("Summary unavailable.")
        return

    # 🔥 FIX: preprocess text BEFORE f-string
    formatted_summary = summary_text.replace("\n", "<br>")

    st.markdown("""
    <div class="card">
        <div class="section-title">📝 Generated Summary</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="summary-box"
             style="font-size:{font_size}px; line-height:1.7;">
            {formatted_summary}
        </div>
        """,
        unsafe_allow_html=True
    )
