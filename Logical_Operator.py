# Taking input from the user for the first and second numbers
x = input("Enter First Number : ")
y = input("Enter Second Number : ")

# Converting the input to integers
x = int(x)
y = int(y)

# Check if both numbers are even
if x % 2 == 0 and y % 2 == 0:
    print(f"Both {x} and {y} Numbers are Even")

# Check if the first number is even and the second is odd
elif x % 2 == 0 and y % 2 == 1:
    print(f"Number {x} is Even and Number {y} is Odd")

# Check if the first number is odd and the second is even
elif x % 2 == 1 and y % 2 == 0:
    print(f"Number {x} is Odd and number {y} is Even")

# If both numbers are odd
else:
    print(f"Both {x} and {y} Numbers are Odd")


a = input("Enter First Number : ")
b = input("Enter Second Number : ")

# Converting the input to integers
a = int(a)
b = int(b)

# Check if both numbers are even
if a % 2 == 0 or y % 2 == 0:
    print(f"One number or Both number can be Odd")

# If both numbers are odd
else:
    print(f"Both {x} and {y} Numbers are Odd")