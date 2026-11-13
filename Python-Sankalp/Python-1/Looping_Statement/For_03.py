'''Write a program to print the sum of number using user input'''

from colorama import Fore, Back, Style, init
init()

start_value = int(input("Enter the Start Value = "))
end_value = int(input("Enter the End Value = "))
total = 0;

for i in range(start_value,end_value,1):
    total = total + i

print(Fore.GREEN+ "Sum of all the numbers = ", total)