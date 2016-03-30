#Maximal Binary Gap for positive integer N is given as the sequence of consecutive zeroes surrounded by 1 at both ends
def max_bin_gap(num):
    max_itr,max_res = 0,0
    bin_num = bin(num)[2:] #bin(int) return output in binary with pre-fix 0b
    print bin_num
    for i in bin_num:
        if i == '0':
            max_itr += 1
            if max_itr >= max_res:
                max_res = max_itr 
                #print max_res
        else: 
            max_itr = 0   
    return max_res

print max_bin_gap(1201)
