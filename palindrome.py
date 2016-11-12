def palindrome(text):
    rev_text = text[::-1]
    text_rev2 = ''.join(reversed(text)) #Another method to reverse srting
    print text_rev2
    if rev_text == text:
        print "Is a palindorm"
    else:
       print "Not a palindrome"
palindrome("madam")

