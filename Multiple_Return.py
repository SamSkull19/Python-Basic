def calculation(num1=0, num2=0):
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2 if num2 != 0 else 'Undefined'

    return sum, sub, mul, div

# Call the function with two arguments and store the returned tuple
ans = calculation(10, 2)
print(ans)

# Loop through each result in the returned tuple and print it
for result in ans:
    print(result)
