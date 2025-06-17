# List of integers
number = [4, 3, 9, 10, 12, 5, 2, 8, 8, 2, 3, 5, 3, 9]

# Using map() to convert each number in the list to float
a = map(float, number)

print(a)           # Prints the map object location (not the values directly)
print(list(a))     # Convert map object to list to see the float values
# Output: [4.0, 3.0, 9.0, 10.0, 12.0, 5.0, 2.0, 8.0, 8.0, 2.0, 3.0, 5.0, 3.0, 9.0]

# Using map() to convert each number to string
x = list(map(str, number))
print(x)
# Output: ['4', '3', '9', '10', '12', '5', '2', '8', '8', '2', '3', '5', '3', '9']

# Using map() with a lambda function to double each number
d = map(lambda x: x * 2, number)
print(list(d))
# Output: [8, 6, 18, 20, 24, 10, 4, 16, 16, 4, 6, 10, 6, 18]

# Using map() with a lambda function to square each number
s = map(lambda x: x * x, number)
print(list(s))
# Output: [16, 9, 81, 100, 144, 25, 4, 64, 64, 4, 9, 25, 9, 81]
