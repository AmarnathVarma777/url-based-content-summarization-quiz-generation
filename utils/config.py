import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    groq_api_key: str = os.getenv("GROQ_API_KEY", "").strip()
    whisper_model: str = "whisper-large-v3"
    llm_model: str = "llama-3.3-70b-versatile"
    hf_summary_model: str = "t5-small"

settings = Settings()

def require_groq_key():
    if not settings.groq_api_key:
        raise RuntimeError("GROQ_API_KEY missing. Set it in your .env or terminal.")
