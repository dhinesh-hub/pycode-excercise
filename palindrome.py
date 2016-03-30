def palindrome(text):
    rev_text = text[::-1]
    if rev_text == text:
        print "Is a palindorm"
    else:
       print "Not a palindrome"
palindrome("madam")

