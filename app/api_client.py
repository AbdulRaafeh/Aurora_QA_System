import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("AURORA_MESSAGES_URL").rstrip("/")


def get_member_messages():
    response = requests.get(BASE_URL)
    response.raise_for_status()

    raw = response.json()

    # Aurora API returns: { "total": x, "items": [ ... ] }
    if isinstance(raw, dict) and "items" in raw:
        return raw["items"]

    # fallback case
    return raw
