# for loop is usually used when we know how many times we want to repeat a block of code
# while loop is usually used when we don't know how many times we want to repeat a block of code

# range() generates numbers from 0 to n-1
#range(x) generates numbers from 0 to x-1
#range(x, y) generates numbers from x to y-1
#range(x, y, z) generates numbers from x to y-1 with a step of z
#range(x(5),y(0),z(-1)) generates numbers from 5 to 0 with a step of -1

for i in range(5):
    print(i+1, end=' ')
print("")

for i in range(1, 5):
    print(i, end=' ')
print("")

for i in range(1, 10, 2):
    print(i, end=' ')
print("")

for i in range(5, 0, -1):
    print(i, end=' ')
print("")

# In Python we can loop through string
for char in "Hello":
    print(char, end=' ')
print("")

# break immideately exits the loop
for i in range(10):
    if i == 5:
        break
    print(i, end=' ')
print("")

#conitune skips the rest of the code in the loop and goes to the next iteration
for i in range(10): 
    if i % 2 == 0:
        continue
    print(i, end=' ')
print("")

#pass measn do nathing but used as a placeholder when we need to write code but we don't want to write anything yet
for i in range(10):
    pass

#Practice 1
i = 1
while i <= 10:
    print(i, end=' ')
    i += 1
print("")

#Practice 2
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=' ')
print("")

#Practice 3
password = input("Enter the password: ")
while password != "python123":
    print("Wrong password, try again.")
    password = input("Enter the password: ")
print("Correct password, welcome!")

#Practice 4
for i in range (10):
    print("*" * i)

#Chellange
num = int(input("Enter a number: "))
for i in range(10):
    print(f"{num} x {i+1} = {num * (i+1)}")