from intent import detect_intent
import re

def intent_node(state):
    user_input = state.get("input", "")
    state["intent"] = detect_intent(user_input)
    return state


# ---------------- SMART RESPONSE ----------------

def rag_node(state):
    intent = state.get("intent")
    last_topic = state.get("last_topic")

    # GREETING
    if intent == "greeting":
        state["response"] = "Hey! 😊 How can I help you today?"

    # PRICING
    elif intent == "pricing":
        state["response"] = (
            "We offer 3 plans:\n"
            "• Free – Basic features\n"
            "• Pro – ₹499/month\n"
            "• Enterprise – Custom pricing\n\n"
            "Want help choosing one?"
        )
        state["last_topic"] = "pricing"

    # INFO
    elif intent == "info":
        user_input = state.get("input", "").lower()

        if "call" in user_input or "agent" in user_input:
            state["response"] = (
                "Great question! 🤖\n"
                "You can build AI agents that:\n"
                "• Handle customer calls\n"
                "• Answer queries automatically\n"
                "• Integrate with your workflows\n\n"
                "Do you want to build a voice agent or chat agent?"
            )

        elif "automate" in user_input:
            state["response"] = (
                "You can automate:\n"
                "• Content creation\n"
                "• Posting & scheduling\n"
                "• Responses to users\n"
                "• Analytics tracking\n\n"
                "What kind of automation are you looking for?"
            )

        elif "domain" in user_input:
            state["response"] = (
                "We work across multiple domains:\n"
                "• Content Creation\n"
                "• Customer Support Automation\n"
                "• AI Chatbots & Voice Agents\n"
                "• Marketing Automation\n\n"
                "Which one interests you?"
            )

        else:
            state["response"] = (
                "Our platform helps creators grow using AI 🚀\n"
                "You can automate tasks, build agents, and scale faster.\n\n"
                "What would you like to explore?"
            )

        state["last_topic"] = "info"

    # FOLLOW-UP (THIS FIXES YOUR ISSUE)
    elif intent == "followup":
        if last_topic == "info":
            state["response"] = (
                "Sure! Let me break it down further 👇\n"
                "• AI Agents → handle chats/calls automatically\n"
                "• Automation → reduces manual work\n"
                "• Insights → helps you grow faster\n\n"
                "What part do you want to go deeper into?"
            )

        elif last_topic == "pricing":
            state["response"] = (
                "The Pro plan is best for most users 💡\n"
                "It gives advanced automation + analytics.\n\n"
                "Do you want to try it?"
            )

        else:
            state["response"] = "Tell me what you'd like more details on 🙂"

    # GENERAL (REMOVE BORING RESPONSE)
    else:
        state["response"] = (
            "I think you're exploring the platform 🙂\n"
            "You can ask about features, pricing, or automation."
        )

    return state


# ---------------- LEAD ----------------

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def lead_node(state):
    user_input = state.get("input", "")
    intent = state.get("intent")

    # only start if user shows interest
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