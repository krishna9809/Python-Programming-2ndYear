# Functions in Python

# 1. Introduction:

# Functions are reusable blocks of code that perform specific tasks.
# They help organize code into manageable chunks, promote code reuse, and enhance readability.


# 2. Defining Functions:

# Functions are defined using the def keyword followed by the function name and parameters enclosed in parentheses.

# def greet(name):
#     print("Hello, " + name + "!")


# 3. Calling Functions:

# Functions are called by using their name followed by parentheses containing any required arguments.


# greet("Alice")  # Output: Hello, Alice!


# 4. Parameters and Arguments:

# Parameters are placeholders for data that the function expects to receive.
# Arguments are the actual values passed to the function when it is called.


# def add(x, y):
#     return x + y

# result = add(3, 5)
# print(result)  # Output: 8


# 5. Return Statement:

# The return statement allows a function to send data back to the caller.
# Functions can return one or more values.

# def square(x):
#     return x ** 2

# result = square(4)
# print(result)  # Output: 16


# 6. Default Parameters:

# Default parameters have predefined values and are used when no argument is provided.

# def greet(name="Guest"):
#     print("Hello, " + name + "!")

# greet()  # Output: Hello, Guest!
# greet("Alice")  # Output: Hello, Alice!



# 7. Lambda Functions:

# Lambda functions, also known as anonymous functions, are small, single-expression functions.
# They are defined using the lambda keyword and are often used for short, simple operations.


# double = lambda x: x * 2
# print(double(5))  # Output: 10


# 8. Recursion:

# Recursion is a technique in which a function calls itself to solve smaller instances of the same problem.


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# result = factorial(5)
# print(result)  # Output: 120



# 9. Key Points:

# Functions are essential building blocks of Python programs.
# They encapsulate logic, promote code reuse, and improve code organization.
# Understanding how to define, call, and work with functions is crucial for effective Python programming.