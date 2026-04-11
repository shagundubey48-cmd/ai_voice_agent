def detect_intent(text):
    text = text.lower()

    intents = []

    if "create file" in text:
        intents.append("create_file")

    if "write code" in text or "python" in text:
        intents.append("write_code")

    if "summarize" in text or "explain" in text:
        intents.append("summarize")

    if not intents:
        intents.append("chat")

    return intents