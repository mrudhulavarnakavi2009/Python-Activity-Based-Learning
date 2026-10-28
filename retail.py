total = 0

n = int(input("Enter number of products: "))

for i in range(n):
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))
    total = total + price * quantity

if total >= 1000:
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

print("Total Amount =", total)
print("Discount =", discount)
print("Final Bill =", final_bill)
