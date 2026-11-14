'''40. Write a program to check whether a password is valid using nested if.'''

password = input("Enter your password: ")

if len(password) >= 8:
    if password == "Python@123":
        print("Password is Valid")
    else:
        print("Incorrect Password")
else:
    print("Password must contain at least 8 characters")