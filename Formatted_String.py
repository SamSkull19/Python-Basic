x = 60
y = 2

# Using f-string to format and print a sentence with the variables
print(f"I need {x} taka for {y} Days")  # Output: I need 60 taka for 2 Days

a = 10
b = 4

# Using f-string to calculate and print the result of a divided by b with 2 decimal precision
print(f"Result of {a} divided by {b} is {a / b : .2f}")  # Output: Result of 10 divided by 4 is 2.50

first = 'Sifat'
last = 'Samin'
country = "Bangladesh"

# Concatenating strings using '+' to create a full sentence
full_info = 'My name is ' + first + ' [ ' + last + ' ]. I am from ' + country + '.'
print(full_info)  # Output: My name is Sifat [ Samin ]. I am from Bangladesh.

# Using f-string for better readability and formatting
full_info_formatted = f'My name is {first} [ {last} ]. I am from {country}.'
print(full_info_formatted)  # Output: My name is Sifat [ Samin ]. I am from Bangladesh.

c = 10
d = 3

# Using f-string to calculate and format the result of c divided by d with 7 decimal precision
ans = f'Answer of C divided by D is: {c / d : 0.7f}'
print(ans)  # Output: Answer of C divided by D is: 3.3333333
