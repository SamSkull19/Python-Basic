number = [4, 3, 9, 10, 1, 19, 15, 20, 18, 17, 13, 6, 7, 11, 14, 16, 12, 5, 2, 8]

# Initialize max_number with the first element of the list
max_number = number[0]

# Loop through each number in the list to find the maximum
for i in number:
    # If the current number is greater than max_number, update max_number
    if i > max_number:
        max_number = i

# Print the maximum number found in the list
print(max_number)  # Output: 20
