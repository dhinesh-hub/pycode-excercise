new_dict={}
with open("/home/dhinesh/pycode/testfile.txt","r") as f:
    for line in f:
        splitline = line.split()
        #print splitline[1]
        new_dict[splitline[0]] = splitline[1:3]
        new_dict[splitline[0]].append(splitline[4:])
    print new_dict  
