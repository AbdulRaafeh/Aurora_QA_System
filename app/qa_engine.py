from openai import OpenAI
import os
from dotenv import load_dotenv
from .api_client import get_member_messages

load_dotenv()

# Initialize OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)


def answer_question(question: str):
    # Fetch all messages
    raw_messages = get_member_messages()

    # Reduce noise: we only keep relevant fields (name, time, message)
    messages = [
        {
            "user_name": m.get("user_name"),
            "timestamp": m.get("timestamp"),
            "message": m.get("message")
        }
        for m in raw_messages
    ]

    # Build a strict, anti-hallucination prompt
    prompt = f"""
    You are an extraction engine that answers questions only using the given messages.

    RULES:
    - If the answer IS explicitly found in the messages, reply with ONLY the answer.
    - Do NOT guess or assume anything.
    - Do NOT explain your reasoning.
    - Do NOT describe the messages.
    - Do NOT generate fake messages.
    - Do NOT add commentary.

    MESSAGES (JSON):
    {messages}

    QUESTION:
    {question}

    FINAL ANSWER:
    """

    # Call OpenRouter model
    response = client.chat.completions.create(
        model="qwen/qwen-2.5-7b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0  # deterministic, prevents hallucinations
    )

    final_answer = response.choices[0].message.content.strip()
    return final_answer
