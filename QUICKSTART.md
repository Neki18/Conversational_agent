# 🚀 Quick Start Guide

## Installation & Setup (2 minutes)

### Step 1: Install Python Packages
```bash
cd c:\Users\Neki jain\Downloads\conversational_agent
pip install -r requirements.txt
```

### Step 2: Verify API Key
The Google Gemini API key is already configured in `llm_utils.py`. No action needed!

## Running the Chatbot

### Option A: Web Interface (Recommended) 🌐
```bash
streamlit run app_web.py
```
- Opens at: http://localhost:8501
- Beautiful UI with chat history
- Better user experience
- Shows lead capture status

### Option B: CLI Interface 💻
```bash
python app_cli.py
```
- Terminal-based interaction
- Good for testing & debugging
- Type 'exit' to quit
- Type 'clear' to reset conversation

## What the Chatbot Can Do

### 1. Answer Questions
Ask about:
- ✅ Platform features
- ✅ Pricing & plans
- ✅ AI agents
- ✅ Automation capabilities

Example:
```
You: What are your pricing plans?
Bot: We offer 3 plans - Free, Pro ₹499/month, and Enterprise...
```

### 2. Capture Leads
Interested users can provide:
- 👤 Name
- 📧 Email (with validation)
- 📱 Platform

Example:
```
You: I'm interested
Bot: What's your name?
You: John
Bot: What's your email?
You: john@example.com
Bot: Which platform do you use?
You: YouTube
Bot: Perfect! We'll reach out soon! 🚀
```

## Technology Stack

| Component | Technology |
|-----------|-----------|
| **AI/LLM** | Google Gemini 1.5 Flash |
| **Workflow** | LangGraph |
| **Embeddings** | Sentence-Transformers |
| **Vector Search** | FAISS |
| **Web UI** | Streamlit |
| **Language** | Python 3.8+ |

## Project Structure

```
├── app_web.py           ← START HERE (Web UI)
├── app_cli.py           ← Alternative (CLI)
├── graph.py             ← Conversation workflow
├── nodes.py             ← Conversation logic
├── llm_utils.py         ← LLM integration
├── rag_enhanced.py      ← Semantic search
├── data/
│   └── knowledge.json   ← Edit for your content
└── README.md            ← Full documentation
```

## Common Tasks

### Update Knowledge Base
Edit `data/knowledge.json`:
```json
{
  "pricing": {
    "basic": "Free - Basic features",
    "pro": "₹499/month - Premium features"
  }
}
```

### Change Bot Personality
Edit prompts in `llm_utils.py`:
- Line ~45: RAG response prompt
- Line ~65: Lead capture prompt

### Add More Intent Types
Edit `intent.py`:
- Add keywords for new intents
- Update routing in `graph.py`

## Troubleshooting

**Q: "Module not found" error?**
A: Run `pip install -r requirements.txt` again

**Q: "API key not valid"?**
A: Check the API key in `llm_utils.py` is correct

**Q: Streamlit not opening?**
A: Try `streamlit run app_web.py --logger.level=debug`

**Q: Responses are slow?**
A: Check internet connection (needed for LLM API calls)

## Example Conversation Flow

```
🤖 Bot: Hello! I'm your AI assistant. Ask me about features, 
        pricing, or get started! 

👤 You: What can you automate?

🤖 Bot: We help automate:
        • Content creation & publishing
        • AI voice & chat agents
        • Performance analytics
        
        What interests you most?

👤 You: Tell me about voice agents

🤖 Bot: Voice agents handle phone calls, automate bookings,
        provide customer support, and more. 
        
        Would you like to get started?

👤 You: Yes!

🤖 Bot: Great! What's your name?

👤 You: Sarah

🤖 Bot: Nice to meet you, Sarah! What's your email?

👤 You: sarah@example.com

🤖 Bot: Perfect! Which platform do you use?

👤 You: Instagram

🤖 Bot: Excellent!
        
        📋 Your Information:
        • Name: Sarah
        • Email: sarah@example.com
        • Platform: Instagram
        
        We'll reach out soon! 🚀
```

## Next Steps

1. ✅ Run `streamlit run app_web.py`
2. ✅ Try asking about features
3. ✅ Fill out the lead capture form
4. ✅ Edit `data/knowledge.json` with your content
5. ✅ Deploy to production (Streamlit Cloud, Heroku, etc.)

## 📚 Learn More

- [Full Documentation](README.md)
- [LangGraph Docs](https://github.com/langchain-ai/langgraph)
- [Google Gemini API](https://ai.google.dev/)
- [Streamlit Docs](https://docs.streamlit.io/)

---

**That's it! Your AI chatbot is ready to go! 🎉**
