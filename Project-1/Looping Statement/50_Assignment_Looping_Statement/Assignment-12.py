'''12. Reverse a number using while loop.'''

number = int(input("Enter the number :"))
reverseNum = 0

while number > 0:
    digit = number % 10
    reverseNum = reverseNum * 10 + digit
    number = number // 10

print(reverseNum)