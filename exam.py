attendance = float(input("Enter attendance percentage: "))
lab = input("Are laboratory works completed? (yes/no): ")
internal_marks = int(input("Enter internal marks: "))
fees = input("Are all fees paid? (yes/no): ")

issues = 0

print("\n--- Examination Eligibility Report ---")

if attendance < 75:
    print("Requirement not met: Low attendance")
    issues = issues + 1

if lab.lower() != "yes":
    print("Requirement not met: Laboratory work incomplete")
    issues = issues + 1

if internal_marks < 40:
    print("Requirement not met: Internal marks are low")
    issues = issues + 1

if fees.lower() != "yes":
    print("Requirement not met: Fees not paid")
    issues = issues + 1

if issues == 0:
    print("Result: Eligible for examination")
else:
    print("Result: Not eligible for examination")

print("Total requirements not met =", issues)
