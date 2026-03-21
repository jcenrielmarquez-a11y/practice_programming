def custom_rstrip(text):
    index = len(text) - 1

    while index >= 0 and text[index] == " ":
        index -= 1
    return text[:index + 1]

sample1 = "Hello World    "
sample2 = "NoTrailingSpace"
print("Original:", repr(sample1))
print("After custom_rstrip:", repr(custom_rstrip(sample1)))
print("Original:", repr(sample2))
print("After custom_rstrip:", repr(custom_rstrip(sample2)))