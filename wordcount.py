def wordcount(file_loc):
    result = {}
    with open(file_loc,'r') as f:
        for line in f:
            words = line.split()        
            for word in words:
                if word in result.keys(): # Iterate over dictionary keys
                    result[word] = result[word] + 1 
                else: 
                    result[word] = 1
    print result         
wordcount('/home/dhinesh/pycode/wordcount_inp')

