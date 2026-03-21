def custom_index(text, sub):
    sub_len = len(sub)

    for i in range(len(text) - sub_len + 1):
        if text[i:i + sub_len] == sub:
            return i
    raise ValueError(f"Substring '{sub}' not found in '{text}'")
