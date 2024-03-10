# 1. Write a Python Program to change a given string to a new string where the first and last chars have been exchanged
# - (2021-22) 


# Define a function named change_string that takes one argument, 'str1'.
# def change_string(str1):
#     # Return a modified version of the input string 'str1' by rearranging its characters.
#     # It takes the last character and moves it to the front, while keeping the middle characters unchanged.
#     return str1[-1:] + str1[1:-1] + str1[:1]

# # Call the change_string function with different input strings and print the results.
# print(change_string('krishna'))   # Output: 'dbca'
# # print(change_string('12345'))  # Output: '52341'




# 2. Write a Python Program, triangle(N), that prints a right triangle having base and height consisting of N * symbols as  shown in these examples. - (2020-21)

# trianlge(3)
# *
# * * 
# * * *

# # triangle(4)
# *
# * *
# * * * 
# * * * *
# * * * * * 


def triangle(n):
  for n in range(1, n+1):

    for n in range(1, n + 1):
        print("*", end=" ")
    print("")

triangle(15)
