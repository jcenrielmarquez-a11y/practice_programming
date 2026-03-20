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

sample1 = "hELLO wORLD"
sample2 = "python"
print("Original:", repr(sample1))
print("After custom_capitalize:", repr(custom_capitalize(sample1)))
print("Original:", repr(sample2))
print("After custom_capitalize:", repr(custom_capitalize(sample2)))