def division_details(a, b):
    keys = {
        "true_division": round(a / b, 2),
        "floor_division": a // b,
        "remainder": a  % b
    }
    return keys
print(division_details(10, 3))


def eligibility_logic(score, attendance, completed_drill):
    if score >= 70 and attendance >= 80 and completed_drill == True:
        return "Eligible"
    else:
        return "Not Eligible"

print(eligibility_logic(80, 90, True))
print(eligibility_logic(60, 90, True))
print(eligibility_logic(80, 90, False))


def safe_calculator(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return round(a / b, 2)
    elif operator == "%":
        return "a % b"
    elif operator == "**":
        return "a ** b"
        return operator
    try:
        if operator == "/" and operator == "%" and b == "0":
            return "Cannot be divide by zero"       
    except:
        return "Cannot be divide by zero"
    else:
        print("invalid operator")
print(safe_calculator(5, "+", 7))
print(safe_calculator(6, "*", 12))
print(safe_calculator(2, "/", 9))
