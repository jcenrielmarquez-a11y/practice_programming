def custom_index(text, sub):
    sub_len = len(sub)

    for i in range(len(text) - sub_len + 1):
        if text[i:i + sub_len] == sub:
            return i
    raise ValueError(f"Substring '{sub}' not found in '{text}'")

sample1 = "banana"
sample2 = "hello world"
print("Original:", repr(sample1))
print("Index of 'na':", custom_index(sample1, "na"))
print("Original:", repr(sample2))
print("Index of 'world':", custom_index(sample2, "world"))  