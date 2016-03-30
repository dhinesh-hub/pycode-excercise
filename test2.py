#newDict = {}
new_dict = {"Address": "Status,State,Load,Owns"}
with open('/home/dhinesh/pycode/testfile.txt', 'r') as f:
    for line in f:
        splitLine = line.split()
        print splitLine[0]
        new_dict[splitLine[0]] = splitLine[1:]
#print new_dict
