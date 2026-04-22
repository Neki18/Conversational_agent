from graph import build_graph
import json
from datetime import datetime

graph = build_graph()

print("""
╔════════════════════════════════════════════════════════════╗
║     🤖 Creator Automation AI Assistant                     ║
║                                                            ║
║  Powered by: Google Gemini AI | LangGraph | Semantic RAG   ║
║                                                            ║
║  Type 'exit' to quit, 'clear' to reset conversation        ║
╚════════════════════════════════════════════════════════════╝
""")

state = {
    "input": "",
    "intent": None,
    "step": None,
    "name": None,
    "email": None,
    "platform": None,
    "history": []
}

message_count = 0

try:
    while True:
        user_input = input("\n📝 You: ").strip()

        if user_input.lower() == "exit":
            print("\n👋 Thanks for chatting! Goodbye!")
            break
        
        if user_input.lower() == "clear":
            state["history"] = []
            state["intent"] = None
            state["step"] = None
            print("🔄 Conversation reset!")
            continue
        
        if not user_input:
            continue

        state["input"] = user_input

        # Store user message
        state["history"].append({"role": "user", "content": user_input})

        # Invoke the graph
        state = graph.invoke(state)
        
        message_count += 1
        
        # Show conversation stats every 5 messages
        if message_count % 5 == 0:
            print(f"\n📊 (Messages: {message_count} | Mode: {'Lead Capture' if state['intent'] == 'lead' else 'FAQ'})")

except KeyboardInterrupt:
    print("\n\n⏹️ Chat interrupted. Goodbye!")
except Exception as e:
    print(f"\n❌ Error: {str(e)}")
    print("Please try again or type 'exit' to quit.")
