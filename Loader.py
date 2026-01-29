import re
from typing import Tuple, List, Optional

import trafilatura
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
from groq import Groq

from .config import settings, require_groq_key
from .video_utils import (
    extract_youtube_id,
    download_youtube_video,
    extract_audio_wav_from_video,
    sample_video_frames_and_caption,
)

require_groq_key()
client = Groq(api_key=settings.groq_api_key)

def transcribe_with_groq_whisper(wav_path: str) -> str:
    with open(wav_path, "rb") as f:
        res = client.audio.transcriptions.create(
            file=("audio.wav", f, "audio/wav"),
            model=settings.whisper_model,
        )
    return res.text


def load_from_url(url: str) -> Tuple[str, str, List[str]]:
    """
    Returns: kind, combined_text, visual_captions

    kind ∈ {"youtube_transcript", "youtube_whisper", "web_article"}
    combined_text = main transcript/article text + (optionally) visual captions
    visual_captions = list of caption strings (for YouTube)
    """
    yt_id = extract_youtube_id(url)
    visual_captions: List[str] = []

    if yt_id:
        # Download video file once
        mp4_path = download_youtube_video(url)

        # Step 1: try official transcript
        base_text: Optional[str] = None
        try:
            transcript = YouTubeTranscriptApi.get_transcript(yt_id, languages=["en"])
            base_text = " ".join([t["text"] for t in transcript if t.get("text")])
            kind = "youtube_transcript"
        except (NoTranscriptFound, TranscriptsDisabled):
            # Step 2: Whisper via Groq on audio
            wav_path = extract_audio_wav_from_video(mp4_path)
            base_text = transcribe_with_groq_whisper(wav_path)
            kind = "youtube_whisper"

        if not base_text or not base_text.strip():
            raise ValueError("Failed to extract speech text from YouTube video.")

        # Step 3: visual captions from frames
        visual_captions = sample_video_frames_and_caption(mp4_path, num_frames=4)

        combined = base_text
        if visual_captions:
            combined += "\n\nVisual scene descriptions:\n" + " ".join(visual_captions)

        return kind, combined, visual_captions

    # ---- Web article flow ----
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        raise ValueError("Failed to fetch URL. Check connectivity and the URL itself.")

    text = trafilatura.extract(downloaded, include_comments=False, include_tables=False, no_fallback=True)
    if not text:
        soup = BeautifulSoup(downloaded, "html.parser")
        for s in soup(["script", "style", "noscript"]):
            s.extract()
        text = re.sub(r"\s+", " ", soup.get_text(" ")).strip()

    if not text:
        raise ValueError("No readable text found at the URL.")

    return "web_article", text, []