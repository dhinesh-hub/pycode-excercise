#Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dup = []
        for i in nums:
            if i in dup:
                return True
            else:
                dup.append(i)
        return False
        
s = Solution()
nums = [1,2,3,4,4]
print s.containsDuplicate(nums)
