def min_num_on(inp_list):
    min_in_list = inp_list[0]
    for i in inp_list:
        if i < min_in_list:
            min_in_list = i
    print min_in_list
 
inp_list=[4,6,2,12]
min_num_on(inp_list)
