import math
# This is exercise file to cover type conversions

# String literals in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello"
# You can assign a multiline string to a variable by using three quotes (single or double)
print(math)


example_1 = "hello world 1"
example_2 = 'hello world 2'
example_3 = """
hello
world"""
print(example_1 + ", " + example_2 + example_3)

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

# Example: Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])     # returns "e"

# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

# Example: Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])      # returns "llo"

# Negative Indexing
# Use negative indexes to start the slice from the end of the string.

# Example: Get the characters from position 5 to position 1 (not included), starting the count from the end of the string:
b = "Hello, World!"
print(b[-5:-2])     # returns "orl"

# String Length
# To get the length of a string, use the len() function.

# Example: The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))       # returns "13"

# String Methods

# Python has a set of built-in methods that you can use on strings.
# Note: All string methods returns new values. They do not change the original string.

# Example: The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())        # returns "hello, world!"

# For more detailed list of string methods, please visit: https://docs.python.org/3/library/stdtypes.html

# To check string if a certain phrase or character is present in a string, we can use the keywords "in" or "not in".


