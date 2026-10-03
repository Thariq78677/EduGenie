import json

from gemini_client import generate_text


def get_learning_recommendations(topic: str) -> dict:
    if not topic or not topic.strip():
        raise ValueError("Please enter a topic for learning recommendations.")

    prompt = (
        "Generate a structured learning path for the topic: '"
        + topic
        + "'\n\n"
        "Return valid JSON only with the following keys:\n"
        "- beginner_level\n"
        "- intermediate_level\n"
        "- advanced_level\n"
        "- suggested_learning_order\n"
        "- practice_suggestions\n"
        "- resource_types\n"
        "- timeline\n\n"
        "Rules:\n"
        "- Keep it useful for a student learner.\n"
        "- Provide a clear progression from beginner to advanced.\n"
        "- Mention practical exercises and learning order.\n"
        "- Include resource types such as Videos, Articles, Books, Documentation.\n"
        "- Keep the output easy to follow.\n\n"
        "Example structure:\n"
        "{\n"
        "  \"beginner_level\": \"Basic understanding and fundamentals\",\n"
        "  \"intermediate_level\": \"Core skills and applications\",\n"
        "  \"advanced_level\": \"Complex usage and optimization\",\n"
        "  \"suggested_learning_order\": [\"Fundamentals\", \"Core concepts\", \"Practice\", \"Advanced topics\"],\n"
        "  \"practice_suggestions\": [\"Build small exercises\", \"Work on mini projects\"],\n"
        "  \"resource_types\": [\"Videos\", \"Articles\", \"Books\", \"Documentation\"],\n"
        "  \"timeline\": \"4-6 weeks\"\n"
        "}\n"
    )

    response = generate_text(prompt)
    cleaned = response.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.replace("```json", "").replace("```", "").strip()

    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise ValueError("Gemini returned an invalid learning path response.") from exc

    required_keys = {
        "beginner_level",
        "intermediate_level",
        "advanced_level",
        "suggested_learning_order",
        "practice_suggestions",
        "resource_types",
        "timeline",
    }
    if not isinstance(data, dict) or not required_keys.issubset(data.keys()):
        raise ValueError("Learning path response did not match the required structure.")
    return data
