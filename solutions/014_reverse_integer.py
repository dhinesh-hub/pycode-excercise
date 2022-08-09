
#Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# LeetCode 7

#Input: x = 123
#Output: 321
#Input: x = -123
#Output: -321

x = -1230
flag = ''
if x < 0:
    flag = '-'
x = abs(x)
x = str(x)
stack = []
for i in x:
    stack.append(i)

print(stack)

result=''
while len(stack) > 0:
    result=result + stack.pop()
if flag == '-':
   print(int(result) * -1)
else:
    print(int(result))