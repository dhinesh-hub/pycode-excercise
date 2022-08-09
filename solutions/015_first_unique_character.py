#Given a string s, return the first non-repeating character in it and return its index.
#If it does not exist, return -1.
#Example 1:
#Input: s = "leetcode"
#Output: 0

#Example 2:
#Input: s = "loveleetcode"
#Output: 2

#Example 3:
#Input: s = "aabb"
#Output: -1

def uni_char():
    dic1 = {}
    result = -1
    s = "leetcode"
    n = len(s)
    for i in reversed(range(0, n)):  #New syntax
        print(s[i])
        if s[i] in dic1.keys():
            continue
        else:
            dic1[s[i]] = 1
            result = i
    print(result)
    print(dic1)

uni_char()