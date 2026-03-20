def custom_lower(text):
    result = ""
    for char in text:
        # Check if character is uppercase A-Z
        if 'A' <= char <= 'Z':
            # Convert to lowercase by adding 32 to ASCII value
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

sample = "Hello WORLD!"
print("Original:", repr(sample))
print("After custom_lower:", repr(custom_lower(sample)))