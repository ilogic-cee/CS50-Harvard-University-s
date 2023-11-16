# interpreter.py

def main():
    # Prompt the user for an arithmetic expression
    expression = input("Enter an arithmetic expression (e.g., 1 + 1): ")

    # Split the expression into operands and operator
    x, op, z = expression.split()

    # Convert operands to integers
    x = int(x)
    z = int(z)

    # Perform the calculation based on the operator
    result = calculate(x, op, z)

    # Output the result as a floating-point value formatted to one decimal place
    print(f"{result:.1f}")

def calculate(x, op, z):
    # Perform the calculation based on the operator
    if op == "+":
        return x + z
    elif op == "-":
        return x - z
    elif op == "*":
        return x * z
    elif op == "/":
        return x / z

if __name__ == "__main__":
    main()
