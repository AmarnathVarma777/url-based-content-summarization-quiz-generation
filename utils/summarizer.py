from transformers import pipeline
from .config import settings
from .text_utils import clean_text, chunk_text

_summarizer = None

def _get_summarizer():
    global _summarizer
    if _summarizer is None:
        _summarizer = pipeline(
            "summarization",
            model=settings.hf_summary_model,
            tokenizer=settings.hf_summary_model,
        )
    return _summarizer

def summarize_text(text: str) -> str:
    summarizer = _get_summarizer()
    text = clean_text(text)

    chunks = chunk_text(text, max_words=350)
    outputs = []

    for ch in chunks:
        result = summarizer(
            ch,
            max_length=180,
            min_length=60,
            do_sample=False,
        )[0]["summary_text"]
        outputs.append(result.strip())

    return " ".join(outputs)
