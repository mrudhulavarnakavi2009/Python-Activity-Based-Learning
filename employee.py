basic_salary = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))
overtime = float(input("Enter overtime amount: "))

gross_salary = basic_salary + allowance + overtime

if gross_salary > 30000:
    deduction = gross_salary * 0.10
else:
    deduction = gross_salary * 0.05

net_salary = gross_salary - deduction

print("Gross Salary =", gross_salary)
print("Deduction =", deduction)
print("Net Salary =", net_salary)
