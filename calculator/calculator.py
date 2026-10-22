def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b
    
def calculate(a, operator, b):
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return subtract(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        return divide(a, b)
    elif operator == "%":
        return modulus(a, b)
    elif operator == "**":
        return power(a, b)
    else:
        return "Invalid operator"


first_number = float(input("Enter the first number: "))
print(first_number)

operator = input("Enter an operation (+, -, *, /, %, **): ")
second_number = float(input("Enter the second number: "))
    
result = calculate(first_number, operator, second_number)
print("Result:", result)