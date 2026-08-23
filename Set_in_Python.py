# Sets are unordered collections of unique elements in Python. 
# They are mutable, meaning you can add or remove elements from a set after its creation.
# Sets are defined using curly braces {} or the set() constructor.

# Creating a set
my_set = {1, 2, 4, 3, 4, 5}
print(my_set) # prints the set

# sets do not allow duplicate values that why sets are faster than lists and tuples
my_set.add(6) # adds 6 to the set
print(my_set) # prints the set after adding 6

my_set.remove(2) # removes 2 from the set
print(my_set) # prints the set after removing 2

#set opreations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) # prints the union of the two sets
print(set1.intersection(set2)) # prints the intersection of the two sets
print(set1.difference(set2)) # prints the difference of the two sets

