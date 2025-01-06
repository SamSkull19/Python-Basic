try:
    # Take user input for age and try to convert it to an integer
    age = int(input("Age : "))
    print(age)

    # Perform a division operation (this might raise ZeroDivisionError)
    x = 1000
    ans = x / age
    print(ans)

# Handle ValueError if input cannot be converted to an integer
except ValueError:
    print("Invalid Number")

# Handle ZeroDivisionError if age is 0 (division by zero)
except ZeroDivisionError:
    print("Age can not be 0")

# Handle a general exception (catches any unhandled errors)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
