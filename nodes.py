from intent import detect_intent
import re

def intent_node(state):
    user_input = state.get("input", "")
    state["intent"] = detect_intent(user_input)
    return state


# ---------------- INFO / PRICING ----------------

def rag_node(state):
    intent = state.get("intent")

    if intent == "pricing":
        state["response"] = (
            "We offer 3 plans:\n"
            "• Free Plan – Basic features\n"
            "• Pro Plan – ₹499/month\n"
            "• Enterprise – Custom pricing\n\n"
            "Would you like to sign up?"
        )

    elif intent == "info":
        state["response"] = (
            "Our platform helps creators grow using AI tools 🚀\n"
            "You can automate content, analyze performance, and scale faster."
        )

    elif intent == "greeting":
        state["response"] = "Hey! 😊 How can I help you today?"

    else:
        state["response"] = "Can you please clarify what you're looking for?"

    return state


# ---------------- LEAD CAPTURE ----------------

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def lead_node(state):
    user_input = state.get("input", "")
    intent = state.get("intent")

    # Only trigger lead if user is interested
    if intent != "lead" and not state.get("collecting"):
        return state

    state["collecting"] = True

    if "name" not in state:
        state["response"] = "Can I know your name?"
        state["step"] = "name"
        return state

    if state.get("step") == "name":
        state["name"] = user_input
        state["response"] = f"Nice to meet you, {user_input}! 😊 What's your email?"
        state["step"] = "email"
        return state

    if state.get("step") == "email":
        if not is_valid_email(user_input):
            state["response"] = "That doesn't look like a valid email. Try again."
            return state

        state["email"] = user_input
        state["response"] = "Which platform do you create content on?"
        state["step"] = "platform"
        return state

    if state.get("step") == "platform":
        state["platform"] = user_input

        state["response"] = (
            f"Perfect! 🎉\n"
            f"Name: {state['name']}\n"
            f"Email: {state['email']}\n"
            f"Platform: {state['platform']}\n"
            f"We’ll reach out soon 🚀"
        )

        state["collecting"] = False
        state["step"] = None
        return state

    return state