# PEMDAS:
# P - Parentheses
# E - Exponents
# M - Multiplication
# D - Division
# A - Addition
# S - Subtraction

# Expression: (2 + 3) × 2^2 - 8 ÷ 4 + 5

# Step 1: Parentheses
# Solve the operation inside parentheses first: (2 + 3)
parentheses_result = 2 + 3  # Result: 5

# Step 2: Exponents
# Calculate the exponent: 2^2
exponent_result = 2 ** 2  # Result: 4

# Step 3: Multiplication
# Multiply the result of parentheses by the exponent result: 5 × 4
multiplication_result = parentheses_result * exponent_result  # Result: 20

# Step 4: Division
# Perform division: 8 ÷ 4
division_result = 8 / 4  # Result: 2.0

# Step 5: Subtraction and Addition (from left to right)
# Subtract the division result from the multiplication result: 20 - 2.0
subtraction_result = multiplication_result - division_result  # Result: 18.0

# Add 5 to the result of subtraction: 18.0 + 5
final_result = subtraction_result + 5  # Result: 23.0

# Print the final result
print("Final result: ", final_result)  # Output: 23.0
