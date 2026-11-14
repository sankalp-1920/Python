'''46. Write a program to print grade description using match case'''

grade = input("Enter your grade (A, B, C, D, F): ")

match grade.upper():
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Pass")
    case "F":
        print("Fail")
    case _:
        print("Invalid Grade")