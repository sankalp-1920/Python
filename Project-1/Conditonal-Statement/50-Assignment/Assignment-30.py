'''30. Write a program to check the type of number (single, double, or three digit)'''

num = int(input("Enter a number: "))

num = abs(num)

if num >= 0 and num <= 9:
    print("Single Digit Number")
elif num >= 10 and num <= 99:
    print("Double Digit Number")
elif num >= 100 and num <= 999:
    print("Three Digit Number")
else:
    print("More than Three Digit Number")