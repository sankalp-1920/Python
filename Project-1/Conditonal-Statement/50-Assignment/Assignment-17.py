'''17. Write a program to check grade based on marks (A, B, C, Fail).'''

marks = int(input("Enter the marks :"))

if marks <= 100 and marks > 0:
    if marks >= 80 and marks <= 100:
        print("A Grade !")
    elif marks >= 60 and marks < 80:
        print("B Grade !")
    elif marks >= 40 and marks < 60:
        print("C Grade !")
    else:
        print("Student is Failed")
else:
    print("Enter the valid marks between 0 to 100")    