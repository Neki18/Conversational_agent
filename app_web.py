import streamlit as st
from graph import build_graph
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Creator Bot - AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        padding-top: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        gap: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
        margin-left: 2rem;
        justify-content: flex-end;
    }
    .bot-message {
        background-color: #f5f5f5;
        margin-right: 2rem;
    }
    .message-content {
        max-width: 80%;
        word-wrap: break-word;
    }
    .bot-avatar {
        font-size: 1.5rem;
    }
    .user-avatar {
        font-size: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "graph" not in st.session_state:
    st.session_state.graph = build_graph()

if "state" not in st.session_state:
    st.session_state.state = {
        "input": "",
        "intent": None,
        "step": None,
        "name": None,
        "email": None,
        "platform": None,
        "history": []
    }

if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
st.markdown("# 🤖 Creator Automation Assistant")
st.markdown("Chat with our AI assistant to learn about features, pricing, and get started!")

# Sidebar with info
with st.sidebar:
    st.header("About")
    st.markdown("""
    ### Creator Bot
    An intelligent chatbot powered by:
    - 🧠 Google Gemini AI
    - 🔗 LangGraph
    - 🔍 Semantic Search (RAG)
    - ⚡ Real-time Responses
    """)
    
    if st.session_state.state.get("name"):
        st.success(f"✅ Lead Captured: {st.session_state.state['name']}")
        st.write(f"📧 {st.session_state.state.get('email', 'N/A')}")
        st.write(f"📱 {st.session_state.state.get('platform', 'N/A')}")
    
    if st.button("🔄 Reset Chat"):
        st.session_state.messages = []
        st.session_state.state = {
            "input": "",
            "intent": None,
            "step": None,
            "name": None,
            "email": None,
            "platform": None,
            "history": []
        }
        st.rerun()

# Display chat history
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user-message">
                <div class="message-content">
                    <strong>You:</strong> {message["content"]}
                </div>
                <div class="user-avatar">👤</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message bot-message">
                <div class="bot-avatar">🤖</div>
                <div class="message-content">
                    <strong>Bot:</strong> {message["content"]}
                </div>
            </div>
            """, unsafe_allow_html=True)

# Input area
st.markdown("---")

col1, col2 = st.columns([0.85, 0.15])

with col1:
    user_input = st.text_input(
        "Type your message here...",
        placeholder="Ask about features, pricing, or get started...",
        label_visibility="collapsed"
    )

with col2:
    send_button = st.button("Send", use_container_width=True, type="primary")

# Process input
if send_button and user_input:
    # Add user message to display
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Update state
    st.session_state.state["input"] = user_input
    st.session_state.state["history"].append({"role": "user", "content": user_input})
    
    # Get bot response
    try:
        # Invoke the graph
        st.session_state.state = st.session_state.graph.invoke(st.session_state.state)
        
        # Get the last bot message from history
        if st.session_state.state["history"]:
            last_message = st.session_state.state["history"][-1]
            if last_message["role"] == "bot":
                bot_response = last_message["content"]
                st.session_state.messages.append({"role": "bot", "content": bot_response})
    except Exception as e:
        error_msg = f"Sorry, something went wrong: {str(e)}"
        st.session_state.messages.append({"role": "bot", "content": error_msg})
        st.error(f"Error: {str(e)}")
    
    st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray; font-size: 0.8rem;">
    Powered by Google Gemini AI | LangGraph | Semantic Search
</div>
""", unsafe_allow_html=True)
