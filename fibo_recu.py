def fibo_rec(num):
   #result = []
   #result.append(num)
   #print result
   if num == 0:
       return 0
   elif num == 1:
       return 1
   else: 
       return fibo_rec(num - 1) + fibo_rec(num - 2) 

fib_limit = raw_input('Enter a number: ')
fib_limit = int(fib_limit) #string to int
if fib_limit <= 0:
    print "Enter a valid number"
else:
    for i in range(fib_limit):
        print(fibo_rec(i))




 
