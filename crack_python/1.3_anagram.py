def anagram(str1,str2):
    for char in str1:
        if str2.find(char) == -1:
            return False
        else:
            str2 = str2.replace(char,"",1)
    return True



print anagram('hello new', 'llohe won')
