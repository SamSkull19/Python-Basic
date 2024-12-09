i = 1

# Loop to print an increasing number of asterisks (`*`) on each line
while i <= 5: 
    print('*' * i) 
    i += 1 

print("Complete")

a = 1

# Loop to print patterns of `#` and `*` based on the value of `a`
while a <= 10: 
    if a % 2 == 1:  # Check if `a` is odd
        print('#' * a)

    else:  # If `a` is even
        print('*' * a)  

    a += 1

print("Complete")

b = 10

# Loop to print patterns of `#` and `*` in decreasing order
while b > 0: 
    if b % 2 == 1:  # Check if `b` is odd
        print('#' * b)
    else:  # If `b` is even
        print('*' * b)  # Print `*` repeated `b` times
    
    b -= 1

print("Complete")
