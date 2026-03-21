def custom_rjust(text, width):
    if len(text) >= width:
        return text
    spaces_to_add = width - len(text)
    return " " * spaces_to_add + text

sample1 = "Hello"
sample2 = "World"
print("Original:", repr(sample1))
print("After custom_rjust:", repr(custom_rjust(sample1, 10)))
print("Original:", repr(sample2))
print("After custom_rjust:", repr(custom_rjust(sample2, 8)))