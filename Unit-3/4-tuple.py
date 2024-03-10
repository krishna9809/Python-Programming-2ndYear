# a. Immutable Nature:

# Once a tuple is created, its elements cannot be modified, added, or removed.

# coordinates = (10, 20)
# coordinates[0] = 5  # This will raise a TypeError



# b. Tuple Unpacking:

# Tuple unpacking allows you to assign the elements of a tuple to separate variables.

# coordinates = (10, 20)
# x, y = coordinates
# print(x, y)  # Output: 10 20



# c. Length and Membership Test:

# The len() function returns the length of a tuple, i.e., the number of elements it contains.
# The in and not in operators are used to test for membership in a tuple.

# fruits = ('apple', 'banana', 'orange')
# print(len(fruits))  # Output: 3
# print('banana' in fruits)  # Output: True



# Key Points:

# Tuples provide a lightweight data structure for storing collections of items.
# They are commonly used for representing fixed collections of data, such as coordinates, database records, or function return values.
# While tuples are immutable, they can contain mutable objects such as lists.


# Ques. Write a Python Program to add an item in a tuple (2021-22)

# tuplex = (2,3,4,5);
# # Convert the tuple to a list.
# listx = list(tuplex)
# # Use different methods to add items to the list.
# listx.append(30)
# # Convert the modified list back to a tuple to obtain 'tuplex' with the added element.
# tuplex = tuple(listx)
# # Print the final 'tuplex' tuple with the added element
# print(tuplex) 