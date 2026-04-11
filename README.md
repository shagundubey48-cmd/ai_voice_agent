AI Voice Agent (Offline)

An intelligent voice-based AI assistant that processes speech input, detects user intent, and executes actions such as code generation, summarization, and file creation. The system runs entirely locally without relying on paid APIs.

Features
Voice input via recording and file upload
Speech-to-text conversion using Whisper (offline)
Multi-intent detection (rule-based)
Action execution:
File creation
Python code generation
Text summarization and explanation
General chat responses
Local LLM integration using Ollama (llama3)
Output file generation
Confirmation mechanism before executing file operations
Session history tracking
Architecture

Voice Input → Whisper (Speech-to-Text) → Text
→ Intent Detection (rule-based)
→ Action Handler
→ Ollama (for code generation and explanation)
→ Output (UI display and file system)

Tech Stack
Python
Streamlit
Whisper
Ollama (llama3)
FFmpeg
Setup Instructions
1. Clone the repository
git clone <https://github.com/shagundubey48-cmd/ai_voice_agent.git>
cd ai_voice_agent
2. Create a virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Install FFmpeg

Download from:
https://www.gyan.dev/ffmpeg/builds/

Add the bin directory to your system PATH.

5. Start Ollama
ollama serve
ollama run llama3
6. Run the application
streamlit run app.py
Example Commands
"Explain Machine Learning"
"Write Python code for factorial"
"Create a file and write code for binary search"
Hardware Notes
Runs on CPU; no GPU required
Initial model loading in Ollama may take time
FFmpeg is required for audio processing
Key Highlight

This project demonstrates a fully offline AI system using a local large language model, eliminating dependency on external APIs and associated costs.