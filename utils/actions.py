import os

OUTPUT_DIR = "output"

def create_file(filename="new_file.txt"):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write("")
    return f"File created: {path}"

def write_code(text):
    import requests
    import os

    os.makedirs("output", exist_ok=True)

    prompt = f"Write clean Python code for: {text}. Only return code."

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()
        code = result["response"]

    except Exception as e:
        code = f"# Error: {e}"

    file_path = "output/generated_code.py"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)

    return f"Code saved to {file_path}"

def summarize(text):
    import requests

    prompt = f"Explain this in simple terms:\n{text}"

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()
        summary = result["response"]

    except Exception as e:
        summary = f"Error: {e}"

    return summary

def chat(text):
    return f"Echo: {text}"