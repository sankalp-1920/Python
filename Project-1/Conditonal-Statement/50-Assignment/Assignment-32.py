'''32. Write a program to check whether a student is eligible for an exam (attendance + marks).'''


attendance = float(input("Enter attendance percentage: "))
marks = int(input("Enter marks: "))

if attendance >= 75:
    if marks >= 35:
        print("Student is Eligible for Exam")
    else:
        print("Student is Not Eligible due to Low Marks")
else:
    print("Student is Not Eligible due to Low Attendance")