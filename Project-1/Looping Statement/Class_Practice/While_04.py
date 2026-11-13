'''Write a Python program to reverse a number using user input'''

num = int(input("Enter the number = "))
rev = 0

while num != 0:
    digit = num % 10 # 4 3 2 1
    rev = rev * 10 + digit # 4321
    num = num // 10 # 123 12 1 0

print("Reverse number = ", rev)
