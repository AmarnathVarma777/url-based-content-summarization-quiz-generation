import streamlit as st

def render_quiz():
    if "quiz" not in st.session_state:
        return

    quiz = st.session_state.quiz

    st.markdown("""
    <div class="card">
        <div class="section-title">🧠 Knowledge Check</div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.current_q < len(quiz):
        q = quiz[st.session_state.current_q]

        st.markdown(
            f"""
            <div class="question-box">
                <strong>Question {st.session_state.current_q + 1}</strong>
            </div>
            """,
            unsafe_allow_html=True
        )

        choice = st.radio(
            q["question"],
            q["options"],
            key=f"q_{st.session_state.current_q}"
        )

        if st.button("Submit Answer"):
            st.session_state.submitted = True
            if choice == q["answer"]:
                st.success("Correct")
                st.session_state.score += 1
            else:
                st.error("Incorrect")

        if st.session_state.submitted:
            if st.button("Next Question"):
                st.session_state.current_q += 1
                st.session_state.submitted = False

    else:
        st.success(f"Final Score: {st.session_state.score} / {len(quiz)}")
