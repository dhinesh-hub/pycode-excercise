#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Leetcode 283
"""
- obtain input as a list with zero integer values
- if 0 is met, pop the list element and add a 0 to the end
"""

inp_list = [0, 1, 0, 3, 12]
for i in range(0,len(inp_list)):
    if inp_list[i] == 0:
        inp_list.pop(i)
        inp_list.append(0)

print(inp_list)

