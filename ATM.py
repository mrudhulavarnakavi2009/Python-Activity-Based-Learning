balance = 5000

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance = balance + amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Withdrawal successful")
        else:
            print("Invalid amount or insufficient balance")

    elif choice == 3:
        print("Current Balance =", balance)

    elif choice == 4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")
