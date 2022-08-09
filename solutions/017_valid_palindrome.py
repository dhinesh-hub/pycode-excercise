#Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#Leetcode 125
'''Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''
'''Solution 1
- Remove spaces and convert to lower case, on input string
- if anything other than lowercase alpha, remvove by using ascii check
- Reverse the string list and store in a new list
- Compare the lists
'''


class Solution:
    def isPalindrome(self,s: str) -> bool:
        cmp_list=[]
        s=s.lower()
        s=s.replace(" ","")
        s_list = list(s)
        for i in s_list:
            print(ord(i))
            if ord(i) >= 97 and ord(i) <= 122: #ASCII Check
                continue
            else:
                s_list.remove(i)
        print(s_list)
        for i in range(len(s_list)-1, -1, -1): #Reverse the list
            cmp_list.append(s_list[i])
        print(cmp_list)
        if cmp_list == s_list:
            return True
        else:
            return False

sol = Solution()
result=sol.isPalindrome(s="A man, a plan, a canal: Panama")
print(result)