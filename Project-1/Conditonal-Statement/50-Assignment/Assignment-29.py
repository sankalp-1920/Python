'''29. Write a program to check blood donation eligibility based on age and weight.'''

age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))

if age >= 18 and weight >= 50:
    print("Eligible for Blood Donation")
else:
    print("Not Eligible for Blood Donation")