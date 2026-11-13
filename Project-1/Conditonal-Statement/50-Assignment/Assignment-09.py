'''9. Write a program to check whether a student has passed or failed (pass marks = 40).'''

stuMarks = int(input("Enter the Student Marks : "))

if stuMarks <= 100 and stuMarks >= 0:
    if stuMarks > 40:
        print("Student is Passed !!!")
    else:
        print("Student is Failed !!!")
else:
    print("Enter Marks Between 0 to 100")
    
        