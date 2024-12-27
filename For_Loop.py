# List of places
place = ['Dhaka', 'Cumilla', 'Sylhet', 'Rajshahi']

x = 1
# Loop through each place in the list and print its index and name
for i in place:
    print(f"{x} -> {i}")  # Format: index -> place
    x += 1  # Increment the counter

# Loop through each character in the first place (place[0] = 'Dhaka')
for i in place[0]:
    print(i)

# Loop through each character in the fourth place (place[3] = 'Rajshahi')
for i in place[3]:
    print(i)

# List of numbers from 1 to 10
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop through each number in the list
for i in num:
    print("Number : ", i)

# Loop through each character in the string 'SAMSKULL'
for i in 'SAMSKULL':
    print(i)
