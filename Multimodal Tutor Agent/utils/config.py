"""Application configuration and environment helpers."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


def _configured_path(name: str, default: str) -> Path:
    path = Path(os.getenv(name) or default)
    if not path.is_absolute():
        path = BASE_DIR / path
    path.mkdir(parents=True, exist_ok=True)
    return path


UPLOAD_DIR = _configured_path("UPLOAD_DIR", "uploads")
AUDIO_DIR = _configured_path("AUDIO_DIR", "audio")

OPENAI_VISION_MODEL = os.getenv("OPENAI_VISION_MODEL", "gpt-4o-mini")
OPENAI_TTS_MODEL = os.getenv("OPENAI_TTS_MODEL", "gpt-4o-mini-tts")
OPENAI_TTS_VOICE = os.getenv("OPENAI_TTS_VOICE", "coral")
MAX_UPLOAD_MB = int(
    os.getenv("MAX_UPLOAD_MB", os.getenv("MAX_UPLOADS", "10"))
)


def required_env(name: str) -> str:
    """Return a required environment variable or raise a clear error."""
    value = os.getenv(name)
    if not value and name == "OPENAI_API_KEY":
        value = os.getenv("OPEN_API_KEY")
    if not value:
        raise ValueError(f"Required environment variable {name} is not set.")
    return value
