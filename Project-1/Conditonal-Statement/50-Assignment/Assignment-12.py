'''12. Write a program to check whether a person is a child or adult (age < 18).'''

age = int(input("Enter the age :"))

if age <= 110 and age > 0:
    if age > 18:
        print("A person is adult !")
    else:
        print("A person is child !")
else:
    print("Enter a valid age between 0 to 110 !")
