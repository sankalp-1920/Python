'''34. Write a program to check whether a year is a leap year and century year.'''

year = int(input("Enter a year: "))

if year % 100 == 0:
    print("It is a Century Year")

    if year % 400 == 0:
        print("It is a Leap Year")
    else:
        print("It is Not a Leap Year")

else:
    print("It is Not a Century Year")

    if year % 4 == 0:
        print("It is a Leap Year")
    else:
        print("It is Not a Leap Year")