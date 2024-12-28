# Initial list of numbers
number = [4, 3, 9, 10, 12, 5, 2, 8]

# Append 20 to the end of the list
number.append(20)
print(number)  # Output: [4, 3, 9, 10, 12, 5, 2, 8, 20]

# Insert 90 at index 3
number.insert(3, 90)
print(number)  # Output: [4, 3, 9, 90, 10, 12, 5, 2, 8, 20]

# Remove the first occurrence of 12 from the list
number.remove(12)
print(number)  # Output: [4, 3, 9, 90, 10, 5, 2, 8, 20]

# Create a new list with the same values as the original list
number2 = [4, 3, 9, 10, 12, 5, 2, 8]
print(number2)  # Output: [4, 3, 9, 10, 12, 5, 2, 8]

# Clear all elements from the second list
number2.clear()
print(number2)  # Output: []

# Print the current state of the first list
print(number)  # Output: [4, 3, 9, 90, 10, 5, 2, 8, 20]

# Pop the last element from the list (remove and return 20)
number.pop()
print(number)  # Output: [4, 3, 9, 90, 10, 5, 2, 8]

# Print the index of the first occurrence of 10 in the list
print(number.index(10))  # Output: 4

# Check if 90 exists in the list
print(90 in number)  # Output: True

# Count the occurrences of 9 in the list
print(number.count(9))  # Output: 1

# Sort the list in ascending order
number.sort()
print(number)  # Output: [2, 3, 4, 5, 8, 9, 10, 90]

# Reverse the order of the list
number.reverse()
print(number)  # Output: [90, 10, 9, 8, 5, 4, 3, 2]

# Create a copy of the current list
number3 = number.copy()

# Pop the last element (90) from the original list
number.pop()
print(number)  # Output: [90, 10, 9, 8, 5, 4, 3]

# Print the copied list (remains unchanged)
print(number3)  # Output: [90, 10, 9, 8, 5, 4, 3, 2]
