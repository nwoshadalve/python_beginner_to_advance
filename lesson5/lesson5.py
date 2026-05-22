#Question 7
num = int(input("Enter a number: "))

if num > 0:
    if num%2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#Practice 1 
num = int(input("Enter a number: ")) 
if num > 0: print("Positive")
elif num < 0: print("Negative")
else: print("Zero") 

#Practice 2 
num = int(input("Enter a number: "))
if num%2 == 0: print("Even")
else: print("Odd")

#Practice 3 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1>num2: 
    print(num1)
else: 
    print(num2)

#Practice 4 
password = input("Enter password: ") 
if password == "admin": 
    print("Correct password") 

#Practice 5 
score = int(input("Enter score: "))
if score >= 80: 
    print("A+") 
elif score >= 70:
    print("A") 
elif score >= 60: 
    print("B") 
else: 
    print("Fail")


#Challange 
age = int(input("Enter age: ")) 
has_ticket = True
if age >= 18 and has_ticket: print("Allowed")
else: print("Not allowed")