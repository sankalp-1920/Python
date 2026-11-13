'''Write a program for a traffic light'''

light = input("Light color : ").lower()

if(light == "red"):
    print("Stop !")
elif(light == "yellow"):
    print("Look !")
elif(light == "green"):
    print("Go !")
else:
    print("Light is broken !")
