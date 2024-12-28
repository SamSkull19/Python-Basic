# Define a 3x3 matrix (2D list)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the second row of the matrix (index 1)
print(matrix[1])  # Output: [4, 5, 6]

# Access and print the element at row 3, column 2 (index 2, 1)
print(matrix[2][1])  # Output: 8

# Access and print the element at row 1, column 3 (index 0, 2)
print(matrix[0][2])  # Output: 3

# Iterate through each row in the matrix
for row in matrix:
    x = ''  # Initialize an empty string to build the row for printing

    for col in row:  # Iterate through each column in the row
        x += str(col) + ' '  # Append the column value and a space to the string

    print(x) 
