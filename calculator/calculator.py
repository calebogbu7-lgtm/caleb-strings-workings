print("\n---- HERE'S YOUR CALCULATOR---")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def divide(a, b):
        try:
            division = (a / b)
            return division
        except ZeroDivisionError:
            print("Error: can't divide by zero")
        

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
while True:
    try:
        first_number = float(input("Enter the first number: "))
        break
    except ValueError:    
        print("Error: enter a valid number")
while True:
    operator = input("Enter an operation (+, -, *, /, %, **): ")
    if operator in ["+", "-", "*", "/", "%","**"]:
        break
    else:
        print("Error: enter a valid operator")
while True:
    try:
        second_number = int(input("Enter the second number: "))
        break  
    except ValueError:
        print("Error: Enter a valid number")
result = calculate(first_number, operator, second_number)
print("Result:", result)