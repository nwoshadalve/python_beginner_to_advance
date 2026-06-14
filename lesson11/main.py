# Lesson 11 Practice

# Do not answer now. Complete these on your own first.

# Task 1

# Create a file named student.txt and write your name into it.

file = open("student.txt", "x")
file.write("Nowshad")
file.close()

# Task 2

# Read the contents of student.txt and print them.

file = open("student.txt", "r")
content = file.read()
print(content)
file.close()

# Task 3

# Create a program that asks the user for 3 favorite programming languages and stores them in a file.

for i in range(3):
    language = input("Enter your favorite programming language: ")
    with open("languages.txt", "a") as file:
        file.write(language + "\n")
    if i == 2:
        print("Closing file")
        file.close()

# Task 4

# Read a file line-by-line using a for loop.

with open("languages.txt", "r") as file:
    for line in file:
        print(line.strip())
file.close()

# Task 5

# Create a simple notes application that:

# Takes user input
# Appends it to notes.txt
# Displays all notes afterward

note = input("Enter a note: ")
with open("notes.txt", "a") as file:
    file.write(note + "\n")
    file.close()

with open("notes.txt", "r") as file:
    print(file.read())
    file.close()

# Question 7

user_name = input("Enter username: ")

with open("users.txt", "a") as file:
    file.write(user_name + "\n")

with open("user.txt", "r") as file:
    print(file.read())