def custom_capitalize(text):
    if not text:
        return text

    first_char = text[0]
    rest = text[1:]

    if 'a' <= first_char <= 'z':
        first_char = chr(ord(first_char) - 32)
        
    new_rest = ""
    for char in rest:
        if 'A' <= char <= 'Z':
            new_rest += chr(ord(char) + 32)
        else:
            new_rest += char

    return first_char + new_rest