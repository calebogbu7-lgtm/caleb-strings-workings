# def division_details(a, b):
#     keys = {
#         "true_division": round(a / b, 2),
#         "floor_division": a // b,
#         "remainder": a  % b
#     }
#     return keys
# print(division_details(10, 3))


# def eligibility_logic(score, attendance, completed_drill):
#     if score >= 70 and attendance >= 80 and completed_drill == True:
#         return "Eligible"
#     else:
#         return "Not Eligible"

# print(eligibility_logic(80, 90, True))
# print(eligibility_logic(60, 90, True))
# print(eligibility_logic(80, 90, False))


# def safe_calculator(a, operator, b):

#     if operator == "+":
#         return a + b
#     elif operator == "-":
#         return a - b
#     elif operator == "*":
#         return a * b
#     elif operator == "/":
#         try:
#             num = round(a / b, 2)

#             return num

#         except ZeroDivisionError:
#             return " cannot divide by zero"

        
            
#     elif operator == "%":
#         return "a % b"
#     elif operator == "**":
#         return "a ** b"

    
# print(safe_calculator(5, "+", 7))
# print(safe_calculator(6, "*", 12))
# print(safe_calculator(2, "/", 0))

# # RECODING ANSWER
def find_largest(numbers):
    if len(numbers) == 0:
        return None
    largest_number = numbers[0]
    for x in numbers:
        if x < largest_number:
            largest_number = x
    return largest_number
   
print(find_largest([]))
print(find_largest([67, 89, 90]))
print(find_largest([-67, -78, -23]))

def list_sum(numbers):
    total = 0

    for x in numbers:
        total += x
    return total

print(list_sum([]))
print(list_sum([67, 89, 90]))
print(list_sum([-67, -78, -23]))
def count_occurrences(numbers, target):
    count = 0

    for number in numbers:
        if number == target:
            count = count + 1

    return count
    def find_number(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index

    return -1
    def reverse_list(items):
    result = []

    for item in items:
        result.insert(0, item)

    return resultdef second_largest(numbers):
    largest = None
    second = None

    for number in numbers:
        if largest is None or number > largest:
            second = largest
            largest = number

        elif number != largest and (second is None or number > second):
            second = number

    return second