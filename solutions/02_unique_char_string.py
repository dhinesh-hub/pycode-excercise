#Given a string find if the characters are unique
#CTCI 1.1
"""
- Read input string as ascii list
- Exit if repeating values appear in ascii list
- 48 to 126 is range for ascii codes
"""
ascii_list = []
inp_str = input("Enter the string:")
for i in inp_str:
    if ord(i) in ascii_list: #ord gives ascii value
        print("String has unique characters")
        exit()
    ascii_list.append(ord(i))
print("String does not have unique characters")
print(ascii_list)

"""
second solution
- read char into list.
- if char present in list, exit
"""
inp_str=input("Enter String:")
tmp_list = []
for i in inp_str:
    if i in tmp_list:
        print("found duplicate")
        exit(0)
    else:
        tmp_list.append(i)
