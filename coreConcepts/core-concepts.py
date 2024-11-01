#!/usr/bin/env python
a = 248.1231238

# You can escape characters with \ so they get printed
print("variable \"a\" has a type of:", type(a))

x = 1+2j

print("variable \"x\" has a type of:", type(x))

print("addition:", 10+25)
print("subtraction:", 2-9)
print("multiplication:", 4*24)
print("division:", 72/6)
print("exponents:", 2**8)

print("The remainder (mod) of 19 and 5 is:", 19%5)

x = 10
y = 25

print("x =", x, "and y =", y)
print("x is greater than y:", x > y)
print("x is less than y:", x < y)
print("x is greater than or equal to y:", x >= y)
print("x is less than or equal to 10:", x <= 10)
print("y is equal to 27:", y == 27)
print("x is not equal to 11:", x != 11)

x = 5

print("x =", x)
x += 1
print("x += 1:", x)
x -= 2
print("x -= 2:", x)
x *= 4
print("x *= 4:", x)
x /= 2
print("x /= 2:", x)
x %= 3
print("x %= 3:", x)

a = "python"
b = "project"

print("Concatenation:", a + b)
print("Repetition:", a*2)

# Membership operator
print('project' in  a)

print("length of a:", len(a))

a = "hello, thank you for reading through my notes!"

# index starts from zero like most languages
print(a[9])

# Slicing is done like: string[start:stop]
print(a[7:16])

a = "hello, thank you for reading through my notes!"
b = "HELLO"
c = "hello"
d = "   hello   "

# Capitalize first letter
print(a.capitalize())

# Checks if string is alpha numeric or not
print(a.isalnum())

# Makes whole string lower case
print(b.lower())

# Makes whole string upper case
print(c.upper())

# Remove spaces at the beginning and at the end of the string
print(d.strip())
