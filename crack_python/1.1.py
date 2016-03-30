#Implement an algorithm to determine if a string has all unique characters.
#What if you cannot use additional data structures?

def uniquechar(text):
    uni_list = []
    for i in text:
        if i in uni_list:
            return False
        else:
            uni_list.append(i)
    return True

print uniquechar("helo")

              
 
