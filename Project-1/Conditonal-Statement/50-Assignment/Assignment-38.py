'''38. Write a program to check whether a student passed all subjects.'''

s1 = int(input("Enter marks in Subject 1: "))
s2 = int(input("Enter marks in Subject 2: "))
s3 = int(input("Enter marks in Subject 3: "))

if s1 >= 35 and s2 >= 35 and s3 >= 35:
    print("Student Passed All Subjects")
else:
    print("Student Failed in One or More Subjects")