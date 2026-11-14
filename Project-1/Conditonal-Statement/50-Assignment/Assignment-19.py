'''19. Write a program to print the day name based on day number (1–7).'''

day_num = int(input("Enter the number between 1 to 7 :"))

if day_num == 1:
    print("Sunday")
elif day_num == 2:
    print("Monday")
elif day_num == 3:
    print("Tuesday")
elif day_num == 4:
    print("Wednesday")
elif day_num == 5:
    print("Thursday")
elif day_num == 6:
    print("Friday")
elif day_num == 7:
    print("Saturday")
else :
    print("Enter the valid number")