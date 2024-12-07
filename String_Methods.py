text = "Try not to get LOST inside your messy life"

# Printing the length of the string
print(len(text))  # Output: 41

# Converting the string to uppercase and printing it
upper_text = text.upper()
print(upper_text)  # Output: TRY NOT TO GET LOST INSIDE YOUR MESSY LIFE
print(upper_text.isupper())  # Checking if the text is in uppercase (True)

# Converting the string to lowercase and printing it
lower_text = text.lower()
print(lower_text)  # Output: try not to get lost inside your messy life
print(lower_text.islower())  # Checking if the text is in lowercase (True)

# Converting the string to title case (first letter of each word capitalized) and printing it
title_text = text.title()
print(title_text)  # Output: Try Not To Get Lost Inside Your Messy Life

# Finding the index of the word "lost" in the string (case-sensitive)
find_text = text.find("lost")
print(find_text)  # Output: -1 (not found because it's case-sensitive)

# Finding the index of the character 'g' in the string
find_text_char = text.find('g')
print(find_text_char)  # Output: -1 (character 'g' is not in the string)

# Finding the index of the character 'x' in the string (does not exist)
find_text_char2 = text.find('x')
print(find_text_char2)  # Output: -1 (indicates 'x' is not in the string)

# Replacing the word 'messy' with 'hazy' and printing the result
replace_text = text.replace('messy', 'hazy')
print(replace_text)  # Output: Try not to get LOST inside your hazy life

# Replacing 'Messy' (case-sensitive) with 'hazy' (does not match)
replace_text2 = text.replace('Messy', 'hazy')
print(replace_text2)  # Output: Try not to get LOST inside your messy life

# Checking if the word 'inside' is in the string
in_check = 'inside' in text
print(in_check)  # Output: True

# Checking if the character 'x' is in the string
in_check_2 = 'x' in text
print(in_check_2)  # Output: False

# Swapping the case of all characters in the string
swap_text = text.swapcase()
print(swap_text)  # Output: tRY NOT TO GET lost INSIDE YOUR MESSY LIFE

# Counting the number of occurrences of 'e' in the string
count_text = text.count('e')
print(count_text)  # Output: 5

# Splitting the string into a list of words (default delimiter is space)
split_text = text.split()
print(split_text)  # Output: ['Try', 'not', 'to', 'get', 'LOST', 'inside', 'your', 'messy', 'life']

# Splitting the string using a custom delimiter (does not exist in the string)
split_text2 = text.split("{}")
print(split_text2)  # Output: ['Try not to get LOST inside your messy life'] (no split occurs)
