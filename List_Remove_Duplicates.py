# List of numbers with duplicates
number = [4, 3, 9, 10, 12, 5, 2, 8, 8, 2, 3, 5, 3, 9]

# Initialize an empty list to store unique numbers
unique_numbers = []

# Iterate through each number in the original list
for i in number:
    # If the number is not already in the unique_numbers list, add it
    if i not in unique_numbers:
        unique_numbers.append(i)

# Print the list of unique numbers
print(unique_numbers)  # Output: [4, 3, 9, 10, 12, 5, 2, 8]

# Sort the unique_numbers list in ascending order
unique_numbers.sort()

# Print the sorted list of unique numbers
print(unique_numbers)  # Output: [2, 3, 4, 5, 8, 9, 10, 12]
