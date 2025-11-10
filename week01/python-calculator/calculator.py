

a = float(input("First number: "))
op = input("Operator (+ - * /): ").strip()
b = float(input("Second number: "))

if op == "+": print(a + b)
elif op == "-": print(a - b)
elif op == "*": print(a * b)
elif op == "/": print(a / b if b != 0 else "Can't divide by zero")
else: print("Unknown operator")