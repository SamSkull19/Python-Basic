# Function to add two numbers
def sumNumber(num1, num2):
    ans = num1 + num2
    return ans

# Calling the function with two arguments
ans = sumNumber(1, 2)
print(ans)  # Output: 3


# Function using *args to accept a variable number of arguments
def functionName(*args):
    print(args)  # Prints the tuple of arguments passed

# Calling the function with multiple values
functionName(2, 323, 56, 131, 18)


# Function that calculates the sum of any number of arguments
def functionName2(*args):
    print(args)  # Print all the arguments as a tuple
    sum = 0

    # Loop through each number in args and add to sum
    for num in args:
        print(num)  # Print the current number
        sum += num  # Add the current number to the running total

    return sum  # Return the final sum

# Define a list of numbers
listNumber = [43, 45, 45, 87, 23, 9, 44, 53]

# Unpack the list using * so that each element is passed as a separate argument
ansList = functionName2(*listNumber)
print(f'Sum : {ansList}')  # Output the sum


# Another function doing the same summing job as functionName2
def functionName3(*args):
    print(args)
    sum = 0

    for num in args:
        print(num)
        sum += num

    return sum

# Directly passing numbers to the function without using a list
ansList = functionName2(43, 45, 45, 87, 23, 9, 44, 53)
print(f'Sum : {ansList}')  # Output the sum
