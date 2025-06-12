# Declare a global variable 'ans'
ans = 50

# Define a function that modifies the global 'ans'
def numberCatch(num):
    global ans  # Use the global 'ans' variable instead of creating a local one
    ans = ans + num  # Add the argument to the global variable
    print(f'Number : {ans}')  # Print the updated value

# Call the function with the value of 'ans' as the argument (50)
numberCatch(ans)


# Declare a global counter
counter = 0

def incrementCounter(step):
    global counter  # Access the global variable
    counter += step  # Increment it by the given step
    print(f'Counter: {counter}')

# Call the function with different step values
incrementCounter(5)   # Output: Counter: 5
incrementCounter(10)  # Output: Counter: 15
