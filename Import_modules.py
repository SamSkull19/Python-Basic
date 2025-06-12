# Importing a specific function named 'incrementCounter' from another Python file (module)
from Local_Global_Scope import incrementCounter

# Importing all functions from the Key_Args_Parameter module
from Key_Args_Parameter import *

# Calling the imported 'incrementCounter' function with argument 10
num = incrementCounter(10)
print(num)

# Calling the imported 'myInfo' function with keyword arguments
info = myInfo(fname='Han', lname='Solo', Age=16, Live='Space')
print(info)
