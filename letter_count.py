def letter_count(text):
    count = {}
    for i in text:
        if count.has_key(i):
           count[i] += 1
        else:
           count[i] = 1
    print count

letter_count("eell")  


  
            
