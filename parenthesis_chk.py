def par_chk(inp_str):
    new_l = []
    counter = 0
    balanced = True
    while counter < len(inp_str) and balanced == True:
        if inp_str[counter] == '(':
            new_l.append(inp_str[counter]) #add to stack if open paren
        else:
            if not new_l: #checking if list is empty   
                balanced = False
            else:
                new_l.pop()
        counter += 1  

    if not new_l and balanced == True:
        return True
    else:
        return False

print par_chk('(()')
print par_chk('())')
print par_chk('(())')

