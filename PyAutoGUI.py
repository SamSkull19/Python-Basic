import pyautogui      # Import pyautogui for automating keyboard and mouse actions
from time import sleep  # Import sleep function to add delays

sleep(3)  # Wait for 3 seconds before starting (gives you time to focus on the input field)

# Loop 5 times to write "Hello World!" and press Enter after each
for i in range(5):
    pyautogui.write("Hello World! ", interval=0.25)  # Type "Hello World!" with 0.25 seconds delay between each character
    pyautogui.press("enter")                          # Press the Enter key to send the message or move to the next line

sleep(2)  # Wait for 2 seconds before sending the next message

# Multi-line text to be typed out
texts = """Hey there, I am Samin. How are you doing? Are you feeling okay? What is your study update? When will you graduate?"""

# Type out the multi-line text with 0.25 seconds delay between each character
pyautogui.write(texts, interval=0.25)

pyautogui.press('enter')  # Press Enter key after typing the message
