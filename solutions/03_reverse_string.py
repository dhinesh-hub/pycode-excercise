#Write a function that reverses a string. The input string is given as an array of characters char[].
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#Leetcode 344
"""
- Read string and convert it to list of char
- Store the First Element in tmp variable
- Swap the locations of the two
- Continue until middle of list is reached
"""

def reverse_str(chr):
    chr_len = len(chr)
    for i in range(0, chr_len//2): #// is whole number floor value
        chr_len = chr_len - 1
        tmp = chr[i]
        chr[i] = chr[chr_len]
        chr[chr_len] = tmp
    print(chr)

reverse_str(chr=['e','n','e','m','y'])