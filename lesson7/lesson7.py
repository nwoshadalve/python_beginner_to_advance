#Python has four major built-in collections:
#list, tuple, set and dictionary.

#Lists are ordered, changeable, and allow duplicate elements.
#Tuples are ordered, unchangeable, and allow duplicate elements.
#Sets are unordered, unchangeable, and do not allow duplicate elements.
#dictionaries are ordered, changeable, and do not allow duplicate keys.

#Lists example:
#like dynamic arrays
fruits = ["apple", "banana", "orange"]
print("is 'banana' in the list?", "banana" in fruits)
print("list:", fruits)
print(fruits[0])
fruits[1] = "mango" #modifying an element in the list
print(fruits[1])
print(fruits[-1]) #negative indexing - accessing from end of the list
fruits.append("grape") #adding an element to the end of the list
fruits.insert(1, "kiwi") #inserting an element at a specific index
print(fruits)
fruits.remove("mango") #removing an element by value
fruits.pop() #removing the last element
fruits.pop(0) #removing an element by index
print(fruits)
print("length of the list:", len(fruits))
print("is 'banana' in the list?", "banana" in fruits)
print(type(fruits).__name__)

for fruit in fruits:
    print("Looping list: ",fruit)



#Tuple is similar to list but immutable.
#slightly faster than lists because of immutability
coordinates = (10, 20)
print(type(coordinates).__name__)
print("coordinates:", coordinates)
print("x coordinate:", coordinates[0])


# Sets are unordered, no duplicate values, and unindexed.
#useful for eliminating duplicates

unique_numbers = {1, 2, 3, 4, 5, 5, 6}
print(type(unique_numbers).__name__)
print("unique numbers:", unique_numbers)
unique_numbers.add(7) #adding an element to the set
print(unique_numbers)
unique_numbers.remove(3) #removing an element from the set
print(unique_numbers)
print("is 4 in the set?", 4 in unique_numbers)
unique_numbers.add(3)
# unique_numbers.clear() #removing all elements from the set
print(unique_numbers)



#Dictionary stores data in key-value pairs.
student = {
    "name" : "Nowshad",
    "age" : 25,
    "country" : "Bangladesh"
}

print(type(student).__name__)
print("student dictionary:", student)
print("student name:", student["name"])
student["age"] = 28
print("student age:", student["age"])
student["hobby"] = "coding" #adding a new key-value pair
student["city"] = "Dhaka"
print(student)
student.pop("city") #removing a key-value pair by key
print(student)

for key, value in student.items():
    print(key, value)


students = [
    {"name": "A", "age": 20},
    {"name": "B", "age": 21}
]

print(students[0]["name"])