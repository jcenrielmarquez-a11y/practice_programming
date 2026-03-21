def custom_count(text, sub):
    count = 0
    sub_len = len(sub)

    for i in range(len(text) - sub_len + 1):
        if text[i:i + sub_len] == sub:
            count += 1
    return count