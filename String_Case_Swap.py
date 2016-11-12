def str_case_swap():
    inp_str = raw_input("Enter String")
    new_str =""
    for i in inp_str:
        if i.isupper():
            new_str += i.lower()
        else:
            new_str += i.upper()
    print new_str

str_case_swap()








