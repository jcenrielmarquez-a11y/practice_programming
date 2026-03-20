def custom_swapcase(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

sample = "Hello World 123!"
print("Original:", repr(sample))
print("After custom_swapcase:", repr(custom_swapcase(sample)))