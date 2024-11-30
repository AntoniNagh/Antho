a = input("Enter operation (gånger, plus, division, minus): ").strip().lower()
b = int(input("Enter first number: ").strip())
c = int(input("Enter second number: ").strip())

if a == "gånger":
    print(int (b * c))
elif a == "plus":
    print(int (b + c))
elif a == "division":
    if c != 0:
        print(int(b / c))
    else:
        print("Error: Cannot divide by zero.")
elif a == "minus":
    print(int(b - c))
else: 
    print("Invalid Operation")