# Function to display the first and second names in the given order
def show_name(first, second):
    print(f"First name : {first}")
    print(f"Second name : {second}")

# Calls the show_name function with positional arguments
show_name("Sifat", "Samin") # Positional Arguments


# Function to display the first and second names using keyword arguments
def show_full_name(first, second):
    print(f"First name : {first}")
    print(f"Second name : {second}")

# Calls the show_full_name function with keyword arguments in a different order
show_full_name(second="Sifat", first="Samin") # Keyword Arguments


# Function to display two numbers as strings using positional arguments
def show_number(first, second):
    print(f"First number : {first}")
    print(f"Second number : {second}")

# Calls the show_number function with positional arguments
show_number("34", "76")


# Function to display two numbers using keyword arguments
def show_num(first, second):
    print(f"First number : {first}")
    print(f"Second number : {second}")

# Calls the show_num function with keyword arguments in a different order
show_num(second="34", first="76")
