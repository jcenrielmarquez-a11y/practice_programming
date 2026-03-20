def custom_endswith(text, suffix):
    if len(suffix) > len(text):
        return False
    return text[-len(suffix):] == suffix

sample1 = "HelloWorld"
sample2 = "HelloWorld"
print("Sample1:", repr(sample1), "->", custom_endswith(sample1, "World"))
print("Sample2:", repr(sample2), "->", custom_endswith(sample2, "Hello"))