"""
Cricket Players Stats Tool - Streamlit App Launcher
Run this script to launch the interactive web application
"""

import subprocess
import sys
import os

def launch_app():
    """Launch the Streamlit application."""
    print("🏏 Starting Cricket Players Stats Tool...")
    print("📊 This will open in your web browser")
    print("-" * 50)
    
    try:
        # Change to the project directory
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        # Launch Streamlit app
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
    
    except KeyboardInterrupt:
        print("\n🛑 Application stopped by user")
    except Exception as e:
        print(f"❌ Error launching app: {e}")
        print("Please ensure Streamlit is installed: pip install streamlit")

if __name__ == "__main__":
    launch_app()
