# Importing all functions from math and random modules
from math import *
from random import *

# Printing mathematical constants
print(pi)        # Output: 3.141592653589793 (Value of π)
print(e)         # Output: 2.718281828459045 (Euler's number)

# Performing basic mathematical operations
print(sqrt(25))      # Output: 5.0 (Square root of 25)
print(pow(5, 2))     # Output: 25.0 (5 raised to the power 2)

# Trigonometric functions
print(sin(pi/2))     # Output: 1.0 (Sine of 90 degrees)
print(cos(0))        # Output: 1.0 (Cosine of 0 degrees)

# Factorial and rounding functions
print(factorial(3))  # Output: 6 (3! = 3×2×1)
print(floor(3.4))    # Output: 3 (Rounding down)
print(ceil(3.4))     # Output: 4 (Rounding up)

# Generating random numbers
print(random())          # Output: Random float between 0.0 and 1.0
print(randint(1, 10))    # Output: Random integer between 1 and 10 (inclusive)

# Working with a list of country names
name = ["Australia", "Bangladesh", "India", "Argentina", "Pakistan", "Saudi Arabia"]
print(choice(name))      # Output: Randomly selects and prints one country name from the list

shuffle(name)            # Shuffles the list in-place (random order)
print(name)              # Output: The shuffled list
