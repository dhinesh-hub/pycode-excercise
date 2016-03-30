class Stack:
    def __init__(self):
        self.item = []

    def size(self):
        return len(self.item)
    
    def peek(self):
   	return self.item[len(self.item) - 1]
  
    def pop(self):
        return self.item.pop()  

    def push(self,one):
        self.item.append(one) 

    def isEmpty(self):
        return self.item == []    

s=Stack() 
s.push('hello')
s.push(1)
print s.size()
print s.item
print s.peek()
print s.isEmpty()
s.pop()
print s.size()
print s.item


