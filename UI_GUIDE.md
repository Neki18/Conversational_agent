# 🚀 Creator Automation Platform - AI Chatbot

A sophisticated conversational AI chatbot with semantic RAG (Retrieval-Augmented Generation) for a creator automation platform. Features include intelligent intent detection, multi-turn conversations, and lead capture.

---

## ✨ What's New in This Update

### 🎨 **Beautiful New UI**
- **Enhanced Streamlit Interface** (`app_ui.py`)
- Modern gradient design with purple/blue theme
- Smooth animations and responsive layout
- Real-time chat with typing indicators
- Info panel showing captured leads
- Feature showcase and quick reference

### 📚 **Improved Knowledge Base**
The `data/knowledge.json` now includes:
- Company information & mission
- Detailed pricing plans (Basic, Pro, Enterprise)
- 10+ key features with descriptions
- Comprehensive policies (refund, support, security, cancellation)
- FAQ section with common questions

### 🔍 **Enhanced RAG System**
- Better semantic search using embeddings
- Structured document processing
- Support for nested JSON knowledge base
- Improved relevance ranking
- Multiple document categories

### 🔇 **Quiet Operation**
- Suppressed error messages and warnings
- Clean console output
- Professional logging setup

---

## 🛠️ Project Structure

```
conversational_agent/
├── app_ui.py              # 🎨 NEW: Beautiful Streamlit UI
├── app_cli.py             # CLI interface
├── app_web.py             # Original web interface
├── graph.py               # LangGraph workflow
├── nodes.py               # Conversation nodes
├── state.py               # State definitions
├── intent.py              # Intent detection
├── llm_utils.py           # LLM integration (Gemini)
├── rag_enhanced.py        # Semantic RAG system
├── rag.py                 # Basic RAG
├── tools.py               # Helper tools
├── data/
│   └── knowledge.json     # 📈 IMPROVED: Knowledge base
├── run_ui.py              # Launcher script
└── requirements.txt       # Dependencies
```

---

## 🚀 Quick Start

### 1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 2. **Run the Beautiful UI** (Recommended)
```bash
# Option A: Using the launcher script
python run_ui.py

# Option B: Direct Streamlit command
streamlit run app_ui.py
```

### 3. **Access the Application**
Open your browser and go to: `http://localhost:8501`

### Alternative: Run CLI Version
```bash
python app_cli.py
```

---

## 🎯 Features

### 💬 **Conversational AI**
- Natural language understanding using Gemini AI
- Multi-turn conversations with context awareness
- Intelligent intent detection (FAQ or Lead Capture)

### 🔍 **Semantic RAG**
- Embeddings-based document retrieval
- FAISS indexing for fast similarity search
- Multiple knowledge categories:
  - Pricing information
  - Product features
  - Company policies
  - FAQs

### 📋 **Lead Capture**
- Multi-step form: Name → Email → Platform
- Email validation
- Lead confirmation message

### 📊 **Analytics**
- Conversation history tracking
- Lead capture statistics
- Message logging

---

## 📖 How It Works

### 1. **User Input Processing**
```
User Input → Intent Detection → Route (FAQ or Lead) → Generate Response
```

### 2. **FAQ Response (RAG)**
```
User Question 
  ↓
Semantic Search in Knowledge Base
  ↓
Retrieve Top 3 Relevant Documents
  ↓
Generate Contextual Response
```

### 3. **Lead Capture**
```
"Start" Intent
  ↓
Ask for Name
  ↓
Ask for Email (with validation)
  ↓
Ask for Platform
  ↓
Confirm & Save Lead
```

---

## 🧠 Knowledge Base Structure

The enhanced `knowledge.json` contains:

```json
{
  "company": {
    "name": "...",
    "description": "...",
    "mission": "..."
  },
  "pricing": {
    "basic": { "name", "price", "features", ... },
    "pro": { ... },
    "enterprise": { ... }
  },
  "features": {
    "ai_content_generation": "...",
    "multi_platform_posting": "...",
    ...
  },
  "policies": {
    "refund": "...",
    "support": "...",
    ...
  },
  "faq": {
    "get_started": "...",
    "free_trial": "...",
    ...
  }
}
```

---

## 🎨 UI Features

### Header
- Branding with gradient background
- Subtitle describing the platform

### Chat Area
- Message history with avatars
- User messages (blue gradient)
- Bot messages (gray background)
- Smooth animations

### Info Panel
- Lead capture status
- Feature showcase button
- Chat reset functionality

### Quick Actions
- Send button with keyboard support
- Feature list toggle
- Reset conversation button

---

## 🔧 Configuration

### API Configuration
Update the `API_KEY` in `llm_utils.py` to use your own Google Gemini API key:

```python
API_KEY = "your-api-key-here"
genai.configure(api_key=API_KEY)
```

### Customize Knowledge Base
Edit `data/knowledge.json` to update:
- Pricing information
- Product features
- Company details
- Policies and FAQs

---

## 🚀 Deployment

### Local Development
```bash
streamlit run app_ui.py
```

### Production Deployment (Streamlit Cloud)
1. Push code to GitHub
2. Connect to Streamlit Cloud
3. Deploy with one click

### Docker Deployment
```bash
docker build -t creator-chatbot .
docker run -p 8501:8501 creator-chatbot
```

---

## 📊 Example Conversations

### FAQ Query
```
You: What are your pricing plans?
Bot: We offer three plans...
     Basic Plan: $29/month, 10 videos/month, 720p...
     Pro Plan: $79/month, Unlimited videos...
```

### Lead Capture
```
You: I want to get started
Bot: Great! Before we continue, what's your name?
You: John Doe
Bot: Nice to meet you, John! What's your email?
You: john@example.com
Bot: What platform do you create content on?
You: YouTube
Bot: Perfect! We'll reach out soon! 🚀
```

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **LLM**: Google Gemini API
- **RAG**: Semantic Search with FAISS
- **Embeddings**: Sentence Transformers
- **Workflow**: LangGraph
- **Language**: Python 3.8+

---

## 📝 Environment Variables

Create a `.env` file (optional):
```
GEMINI_API_KEY=your-key-here
LOG_LEVEL=ERROR
```

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution**: `pip install streamlit`

### Issue: API Key errors
**Solution**: Ensure valid Gemini API key in `llm_utils.py`

### Issue: FAISS or Sentence Transformers not found
**Solution**: `pip install faiss-cpu sentence-transformers`

### Issue: Knowledge base not loading
**Solution**: Check `data/knowledge.json` exists and is valid JSON

---

## 📈 Future Enhancements

- [ ] Multi-language support
- [ ] Database persistence
- [ ] User authentication
- [ ] Advanced analytics dashboard
- [ ] Integration with CRM systems
- [ ] Voice input support
- [ ] WhatsApp integration
- [ ] Email notification system

---

## 📄 License

This project is provided as-is for creator automation.

---

## 💡 Tips for Best Results

1. **Keep Knowledge Base Updated**: Regularly update `knowledge.json` with new information
2. **Test Intent Detection**: Adjust keywords in `intent.py` for your use case
3. **Monitor Conversations**: Review chat history to improve responses
4. **Use Rich Formatting**: Add emojis and markdown to make responses engaging
5. **Customize Pricing**: Update pricing plans to match your actual offerings

---

## 🤝 Support

For issues or questions, check the documentation or review the code comments.

---

**Made with ❤️ for Creators | Powered by AI**
