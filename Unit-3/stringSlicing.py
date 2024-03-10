# # 1. Basic

# message = "Hello, World!"
# print(message[2:6])  # Output: "llo,"


# # 2. Omitting Start or End

# # If you omit the start parameter, the slice starts from the beginning of the string.
# # If you omit the end parameter, the slice extends to the end of the string.

# message = "Hello, World!"
# print(message[:5])  # Output: "Hello"
# print(message[7:])  # Output: "World!"


# 3. Negative Indices
# # Negative indices count from the end of the string.
# # Slicing with negative indices allows you to extract substrings from the end of the string.

# message = "Hello, World!"
# print(message[-6:-1])  # Output: "World"


# 4. Step Parameter
# # The step parameter specifies how many characters to skip between each character included in the slice.

# message = "Hello, World!"
# print(message[::2])  # Output: "HloWrd"


# 5. Reversing a String

# message = "Hello, World!"
# print(message[::-1])  # Output: "!dlroW ,olleH"
