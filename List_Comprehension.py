# Define the original list of numbers
number = [4, 3, 9, 10, 1, 19, 15, 20, 18, 17, 13, 6, 7, 11, 14, 16, 12, 5, 2, 8]

# Create an empty list to store numbers that meet the condition
odds = []

# Loop through each number in the list
for num in number:
    # Check if the number is odd OR divisible by 3
    if num % 2 == 1 or num % 3 == 0:
        # If condition is true, add the number to the odds list
        odds.append(num)

# Print the filtered list using the loop
print(odds)


# Do the same filtering using list comprehension (more concise)
ans = [num for num in number if num % 2 == 1 or num % 3 == 0]

# Print the filtered list from list comprehension
print(ans)


number = [4, 3, 9, 10, 1, 19, 15, 20, 18]

ans_and = [num for num in number if num % 2 == 1 if num % 3 == 0]
ans_or = [num for num in number if num % 2 == 1 or num % 3 == 0]

print("AND condition:", ans_and)  # [3, 9, 15]
print("OR condition:", ans_or)    # [3, 9, 1, 19, 15, 18]



