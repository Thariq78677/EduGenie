import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL_NAMES = ["gemini-3.8-flash", "gemini-2.5-flash", "gemini-2.0-flash"]


def get_gemini_client() -> genai.Client:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key.strip() == "YOUR_GEMINI_API_KEY":
        raise ValueError("Gemini API key is missing or not configured. Add a valid key to the .env file.")
    return genai.Client(api_key=api_key)


def generate_text(prompt: str) -> str:
    client = get_gemini_client()
    last_error = None

    for model_name in MODEL_NAMES:
        for attempt in range(3):
            try:
                response = client.models.generate_content(model=model_name, contents=prompt)

                text = getattr(response, "text", None)
                if text:
                    return text

                if hasattr(response, "candidates") and response.candidates:
                    candidate = response.candidates[0]
                    if hasattr(candidate, "content") and hasattr(candidate.content, "parts"):
                        parts = []
                        for part in candidate.content.parts:
                            if hasattr(part, "text"):
                                parts.append(part.text)
                        if parts:
                            return "".join(parts)

                return str(response)
            except Exception as exc:  # pragma: no cover - depends on external API status
                last_error = exc
                status_code = getattr(exc, "status_code", None)
                if status_code not in {429, 500, 502, 503, 504}:
                    raise
                if attempt < 2:
                    time.sleep(2 ** attempt)
                    continue
        if last_error is not None:
            continue

    if last_error is not None:
        raise last_error

    raise ValueError("Gemini returned no usable response.")
