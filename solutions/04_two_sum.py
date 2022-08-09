# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#Leetcode 1
"""
- Get input as a integer list and integer(target number)
- Add two numbers from list for all combination and check if it is equal to the target number
"""
inp_str = input("Enter numbers:")
inp_list = []
#Convert string to int list
for i in inp_str:
    inp_list.append(int(i))
print(inp_list)

target_num = input("Enter two-sum target number:")
target_num = int(target_num)

for i in range(0, len(inp_list)):
    for j in range(i+1, len(inp_list)):
        sum = inp_list[i] + inp_list[j]
        print(sum)
        if sum == target_num:
            print("Location {0} and {1}".format(i, j))