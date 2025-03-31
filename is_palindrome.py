def is_palindrome():
    s=input("Type one or more words: ")
    
    a=""
    
    for letter in s:
        a=letter+a
        
       
    if s==a:
        print(s, " is a palindrome")
    else:
        print(s," is not palindrome")
        



is_palindrome()
