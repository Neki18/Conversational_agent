from google import genai
import os

client = genai.Client(api_key=("AIzaSyAolc9qcMjvyFLLhzuybsn-j2E2W6EI1FY"))

def detect_intent(user_input):
    text = user_input.lower()

    if any(word in text for word in ["price", "pricing", "cost", "plan"]):
        return "rag"

    if any(word in text for word in ["feature", "platform", "what", "how"]):
        return "rag"

    if any(word in text for word in ["agent", "automation", "automate"]):
        return "rag"

    if any(word in text for word in ["start", "signup", "register", "interested"]):
        return "lead"

    # fallback
    return "rag"