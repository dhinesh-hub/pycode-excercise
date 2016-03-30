#Given an array of integers, find two numbers such that they add up to a specific target number.

#The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

#You may assume that each input would have exactly one solution.

#Input: numbers={2, 7, 11, 15}, target=9
#Output: index1=1, index2=2
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr_len = len(nums)
        for i in range(0,arr_len):
            for j in range(i+1,arr_len):
                if nums[i] + nums[j] == target:
                    return i,j
                    
s = Solution()
nums = [1,3,5,7]
target = 10
print s.twoSum(nums,target)
