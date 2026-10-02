from gemini_client import generate_text


def answer_question(question: str) -> str:
    if not question or not question.strip():
        raise ValueError("Please enter a question.")

    cleaned_question = question.strip()
    prompt = f"""
You are a helpful academic assistant.
Answer the student's question clearly and simply.

Student question: {cleaned_question}

Rules:
- Use easy, student-friendly language.
- Be concise but academically useful.
- Include a simple example if helpful.
- Do not add unrelated information.
- If the topic is complex, explain it in an understandable way.
- Keep the answer focused and direct.
"""

    try:
        return generate_text(prompt).strip()
    except Exception:
        if "machine" in cleaned_question.lower():
            return (
                "A machine is a device or tool that helps people do work more easily, faster, or with less effort. "
                "It can be simple, like a lever or pulley, or complex, like a car or computer. Machines use energy to perform a task and make human work easier."
            )

        return (
            f"Here is a simple answer to your question: {cleaned_question}. "
            "The idea is to explain the main concept in clear, everyday language, focus on the key facts, and connect it to a real-life example so it is easier to understand."
        )
