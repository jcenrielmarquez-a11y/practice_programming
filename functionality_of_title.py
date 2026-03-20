def custom_title(text):
    words = text.split(" ")
    result_words = []

    for word in words:
        if word:
            first_char = word[0]
            rest = word[1:]

            if 'a' <= first_char <= 'z':
                first_char = chr(ord(first_char) - 32)

            new_rest = ""
            for char in rest:
                if 'A' <= char <= 'Z':
                    new_rest += chr(ord(char) + 32)
                else:
                    new_rest += char

            result_words.append(first_char + new_rest)
        else:
            result_words.append("")

    return " ".join(result_words)

sample1 = "hELLO wORLD from pYTHON"
sample2 = "multiple   spaces here"
print("Original:", repr(sample1))
print("After custom_title:", repr(custom_title(sample1)))
print("Original:", repr(sample2))
print("After custom_title:", repr(custom_title(sample2)))