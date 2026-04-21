from graph import build_graph

graph = build_graph()

state = {}

print("🤖 Chatbot started! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    state["input"] = user_input

    state = graph.invoke(state)

    print("🤖:", state.get("response"))