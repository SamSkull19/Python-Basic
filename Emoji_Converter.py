# Prompt the user to input a message
message = input(">")

# Split the input message into a list of words based on spaces
words = message.split(' ')

# Define a dictionary mapping text-based emoticons to their emoji equivalents
emoji = {
    ":)" : "😊",     # Smiley face
    ":D" : "😃",     # Grinning face
    ":(" : "☹️",    # Sad face
    ":X" : "🤐",     # Zipped mouth
    "XD" : "😝",     # Laughing face with tongue
    "X(" : "😫",     # Tired or stressed face
    ":/" : "🫤",     # Skeptical face
    ":3" : "🥴",     # Woozy face
    "-_-" : "😑",    # Expressionless face
    ":o" : "😯",     # Surprised face
}

s = ""

# Iterate over each word in the input message
for word in words:
    # Replace the word with its emoji equivalent if it exists in the dictionary
    # Otherwise, keep the original word
    s += emoji.get(word, word) + " "

print(s)
