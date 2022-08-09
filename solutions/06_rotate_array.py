#Given an array, rotate the array to the right by k steps, where k is non-negative.
#Leetcode 189
"""Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

new_list = [1, 2, 3, 4, 5, 6, 7]
k_val = input("Enter k value:")
k_val = int(k_val)

for i in range(0, k_val):
    new_list.insert(0, new_list.pop())
    print(new_list)