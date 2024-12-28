number = [6, 2, 6, 2, 6]

# Outer loop iterates through each number in the list
for i in number:
    shape = ''  # Initialize an empty string to build the shape
    
    for j in range(i):  # Inner loop adds '*' equal to the current number
        shape += '*'

    print(shape)  # Print the line of '*'

# Create a diagonal "X" shape within a 5x5 grid
for i in range(5):  # Outer loop for rows
    x = ''
    
    for j in range(5):  # Inner loop for columns
        if i == j:  # Primary diagonal condition
            x += 'x'
        elif j == 4 - i:  # Secondary diagonal condition
            x += 'x'
        else:  # Fill the rest of the grid with spaces
            x += ' '

    print(x)  # Print the row
