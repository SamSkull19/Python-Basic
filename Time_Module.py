import time  # Importing the time module

# Get the current time in seconds since the Unix Epoch (January 1, 1970)
print(time.time())  # Output: Floating-point number representing current timestamp

# Demonstrating time delay using sleep
print("Start")
time.sleep(2)  # Pauses the program for 2 seconds
print("End")

# Measuring execution time of a loop
start = time.time()  # Record start time
for i in range(1000):  # Dummy loop
    pass
end = time.time()  # Record end time

print("Execution time:", end - start, "seconds")  # Calculate and print time taken by loop

# Get the current time as a human-readable string
currentTime = time.ctime()
print(currentTime)  # Example Output: 'Tue Jun 17 00:45:12 2025'

# Formatting local time into a custom string
t = time.localtime()  # Get the current local time as a struct_time
ft = time.strftime("%Y-%m-%d %H:%M:%S", t)  # Format it into a readable string
print(f"Formatted Time : {ft}")

# Convert struct_time back to timestamp (seconds since epoch)
t = time.localtime()  # Again get the current local time
print(time.mktime(t))  # Output: timestamp (float)
