targetNumber = 5

guess_count = 0

while guess_count < 3: 
    guess = int(input("Guess a Number: "))

    # Check if the user's guess matches the target number
    if guess == targetNumber:  
        print('You Won!')  # Inform the user they guessed correctly
        break  # Exit the loop since the game is won

    # Increment the guess counter after each incorrect guess
    guess_count += 1

# The `else` block is executed if the loop ends without a `break` (i.e., all guesses were incorrect)
else:
    print("Sorry, You Failed!")  # Inform the user they ran out of attempts
