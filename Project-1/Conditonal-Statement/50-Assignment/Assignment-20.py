'''20. Write a program to check ticket price based on age.'''

age = int(input("Enter the age between 1 to 110 : "))

if age > 0 and age <= 110:
    if age < 6:
        print("No ticket !")
    elif age > 6 and age <= 18:
        print("Half ticket !")
    elif age > 18 and age <= 60:
        print("Full Ticket !")
    else:
        print("Half Ticket for Older people")
else:
    print("Enter valid age !")