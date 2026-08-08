# Practice Question 1
# List Data Structure in Python
numbers = [1, 2, 3, 4, 5]
print(numbers) # prints the list

numbers.insert(5, 6) # inserts 6 at index 5
print(numbers) # prints the updated list

# Tuple Data Structure in Python
cities = ("Sialkot", "Lahore", "Daska", "Islamabad")
print(cities) # prints the tuple
print(cities[2]) # prints the third element of the tuple

# Set Data Structure in Python
set_1 = {1, 4, 7, 8, 10}
set_2 = {2, 4, 6, 8, 10}
print(set_1.intersection(set_2)) # prints the intersection of the two sets

# Dictionary Data Structure in Python
myself = {
    "name": "Usman",
    "age" : 19,
    "major": "Computer Science"
}
print(myself.keys()) # prints all the keys in the dictionary
print(myself.values()) # prints all the values in the dictionary
print(myself.items()) # prints all the key-value pairs in the dictionary