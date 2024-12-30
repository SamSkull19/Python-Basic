number = {
    0: 'Zero',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine'
}

num = input("Phone : ")
s = ""

# Iterate over each character in the input string
for i in num:
    # Convert the character to an integer to use as a key in the dictionary
    x = int(i)
    s += number[x] + " "

print(s)
