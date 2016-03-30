def bin_2_decimal(bin_str):
    result = 0
    str_len = len(bin_str) - 1
    #print str_len
    for i in bin_str:
        if i == '1':
            print str_len
            #print pow(2,str_len)
            result = result + pow(2,str_len)
            print result
        str_len = str_len - 1
    print result
 
        
    

bin_2_decimal('1010')


