from google import genai
import os

client = genai.Client(api_key=("AIzaSyAolc9qcMjvyFLLhzuybsn-j2E2W6EI1FY"))

def detect_intent(user_input):
    text = user_input.lower()

    if any(word in text for word in ["price", "pricing", "cost", "plan"]):
        return "pricing"

    elif any(word in text for word in ["what", "about", "platform", "service"]):
        return "info"

    elif any(word in text for word in ["signup", "register", "join", "interested"]):
        return "lead"

    elif any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    else:
        return "general"