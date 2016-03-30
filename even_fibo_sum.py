def even_fib(num):
    a=0
    b=1
    c = a + b
    even = 0
    for i in range(0,num):
        print c
        if c % 2 == 0:
            even = even + c
        a = b
        b = c  
        c = a + b 
    print "Even Sum {0}".format(even)

even_fib(10)


