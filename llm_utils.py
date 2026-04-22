import warnings
import logging
import os
import sys

# Suppress all warnings and logs
warnings.filterwarnings("ignore")
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
logging.disable(logging.CRITICAL)
logging.getLogger('google.generativeai').setLevel(logging.CRITICAL)
logging.getLogger('absl').setLevel(logging.CRITICAL)
logging.getLogger('urllib3').setLevel(logging.CRITICAL)

# Redirect stderr to suppress startup messages
import io
sys.stderr = io.StringIO()

import google.generativeai as genai
import json
from typing import Optional
from rag_enhanced import retrieve_semantic_answer

# Configure the Gemini API
API_KEY = "AIzaSyAolc9qcMjvyFLLhzuybsn-j2E2W6EI1FY"
genai.configure(api_key=API_KEY)


def detect_intent_llm(user_input: str) -> str:
    """
    Use LLM to detect user intent with fallback to keyword matching.
    Returns either 'rag' (answer FAQ) or 'lead' (capture lead info)
    """
    try:
        model = genai.GenerativeModel("gemini-pro")
        
        prompt = f"""Analyze this user message and determine their intent. 
        Respond with ONLY one word: either 'rag' or 'lead'
        
        'rag' = User is asking about features, pricing, capabilities, or has general questions
        'lead' = User is interested in signing up, wants to start, or is ready to provide their information
        
        User message: "{user_input}"
        
        Intent:"""
        
        response = model.generate_content(prompt)
        intent = response.text.strip().lower()
        
        if intent in ["rag", "lead"]:
            return intent
        else:
            return "rag"  # default fallback
    except Exception as e:
        pass  # Silently fallback
        return _fallback_intent_detection(user_input)


def _fallback_intent_detection(user_input: str) -> str:
    """Fallback keyword-based intent detection"""
    text = user_input.lower()

    if any(word in text for word in ["start", "signup", "register", "interested", "let's go", "get started"]):
        return "lead"

    # Default to rag for questions and info
    return "rag"


def generate_response_llm(user_input: str, context: dict, intent: str) -> str:
    """
    Use LLM to generate contextual responses with semantic RAG context.
    Falls back to template responses if LLM fails.
    """
    try:
        model = genai.GenerativeModel("gemini-pro")
        
        # Build context from conversation history
        history_context = "\n".join(
            [f"{msg['role'].upper()}: {msg['content']}" 
             for msg in context.get("history", [])[-4:]]  # Last 4 messages
        )
        
        if intent == "rag":
            # Retrieve relevant knowledge using semantic search
            rag_context = retrieve_semantic_answer(user_input)
            
            prompt = f"""You are a helpful sales assistant for a creator automation platform.
            
Conversation history:
{history_context}

Relevant knowledge base:
{rag_context}

User just said: "{user_input}"

Based on the knowledge base above, provide a helpful, conversational response.
Keep response brief (2-3 sentences). Be friendly and engaging."""
        else:
            prompt = f"""You are collecting lead information for a creator automation platform.
            
Current user info:
- Name: {context.get('name', 'Not provided')}
- Email: {context.get('email', 'Not provided')}
- Platform: {context.get('platform', 'Not provided')}

You are at step: {context.get('step', 'ask_name')}

User just said: "{user_input}"

If you haven't collected the name yet, ask for their name.
If you have the name, ask for their email.
If you have email, ask which platform they create content on.
If you have all info, thank them and confirm details.

Keep response brief and conversational."""
        
        response = model.generate_content(prompt)
        return response.text.strip()
    
    except Exception as e:
        pass  # Silently fallback
        return _get_fallback_response(user_input, context, intent)


def _get_fallback_response(user_input: str, context: dict, intent: str) -> str:
    """Fallback to template responses when LLM fails"""
    text = user_input.lower()
    
    if intent == "rag":
        if any(word in text for word in ["hi", "hello", "hey", "help", "what"]):
            return "Hi! Our platform helps creators automate with AI agents and RAG. Ask about features, pricing, or say 'start' to get going!"
        if "feature" in text or "platform" in text:
            return "Our platform helps creators grow using AI 🚀\n\nYou can:\n• Automate content\n• Build AI agents\n• Analyze performance\n\nWhat would you like to explore?"
        elif "pricing" in text or "price" in text:
            return "We offer 3 plans:\n\n• Free – Basic features\n• Pro – ₹499/month\n• Enterprise – Custom pricing\n\nWant help choosing one?"
        elif "agent" in text or "automation" in text:
            return "You can build AI agents 🤖:\n\n1. Voice Agent (handles calls)\n2. Chat Agent (handles chats)\n\nReply with 1 or 2 to continue."
        else:
            return "Sure, tell me more about features, pricing, or getting started!"
    else:
        if context.get("step") == "ask_name":
            return f"Nice to meet you, {user_input}! 😊 What's your email?"
        elif context.get("step") == "ask_email":
            return "Great! Which platform do you create content on?"
        else:
            return "Thank you for your interest! We'll be in touch soon. 🚀"


def load_knowledge() -> dict:
    """Load knowledge base"""
    try:
        with open("data/knowledge.json") as f:
            return json.load(f)
    except:
        return {
            "pricing": {
                "basic": "Basic Plan: $29/month, 10 videos/month, 720p",
                "pro": "Pro Plan: $79/month, Unlimited videos, 4K, AI captions"
            },
            "policies": {
                "refund": "No refunds after 7 days",
                "support": "24/7 support only on Pro plan"
            }
        }


def retrieve_answer(query: str) -> str:
    """Retrieve answer from knowledge base based on query"""
    kb = load_knowledge()
    text = str(kb).lower()

    if "price" in query.lower() or "plan" in query.lower():
        return kb["pricing"]["basic"] + "\n" + kb["pricing"]["pro"]

    if "refund" in query.lower():
        return kb["policies"]["refund"]

    if "support" in query.lower():
        return kb["policies"]["support"]

    return "Let me help you with that."

