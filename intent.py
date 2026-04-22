from google import genai
import os

client = genai.Client(api_key=("AIzaSyAolc9qcMjvyFLLhzuybsn-j2E2W6EI1FY"))

def detect_intent(user_input):
    text = user_input.lower()

    # PRICING
    if any(word in text for word in ["price", "pricing", "cost", "plan"]):
        return "pricing"

    # PLATFORM / INFO
    elif any(word in text for word in [
        "platform", "about", "features", "what does", "how does",
        "automate", "automation", "ai tools", "agent", "calls", "domain"
    ]):
        return "info"

    # FOLLOW-UP / CONTINUE
    elif any(word in text for word in [
        "elaborate", "more", "explain", "details", "tell me more"
    ]):
        return "followup"

    # LEAD / INTEREST
    elif any(word in text for word in [
        "join", "signup", "register", "interested", "start", "try"
    ]):
        return "lead"

    # GREETING
    elif any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    return "general"