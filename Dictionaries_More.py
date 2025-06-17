# Creating a dictionary with person information
information = {
    "name": "SamSkull",
    "age": 24,
    "is_studying": True,
    "location": "Cumilla",
    "university": "SEC",
    "subject": "CSE"
}
print(information)  # Prints the whole dictionary

# Looping through dictionary items (key-value pairs)
for key, value in information.items():
    print(key, " : ", value)  # Prints each key with its value

# Deleting a key from the dictionary
del information['subject']  # Removes the 'subject' key
print(information)  # Prints updated dictionary

# Creating a dictionary using the dict() constructor
person = dict(
    name = "SamSkull",
    age = 24,
    is_studying = True,
    location = "Cumilla",
    university = "SEC",
    subject = "CSE"
)

print(person)  # Prints the new dictionary

# Removing and returning the last inserted key-value pair
key, value = person.popitem()  # Removes the last item: 'subject': 'CSE'
print(f"{key} : {value}")  # Prints the popped key and value
