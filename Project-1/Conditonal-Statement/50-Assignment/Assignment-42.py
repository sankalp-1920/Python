'''42. Write a program to perform calculator operations using match case.'''

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (+, -, *, /): ")

match choice:
    case "+":
        print("Addition =", num1 + num2)
    case "-":
        print("Subtraction =", num1 - num2)
    case "*":
        print("Multiplication =", num1 * num2)
    case "/":
        if num2 != 0:
            print("Division =", num1 / num2)
        else:
            print("Division by zero is not possible")
    case _:
        print("Invalid Choice")