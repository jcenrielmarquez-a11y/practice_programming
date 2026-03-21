def custom_removesuffix(text, suffix):
    
    if len(suffix) > len(text):
        return text
    if text[-len(suffix):] == suffix:
        return text[:-len(suffix)]
    return text