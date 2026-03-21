def custom_upper(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

sample1 = "Hello World!"
sample2 = "python123"
print("Original:", repr(sample1))
print("After custom_upper:", repr(custom_upper(sample1)))
print("Original:", repr(sample2))
print("After custom_upper:", repr(custom_upper(sample2)))