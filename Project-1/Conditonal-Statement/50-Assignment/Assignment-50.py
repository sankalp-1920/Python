'''50. Write a program to build a simple ATM menu using a match case.'''

print("----- Result Menu -----")
print("1. Pass")
print("2. Fail")
print("3. Distinction")
print("4. First Class")

choice = int(input("Enter your result choice (1-4): "))

match choice:
    case 1:
        print("Result: Pass")
    case 2:
        print("Result: Fail")
    case 3:
        print("Result: Distinction")
    case 4:
        print("Result: First Class")
    case _:
        print("Invalid Choice")
