import json
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import os

# Initialize the embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

class SemanticRAG:
    """Enhanced RAG system with semantic search using embeddings"""
    
    def __init__(self, knowledge_file="data/knowledge.json"):
        self.knowledge_file = knowledge_file
        self.documents = []
        self.embeddings = None
        self.index = None
        self._initialize()
    
    def _initialize(self):
        """Initialize the RAG system by loading and indexing documents"""
        self.documents = self._load_and_split_documents()
        
        if self.documents:
            # Generate embeddings for all documents
            doc_texts = [doc["text"] for doc in self.documents]
            self.embeddings = embedding_model.encode(doc_texts)
            
            # Create FAISS index for efficient similarity search
            dimension = self.embeddings.shape[1]
            self.index = faiss.IndexFlatL2(dimension)
            self.index.add(np.array(self.embeddings).astype('float32'))
    
    def _load_and_split_documents(self):
        """Load knowledge base and split into searchable documents"""
        documents = []
        
        try:
            with open(self.knowledge_file) as f:
                kb = json.load(f)
        except:
            kb = self._get_default_knowledge()
        
        # Add pricing information
        for plan_name, plan_details in kb.get("pricing", {}).items():
            documents.append({
                "text": plan_details,
                "category": "pricing",
                "plan": plan_name
            })
        
        # Add policy information
        for policy_name, policy_text in kb.get("policies", {}).items():
            documents.append({
                "text": policy_text,
                "category": "policy",
                "policy": policy_name
            })
        
        # Add platform features
        features = {
            "automation": "Automate content creation and publishing across multiple platforms",
            "ai_agents": "Build and deploy AI agents for voice calls and chat support",
            "analytics": "Track and analyze content performance with detailed metrics",
            "collaboration": "Work with your team in real-time with collaboration tools",
            "scheduling": "Schedule posts and campaigns across all your platforms"
        }
        
        for feature_name, feature_text in features.items():
            documents.append({
                "text": feature_text,
                "category": "feature",
                "feature": feature_name
            })
        
        return documents
    
    def retrieve(self, query, top_k=3):
        """Retrieve most relevant documents for a given query"""
        if not self.documents or self.index is None:
            return []
        
        # Encode the query
        query_embedding = embedding_model.encode([query]).astype('float32')
        
        # Search in FAISS index
        distances, indices = self.index.search(query_embedding, min(top_k, len(self.documents)))
        
        # Return relevant documents
        results = []
        for idx in indices[0]:
            if idx < len(self.documents):
                results.append({
                    "document": self.documents[int(idx)],
                    "score": float(distances[0][len(results)])
                })
        
        return results
    
    def _get_default_knowledge(self):
        """Provide default knowledge base if file not found"""
        return {
            "pricing": {
                "basic": "Basic Plan: ₹0/month - Perfect for getting started with core features",
                "pro": "Pro Plan: ₹499/month - Unlimited automation, priority support, advanced analytics",
                "enterprise": "Enterprise Plan: Custom pricing - Dedicated account manager, custom integrations, SLA guarantee"
            },
            "policies": {
                "refund": "30-day money back guarantee - Full refund if you're not satisfied",
                "support": "24/7 support on Pro & Enterprise, email support on Basic",
                "uptime": "99.9% uptime SLA on Enterprise plans"
            }
        }
    
    def get_answer(self, query):
        """Get answer to a user query using semantic search"""
        results = self.retrieve(query, top_k=3)
        
        if not results:
            return "I'm not sure about that. Can you rephrase your question?"
        
        # Combine top results into a coherent answer
        answer_parts = []
        for result in results:
            answer_parts.append(result["document"]["text"])
        
        return "\n\n".join(answer_parts)


# Global RAG instance
_rag_instance = None

def get_rag():
    """Get or create the global RAG instance"""
    global _rag_instance
    if _rag_instance is None:
        _rag_instance = SemanticRAG()
    return _rag_instance

def retrieve_semantic_answer(query):
    """Retrieve answer using semantic search"""
    rag = get_rag()
    return rag.get_answer(query)
