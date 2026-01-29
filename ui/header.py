import streamlit as st

def render_header():
    st.markdown("""
    <div class="card">
        <div class="header">
            <div class="title-text">
                URL-Based Content Summarization & Quiz System
            </div>
        </div>
        <p class="subtitle-text">
            A Modern Learning Assistant Powered by AI for Efficient Knowledge Acquisition.
        </p>
    </div>
    """, unsafe_allow_html=True)
