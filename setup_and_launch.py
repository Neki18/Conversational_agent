#!/usr/bin/env python3
"""
✨ Creator Automation Platform - Setup & Launch Wizard
Ensures all dependencies are installed and launches the beautiful UI
"""

import subprocess
import sys
import os
import json

def check_file_exists(filepath):
    """Check if a required file exists"""
    return os.path.isfile(filepath)

def check_json_valid(filepath):
    """Verify JSON file is valid"""
    try:
        with open(filepath) as f:
            json.load(f)
        return True
    except:
        return False

def print_header():
    """Print welcome header"""
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║     🚀 Creator Automation Platform - Setup & Launch Wizard       ║
║                                                                   ║
║  This wizard will check all dependencies and start the app       ║
╚═══════════════════════════════════════════════════════════════════╝
    """)

def check_dependencies():
    """Check if required packages are installed"""
    print("📦 Checking dependencies...")
    
    required_packages = {
        'streamlit': 'Streamlit (UI Framework)',
        'google.generativeai': 'Google Generative AI',
        'langgraph': 'LangGraph (Workflow)',
        'langchain': 'LangChain',
        'sentence_transformers': 'Sentence Transformers (Embeddings)',
        'faiss': 'FAISS (Vector Search)',
        'pydantic': 'Pydantic',
    }
    
    missing_packages = []
    
    for module, name in required_packages.items():
        try:
            __import__(module.split('.')[0])
            print(f"✅ {name}")
        except ImportError:
            print(f"❌ {name}")
            missing_packages.append(module)
    
    return missing_packages

def check_files():
    """Check if required files exist"""
    print("\n📁 Checking project files...")
    
    required_files = {
        'app_ui.py': 'Beautiful UI Application',
        'app_cli.py': 'CLI Application',
        'graph.py': 'LangGraph Definition',
        'nodes.py': 'Conversation Nodes',
        'llm_utils.py': 'LLM Utilities',
        'rag_enhanced.py': 'RAG System',
        'data/knowledge.json': 'Knowledge Base',
    }
    
    missing_files = []
    
    for filepath, description in required_files.items():
        if check_file_exists(filepath):
            print(f"✅ {description}")
        else:
            print(f"❌ {description} ({filepath})")
            missing_files.append(filepath)
    
    return missing_files

def check_knowledge_base():
    """Verify knowledge base is valid"""
    print("\n📚 Checking knowledge base...")
    
    if check_json_valid('data/knowledge.json'):
        print("✅ Knowledge base is valid JSON")
        
        with open('data/knowledge.json') as f:
            kb = json.load(f)
            sections = list(kb.keys())
            print(f"   Sections: {', '.join(sections)}")
        
        return True
    else:
        print("❌ Knowledge base is invalid or missing")
        return False

def install_missing_packages(packages):
    """Install missing packages"""
    if not packages:
        return True
    
    print(f"\n📥 Installing {len(packages)} missing package(s)...")
    print("   This may take a few minutes...\n")
    
    try:
        for package in packages:
            print(f"   Installing {package}...")
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "-q", package]
            )
        
        print("\n✅ All packages installed successfully!")
        return True
    except Exception as e:
        print(f"\n❌ Error installing packages: {e}")
        print("   Try running: pip install -r requirements.txt")
        return False

def launch_app():
    """Launch the beautiful Streamlit UI"""
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║                    🎨 Launching Beautiful UI                      ║
║                                                                   ║
║  Your application is starting...                                 ║
║  Browser will open at: http://localhost:8501                     ║
║  Press Ctrl+C to stop the application                            ║
╚═══════════════════════════════════════════════════════════════════╝
    """)
    
    try:
        subprocess.run(
            [sys.executable, "-m", "streamlit", "run", "app_ui.py"],
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
    except KeyboardInterrupt:
        print("\n\n✅ Application stopped gracefully.")
    except Exception as e:
        print(f"\n❌ Error launching app: {e}")

def main():
    """Main setup wizard flow"""
    print_header()
    
    # Check dependencies
    missing_packages = check_dependencies()
    
    # Check files
    missing_files = check_files()
    
    # Check knowledge base
    kb_valid = check_knowledge_base()
    
    # Summary
    print("\n" + "="*70)
    print("📋 SETUP SUMMARY")
    print("="*70)
    
    all_good = True
    
    if missing_packages:
        print(f"\n⚠️  Missing {len(missing_packages)} package(s):")
        for pkg in missing_packages:
            print(f"   - {pkg}")
        all_good = False
    else:
        print("\n✅ All packages installed")
    
    if missing_files:
        print(f"\n⚠️  Missing {len(missing_files)} file(s):")
        for file in missing_files:
            print(f"   - {file}")
        all_good = False
    else:
        print("✅ All project files present")
    
    if kb_valid:
        print("✅ Knowledge base valid")
    else:
        print("⚠️  Knowledge base issue")
        all_good = False
    
    print("\n" + "="*70)
    
    # Try to install missing packages
    if missing_packages:
        response = input("\n🤔 Install missing packages? (y/n): ").lower().strip()
        if response == 'y':
            if not install_missing_packages(missing_packages):
                print("\n⚠️  Some packages failed to install")
                response = input("Continue anyway? (y/n): ").lower().strip()
                if response != 'y':
                    return
    
    # Launch app
    if all_good or missing_packages:
        response = input("\n🚀 Ready to launch the application? (y/n): ").lower().strip()
        if response == 'y':
            launch_app()
        else:
            print("\n👋 Goodbye!")
    else:
        print("\n❌ Please fix the issues above before launching.")
        print("   Run: pip install -r requirements.txt")

if __name__ == "__main__":
    main()
