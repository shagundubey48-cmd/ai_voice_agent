import whisper
import tempfile
import subprocess
import os

model = whisper.load_model("base")

def transcribe_audio(audio_file):
    try:
        # Save raw recorded audio (webm format)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as temp_in:
            temp_in.write(audio_file.read())
            input_path = temp_in.name

        # Output WAV file
        output_path = input_path.replace(".webm", ".wav")

        # Convert using ffmpeg
        subprocess.run([
            "ffmpeg",
            "-i", input_path,
            "-ar", "16000",
            "-ac", "1",
            output_path
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Transcribe converted file
        result = model.transcribe(output_path)

        # Cleanup
        os.remove(input_path)
        os.remove(output_path)

        return result["text"]

    except Exception as e:
        return f"Error: {str(e)}"