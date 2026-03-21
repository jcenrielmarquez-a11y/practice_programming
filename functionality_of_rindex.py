def custom_rindex(text, sub):
    sub_len = len(sub)

    for i in range(len(text) - sub_len, -1, -1):

        if text[i:i + sub_len] == sub:
            return i

    raise ValueError(f"Substring '{sub}' not found in '{text}'")

sample1 = "banana"
sample2 = "hello world, hello universe"
print("Original:", repr(sample1))
print("rindex of 'na':", custom_rindex(sample1, "na"))  
print("Original:", repr(sample2))
print("rindex of 'hello':", custom_rindex(sample2, "hello"))