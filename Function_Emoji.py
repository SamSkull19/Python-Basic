# Function to convert text containing emoji symbols into their corresponding emoji characters
def emoji_converter(words):
    # Dictionary mapping text-based emoji symbols to actual emoji characters
    emoji = {
        ":)" : "😊",     # Smiley face
        ":D" : "😃",     # Grinning face
        ":(" : "☹️",     # Sad face
        ":X" : "🤐",     # Zipped mouth
        "XD" : "😝",     # Laughing face with tongue
        "X(" : "😫",     # Tired or stressed face
        ":/" : "🫤",     # Skeptical face
        ":3" : "🥴",     # Woozy face
        "-_-" : "😑",    # Expressionless face
        ":o" : "😯",     # Surprised face
    }

    output = ""
    # Loop through each word in the input list
    for word in words:
        # Use the dictionary to get the corresponding emoji or keep the word unchanged if not found
        output += emoji.get(word, word)

    return output  # Return the converted text

# Prompt the user for input containing emoji symbols
texts = input("> ")  # Example input: ":) XD :o -_-"

# Split the input text into individual words and pass to the emoji_converter function
converted = emoji_converter(texts.split(' '))

# Print the converted text with emojis
print(converted)
