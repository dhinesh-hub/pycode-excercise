def string_reverse(text):
    new_str = ""
    str_len = len(text) - 1
    while str_len >= 0:
        new_str = new_str + text[str_len] 
        str_len = str_len - 1
    return new_str

print string_reverse("new")


