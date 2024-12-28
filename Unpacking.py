# Tuple with three values
number = (4, 5, 6)

# Unpacking the tuple into individual variables x, y, z
x, y, z = number

# Print the values of x, y, and z after unpacking
print(f"x = {x}, y = {y}, z = {z}")  # Output: x = 4, y = 5, z = 6

# List of city names
place = ['Dhaka', 'Cumilla', 'Sylhet', 'Rajshahi']

# Unpacking the list into four variables x, y, z, s
x, y, z, s = place

# Print the values of x, y, z, and s after unpacking
print(f"City - 1 = {x}, City - 2 = {y}, City - 3 = {z}, City - 4 = {s}")
# Output: City - 1 = Dhaka, City - 2 = Cumilla, City - 3 = Sylhet, City - 4 = Rajshahi

number2 = [4, 3, 9, 10, 12]

# Unpack the first two elements into x and y, and the remaining elements into the 'others' list
x, y, *others = number2

# Print the unpacked values
print(f"x = {x}, y = {y}, rest = {others}")  
# Output: x = 4, y = 3, rest = [9, 10, 12]


# Example of nested unpacking, where each tuple in the list is unpacked into variables
nested_list = [(1, 2), (3, 4), (5, 6)]

# Iterate through the nested list and unpack each tuple into a and b
for a, b in nested_list:
    # Print the unpacked values for each tuple
    print(f"a = {a}, b = {b}")
    
# Output:
# a = 1, b = 2
# a = 3, b = 4
# a = 5, b = 6


# Example of swapping values using tuple unpacking
a, b = 10, 20

# Swap the values of a and b
a, b = b, a

# Print the swapped values
print(f"a = {a}, b = {b}")  # Output: a = 20, b = 10
