import streamlit as st
from utils.stt import transcribe_audio
from utils.intent import detect_intent
from utils.actions import create_file, write_code, summarize, chat

st.set_page_config(page_title="AI Voice Agent", layout="centered")

st.title("🎙️ AI Voice Agent")
st.info("Upload an audio file OR record your voice 🎤")

# -------------------------
# SESSION MEMORY
# -------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------
# INPUT SECTION
# -------------------------
uploaded_file = st.file_uploader("📁 Upload Audio", type=["wav", "mp3"])
audio_bytes = st.audio_input("🎤 Record your voice")

audio_file = None

if audio_bytes is not None:
    st.success("Using recorded audio 🎤")
    st.audio(audio_bytes)
    audio_file = audio_bytes

elif uploaded_file is not None:
    st.success("Using uploaded file 📁")
    st.audio(uploaded_file)
    audio_file = uploaded_file

# -------------------------
# PROCESSING SECTION
# -------------------------
if audio_file is not None:
    try:
        with st.spinner("Transcribing audio..."):
            text = transcribe_audio(audio_file)

        st.subheader("📝 Transcription")
        st.write(text)

        # Intent detection
        intents = detect_intent(text)

        st.subheader("🧠 Detected Intent")
        st.write(", ".join(intents))

        # -------------------------
        # CONFIRMATION
        # -------------------------
        confirm = st.checkbox("⚠️ Confirm execution of file operations")

        if confirm:
            st.subheader("⚙️ Action Output")

            outputs = []

            for intent in intents:
                if intent == "create_file":
                    outputs.append(create_file())

                elif intent == "write_code":
                    outputs.append(write_code(text))

                elif intent == "summarize":
                    outputs.append(summarize(text))

                else:
                    outputs.append(chat(text))

            for out in outputs:
                st.success(out)

            # Save to memory
            st.session_state.history.append({
                "text": text,
                "intent": intents,
                "output": outputs
            })

        else:
            st.warning("Please confirm before executing actions.")

    except Exception as e:
        st.error(f"Error: {e}")

# -------------------------
# SESSION HISTORY
# -------------------------
st.subheader("📜 Session History")

for item in reversed(st.session_state.history):
    st.write(f"🗣️ {item['text']}")
    st.write(f"🧠 {item['intent']}")
    st.write(f"⚙️ {item['output']}")
    st.markdown("---")