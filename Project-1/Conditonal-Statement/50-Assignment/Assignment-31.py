'''31. Write a program to check whether a number is positive and even using nested if.'''

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Number is Positive and Even")
    else:
        print("Number is Positive but Odd")
else:
    print("Number is Not Positive")