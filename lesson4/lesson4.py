#Question 12
username = input("Enter username: ")
password = input("Enter password: ")

print(username == "admin" and password == "python123")

#Question 11:
num = int(input("Enter a number: "))
if (num % 2 == 0):
    print("Even.")
else:
    print("Odd.")


#Practice 1 
a = 10
b = 5 
print(a+b) 
print(a-b)
print(a*b)
print(a/b) # a/b will result in a float value
print(a//b) # a//b will result in an integer value (floor division)

#Practice 2 
num1 = int(input("Enter number 1: ")) 
num2 = int(input("Enter number 2: ")) 
print("Remainder: ", num1%num2) 
print("Power: ", num1**num2) 

#Practice 3 
num = 3 
print(num%2 == 0) 

#Practice 4 

saved_username = "admin" 
saved_password = "1234" 
username = input("Enter username: ") 
password = input("Enter password: ") 
print(saved_username == username and saved_password == password)