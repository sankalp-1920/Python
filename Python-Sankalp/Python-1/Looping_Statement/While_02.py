#'''Write a program to print even number from 0 to 10'''

start_value = int(input("Enter the Start Value = "))
end_value = int(input("Enter the End Value = "))

i = start_value
count = 0

while i <= end_value:
    if i % 2 == 0:
        print(i)
        count = count + 1
    i = i + 1

print("The count of even no. is = ",count)
