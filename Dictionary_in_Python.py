# Dictionary in Python
# Dictionaries are unordered collections of key-value pairs in Python.
# They are mutable, meaning you can add or remove key-value pairs from a dictionary after its creation.
# Dictionaries are defined using curly braces {} with key-value pairs separated by colons.

# Creating a dictionary
student ={
    "name": "Usman",
    "age": 19,
    "major": "Computer Science"
}
print(student) # prints the dictionary

print(student["age"]) # prints the value associated with the key "age"
print(student.get("major")) # prints the value associated with the key "major"
print(student.keys()) # prints all the keys in the dictionary
print(student.values()) # prints all the values in the dictionary
print(student.items()) # prints all the key-value pairs in the dictionary

# Dictionary Methods
student["age"] = 20 # updates the value associated with the key "age"
student["GPA"] = 2.8 # adds a new key-value pair to the dictionary
student.pop("major") # removes the key-value pair with the key "major"
print(student) # prints the updated dictionary

# Looping through a dictionary
for key, value in student.items():
    print(key, ":", value) # prints each key-value pair in the dictionary

    # Quick Summary of Data Structures in Python
# 1. List: Ordered, allows duplicate values, mutable
# 2. Tuple: Ordered, allows duplicate values, immutable
# 3. Set: Unordered, does not allow duplicate values, mutable
# 4. Dictionary: Unordered, stores key-value pairs, mutable