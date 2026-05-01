# AI Voice Agent (Offline)

## Overview  
An intelligent voice-based AI assistant that processes speech input, detects user intent, and executes tasks such as code generation, summarization, and file creation.  
The system runs entirely offline using local models, eliminating dependency on paid APIs.

---

## Features  
- Voice input via recording and file upload  
- Speech-to-text conversion using Whisper (offline)  
- Multi-intent detection (rule-based)  
- Action execution:
  - File creation  
  - Python code generation  
  - Text summarization and explanation  
  - General chat responses  
- Local LLM integration using Ollama (Llama3)  
- Output file generation  
- Confirmation before executing file operations  
- Session history tracking  

---

## Architecture  
```
Voice Input 
   ↓
Whisper (Speech-to-Text)
   ↓
Text Processing
   ↓
Intent Detection (Rule-Based)
   ↓
Action Handler
   ↓
Ollama (Llama3)
   ↓
Output (UI Display / File System)
```

---

## Tech Stack  
- Language: Python  
- Framework: Streamlit  
- Speech Recognition: Whisper (offline)  
- LLM: Ollama (Llama3)  
- Audio Processing: FFmpeg  

---

## Setup Instructions  

### 1. Clone the Repository  
```
git clone https://github.com/shagundubey48-cmd/ai_voice_agent.git
cd ai_voice_agent
```

### 2. Create Virtual Environment  
```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies  
```
pip install -r requirements.txt
```

### 4. Install FFmpeg  
Download from: https://www.gyan.dev/ffmpeg/builds/  
Add the `bin` folder to your system PATH.

### 5. Start Ollama  
```
ollama serve
ollama run llama3
```

### 6. Run the Application  
```
streamlit run app.py
```

---

## Example Commands  

- "Explain Machine Learning"  
- "Write Python code for factorial"  
- "Create a file and write code for binary search"  

---

## Hardware Notes  
- Runs on CPU (GPU not required)  
- Initial model loading in Ollama may take time  
- FFmpeg is required for audio processing  

---

## Key Highlight  
This project demonstrates a fully offline AI system using a local large language model, removing dependency on external APIs and reducing cost.

---

## Author  
Shagun Dubey  
