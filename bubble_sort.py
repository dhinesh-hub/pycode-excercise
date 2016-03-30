def bubble_sort(num_list): 
    for i in range(len(num_list) - 1):
        for j in range(len(num_list) - i - 1):
           if num_list[j] > num_list[j+1]:
               temp = num_list[j]
               num_list[j] = num_list[j+1]
               num_list[j+1] = temp
    return num_list  

num_list = [9,6,1,4,8]
print bubble_sort(num_list)

  
         
                          



