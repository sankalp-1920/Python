'''6. Write a program to compare two numbers and print the greater one.'''

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

if num1 > num2:
    print(num1, " is the greater one")
elif num2 > num1:
    print(num2, " is the greater one")
else:
    print(num1,"&", num2, "These are equal numbers")

