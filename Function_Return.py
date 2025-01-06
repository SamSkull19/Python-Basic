# Function to calculate and print the square of a number
def square1(number):
    # Prints the square of the given number
    print(number * number)

# Calls the square1 function with the argument 4
# Note: The function prints the square but does not return a value
print(square1(4))  # This will print "None" after the square, since the function does not return a value


# Function to calculate and return the square of a number
def square2(number):
    # Returns the square of the given number
    return number * number

# Calls the square2 function with the argument 5 and prints the returned value
print(square2(5))


# Function to calculate and return the sum of two numbers
def sum(num1, num2):
    # Returns the sum of num1 and num2
    return num1 + num2

# Calls the sum function with the arguments 5 and 2, and prints the result
print(sum(5, 2))


# Function to calculate and return the difference between two numbers
def sub(num1, num2):
    # Returns the result of subtracting num2 from num1
    return num1 - num2

# Calls the sub function with the arguments 8 and 7, and prints the result
print(sub(8, 7))
