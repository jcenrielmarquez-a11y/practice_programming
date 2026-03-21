def custom_rjust(text, width):
    if len(text) >= width:
        return text
    spaces_to_add = width - len(text)
    return " " * spaces_to_add + text