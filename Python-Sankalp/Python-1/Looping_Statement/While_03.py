'''The Program for Sum of even number between start_value and end_value'''

start_value = int(input("Enter the Start Value = "))
end_value = int(input("Enter the End Value = "))

i = start_value
total = 0

while i <= end_value:
    if i % 2 == 0:
        total = total + i
    i = i + 1

print("The sum of even no. is = ",total)