from intent import detect_intent
import re


# -------- HELPER: SMART RESPONSE --------
def smart_reply(state, base_response):
    history = state.get("history", [])

    # Use last 2 messages for context
    last_msgs = " ".join([msg["content"] for msg in history[-2:]])

    # Make response feel contextual
    if "okay" in last_msgs or "ok" in last_msgs:
        return base_response + "\n\nLet me know what you'd like to explore next 🙂"

    if "more" in last_msgs or "elaborate" in last_msgs:
        return base_response + "\n\nI can go deeper into any part if you want 👍"

    return base_response


# ---------------- INTENT ----------------
def intent_node(state):
    if state.get("intent") == "lead" and state.get("step") is not None:
        return state

    user_input = state["input"]
    state["intent"] = detect_intent(user_input)
    return state


# ---------------- RAG ----------------
def rag_node(state):
    text = state["input"].lower()

    if "feature" in text or "platform" in text:
        response = """Our platform helps creators grow using AI 🚀

You can:
• Automate content
• Build AI agents
• Analyze performance

What would you like to explore?"""

    elif "pricing" in text or "price" in text:
        response = """We offer 3 plans:

• Free – Basic features  
• Pro – ₹499/month  
• Enterprise – Custom pricing  

Want help choosing one?"""

    elif "agent" in text or "automation" in text:
        response = """You can build AI agents 🤖:

1. Voice Agent (handles calls)
2. Chat Agent (handles chats)

Reply with 1 or 2 to continue."""

    elif text.strip() == "1":
        response = """Voice agents can:
• Handle calls 📞
• Automate bookings
• Provide support

Do you want help setting one up?"""

    elif text.strip() == "2":
        response = """Chat agents can:
• Automate replies 💬
• Handle FAQs
• Provide instant support

Let’s get you started!"""

        state["intent"] = "lead"
        state["step"] = "ask_name"

    else:
        response = """I’m an AI assistant with limited scope 🙂

I can help with:
• Platform features
• Pricing
• Automation & agents

If you need more advanced help, you can upgrade your plan."""

    # ✅ make it smarter
    final_response = smart_reply(state, response)

    print("🤖:", final_response)

    # ✅ store bot reply
    state["history"].append({"role": "bot", "content": final_response})

    return state


# ---------------- LEAD ----------------
def lead_node(state):
    user_input = state["input"]

    if state.get("step") is None:
        state["step"] = "ask_name"
        response = "Before we continue, what's your name?"

    elif state["step"] == "ask_name":
        state["name"] = user_input
        state["step"] = "ask_email"
        response = f"Nice to meet you, {user_input} 😊 What's your email?"

    elif state["step"] == "ask_email":
        if not re.match(r"[^@]+@[^@]+\.[^@]+", user_input):
            response = "That doesn't look like a valid email. Try again."
            print("🤖:", response)
            return state

        state["email"] = user_input
        state["step"] = "ask_platform"
        response = "Great 👍 Which platform do you create content on?"

    elif state["step"] == "ask_platform":
        state["platform"] = user_input

        response = f"""Perfect! 🎉

Name: {state['name']}
Email: {state['email']}
Platform: {state['platform']}

We’ll reach out soon 🚀"""

        # reset
        state["step"] = None
        state["intent"] = None

    print("🤖:", response)

    # store bot reply
    state["history"].append({"role": "bot", "content": response})

    return state