def compress(str1):
    new_str = ""
    str_len = len(str1)
    count = 1
    for i in range(0,str_len):
        if str1[i] == str1[i-1]:
            count += 1
        else:
            new_str = new_str + str1[i -1] + str(count)
            count = 1
    print new_str


compress("aaabffffccd")