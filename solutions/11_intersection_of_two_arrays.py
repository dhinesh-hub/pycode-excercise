#Given two integer arrays nums1 and nums2, return an array of their intersection.
#Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
#Leetcode350
#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2,2]
"""
- Get both arrays as a list.
- Declare a dictionary and store values of nums1(key, frequency)
- Iterate through nums2
- If element in dictionary and count is greater than 1 , append to result
- Remove 1 frequency value for that element
"""

import collections

nums1 = [4, 9, 5, 8]
nums2 = [9, 4, 8, 8, 4]

#c1 = collections.Counter(nums1)
#print (c1.keys())

dict1 = {}
result = []

for i in nums1:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] = + 1
print(dict1)

for j in nums2:
    if j in dict1.keys() and dict1[j] >= 1:
        result.append(j)
        dict1[j] = - 1

print(result)



