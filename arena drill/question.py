
Implement division_details(a, b). Return a dictionary with three keys: "true_division", "floor_division", and "remainder". true_division should be a / b rounded to 2 decimal places. floor_division should be a // b. remainder should be a % b.
Implement eligibility_logic(score, attendance, completed_drill). Return "Eligible" only when score is greater than or equal to 70, attendance is greater than or equal to 80, and completed_drill is True. Otherwise return "Not eligible".
Implement safe_calculator(a, operator, b). Return the result of applying the operator to the two numbers. Supported operators are "+", "-", "*", "/", "%", and "**". If the operator is unknown, return "Invalid operator". If the operator is "/" or "%" and b is 0, return "Cannot divide by zero". Round division results to 2 decimal places.


RECODING QUSTIONS
Problem 1: Find the Largest Number in a List
Description
Write a Python function named find_largest(numbers) that takes a list of numbers and returns the largest number in the list.
Constraints
Do not use max().
Do not use sort() or sorted().
If the list is empty, return None.
Aim for O(n) time complexity and O(1) auxiliary space.
Examples
Example 1
Input: [3, 41, 56, 21, 76, 9]
Output: 76
Example 2
Input: [-10, -5, -2, -18]
Output: -2
Example 3
Input: []
Output: None
Hints
What value could you assume is the largest before checking the rest?
Compare each number with the current largest value.
When you find a larger number, update what you are storing.


