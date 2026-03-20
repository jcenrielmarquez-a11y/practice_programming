def custom_lstrip(text):
    result = ""
    space_found = False

    for char in text:
        if not space_found and char != " ":
            space_found = True
        if space_found:
            result += char
    return result


sample = "    Hello World!   "
print("Original:", repr(sample))
print("After custom_lstrip:", repr(custom_lstrip(sample)))
