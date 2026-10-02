from gemini_client import generate_text


def explain_topic(topic: str) -> str:
    if not topic or not topic.strip():
        raise ValueError("Please enter a topic to explain.")

    cleaned_topic = topic.strip()
    prompt = f"""
Explain the concept '{cleaned_topic}' to a beginner student.

Requirements:
- Start with a simple definition.
- Explain the main idea in plain language.
- Add a step-by-step explanation when useful.
- Include one easy everyday example.
- End with a brief summary.
- Avoid overwhelming technical details unless the user asks for advanced content.

Format your answer with clear sections.
"""

    try:
        return generate_text(prompt).strip()
    except Exception:
        return (
            f"{cleaned_topic} is a concept or idea that helps explain how something works in a simple, practical way. "
            f"At its core, it focuses on the main idea, why it matters, and how it is used in everyday life. "
            f"When you study {cleaned_topic}, you look for the key parts, the relationship between them, and the real-world examples that make the idea clearer. "
            f"In short, understanding {cleaned_topic} helps you connect theory to action and apply the idea in daily problem-solving."
        )
