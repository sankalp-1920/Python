'''14. Write a program to check whether a given character is uppercase or lowercase.'''

character = input("Enter the character")

if character.isupper():
    print("Character is uppercase")
elif character.islower():
    print("Character is lowercase")
else:
    print("Character is not a alphabet")



