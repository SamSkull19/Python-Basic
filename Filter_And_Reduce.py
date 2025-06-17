from functools import reduce  # Import reduce function from functools module

# List of numbers
number = [4, 3, 9, 10, 12, 5, 2, 8, 8, 2, 3, 5, 3, 9]

# Filter even numbers from the list using lambda function
a = filter(lambda x: x % 2 == 0, number)
print(list(a))  # Output: List of even numbers from 'number'

# Filter odd numbers from the list using lambda function
b = filter(lambda x: x % 2, number)
print(list(b))  # Output: List of odd numbers from 'number'

# Use reduce to sum all elements in the list
s = reduce(lambda x, y: x + y, number)
print(s)  # Output: Sum of all numbers in the list

# Use reduce to multiply all elements in the list
x = reduce(lambda x, y: x * y, number)
print(x)  # Output: Product of all numbers in the list
