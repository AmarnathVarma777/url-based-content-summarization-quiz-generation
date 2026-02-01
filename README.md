<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    
</head>

<body style="font-family: Arial, sans-serif; line-height: 1.6;">

<h1>📘 LearnLens</h1>
<h3>URL-Based Content Summarization & Quiz Generation System</h3>

<hr>

<h2>📌 Project Overview</h2>
<p>
LearnLens is an AI-powered learning assistant designed to help users efficiently understand
online educational content. The system accepts a URL as input (YouTube video or website article),
extracts the textual content, generates a concise summary using Natural Language Processing,
and produces quiz questions for self-assessment.
</p>

<p>
This project was developed as part of an <strong>MCA Minor Project</strong> to demonstrate the
practical application of NLP, transformer-based models, and modular software design.
</p>

<hr>

<h2>🎯 Objectives</h2>
<ul>
    <li>Automatically extract text from online URLs</li>
    <li>Generate concise and meaningful summaries</li>
    <li>Create quiz questions to assess learner understanding</li>
    <li>Provide an interactive and user-friendly web interface</li>
</ul>

<hr>

<h2>⚙️ Features</h2>
<ul>
    <li>Supports YouTube video URLs and website article URLs</li>
    <li>Transcript-based text extraction for YouTube videos</li>
    <li>Abstractive text summarization using T5 Transformer</li>
    <li>Quiz generation using a Large Language Model</li>
    <li>Interactive quiz flow (one question at a time)</li>
    <li>Dynamic font size adjustment for better readability</li>
    <li>Clean and modern UI using Streamlit and external CSS</li>
</ul>

<hr>

<h2>🛠️ Technologies Used</h2>
<ul>
    <li>Python</li>
    <li>Streamlit</li>
    <li>PyTorch</li>
    <li>Hugging Face Transformers (T5)</li>
    <li>Large Language Model (Groq API)</li>
    <li>YouTube Transcript API</li>
    <li>BeautifulSoup (Web Content Extraction)</li>
    <li>HTML & CSS</li>
</ul>

<hr>

<h2>📁 Project Structure</h2>
<pre>
LearnLens/
│
├── app.py
├── Loader.py
├── summarizer.py
├── quizgen.py
├── requirements.txt
├── README.html
│
├── core/
│   └── processor.py
│
├── utils/
│   └── loaders.py
│
├── ui/
│   ├── sidebar.py
│   ├── header.py
│   ├── summary_view.py
│   └── quiz_view.py
│
└── styles/
    └── style.css
</pre>

<hr>

<h2>🚀 How to Run the Project</h2>

<ol>
    <li><strong>Clone the repository</strong></li>
</ol>

<pre>
git clone https://github.com/your-username/learnlens.git
cd learnlens
</pre>

<ol start="2">
    <li><strong>Install required dependencies</strong></li>
</ol>

<pre>
pip install -r requirements.txt
</pre>

<ol start="3">
    <li><strong>Run the Streamlit application</strong></li>
</ol>

<pre>
streamlit run app.py
</pre>

<hr>

<h2>🔄 Application Workflow</h2>
<ul>
    <li>User enters a URL through the web interface</li>
    <li>System extracts textual content from the URL</li>
    <li>Extracted text is summarized using NLP</li>
    <li>Quiz questions are generated from the summary</li>
    <li>User interacts with the quiz and receives feedback</li>
</ul>

<hr>

<h2>🧪 Testing</h2>
<ul>
    <li>Functional testing of each module</li>
    <li>Integration testing of end-to-end pipeline</li>
    <li>Manual testing using multiple real-world URLs</li>
</ul>

<hr>

<h2>⚠️ Assumptions & Limitations</h2>
<ul>
    <li>YouTube videos must have transcripts enabled</li>
    <li>Only English-language content is supported</li>
    <li>No database is used for persistent storage</li>
</ul>

<hr>

<h2>🔮 Future Enhancements</h2>
<ul>
    <li>Multilingual content support</li>
    <li>Speech-to-text fallback for videos without transcripts</li>
    <li>User profiles and progress tracking</li>
    <li>Export summary and quiz results</li>
</ul>

<hr>

<h2>📚 Academic Note</h2>
<p>
This project is intended strictly for academic and educational purposes and demonstrates
the practical application of NLP and Generative AI techniques.
</p>

<hr>

<h2>📜 License</h2>
<p>
This project is developed for academic use only.
</p>

</body>
</html>

