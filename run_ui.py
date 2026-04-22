#!/usr/bin/env python3
"""
🚀 Creator Automation Platform - Beautiful UI Launcher
Starts the Streamlit web application with the enhanced UI
"""

import subprocess
import sys
import os

def run_beautiful_ui():
    """Launch the beautiful Streamlit UI"""
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║       🚀 Creator Automation Platform - Beautiful UI           ║
    ║                                                               ║
    ║  Starting Streamlit application...                           ║
    ║  Open your browser to: http://localhost:8501                 ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)
    
    try:
        subprocess.run(
            [sys.executable, "-m", "streamlit", "run", "app_ui.py"],
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
    except KeyboardInterrupt:
        print("\n✅ Application stopped gracefully.")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure Streamlit is installed: pip install streamlit")

if __name__ == "__main__":
    run_beautiful_ui()
