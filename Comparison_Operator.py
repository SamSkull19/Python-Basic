# Taking input from the user for the first and second numbers
x = input("Enter First Number : ")
y = input("Enter Second Number : ")

# Converting the input to integers
x = int(x)
y = int(y)

# Check if the sum of x and y is less than 30 or the difference is less than 10
if x + y < 30 or x - y < 10:
    print("Number In Range")

# Check if the product of x and y is greater than 30 or the division result is less than 30
elif x * y > 30 or x / y < 30:
    print("Number can be In Range")

# If none of the above conditions are met, the numbers are outside the range
else:
    print("Number Outside Range")
