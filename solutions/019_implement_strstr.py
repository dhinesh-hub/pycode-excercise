'''
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java
's indexOf().

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0
'''

'''
Solution:

'''

def strStr(haystack,needle):
    needle_len = len(needle)
    for i in range(0,len(haystack)-1):
        hs_sub = haystack[i : needle_len]
        if hs_sub == needle:
            print(i)
            exit()
        needle_len = needle_len + 1
    print("-1")

strStr("hello","ll")
