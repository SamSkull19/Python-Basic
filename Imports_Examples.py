# --------- Using 'import math' ---------
import math

# Must use 'math.' prefix to access functions/constants
print(math.sqrt(25))  # Output: 5.0
print(math.pi)        # Output: 3.141592653589793

# --------- Using 'from math import *' ---------
from math import *

# Can use functions/constants directly without 'math.' prefix
print(sqrt(25))  # Output: 5.0
print(pi)        # Output: 3.141592653589793

# --------- Using 'import random' ---------
import random

# Must use 'random.' prefix to access functions
print(random.randint(1, 10))       # Random int between 1 and 10
print(random.choice(['a', 'b', 'c']))  # Random choice from list

# --------- Using 'from random import *' ---------
from random import *

# Can use functions directly without 'random.' prefix
print(randint(1, 10))               # Random int between 1 and 10
print(choice(['a', 'b', 'c']))     # Random choice from list

# --------- Recommended usage ---------
# For clean and readable code, use one of the following:

# Import full module
import math
import random

print(math.sqrt(16))
print(random.randint(1, 5))

# Or import specific functions only
from math import sqrt, pi
from random import randint, choice

print(sqrt(16))
print(pi)
print(randint(1, 5))
print(choice(['x', 'y', 'z']))
