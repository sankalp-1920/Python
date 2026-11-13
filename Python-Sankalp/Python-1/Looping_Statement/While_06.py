'''Write a Python program to get sum of even number from user input'''
from colorama import Fore,Back,Style,init
init()

num = int(input("Enter the number = "))
total = 0

while num != 0:
    digit = num % 10
    if digit % 2 == 0:
        total = total + digit
    num = num // 10

print(Fore.RED + "The Addition of even number = ", total)