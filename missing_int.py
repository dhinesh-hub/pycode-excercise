#Find missing numbers in a integer list
def missing_int(inp_list):
    result = []
    print inp_list
    max_int = len(inp_list) - 1
    static = [0] * inp_list[max_int] #create a list with all zeros and size as the last number of the input
    for i in inp_list:
         static[i-1] = 1
    print static 
    print max_int
    for j in range(0,len(static)): #print all the index locations of zero in static
       if static[j] == 0:
           result.append(j + 1) 
    print result 

inp_list = range(4)
inp_list.extend(range(7,9))
missing_int(inp_list)
