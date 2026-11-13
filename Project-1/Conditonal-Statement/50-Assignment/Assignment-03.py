'''3. Write a program to check whether a person is eligible to vote or not.'''

personAge = int(input("Enter the Person Age : "))

if personAge >= 18 and personAge <= 110:
    print("This person is eligible to vote ")
else:
    print("This person is not eligible to vote ")
