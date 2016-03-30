def string_reverse(text):
    new_str = ""
    for word in text.split():
        str_len = len(word) - 1
        while str_len >= 0:
            new_str = new_str + word[str_len]
            str_len = str_len - 1
        new_str = new_str + " "
    return new_str

print string_reverse("hello world")

