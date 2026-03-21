def custom_startswith(text, prefix):
    if len(prefix) > len(text):
        return False
    return text[:len(prefix)] == prefix