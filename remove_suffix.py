def custom_removesuffix(text, suffix):

    if len(suffix) > len(text):
        return text
    if text[-len(suffix):] == suffix:
        return text[:-len(suffix)]
    return text

sample1 = "HelloWorld"
sample2 = "HelloWorld"
print("Original:", repr(sample1))
print("After custom_removesuffix:", repr(custom_removesuffix(sample1, "World")))  # "Hello"
print("Original:", repr(sample2))
print("After custom_removesuffix:", repr(custom_removesuffix(sample2, "Hello")))  # "HelloWorld"