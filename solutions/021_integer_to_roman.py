#Leetcode 12
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#Create a list with 2 elements Character and Integer
#Roman numerals start from large value reduced to small values, but exceptions are 4,9,40,90,400,900.
#Iterate the list in reverse order, divide the integer input to get the quotient, convert and add it to output string
#Modulo the integer input to work on the next digit


# Let us start with 1 ro 10
#1 - I,2-II, 3-III, 4-IV, 5-V, 6-VI,7-VII,8-VIII,9-IX,10-X

def int_to_roman(num1):
    roman_int = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10], ['XL', 40], ['L', 50], ['XC', 90], ['C', 100],
                 ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]]
    romanstr = ''
    for sym, number in reversed(roman_int):
        #print(sym, number)
        if num1 // number >= 1: #Goes into loop if true or equal to 1
            count = num1 // number
            romanstr += (sym * count) # Example 'I' * 3 will be III
            num1 = num1 % number
    print(romanstr)
int_to_roman(3999)
