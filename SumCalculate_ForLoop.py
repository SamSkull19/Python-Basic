price = [20, 40, 50, 70, 100, 300, 10, 30]

sum = 0

# Iterate through the indices of the 'price' list using range(len(price))
for i in range(len(price)):  
    # Add the current price to the total sum
    sum += price[i]

# Print the total sum of prices
print(f"Total Price : {sum}")
