# Dictionary


# a. Adding Items:

# New key-value pairs can be added to a dictionary using assignment.

# person = {"name": "Alice", "age": 30}
# person["city"] = "New York"


# b. Removing Items:

# Items can be removed from a dictionary using the del keyword or the pop() method.

# person = {"name": "Alice", "age": 30, "city": "New York"}
# del person["age"]
# person.pop("city")


# Dictionary Methods:

# a. keys():

# The keys() method returns a view of all keys in the dictionary.

# person = {"name": "Alice", "age": 30, "city": "New York"}
# print(person.keys())  # Output: dict_keys(['name', 'age', 'city'])


# b. values():

# The values() method returns a view of all values in the dictionary.

# person = {"name": "Alice", "age": 30, "city": "New York"}
# print(person.values())  # Output: dict_values(['Alice', 30, 'New York'])


# c. items():

# The items() method returns a view of all key-value pairs in the dictionary as tuples.

# person = {"name": "Alice", "age": 30, "city": "New York"}
# print(person.items())  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])


#  Key Points:

# Dictionaries are versatile data structures used to store key-value pairs.
# They offer fast and efficient lookup capabilities, making them ideal for various programming tasks in Python.