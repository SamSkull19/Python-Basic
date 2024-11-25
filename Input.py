name = input("What is your name? ")
print("My name is ", name);
print('\n')

place = input("Where do you live? ")
print("I live in "+ place);
print('\n')

print(name + " likes " + place)
print('\n')

# input() in Python always returns a string thats why use type conversion
x = int(input("Enter a number: ")) 
print(x*x)