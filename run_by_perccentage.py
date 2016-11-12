#split running a task by X=%20 , Y=%20, Z=%60
counter = 0
print counter
def run_task():
   print "inside func"     
   counter += 1
   if(counter <= 2):
       print "Executing X{0}".format(counter)
   elif(counter <= 4 and counter > 2):
       print "Executing Y{0}".format(counter)
   elif(counter >= 5 and counter <= 10):
       print "Executing Z{0}".format(counter)
   else:
       counter = 0

for i in range(0,20):
     run_task

       
