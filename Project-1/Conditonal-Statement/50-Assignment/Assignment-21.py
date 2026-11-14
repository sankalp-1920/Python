'''21. Write a program to find the smallest of three numbers.'''

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

if num1 < num2 and num1 < num3:
    print(num1, "is smaller than",num2,"&", num3)
elif num2 < num3 and num2 < num1:
    print(num2, "is samller than",num1,"&", num3)
else:
    print(num3, "is smaller than",num1,"&", num2)
