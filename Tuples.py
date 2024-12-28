# Tuple of numbers
number = (1, 2, 3, 4, 5, 6)

# Access and print the 3rd element in the tuple (index 2)
print(number[2])  # Output: 3

# Access and print the 2nd last element in the tuple using negative indexing
print(number[-2])  # Output: 5

# Count how many times the number 4 appears in the tuple
print(number.count(4))  # Output: 1

# Find the index of the first occurrence of the number 5 in the tuple
print(number.index(5))  # Output: 4

# Print a slice from the beginning to the 4th element (index 3), excluding the 4th element
print(number[:4])  # Output: (1, 2, 3, 4)

# Print a slice from the 3rd element (index 2) to the 5th element (index 4), excluding the 5th element
print(number[2:5])  # Output: (3, 4, 5)

# Print the entire tuple (slice from the beginning to the end)
print(number[:])  # Output: (1, 2, 3, 4, 5, 6)

# Print a slice from the beginning to the 2nd last element (index -1)
print(number[0:-1])  # Output: (1, 2, 3, 4, 5)
