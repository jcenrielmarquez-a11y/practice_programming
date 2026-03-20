def custom_removeprefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

sample = "HelloWorld"
print("Original:", repr(sample))
print("After custom_removeprefix:", repr(custom_removeprefix(sample, "Hello")))