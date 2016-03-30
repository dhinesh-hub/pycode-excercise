def anagram_check(str1,str2):
    list_str1 = [0]*26
    list_str2 = [0]*26
    print list_str1
    print list_str2
    for c in str1:
        res1 =  ord(c) - 97 #ord gives ASCII value of a charcter 97 ASCII value of a
        print res1 
	list_str1[res1] = list_str1[res1] + 1
    print list_str1 
    for c in str2:
        res2 =  ord(c) - 97 #ord gives ASCII value of a charcter
        print res2
        list_str2[res2] = list_str2[res2] + 1
    print list_str2

    for i in range(0,26):
        if list_str1[i] != list_str2[i]:
            return 'Strings not a anagram'    
    print 'Strings are anagram'    

print anagram_check('azllo','lloza')
