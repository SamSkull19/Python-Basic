command = ""
# Initialize a flag to track whether the car is started or not
is_Started = False

# Infinite loop to continuously accept commands from the user
while True:
    command = input("> ").lower()

    if command == "start":  # Check if the command is "start"
        if is_Started:  # If the car is already started
            print("Car is already started!") 

        else:
            is_Started = True  # Update the flag to indicate the car is started
            print("Car Started...") 

    elif command == "stop":  # Check if the command is "stop"
        if not is_Started:  # If the car is already stopped
            print("Car is already stopped!")

        else:
            is_Started = False  # Update the flag to indicate the car is stopped
            print("Car Stopped.") 

    elif command == "help":  # Check if the command is "help"
        # Display the list of available commands
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)

    elif command == "quit":  # Check if the command is "quit"
        break  # Exit the loop to end the program

    else:
        # Inform the user that the entered command is not recognized
        print("Sorry, I don't understand that!")
