# Assigning the name of the country to the variable
country_name = "My Country name is Bangladesh"

# Printing the entire string using slicing
print(country_name[:])  # Output: My Country name is Bangladesh

# Printing characters from index 2 to 9 (inclusive of start, exclusive of end)
print(country_name[2:10])  # Output: Country 

# Printing characters from index 19 to the end
print(country_name[19:])  # Output: Bangladesh

# Printing the last character of the string
print(country_name[-1])  # Output: h

# Printing the second last character of the string
print(country_name[-2])  # Output: s

# Printing the third last character of the string
print(country_name[-3])  # Output: e

# Printing the 12th last character of the string
print(country_name[-12])  # Output: i

# Printing the first character of the string
print(country_name[0])  # Output: M

# Printing all characters except the last 11
print(country_name[:-11])  # Output: My Country name 

# Printing characters from the start up to index 17
print(country_name[:18])  # Output: My Country name is

# Assigning the entire string to another variable and printing it
another = country_name[:]
print(another)  # Output: My Country name is Bangladesh

# Printing characters from index 1 (2nd character) to the second last character
print(another[1:-1])  # Output: y Country name is Banglades