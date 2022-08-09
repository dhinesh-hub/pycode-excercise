#Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length
#Leetcode 26
"""
- run input list through for loop
- if next element is same as current element, pop current element
"""
nums = [0,0,1,1,1,2,2,3,3,4,4,6,7]
print(len(nums))
for i in range(0,len(nums)):
    print(nums)
    print(i)
    if nums[i] == nums[i+1]:
        nums.pop(i)
print(nums)
print(len(nums))