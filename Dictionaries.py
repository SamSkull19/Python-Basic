# Define a dictionary with keys and values
information = {
    "name": "SamSkull",
    "age": 24,
    "is_studying": True,
    "location": "Cumilla"
}

# Print the entire dictionary
print(information)

# Access and print the value associated with the key 'location'
print(information['location'])

# Access and print the value associated with the key 'age'
print(information['age'])

# Use the get() method to retrieve the value associated with the key 'name'
print(information.get('name'))

# Try to get a value for a key ('subject') that does not exist, returns None
print(information.get('subject'))

# Use the get() method with a default value, if the key ('subject') does not exist
print(information.get('subject', 'CSE'))

# Update the value of the key 'name' to 'NeffRoxx'
information['name'] = 'NeffRoxx'
print(information)

# Add a new key-value pair ('subject': 'CSE') to the dictionary
information['subject'] = 'CSE'
print(information)

# Get and print all the keys of the dictionary
print(information.keys())

# Get and print all the values of the dictionary
print(information.values())
