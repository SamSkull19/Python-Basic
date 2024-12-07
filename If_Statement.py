is_Playable = input("Enter True or False : ")

# Checking if the input is 'True'. If so, set is_Playable to True, else set it to False
if is_Playable == 'True':
    is_Playable = True
else:
    is_Playable = False

# Printing a message based on the value of is_Playable
if is_Playable:
    print("Gather People To have a Match")  # If True, message to gather people
else:
    print("Dont need to call anyone")  # If False, no need to gather people

n = input("Enter a Number : ")

# Converting the input to an integer
n = int(n)

# Checking if the number is even or odd using modulus operation
if n % 2 == 0:  
    print(f'{n} is Even')  # Print the result if even
else:
    print(f'{n} is Odd')  # Print the result if odd
