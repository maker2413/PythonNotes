#!/usr/bin/env python
class MyClass:
    # Class variable
    class_variable = "I am a class variable"

    # Constructor (initializer) method
    def __init__(self, attribute1, attribute2):
        # Instance variables
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def display_attributes(self):
        print(f"Attribute 1: {self.attribute1}")
        print(f"Attribute 2: {self.attribute2}")

    def modify_attributes(self, new_value1, new_value2):
        self.attribute1 = new_value1
        self.attribute2 = new_value2

# Creating objects
obj1 = MyClass("Value1", "Value2")
obj2 = MyClass("AnotherValue1", "AnotherValue2")

# Accessing attributes and methods
print(obj1.attribute1)
obj2.display_attributes()

# Modifying attributes
obj1.modify_attributes("NewValue1", "NewValue2")
obj1.display_attributes()
