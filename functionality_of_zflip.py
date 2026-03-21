def custom_zfill(text, width):
    if len(text) >= width:
        return text
    zeros_to_add = width - len(text)
    return "0" * zeros_to_add + text

sample1 = "123"
sample2 = "Hello"
print("Original:", repr(sample1))
print("After custom_zfill:", repr(custom_zfill(sample1, 6)))
print("Original:", repr(sample2))
print("After custom_zfill:", repr(custom_zfill(sample2, 8)))