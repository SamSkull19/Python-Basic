# Creating a set with duplicate values
numberSet = {12, 43, 34, 4, 2, 2, 2, 5, 65, 35, 34, 43, 12}
print(numberSet)  # Sets automatically remove duplicates

# Creating a list with duplicate values
numberList = [12, 43, 34, 4, 2, 2, 2, 5, 65, 35, 34, 43, 12]

# Converting the list to a set to remove duplicates
a = set(numberList)
print(a)  # Prints unique values from the list

# Adding new elements to the set
a.add(23)  # Adds 23 to the set
a.add(2)   # 2 already exists, so no change
a.add(65)  # 65 already exists, so no change
a.add(6)   # Adds 6 to the set
print(a)   # Prints the set after additions

# Removing elements from the set
a.remove(2)   # Removes 2 from the set
a.remove(65)  # Removes 65 from the set
print(a)      # Prints the set after removals

# Looping through the set elements
for i in a:
    print(i)  # Prints each element in the set

# Checking membership in the set
if 5 in a:
    print("Exist")  # Prints "Exist" if 5 is in the set

# Set operations
A = {1, 2, 3, 4, 5, 8}
B = {1, 2, 3, 4, 7, 9}

print(A & B)  # Intersection: elements common to both A and B
print(A | B)  # Union: all unique elements from A and B
