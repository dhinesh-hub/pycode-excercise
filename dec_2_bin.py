#decimal to any base element

def dec_to_bin(num,base):
    bin_list = []
    while num != 0:
        bin_ele = num % base
        num = num // base 
        bin_list.append(bin_ele)
    print bin_list
    num_str = 0
    for i in bin_list:
        num_str = num_str + bin_list.pop() 
    return num_str
   

print dec_to_bin(43,2)
print dec_to_bin(43,8)
 
