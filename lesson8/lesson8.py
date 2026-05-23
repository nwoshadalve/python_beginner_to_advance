#parameter: variable inside function definition
#argument: value passed to a function when calling it

# In python functions are first class objects.
# Can be stored in variable
# Passed to other function
# returned from functions


def greet():
    print("Hello!!!")

greet()

res = greet()
print(res) #print Hello!!! and None

def greet(name = "Guest"):
    print(f"Hello {name}!!!")

greet() #print Hello Guest!!!
greet("Nowshad") #print Hello Alice!!!

# explicitly specify parameter name

def introduce(name = "Guest", age = 300):
    print(f"Name: {name} Age: {age}")
    return
introduce(age = 28, name = "Nowshad")

# stored in variable
def greet():
    print("I am stored in x varaible!!!")
x = greet
x()

#Practice 1
def welcome():
    print("Welcome to Python")
welcome()

#Practice 2
def square(num):
    return num ** 2
print(square(5))

#Practice 3
def name_age_printer(name, age):
    print(f"My name is {name} and I am {age} years old")
name_age_printer("Nowshad", 28)

#Practice 4
def country(name = "Bangladesh"):
    print(name)
country()

#Practice 5
def calculator(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "sub":
        if num1 > num2:
            return num1 - num2
        else:
            num2 - num1
    elif operation == "mul":
        return num1 * num2
    else:
        return "Invalid operation"
    
print(calculator(3,5,"add"))
print(calculator(3,5,"sub"))
print(calculator(3,5,"mul"))

# Mini Chanllange:
def add(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def mul(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

def display(num1, num2, operation):
    if operation == "add":
        print(add(num1, num2))
    elif operation == "sub":
        print(sub(num1, num2))
    elif operation == "div":
        print(div(num1, num2))
    elif operation == "mul":
        print(mul(num1, num2))
    else:
        print("Invalid operation")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation(available: add, sub, mul, div): ")
display(num1, num2, operation)

#Q10
def is_even(num):
    return num%2 == 0
print(is_even(2))

#Q11
def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
print(f"Lagest number: {largest(7, 8, 9)}")

#Q12
def power(base, exponent=2):
    return base**exponent
power(5)
power(2,3)

#Q13
def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def mul(x, y):
    return x*y

def div(x, y):
    return x/y

print("Instructions: ")
print("You can perform addiotion, subtruction and divition between two numbers")
print("Please follor the format below")
print("x+y")
print("x-y")
print("x*y")
print("x/y")
print("Type exit to quit the program")

command = ""
while command != "exit":
    command = input("Enter operation: ")
    if command.__contains__(" "):
        print("Space is not allowed!!")
    elif command.__contains__("+"):
        splitor = command.split("+")
        print(add(int(splitor[0]), int(splitor[1])))
    elif command.__contains__("-"):
        splitor = command.split("-")
        print(sub(int(splitor[0]), int(splitor[1])))
    elif command.__contains__("*"):
        splitor = command.split("*")
        print(mul(int(splitor[0]), int(splitor[1])))
    elif command.__contains__("/"):
        splitor = command.split("/")
        print(div(int(splitor[0]), int(splitor[1])))
    elif command.__contains__("exit"):
        print("Closing program!!")

    else:
        print("Invalid operation!!")