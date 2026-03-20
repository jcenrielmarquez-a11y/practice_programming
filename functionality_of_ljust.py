def custom_ljust(text, width):
    if len(text) >= width:
        return text
    spaces_to_add = width - len(text)
    return text + " " * spaces_to_add

sample = "Hello"
print("Original:", repr(sample))
print("After custom_ljust:", repr(custom_ljust(sample, 10)))