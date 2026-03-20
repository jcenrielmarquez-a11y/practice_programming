def custom_endswith(text, suffix):
    if len(suffix) > len(text):
        return False
    return text[-len(suffix):] == suffix