def factors(num):
    facts = [] 
    for i in range(1,num):
        if num%i == 0:
            facts.append(i)
    print facts
    print len(facts)

factors(10)        

