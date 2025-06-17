# Define a multi-line string
texts = """Hey there, I am Samin. How are you doing? Are you feeling okay? What is your study update? When will you graduate? """

# Open (or create) a file named 'myFile.txt' in write mode ('w')
# Writing the 'texts' string into the file (this overwrites existing content)
with open('myFile.txt', 'w') as file:
    file.write(texts)

# Open the same file in append mode ('a')
# Add another string at the end of the file without deleting previous content
with open('myFile.txt', 'a') as file:
    file.write("Careful, what you want to do next! ")

# Open the file in read mode ('r') to read the entire content
with open('myFile.txt', 'r') as file:
    texts = file.read()  # Read the content of the file into the variable 'texts'
    print(texts)         # Print the content to the console
