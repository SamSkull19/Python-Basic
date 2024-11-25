# Prompting user for birth year
birthYear = input("Enter your Birth Year: ")
birthYear = int(birthYear)  # Convert and reassign to integer
currentYear = 2024

# Calculating age
age = currentYear - birthYear
print("Your age is", age)  # Printing age as an integer
print("Your age is " + str(age))  # Convert age to string for concatenation


# Demonstrating float to int conversion
a = 12.42424  # Float value
print("Before conversion: Value =", a, ", Type =", type(a))
a = int(a)  # Convert and reassign to integer
print("After conversion: Value =", a, ", Type =", type(a))


# Demonstrating int to float conversion
b = 32  # Integer value
print("Before conversion: Value =", b, ", Type =", type(b))
b = float(b)  # Convert and reassign to float
print("After conversion: Value =", b, ", Type =", type(b))


# Demonstrating int to bool conversion
c = 0  # Integer value
print("Before conversion: Value =", c, ", Type =", type(c))
c = bool(c)  # Convert and reassign to boolean
print("After conversion: Value =", c, ", Type =", type(c))
