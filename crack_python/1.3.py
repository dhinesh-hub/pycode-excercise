#Given two strings, write a method to decide if one is a permutation of the other.
#Anagram

def anagram(text1,text2):
    if len(text1) != len(text2):
        return False
    else:
        for char in text1:
            if text2.find(char) == -1:  #returns -1 if char is not found
                return False
            else:  
                text2 = text2.replace(char,"",1) # replace(old char,new char,max times) , text2 will be empty if all characters match
        return True

print anagram('hello','llohi')
 
