#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
#leetcode 136
"""
- take input as array list
- split the list into two for each index location
- if element not present in both split lists, print value, exit code
"""

inp_lst = [1, 2, 1, 2, 4, 6, 6]
for i in range(0, len(inp_lst)):
    print(inp_lst[0:i])
    print(inp_lst[i+1:])
    print("---")
    if inp_lst[i] not in inp_lst[0:i] and inp_lst[i] not in inp_lst[i+1:]:
        print("single number is: {0}".format(inp_lst[i]))
        exit()

