def custom_center(text, width):
    if len(text) >= width:
        return text
    total_spaces = width - len(text)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    return " " * left_spaces + text + " " * right_spaces

sample = "Hello"
print("Original:", repr(sample))
print("After custom_center:", repr(custom_center(sample, 11)))