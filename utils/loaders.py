from typing import Tuple
from urllib.parse import urlparse, parse_qs
import re

import trafilatura
from bs4 import BeautifulSoup

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound


def _extract_youtube_id(url: str):
    q = urlparse(url)
    if q.hostname in {"www.youtube.com", "youtube.com"}:
        return parse_qs(q.query).get("v", [None])[0]
    if q.hostname == "youtu.be":
        return q.path.strip("/")
    return None


def load_from_url(url: str) -> Tuple[str, str]:
    """
    Returns: (kind, text)
    kind ∈ {"youtube_transcript", "web_article"}
    """

    yt_id = _extract_youtube_id(url)

    # -------- YouTube transcript (v1.2.3 compatible) --------
    if yt_id:
        try:
            api = YouTubeTranscriptApi()
            transcript = api.fetch(yt_id)

            text = " ".join(
                item.text for item in transcript if item.text
            )

            if not text.strip():
                raise ValueError("Transcript is empty")

            return "youtube_transcript", text

        except (TranscriptsDisabled, NoTranscriptFound):
            raise ValueError(
                "Transcript is not available for this YouTube video. "
                "Please try a public educational video with captions."
            )

    # -------- Web article --------
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        raise ValueError("Failed to fetch URL")

    text = trafilatura.extract(downloaded, no_fallback=True)
    if not text:
        soup = BeautifulSoup(downloaded, "html.parser")
        for s in soup(["script", "style", "noscript"]):
            s.extract()
        text = re.sub(r"\s+", " ", soup.get_text(" ")).strip()

    if not text:
        raise ValueError("No readable text found")

    return "web_article", text



