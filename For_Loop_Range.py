# Loop from 0 to 9 (range(10) generates numbers from 0 up to, but not including, 10)
for i in range(10):
    print(i)

# Loop from 3 to 10 (range(3, 11) generates numbers starting at 3 and ending before 11)
for i in range(3, 11):
    print(i)

# Loop from 10 to 100 in steps of 10 (range(10, 101, 10) generates numbers from 10 to 100 with a step of 10)
for i in range(10, 101, 10):
    print(i)

# List of places
place = ['Dhaka', 'Cumilla', 'Sylhet', 'Rajshahi']

# Iterate through the indices of the 'place' list using range(len(place))
for i in range(len(place)):  
    # Access each element by its index and print a message
    print(f"I am from {place[i]}")

# List of fruits
fruits = ['Apple', 'Banana', 'Cherry', 'Date']

# Iterate through the indices of the 'fruits' list using range(len(fruits))
for i in range(len(fruits)):
    # Access each fruit by its index and print a message
    print(f"Fruit name is {fruits[i]}")
