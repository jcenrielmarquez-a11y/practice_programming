def custom_zfill(text, width):
    if len(text) >= width:
        return text
    zeros_to_add = width - len(text)
    return "0" * zeros_to_add + text