# Types of variables in Python
# 1. String
# 2. Integer
# 3. Float
# 4. Boolean

a = 5
b = 6.565
c = True
d = "Hello, World!"

## type() returns object type of the variable
## type().__name__ returns the name of the type as a string
print("Type of a: ", type(a).__name__)
print("Type of b: ", type(b).__name__)
print("Type of c: ", type(c).__name__)
print("Type of d: ", type(d).__name__)

def print_separator():
    for i in range(1, 50):
        print("-", end="")
    print("")

print_separator()

## input() retuns string
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello ", name)
print("Next year you will be ", age +1, " years old.")