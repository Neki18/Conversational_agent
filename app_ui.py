import streamlit as st
import warnings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings("ignore")

from graph import build_graph
import json
from datetime import datetime
import time

# Configure Streamlit page
st.set_page_config(
    page_title="Creator Automation Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "🤖 AI-Powered Creator Automation Platform"
    }
)

# Custom CSS for beautiful UI
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main {
        background: white;
        border-radius: 10px;
        padding: 20px;
    }
    
    /* Header Styling */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 30px;
        border-radius: 10px;
        margin-bottom: 30px;
        text-align: center;
    }
    
    .header-title {
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    .header-subtitle {
        font-size: 1.1em;
        opacity: 0.9;
    }
    
    /* Chat Messages */
    .chat-message {
        padding: 15px 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        animation: slideIn 0.3s ease;
        color: #333;
    }
    
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin-left: 40px;
        border-radius: 18px 18px 4px 18px;
    }
    
    .bot-message {
        background: #f0f0f0;
        color: #333;
        margin-right: 40px;
        border-radius: 18px 18px 18px 4px;
        border-left: 4px solid #667eea;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Input Area */
    .input-container {
        display: flex;
        gap: 10px;
        padding: 20px;
        background: #f9f9f9;
        border-radius: 10px;
        margin-top: 20px;
    }
    
    /* Sidebar */
    .sidebar-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    
    .stats-box {
        background: white;
        color: #333;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
        border-left: 4px solid #667eea;
    }
    
    .feature-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        color: #333;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
        border-left: 4px solid #667eea;
    }
    
    .button-primary {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: bold;
        cursor: pointer;
    }
    
    /* Badges */
    .badge {
        display: inline-block;
        background: #667eea;
        color: white;
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 0.9em;
        margin-right: 5px;
    }
    
    /* Cards */
    .info-card {
        background: white;
        color: #333;
        border: 2px solid #667eea;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    
    .success-message {
        background: #d4edda;
        color: #155724;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #28a745;
        margin-bottom: 15px;
    }
    
    .loading-spinner {
        display: inline-block;
        animation: spin 1s linear infinite;
    }
    
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
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

if "show_features" not in st.session_state:
    st.session_state.show_features = False

# Header
st.markdown("""
<div class="header-container">
    <div class="header-title">🚀 Creator Automation Platform</div>
    <div class="header-subtitle">AI-Powered Content Creation & Automation</div>
</div>
""", unsafe_allow_html=True)

# Main Content
col1, col2 = st.columns([3, 1])

with col1:
    # Chat Display Area
    st.markdown("### 💬 Chat with our AI Assistant")
    
    chat_container = st.container()
    
    with chat_container:
        if len(st.session_state.messages) == 0:
            st.markdown("""
            <div style='text-align: center; padding: 40px;'>
                <h3>👋 Welcome to Creator Bot!</h3>
                <p>Ask me about:</p>
                <div style='display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;'>
                    <span class='badge'>✨ Features</span>
                    <span class='badge'>💰 Pricing</span>
                    <span class='badge'>🚀 Getting Started</span>
                    <span class='badge'>🤖 AI Agents</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            for message in st.session_state.messages:
                if message["role"] == "user":
                    st.markdown(f"""
                    <div class="chat-message user-message">
                        <strong>You:</strong> {message["content"]}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="chat-message bot-message">
                        <strong>🤖 Assistant:</strong> {message["content"]}
                    </div>
                    """, unsafe_allow_html=True)
    
    # Input Area
    st.markdown("---")
    col_input, col_send = st.columns([0.87, 0.13])
    
    with col_input:
        user_input = st.text_input(
            "Your message",
            placeholder="Ask about features, pricing, or how to get started...",
            label_visibility="collapsed",
            key="user_input"
        )
    
    with col_send:
        send_button = st.button("📤 Send", use_container_width=True, type="primary")
    
    # Process user input
    if send_button and user_input.strip():
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Update state
        st.session_state.state["input"] = user_input
        st.session_state.state["history"].append({"role": "user", "content": user_input})
        
        # Get bot response with error suppression
        try:
            with st.spinner("🤔 Thinking..."):
                st.session_state.state = st.session_state.graph.invoke(st.session_state.state)
        except Exception as e:
            st.session_state.state["history"].append({
                "role": "bot",
                "content": "I'm having trouble processing your request. Please try again!"
            })
        
        # Get the last bot message from history
        if len(st.session_state.state["history"]) > 0:
            last_msg = st.session_state.state["history"][-1]
            if last_msg.get("role") == "bot":
                st.session_state.messages.append({"role": "bot", "content": last_msg["content"]})
        
        st.rerun()

with col2:
    st.markdown("### ℹ️ Info Panel")
    
    # Lead Info
    if st.session_state.state.get("name"):
        st.markdown("""
        <div class="success-message">
            ✅ Lead Captured Successfully!
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="stats-box">
            <strong>Name:</strong> {st.session_state.state['name']}<br>
            <strong>Email:</strong> {st.session_state.state.get('email', 'N/A')}<br>
            <strong>Platform:</strong> {st.session_state.state.get('platform', 'N/A')}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="feature-box">
            <strong>💡 Tip:</strong> Tell us your name to start the lead capture process!
        </div>
        """, unsafe_allow_html=True)
    
    # Quick Features
    if st.button("📋 View Features", use_container_width=True):
        st.session_state.show_features = not st.session_state.show_features
    
    if st.session_state.show_features:
        st.markdown("#### 🎯 Key Features:")
        features = [
            "🎬 AI Content Generation",
            "📱 Multi-Platform Posting",
            "🤖 Voice AI Agent",
            "💬 Chat AI Agent",
            "📊 Analytics Dashboard",
            "👥 Team Collaboration",
            "⏰ Content Scheduling",
            "🎨 Content Templates"
        ]
        for feature in features:
            st.markdown(f"• {feature}")
    
    # Reset Button
    if st.button("🔄 Reset Chat", use_container_width=True):
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

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px; color: #666;'>
    <p><strong>Creator Automation Platform</strong> | Powered by 🧠 Google Gemini AI | 🔗 LangGraph | 🔍 Semantic RAG</p>
    <p style='font-size: 0.9em;'>© 2024 Creator Automation. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
