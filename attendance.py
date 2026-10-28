attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes: "))

if attended < 0 or total < attended:
    print("Invalid attendance details")
else:
    count = 0

    while attended / total < 0.75:
        attended = attended + 1
        total = total + 1
        count = count + 1

    print("Additional classes required =", count)
    print("Final attendance =", attended / total * 100, "%")
