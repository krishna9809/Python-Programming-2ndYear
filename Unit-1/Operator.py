# Operator => Operators are used to perform operations on variables and values.

# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Bitwise operators


# Python Arithmetic Operators

# Arithmetic operators are used with numeric values to perform common mathematical operations:

# +	    Addition	            x + y	
# - 	Subtraction           	x - y	
# * 	Multiplication       	x * y	
# /  	Division	            x / y	
# %	    Modulus	                x % y	
# **	Exponentiation	        x ** y	
# //	Floor division	        x // y


# print(2+3)

# a = 4
# b = 2
# print(a+b)
# print(a-b)
# print(a/b)
# print(a*b)
# print(a**b)
# print(a//b)
# print(a%b)





# Python Assignment Operators

# Assignment operators are used to assign values to variables:
 
# =	             x = 5	             x = 5	
# +=	            x += 3	             x = x + 3	
# -=	            x -= 3	             x = x - 3	
# *=	            x *= 3	             x = x * 3	
# /=	            x /= 3	             x = x / 3	
# %=	            x %= 3	             x = x % 3	
# //=	            x //= 3	             x = x // 3



# Python Comparison Operators

# Comparison operators are used to compare two values:


# ==	         Equal	                          x == y	
# !=	         Not equal	                      x != y	
# >	             Greater than                     x > y	
# <	             Less than	                      x < y	
# >=	         Greater than or equal to	      x >= y	
# <=	         Less than or equal to	          x <= y


# a = 4
# b = 2

# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)




# Python Logical Operators

# Logical operators are used to combine conditional statements:



# and 	      Returns True if both statements are true	                        x < 5 and  x < 10	
# or	      Returns True if one of the statements is true	                    x < 5 or x < 4	

# not	      Reverse the result, returns False if the result is true 	        not(x < 5 and x < 10)

# a = 2

# print(a<1 and a<10)
# print(not(a<1 or a<10))


# Python Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:
    

'''& 	AND
     	Sets each bit to 1 if both bits are 1                                              x & y	

   |	OR
       	Sets each bit to 1 if one of two bits is 1                                         x | y	

   ^	XOR	
        Sets each bit to 1 if only one of two bits is 1	                                   x ^ y	

   ~	NOT	
        Inverts all the bits	                                                            ~x	

   <<	Zero fill left shift 
        Shift left by pushing zeros in from the right                                       x << 2	
        and let the leftmost bits fall off	
   >>	Signed right shift
        Shift right by pushing copies of the leftmost
        bit in from the left, and let the rightmost bits
        fall off	                                                                         x >> 2'''



# 5 -> 1 0 1 
# 7 -> 1 1 1

a = 5
b = 7
c = 3

print(a&b)
print(a|b)
print(a^b)
print(~c)







"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""