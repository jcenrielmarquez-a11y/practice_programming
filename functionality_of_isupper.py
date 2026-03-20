def custom_isupper(text):
    if not text:
        return False

    for char in text:
        if 'a' <= char <= 'z':
            return False
    return True

sample1 = "HELLO WORLD"
sample2 = "Hello World"
print("Sample1:", repr(sample1), "->", custom_isupper(sample1))
print("Sample2:", repr(sample2), "->", custom_isupper(sample2))