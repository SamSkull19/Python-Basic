# Function to display the user's name
def show_name(name):
    print(f"My name is : {name}")

# Prompt the user to enter their name
name = input("Enter your name : ") 
show_name(name)  # Calls the show_name function to display the name

# Function to perform basic arithmetic operations
def calculation(a, b):
    # Calculates and prints the sum of a and b
    print(f"Sum : {a + b}")
    # Calculates and prints the subtraction of b from a
    print(f"Sub : {a - b}")
    # Calculates and prints the multiplication of a and b
    print(f"Mul : {a * b}")
    # Calculates and prints the division of a by b
    print(f"Div : {a / b}")

# Prompt the user to enter two numbers
a = int(input("Enter a : "))
b = int(input("Enter b : "))

# Calls the calculation function with the provided numbers
calculation(a, b)
