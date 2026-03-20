def custom_removeprefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text