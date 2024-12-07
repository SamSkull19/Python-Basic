import math

# Using ceil() to get the smallest integer greater than or equal to 'a'
a = 3.45
print(math.ceil(a))  # Output: 4

# Using floor() to get the largest integer less than or equal to 'a'
print(math.floor(a))  # Output: 3

# Using pow() to calculate b raised to the power of 2
b = 5
print(math.pow(b, 2))  # Output: 25.0

# Using sqrt() to calculate the square root of c
c = 16
print(math.sqrt(c))  # Output: 4.0

# Using log() to calculate the logarithm of d with base 2
d = 8
print(math.log(d, 2))  # Output: 3.0 (log base 2 of 8)

# Using log10() to calculate the logarithm of e with base 10
e = 10
print(math.log10(e))  # Output: 1.0 (log base 10 of 10)

# Using radians() to convert degrees to radians, then calculating the sine of f (in radians)
f = 90
rad_f = math.radians(f)
print(math.sin(rad_f))  # Output: 1.0 (sine of 90 degrees)

# Using radians() to convert degrees to radians, then calculating the cosine of g (in radians)
g = 0
rad_g = math.radians(g)
print(math.cos(rad_g))  # Output: 1.0 (cosine of 0 degrees)

# Using radians() to convert degrees to radians, then calculating the tangent of h (in radians)
h = 45
rad_h = math.radians(h)
print(math.tan(rad_h))  # Output: 1.0 (tangent of 45 degrees)

# Using factorial() to calculate the factorial of x
x = 5
print(math.factorial(x))  # Output: 120 (5! = 5 * 4 * 3 * 2 * 1)
