#decimal to any base element

def dec_to_bin(num,base):
    bin_list = []
    while num != 0:
        bin_ele = num % base
        num = num // base 
        bin_list.append(bin_ele)
    print bin_list
    bin_list.reverse() #reverse the elements in list
    print bin_list
    str1 = ''.join(str(e) for e in bin_list) #important integer list to string
    return str1

print dec_to_bin(43,2)
print dec_to_bin(43,8)
 
