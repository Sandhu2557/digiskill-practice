# Tuple Ordered Data Structure(also allows duplicate values but cannot be modified after creation)

countries = ("India", "USA", "UK", "Australia", "Canada")
print(countries)

print(countries[0]) # prints the first element of the tuple

# Tuple properties
# 1. Ordered
# 2. Allows duplicate values
# 3. Immutable

# countries[0] = "Germany" # This will raise an error because tuples are immutable

countries_list = list(countries) # converting tuple to list to modify
countries_list[0] = "Germany" # modifying the first element of the list
countries = tuple(countries_list) # converting the list back to tuple
print(countries) # prints the modified tuple

numbers = (1,2,3,4,2,3,1) # tuple with duplicate values
print(numbers.count(2)) # prints the count of occurrences of 2 in the tuple
print(numbers.index(3)) # prints the index of the first occurrence of 3 in the tuple
