'''48. Write a program to print language choice using match case.'''

print("----- Language Menu -----")
print("1. English")
print("2. Hindi")
print("3. Marathi")
print("4. French")
print("5. German")

choice = int(input("Enter your language choice (1-5): "))

match choice:
    case 1:
        print("You selected English")
    case 2:
        print("You selected Hindi")
    case 3:
        print("You selected Marathi")
    case 4:
        print("You selected French")
    case 5:
        print("You selected German")
    case _:
        print("Invalid Language Choice")