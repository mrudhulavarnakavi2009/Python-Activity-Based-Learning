consultation = float(input("Enter consultation fee: "))
tests = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

total = consultation + tests + treatment

if total >= 5000:
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

print("Total Bill =", total)
print("Discount =", discount)
print("Final Bill =", final_bill)
