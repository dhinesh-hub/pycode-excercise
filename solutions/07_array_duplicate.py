#Given an array of integers, find if the array contains any duplicates.
#Leetcode 217
"""
- Take input list and create a map of integer and frequecy of integer
- If frequency is greater than 1, exit saying duplicate exists
"""
inp_lst=[1,2,3,3,4,4]
tmp_dict={}
for i in inp_lst:
    if i in tmp_dict.keys():
        print("Array has duplicates")
        exit()
    else:
        tmp_dict[i] = 1