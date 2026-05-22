#f-string in python is a way to format strings using expressions inside curly braces {}. It allows you to embed variables and expressions directly within a string, making it easier to create dynamic and readable output.

#Practice 1
name = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enyter your country: ")

print(f"My name is {name}. I am {age} years old. I live in {country}.")

#Practice 2
first_int = int(input("Enter first value: "))
second_int = int(input("Enter second value: "))

print(first_int+second_int)
print(first_int-second_int)
print(first_int*second_int)

#Practice 3
temperature_in_celsius = float(input("Enter temperature if celsius: "))

temperature_in_fahrenheit = (9/5) * temperature_in_celsius
temperature_in_fahrenheit += 32
print(f"Temperature is {temperature_in_fahrenheit} Fahremheit")

#Chellage
username = input("Enter your username: ")
favorite_number = int(input("Enter your favorite number: "))

print("Your username is " + username + " and your favorite number is " + str(favorite_number))

#Q6
username = input("Enter your username: ")
first_decimal = float(input("Enter first decimal number: "))
second_decimal = float(input("Enter second decimal number: "))

print(f"Your username is {username} and the sum of the two decimal numbers is {first_decimal + second_decimal}")