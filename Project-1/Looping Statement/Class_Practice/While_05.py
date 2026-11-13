'''Write a Python program to reverse a number using user input and make sum'''

num = int(input("Enter the number = "))
total = 0

while num != 0:
    digit = num % 10
    total = total + digit
    num = num // 10

print("Reverse number = ", total)
