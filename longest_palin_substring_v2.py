def long_palin_sub(str1):
    lst1 = []
    palindrome = []
    for i in range(1,len(str1) + 1):
        for j in range(len(str1) + 1 - i):
            #print i
            #print j
            substr = str1[j:j + i] 
            lst1.append(substr)
            if substr == substr[::-1]:
                palindrome.append(substr) 
    print lst1 
    print palindrome
    return max(palindrome, key=len) #important key=len will specify lenght as criteria rather than integer value   
    
print long_palin_sub('roorket') 
