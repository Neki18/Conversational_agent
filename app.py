from graph import build_graph

graph = build_graph()

print("🤖 Chatbot started! Type 'exit' to stop.\n")

state = {
    "input": "",
    "intent": None,
    "step": None,
    "name": None,
    "email": None,
    "platform": None,
    "history": []   # ✅ NEW
}

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("🤖: Bye! 👋")
        break

    state["input"] = user_input

    # ✅ store user message
    state["history"].append({"role": "user", "content": user_input})

    state = graph.invoke(state)