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

x = [20, 30, "hello", "world", 12.25]

print("x type:", type(x), "x contains:", x)

x = [10, 20]
y = ['hello', 'world']

print("Concate:", x + y)
print("Repetition:", x * 3)
print("10 in x:", 10 in x)
print(len(x))
print("First index in x:", x[0])
print("Slice of x and y:", (x+y)[0:3])

# Append
x.append(42)
print("append 42 to x:", x)

# Remove
x.remove(20)
print("remove 20 from x:", x)

tup = (10, 20, 'welcome', 'mlops', 12.567)

print(type(tup))
print(tup)

print("Concate:", tup + tup)
print("Repetition:", tup * 2)

print("Index 2:", tup[2])
print("Slice:", tup[0:3])

x = {'number': 9000, "name": "john", 'age': 25, 'city': 'New York'}

print(x)
print("Name:", x['name'])

x['age'] = 55
print("New Age:", x['age'])

print(len(x))
print(x.keys())
print(x.values())
print(x.items())

m = {10, 20, 30, "hello", "welcome", 100, 100, "hi"}

print("Notice how the order changes:", m)
print("Also notice how there was only one instance of 100")

print(len(m))
print("hi" in m)

x = 3.14

x = int(x)
print("Cast x to int:", x, "type:", type(x))
x = float(x)
print("Recast x to float", x, "type:", type(x))
x = str(x)
print("Cast x to string", x, "type:", type(x))

x = 10

if x > 0:
    print("x is greater than 0")

x = -10
if x > 0:
    print("x is greater than 0")
elif x == 0:
    print("x is equal to 0")
else:
    print("x is less than 0")

fruits = ["apple", 'banana', 'cherry']

print("For Loop:")
for i in fruits:
    print("Fruit:", i)

count = 0

print("\nWhile Loop:")
while count < 3:
    print(count)
    count += 1

for i in fruits:
    print("Fruit:", i)
    if i == "banana":
        break

for i in fruits:
    if i == 'apple':
        continue
    print("Fruit:", i)

x = [1, 2, 3, 4, 5, 6, 7, 8]

results = [i**2 for i in x]

print(results)

def greet(name):
    print(f"Hello {name}!")

greet("Maker")

def add_numbers(a, b):
    result = a + b
    return result

x = add_numbers(5, 12)

print(x)

def sub_numbers(a, b=1):
    result = a - b
    return result

x = sub_numbers(10)

print(x)
