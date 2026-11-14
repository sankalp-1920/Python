'''13. Check whether a number is palindrome.'''

number = int(input("Enter the number :"))
palindrome = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if palindrome == reverse:
    print("This is a Palindrome Number")
else:
    print("This is not a Palindrome Number")
