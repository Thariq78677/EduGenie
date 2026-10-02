from gemini_client import generate_text


def summarize_text(text: str) -> str:
    if not text or not text.strip():
        raise ValueError("Please enter text to summarize.")

    prompt = f"""
Summarize the following educational content.

Rules:
- Keep the main ideas.
- Remove repetition and unnecessary details.
- Use simple and clear language.
- Do not invent new facts.
- Keep it concise but informative.

Text to summarize:
{text}
"""

    return generate_text(prompt).strip()
