# List of places in Bangladesh
place = ['Dhaka', 'Cumilla', 'Sylhet', 'Rajshahi', 'Barishal', 'Chattogram']

# Print the entire list of places
print(place)

# Access and print the 2nd element in the list (index 1)
print(place[1])  # Output: 'Cumilla'

# Access and print the 5th element in the list (index 4)
print(place[4])  # Output: 'Barishal'

# Access and print the last element in the list using negative indexing
print(place[-1])  # Output: 'Chattogram'

# Access and print the 3rd last element in the list using negative indexing
print(place[-3])  # Output: 'Rajshahi'

# Print the sublist starting from the 3rd element to the end
print(place[2:])  # Output: ['Sylhet', 'Rajshahi', 'Barishal', 'Chattogram']

# Print the sublist containing the first 4 elements
print(place[:4])  # Output: ['Dhaka', 'Cumilla', 'Sylhet', 'Rajshahi']

# Print the sublist excluding the last 3 elements
print(place[:-3])  # Output: ['Dhaka', 'Cumilla', 'Sylhet']

# Print the entire list again to confirm it remains unchanged
print(place)  # Output: ['Dhaka', 'Cumilla', 'Sylhet', 'Rajshahi', 'Barishal', 'Chattogram']

# Modify the last element in the list using negative indexing
place[-1] = 'Khulna'  # Replace 'Chattogram' with 'Khulna'

# Print the updated list to confirm the change
print(place)  # Output: ['Dhaka', 'Cumilla', 'Sylhet', 'Rajshahi', 'Barishal', 'Khulna']
