# list[start : stop : step]

# Define a list of numbers
number = [4, 3, 9, 10, 1, 19, 15, 20, 18, 17, 13, 6, 7, 11, 14, 16, 12, 5, 2, 8]

# 1️⃣ Reverse the entire list
print(number[ : :-1])
# Explanation: start = end, stop = start, step = -1 → full reverse
# Output: [8, 2, 5, 12, 16, 14, 11, 7, 6, 13, 17, 18, 20, 15, 19, 1, 10, 9, 3, 4]

# 2️⃣ Reverse every second element
print(number[ : :-2])
# Explanation: start = end, step = -2 → every 2nd item in reverse
# Output: [8, 5, 16, 11, 6, 17, 20, 19, 10, 3]

# 3️⃣ From index 2 to 10 (excluded), every second element
print(number[2 : 11: 2])
# Explanation: index 2 = 9, index 4 = 1, 6 = 15, 8 = 18, 10 = 13
# Output: [9, 1, 15, 18, 13]

# 4️⃣ From index 12 to index 1 (excluded), every 3rd element in reverse
print(number[12 : 1: -3])
# Explanation: indices 12 = 7, 9, 6, 3
# Output: [7, 17, 20, 10]

# 5️⃣ Invalid slicing: from start to index 5 (excluded) with step -1
print(number[ : 5: -1])
# Explanation: This won't work because direction and range conflict (nothing will be returned)
# Output: []

# 6️⃣ From index 13 to start in reverse
print(number[13 : : -1])
# Explanation: Starts from index 13 (value = 11), steps back to index 0
# Output: [11, 7, 6, 13, 17, 18, 20, 15, 19, 1, 10, 9, 3, 4]
