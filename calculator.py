First = float(input("Enter your first number: "))
Second = float(input("Enter your second number: "))

operation = input("Select your operation (+,-,*,/): ")

if operation == "+":
    print(f"{First} {operation} {Second} = {First + Second}")
elif operation == "-":
    print(f"{First} {operation} {Second} = {First - Second}")
elif operation == "*":
    print(f"{First} {operation} {Second} = {First * Second}")
elif operation == "/":
    if Second == 0:
        print("Cannot divide by Zero")
    else:
        print(f"{First} {operation} {Second} = {First / Second}")
else:
    print("Invalid Operation selected")

