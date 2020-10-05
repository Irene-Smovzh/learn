# This is an excercise file to cover Python Data Types

# Built-in Data Types
print("""Python has the following data types built-in by default, in these categories: 
    Text Type =	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview """)

# Setting the Data Type
print("In Python, the data type is set when you assign a value to a variable. Example:")

# str - string
a = "Hello world"
print(type(a), a)

# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
b = 20
print(type(b), b)

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
# Float can also be scientific numbers with an "e" to indicate the power of 10.
c = 20.5
print(type(c), c)

# Complex numbers are written with a "j" as the imaginary part
d = 1j
print(type(d), d)

# list
e = ["apple", "banana", "cherry"]
print(type(e), e)

# tuple
f = ("apple", "banana", "cherry")
print(type(f), f)

# range
g = range(6)
print(type(g), g)

# dict
h = {"name" : "John", "age" : 36}
print(type(h), h)

# set
i = {"apple", "banana", "cherry"}
print(type(i), i)

# frozenset
j = frozenset({"apple", "banana", "cherry"})
print(type(j), j)

# bool
k = True
print(type(k), k)

# bytes
l = b"Hello"
print(type(l), l)

# bytearray
m = bytearray(5)
print(type(m), m)

# memoryview
n = memoryview(bytes(5))
print(type(n), n)

