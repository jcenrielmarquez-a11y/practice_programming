def custom_islower(text):
    if not text:
        return False

    for char in text:
        if 'A' <= char <= 'Z':
            return False
    return True

sample1 = "hello world"
sample2 = "Hello World"
sample3 = "123!@#"
print("Sample1:", repr(sample1), "->", custom_islower(sample1))
print("Sample2:", repr(sample2), "->", custom_islower(sample2))
print("Sample3:", repr(sample3), "->", custom_islower(sample3))
