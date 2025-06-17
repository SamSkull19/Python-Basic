# Regular function that doubles the input
def double(x):
    return x * 2

a = double(2)  # Call function with 2, result is 4
print(a)       # Output: 4

# Lambda function to double the input (anonymous function)
double = lambda x: x * 2

a = double(3)  # Call lambda with 3, result is 6
print(a)       # Output: 6

# Lambda function to square the input
sq = lambda x: x * x

b = sq(5)      # Square of 5 is 25
print(b)       # Output: 25

# Lambda function to add two inputs
add = lambda x, y: x + y

c = add(3, 5)  # Sum of 3 and 5 is 8
print(c)       # Output: 8

# Additional examples:

# Lambda to subtract two numbers
sub = lambda x, y: x - y
print(sub(10, 4))  # Output: 6

# Lambda to check if a number is even (returns True or False)
is_even = lambda x: x % 2 == 0
print(is_even(4))  # Output: True
print(is_even(7))  # Output: False

# Lambda with no input - returns a constant string
greet = lambda: "Hello!"
print(greet())     # Output: Hello!

# Lambda used inside a list sorting - sort by absolute value
numbers = [-3, 1, -7, 4, 2]
numbers.sort(key=lambda x: abs(x))
print(numbers)     # Output: [1, 2, -3, 4, -7]
