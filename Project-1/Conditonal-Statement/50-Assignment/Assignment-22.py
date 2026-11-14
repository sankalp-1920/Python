'''22. Write a program to check salary bonus based on years of service'''

salary = float(input("Enter your salary: "))
years = int(input("Enter years of service: "))

if years >= 10:
    bonus = salary * 20 / 100
elif years >= 5:
    bonus = salary * 10 / 100
elif years >= 2:
    bonus = salary * 5 / 100
else:
    bonus = 0

total_salary = salary + bonus

print("Basic Salary = Rs.", salary)
print("Bonus Amount = Rs.", bonus)
print("Total Salary = Rs.", total_salary)




