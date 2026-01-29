def generate_quiz(summary):
    """
    Generates MCQ-based quiz questions from the summary.
    Each question has 4 options and one correct answer.
    """

    sentences = summary.split(".")
    quiz = []

    for sentence in sentences:
        sentence = sentence.strip()

        # Limit to meaningful sentences and max 5 questions
        if len(sentence) > 20 and len(quiz) < 5:
            question = "What does the following statement explain?"

            options = [
                sentence,  # correct answer
                "It is unrelated to the topic",
                "It explains an opposite concept",
                "It is an example without explanation"
            ]

            quiz.append({
                "question": question,
                "options": options,
                "answer": sentence
            })

    return quiz

