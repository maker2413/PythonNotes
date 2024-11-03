#!/usr/bin/env python
print("hello")

# \n is for newlines
print("hello \nworld!")

# \t is for tabs
print("hello \tworld!")

# \\ will escape the backslash character
print("hello \\world!")

u = input("Enter the value to store: ")

print("output is:", u)

u = int(input("Enter a number: "))

example_text = """This file was created with python.
all of the contents of this file are defined in
the same Python program.
"""

fileobj = open("example.txt", "wt")
fileobj.write(example_text)
fileobj.close()

fileobj = open("example.txt", "rt")
data = fileobj.read()
fileobj.close()

print(data)
