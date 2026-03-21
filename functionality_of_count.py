def custom_count(text, sub):
    count = 0
    sub_len = len(sub)

    for i in range(len(text) - sub_len + 1):
        if text[i:i + sub_len] == sub:
            count += 1
    return count

sample1 = "banana"
sample2 = "hello world, hello universe"
print("Original:", repr(sample1))
print("Count of 'na':", custom_count(sample1, "na"))
print("Original:", repr(sample2))
print("Count of 'hello':", custom_count(sample2, "hello"))  