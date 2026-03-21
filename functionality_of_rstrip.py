def custom_rstrip(text):
    index = len(text) - 1

    while index >= 0 and text[index] == " ":
        index -= 1
    return text[:index + 1]

