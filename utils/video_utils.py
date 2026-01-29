import os
import tempfile
import subprocess
from typing import List
from urllib.parse import urlparse, parse_qs

from pytube import YouTube
import cv2
from PIL import Image

from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch

# ---------- YouTube helpers ----------

def extract_youtube_id(url: str):
    try:
        q = urlparse(url)
        if q.hostname in {"www.youtube.com", "youtube.com"}:
            return parse_qs(q.query).get("v", [None])[0]
        if q.hostname == "youtu.be":
            return q.path.strip("/")
    except Exception:
        return None
    return None

def download_youtube_video(url: str) -> str:
    """Download full YouTube video as mp4, return path."""
    tmpdir = tempfile.mkdtemp()
    mp4_path = os.path.join(tmpdir, "video.mp4")
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
    stream.download(filename=mp4_path)
    return mp4_path

def extract_audio_wav_from_video(mp4_path: str) -> str:
    """Use ffmpeg CLI to convert video to mono 16kHz WAV (NO moviepy)."""
    wav_path = os.path.join(os.path.dirname(mp4_path), "audio.wav")
    cmd = ["ffmpeg", "-i", mp4_path, "-ar", "16000", "-ac", "1", wav_path, "-y"]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return wav_path

# ---------- Visual captioning ----------

_caption_model = None
_caption_processor = None
_caption_tokenizer = None

def _load_caption_model():
    global _caption_model, _caption_processor, _caption_tokenizer
    if _caption_model is None:
        model_name = "nlpconnect/vit-gpt2-image-captioning"
        _caption_model = VisionEncoderDecoderModel.from_pretrained(model_name)
        _caption_processor = ViTImageProcessor.from_pretrained(model_name)
        _caption_tokenizer = AutoTokenizer.from_pretrained(model_name)
    return _caption_model, _caption_processor, _caption_tokenizer

def caption_image(pil_image: Image.Image, max_length: int = 20) -> str:
    model, processor, tokenizer = _load_caption_model()
    pixel_values = processor(images=pil_image, return_tensors="pt").pixel_values
    with torch.no_grad():
        output_ids = model.generate(pixel_values, max_length=max_length, num_beams=4)
    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return caption.strip()

def sample_video_frames_and_caption(mp4_path: str, num_frames: int = 4) -> List[str]:
    """Sample a few frames across the video and generate captions."""
    cap = cv2.VideoCapture(mp4_path)
    if not cap.isOpened():
        return []

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if frame_count <= 0:
        cap.release()
        return []

    step = max(frame_count // (num_frames + 1), 1)
    frames_idx = [step * (i + 1) for i in range(num_frames)]
    captions: List[str] = []

    for idx in frames_idx:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        success, frame = cap.read()
        if not success:
            continue

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(frame_rgb)

        cap_txt = caption_image(pil_img)
        captions.append(cap_txt)

    cap.release()
    return captions
