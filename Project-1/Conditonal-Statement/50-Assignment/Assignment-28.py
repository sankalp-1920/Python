'''28. Write a program to calculate discounts based on total shopping amount'''

amount = float(input("Enter total shopping amount: "))

if amount >= 5000:
    discount = amount * 20 / 100
elif amount >= 3000:
    discount = amount * 15 / 100
elif amount >= 1000:
    discount = amount * 10 / 100
else:
    discount = 0

final_amount = amount - discount

print("Total Amount = Rs.", amount)
print("Discount = Rs.", discount)
print("Final Amount = Rs.", final_amount)