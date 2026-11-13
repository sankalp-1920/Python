'''15. Write a program to check whether a number is divisible by both 3 and 7 or not.'''

number = int(input("Enter the number :"))
if number%3 == 0 and number%7 == 0:
    print("The given number is divisible by both 3 and 7")
else:
    print("The given number is not divisible by both 3 and 7")