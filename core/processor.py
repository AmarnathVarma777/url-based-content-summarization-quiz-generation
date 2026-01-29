import streamlit as st
from utils.loaders import load_from_url
from utils.summarizer import summarize_text
from utils.quizgen import generate_quiz

def process_url(url):
    if not url.strip():
        st.warning("Please enter a valid URL.")
        return

    with st.spinner("🔍 Extracting content..."):
        kind, text = load_from_url(url)

    if not text or not isinstance(text, str):
        st.error("Unable to extract usable content.")
        return

    with st.spinner("✍️ Generating summary..."):
        summary = summarize_text(text)

    if not summary or not isinstance(summary, str):
        st.error("Summary generation failed.")
        return

    with st.spinner("🧠 Generating quiz..."):
        quiz = generate_quiz(summary)

    st.session_state.summary = summary
    st.session_state.quiz = quiz
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.submitted = False
