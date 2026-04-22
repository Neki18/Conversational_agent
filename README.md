# 🤖 Creator Automation Chatbot

An intelligent conversational AI assistant built with LangGraph, Google Gemini AI, and semantic search. The chatbot helps creators learn about platform features, pricing, and captures lead information.

## ✨ Features

- **🧠 LLM-Powered Responses**: Uses Google Gemini AI for intelligent, context-aware conversations
- **🎯 Intent Detection**: Automatically detects whether user wants information (RAG) or to sign up (Lead capture)
- **🔍 Semantic Search**: Enhanced RAG system using embeddings for accurate knowledge retrieval
- **📱 Beautiful Web UI**: Streamlit-based interface with real-time chat
- **✅ Enhanced Validation**: Smart email validation and lead capture flow
- **📚 Conversation History**: Maintains context across multiple turns

## 📁 Project Structure

```
conversational_agent/
├── app.py                 # CLI-based chatbot (original)
├── app_web.py            # Streamlit web UI (recommended)
├── graph.py              # LangGraph workflow definition
├── nodes.py              # Graph nodes (intent, RAG, lead)
├── intent.py             # Intent detection module
├── llm_utils.py          # LLM and utility functions
├── rag_enhanced.py       # Semantic search RAG system
├── rag.py                # Original RAG module
├── tools.py              # Helper tools
├── state.py              # State definition
├── data/
│   └── knowledge.json    # Knowledge base
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up API Key

The chatbot uses Google Gemini API. The API key is already configured in `llm_utils.py`:

```python
API_KEY = "AIzaSyAolc9qcMjvyFLLhzuybsn-j2E2W6EI1FY"
```

For production, use environment variables:

```bash
export GOOGLE_API_KEY="your-api-key"
```

### 3. Run the Web UI (Recommended)

```bash
streamlit run app_web.py
```

This will open a beautiful web interface at `http://localhost:8501`

### 4. Or Run the CLI Version

```bash
python app.py
```

## 🏗️ Architecture

### Workflow Flow

```
User Input
    ↓
Intent Detection (LLM-based)
    ├─→ RAG Node (Answer FAQ questions)
    │   └─→ Uses semantic search + LLM
    └─→ Lead Node (Capture lead info)
        ├─→ Ask name
        ├─→ Ask email (with validation)
        ├─→ Ask platform
        └─→ Confirm & end conversation
```

### Key Components

#### 1. **Intent Detection** (`intent.py`)
- Uses LLM to classify user intent
- Returns: `"rag"` (information) or `"lead"` (sign up)
- Fallback to keyword matching if LLM fails

#### 2. **RAG Node** (`nodes.py` + `rag_enhanced.py`)
- Answers questions about features, pricing, capabilities
- Uses semantic search with embeddings
- FAISS-based vector search for efficient retrieval
- LLM synthesizes responses from knowledge base

#### 3. **Lead Node** (`nodes.py`)
- Multi-step form to collect user information
- Enhanced email validation using regex
- Confirms all information before submission
- Resets state after capturing lead

#### 4. **LLM Integration** (`llm_utils.py`)
- Google Gemini AI for all NLP tasks
- Context-aware response generation
- Graceful fallback to templates

#### 5. **Semantic Search** (`rag_enhanced.py`)
- Sentence-Transformers embeddings
- FAISS vector index for fast retrieval
- Automatic document splitting and indexing
- Relevance scoring

## 💬 Example Conversations

### Example 1: Product Information

```
You: What can I do with your platform?
Bot: Our platform helps creators automate content and build AI agents. 
     You can set up voice agents for calls or chat agents for support.
     What interests you most?

You: Tell me about pricing
Bot: We offer 3 plans - Free for basics, Pro at ₹499/month for unlimited features,
     and Enterprise for custom needs. Which would you like to explore?
```

### Example 2: Lead Capture

```
You: I'm interested in getting started
Bot: Great! Before we continue, what's your name?

You: John
Bot: Nice to meet you, John! What's your email?

You: john@example.com
Bot: Which platform do you create content on?

You: YouTube
Bot: Perfect! 🎉
     Name: John
     Email: john@example.com
     Platform: YouTube
     We'll reach out soon! 🚀
```

## 🔧 Configuration

### Knowledge Base

Edit `data/knowledge.json` to update:
- Pricing information
- Refund policies
- Support details

Example:
```json
{
  "pricing": {
    "basic": "Basic Plan: ₹0/month - Perfect for getting started",
    "pro": "Pro Plan: ₹499/month - Unlimited features"
  },
  "policies": {
    "refund": "30-day money back guarantee",
    "support": "24/7 support on Pro & Enterprise"
  }
}
```

### Conversation State

The chatbot maintains state including:
```python
{
    "input": str,              # Current user input
    "intent": str,             # "rag" or "lead"
    "step": str,               # Lead capture step
    "name": str,               # Captured name
    "email": str,              # Captured email
    "platform": str,           # Captured platform
    "history": List[dict]      # Conversation history
}
```

## 🎯 Customization

### Change the API Key

Edit `llm_utils.py`:
```python
API_KEY = "your-new-api-key"
```

### Update the Embedding Model

Edit `rag_enhanced.py`:
```python
embedding_model = SentenceTransformer('all-mpnet-base-v2')  # More accurate but slower
```

### Modify Response Style

Edit prompts in `llm_utils.py`:
- `detect_intent_llm()`: Change intent classification logic
- `generate_response_llm()`: Change response generation style

## 📊 Performance

- **Intent Detection**: ~500ms (LLM inference)
- **RAG Retrieval**: ~50ms (FAISS vector search)
- **Response Generation**: ~1-2s (LLM inference)
- **Total Response Time**: ~2-3s per message

## 🐛 Troubleshooting

### Error: "API key not valid"
- Check your Google Gemini API key in `llm_utils.py`
- Ensure the API is enabled in Google Cloud Console

### Error: "FAISS not found"
```bash
pip install faiss-cpu
```

### Slow responses
- Check internet connection for LLM calls
- Consider using a faster embedding model (smaller)

### Knowledge base not loading
- Verify `data/knowledge.json` exists
- Check JSON syntax for errors

## 🚀 Future Enhancements

- [ ] Multi-language support
- [ ] Sentiment analysis
- [ ] Lead CRM integration
- [ ] Analytics dashboard
- [ ] Custom intent categories
- [ ] Voice input/output
- [ ] WhatsApp/Telegram integration
- [ ] Admin panel for knowledge base management

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Development

To modify the chatbot:

1. **Update nodes**: Edit `nodes.py` for conversation logic
2. **Update knowledge**: Edit `data/knowledge.json` for info
3. **Update prompts**: Edit `llm_utils.py` for LLM behavior
4. **Test changes**: Run `python app.py` or `streamlit run app_web.py`

## 📚 Resources

- [LangGraph Documentation](https://github.com/langchain-ai/langgraph)
- [Google Gemini API](https://ai.google.dev/)
- [Sentence-Transformers](https://www.sbert.net/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Streamlit](https://streamlit.io/)

## 🤝 Support

For issues or questions, please create an issue or contact me.

---

**Built with ❤️ using AI & Python**
