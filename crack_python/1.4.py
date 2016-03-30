#write a method to replace all space in a string with '%20

def insert_20(text):
    new_text = []
    for char in text:
        if char == ' ':
            char = '%20'
        new_text.append(char)
    print ''.join(new_text) #converting list to string

insert_20(" new hope ")        
            
