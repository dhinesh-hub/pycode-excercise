def rep_spa(str1):
    count = 0
    for char in str1:
        if char == " " :
            count += 1
    str1 = str1.replace(" ","%20",count)
    return str1

print rep_spa("s pa ce s")

            