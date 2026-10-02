import json
import re

from gemini_client import generate_text


def clean_json_block(text: str) -> str:
    if not text:
        return text

    cleaned = text.strip()
    cleaned = re.sub(r"```(?:json)?\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = cleaned.replace("```", "").strip()
    return cleaned


def generate_quiz(text: str):
    if not text or not text.strip():
        raise ValueError("Please enter a topic or passage to generate a quiz.")

    prompt = f"""
Create exactly 3 multiple-choice questions based on the following educational content.

Return valid JSON only in this exact structure:
[
  {{
    "question": "...",
    "options": ["...", "...", "...", "..."],
    "correct_answer": "...",
    "explanation": "..."
  }}
]

Rules:
- Exactly 3 questions.
- Each question must have 4 options.
- Only one option is correct.
- Use simple academic language.
- Provide a brief explanation for why the correct answer is right.
- Ensure the JSON is valid and parseable.

Content:
{text}
"""

    response = generate_text(prompt)
    cleaned = clean_json_block(response)

    try:
        parsed = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise ValueError("Gemini returned invalid quiz JSON. Please try a different topic or passage.") from exc

    if not isinstance(parsed, list) or len(parsed) != 3:
        raise ValueError("Quiz generation failed because the response did not contain exactly 3 questions.")

    for item in parsed:
        if not isinstance(item, dict):
            raise ValueError("Each quiz item must be a JSON object.")
        required_fields = {"question", "options", "correct_answer", "explanation"}
        if not required_fields.issubset(item.keys()):
            raise ValueError("One or more quiz items are missing required fields.")
        if not isinstance(item["options"], list) or len(item["options"]) != 4:
            raise ValueError("Every question must have exactly 4 options.")
        if item["correct_answer"] not in item["options"]:
            raise ValueError("The correct answer must be one of the listed options.")

    return parsed
