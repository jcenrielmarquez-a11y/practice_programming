def custom_startswith(text, prefix):
    if len(prefix) > len(text):
        return False
    return text[:len(prefix)] == prefix

sample1 = "HelloWorld"
sample2 = "HelloWorld"
print("Sample1:", repr(sample1), "->", custom_startswith(sample1, "Hello"))
print("Sample2:", repr(sample2), "->", custom_startswith(sample2, "World"))  