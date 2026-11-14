'''47. Write a program to check user role (admin, user, guest) using match case.'''

role = input("Enter your role (admin/user/guest): ")

match role.lower():
    case "admin":
        print("Welcome Admin")
        print("You have full access")
    case "user":
        print("Welcome User")
        print("You have limited access")
    case "guest":
        print("Welcome Guest")
        print("You have read-only access")
    case _:
        print("Invalid User Role")