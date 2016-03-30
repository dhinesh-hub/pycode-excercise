#Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring

def substring(s):
    result = []
    max_len = 0
    for i in range(0,len(s)):
        for j in range(0,i):
    	    chunk = s[j:i+1] # i+1 becasuse [0,3] will return 0,1,2 elements without 3 
            if chunk == chunk[::-1]: #reverse string shortcut
	       result.append(chunk)	
    for s in result:
        #print s
        s_len = len(s)
        #print s_len
        if s_len > max_len:
            max_len = s_len
            max_str = s

    return max_str
print substring('abaabaa')


