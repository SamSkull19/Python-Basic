price = 10 # Integer
name = 'John Doe' # String
flag = True # Bool
num = 4.5545355 # Float

# Correct way to print with commas (no concatenation issue)
print(price, " ", name, " ", flag, " ", num)

# Correct way to concatenate strings
print(str(price) + " " + name + " " + str(flag) + " " + str(num))