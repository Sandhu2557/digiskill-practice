# four Data structures in python 
# 1. List allows duplicate values, is mutable
# 2. Tuple allows duplicate values, is immutable
# 3. Set does not allow duplicate values, is mutable
# 4. Dictionary stores key-value pairs, is mutable

# List

fruits = ["apple","banana", "mango", "orange", "banana"]

print(fruits[-1]) # prints last element of the list

print(fruits[1:4]) # prints elements from index 1 to 3

fruits.append("grapes") # adds grapes to the end of the list
for fruit in fruits:
    print(fruit) # prints all the elements of the list

fruits.remove("banana") # removes the first occurrence of banana from the list
print(fruits) # prints the list after removing banana

fruits.sort() # sorts the list in ascending order
print(fruits) # prints the sorted list

fruits.pop() # removes the last element from the list
print(fruits) # prints the list after popping the last element

fruits.insert(1, "kiwi") # inserts kiwi at index 1
print(fruits) # prints the list after inserting kiwi

for fruit in fruits:
    print(fruit) # prints all the elements of the list after modifications