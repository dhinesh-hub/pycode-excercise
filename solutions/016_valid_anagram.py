#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#Leetcode 242
#Example 1:
#Input: s = "anagram", t = "nagaram"
#Output: true
#Example 2:

#Input: s = "rat", t = "car"
#Output: false
'''Logic 1:
- Convert 1'st string to a list.
- Iterate through the chars on 2nd string
- If char present in 1'st string, remove that char from 1'st string .
- At End of iteration, if 1st string is empty, Return True
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tmp = []
        if len(s) != len(t):
            return False
        list_s = list(s)
        print(list_s)
        for i in t:
            print(list_s)
            if i in list_s:
                list_s.remove(i)
        if len(list_s) == 0:
            return True
        else:
            return False
sol = Solution()
result = sol.isAnagram(s='rat', t='car')
print(result)