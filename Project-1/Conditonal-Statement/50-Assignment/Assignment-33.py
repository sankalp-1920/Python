'''33. Write a program to check whether a person can apply for a loan.'''

age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary: "))

if age >= 21:
    if salary >= 25000:
        print("Person is Eligible to Apply for Loan")
    else:
        print("Person is Not Eligible due to Low Salary")
else:
    print("Person is Not Eligible due to Age")