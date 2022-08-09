#Find if sting is palindrome or not
"""Logic 1:
   -Add input string to stack
   -Pop the stack to a new string
   -Compare the string for palindrome"""

palindrome_str = input("Enter the string:")
tmp_lst = []
reverse_str = ''
for i in palindrome_str:
    tmp_lst.append(i)

print(tmp_lst)

for i in range(0,len(tmp_lst)):
    reverse_str = reverse_str + tmp_lst.pop()
print(reverse_str)

if palindrome_str == reverse_str:
    print("String is a palindrome")
else:
    print("String is not a palindrome")