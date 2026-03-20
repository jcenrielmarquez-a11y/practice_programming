def custom_isupper(text):
    if not text:
        return False

    for char in text:
        if 'a' <= char <= 'z':
            return False
    return True

