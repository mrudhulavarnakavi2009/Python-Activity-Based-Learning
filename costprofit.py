material_cost = float(input("Enter material cost: "))
labour_cost = float(input("Enter labour cost: "))
machine_cost = float(input("Enter machine cost: "))
selling_price = float(input("Enter selling price: "))

total_cost = material_cost + labour_cost + machine_cost
profit = selling_price - total_cost

print("Total Cost =", total_cost)
print("Profit =", profit)

if profit > 0:
    print("Result: Profit")
elif profit < 0:
    print("Result: Loss")
else:
    print("Result: No Profit No Loss")
