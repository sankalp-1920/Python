'''44. Write a program to check traffic signal actions using match case.'''

signal = input("Enter traffic signal color (Red/Yellow/Green): ")

match signal.lower():
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Traffic Signal")