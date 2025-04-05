# Integers / Flats
# Operator	Name	                Example
# +	        Addition	            x + y	
# -	        Subtraction	            x - y	
# *	        Multiplication	        x * y	
# /	        Division	            x / y	
# %	        Modulus	                x % y	
# **        Exponentiation	        x ** y	
# //       	Floor division	        x // y
# plus-equals operator    +=

# -------------------------------------------------------------------------
# Type casting in Python : changing string to int, int to float etc.

number = -1.123
print(type(number))                         # prints type of the variable i.e number which is float

# # convert float to integer:
number = 99.95                              # float value
number = int(number)                        # type casting converting float --> int
print(number)                               # 99 
print(type(number))                         # <class 'int'>

# # convert int to float:
number = 50                                 # int value
number = float(number)                        # type casting converting int --> float
print(number)                               # 50.0
print(type(number))                         # <class 'float'>

# # convert int to string:
number = 50                                 # int value
number = str(number)                        # type casting converting int --> str
print(number)                               # '50'
print(type(number))                         # <class 'str'>

# # convert str to int:
number = "999"                              # string value
number = int(number)                        # type casting converting str --> int
print(number)                               # 999
print(type(number))                         # <class 'int'>

# # convert str to float:
number = "36.5"                             # str value
number = float(number)                      # type casting converting str --> float
print(number)                               # 36.5
print(type(number))                         # <class 'float'>

# -------------------------------------------------------------------------
# Basic operations in python i.e addition, sub, div, mul ..

num_1 = 90
num_2 = 10

print(int(num_1 + num_2))                   # +	    Addition	      100   int	
print(int(num_1 - num_2))                   # -	    Subtraction	      80    int
print(int(num_1 * num_2))                   # *	    Multiplication	  900   int	
print(int(num_1 / num_2))                   # /	    Division	      9.0   float

num_1 = 36.6
num_2 = 6

print(int(num_1 + num_2))                   # +	    Addition	      42.6  float	
print(int(num_1 - num_2))                   # -	    Subtraction	      30.6  float
print(int(num_1 * num_2))                   # *	    Multiplication	  219.6 float	
print(int(num_1 / num_2))                   # /	    Division	      6.1   float


# int and flaot --> float
# int and int --> int (except for div)
# float and float --> float


num_1 = 56
num_2 = 9

remender = num_1 % num_2                    # %     Modulus (remender)          2          
quot = num_1 // num_2                       # //    Floor division (quotient)   6

print(f'remender is: {remender} quotient is: {quot}')

# 92 / 9 --> 10 quotient ,  2 remender
# 77 / 7 --> 11 quotient , 0 remender
# 56 / 9 --> 6 quotient , 2 remender


# 5^2 = 5*5
# 9^3 = 9*9*9
print(5 ** 2)                               # **        Exponentiation      25	
print(9 ** 3)                               # **        Exponentiation      25


# -------------------------------------------------------------------------

# increment num by 2 and store its value in num 
num = 50
# num = num + 2
num += 2                               # 50 + 2                       
print(num)                              # 52

# substract num by 2 and store its value in num 
num = 50
# num = num - 2
num -= 2                               # 50 - 2                       
print(num)                              # 48

# multiply num by 2 and store its result in num
num = 50
# num = num*2
num *= 2                                # 50 * 2
print(num)                              # 100

# divide num by 2 and store its result in num
num = 50
# num = num/2
num /= 2                                # 50 / 2
print(num)                              # 25.0

# num //=2 
# num %=2 
# num **=2 


# -------------------------------------------------------------------------

# # Comparison  operator gives output in True / False
# It is used in if / else conditions
# Operator	    Name	                    Example	Try it
# ==	        Equal	                    x == y	
# !=	        Not equal	                x != y	
# >	            Greater than	            x > y	
# <	            Less than	                x < y	
# >=	        Greater than or equal to	x >= y	
# <=	        Less than or equal to	    x <= y

num_1 = 100
num_2 = 20
print(num_1 == num_2)                   #   100 == 2 ? False
print(num_1 != num_2)                   #   100 != 2 ? True  
print(num_1 > num_2)                    #   100 > 2 ? True  
print(num_1 < num_2)                    #   100 < 2 ? False  
print(num_1 >= num_2)                   #   100 >= 2 ? True  
print(num_1 <= num_2)                   #   100 <= 2 ? False  


# -------------------------------------------------------------------------
# Type casting:
num_1 = input("enter no: ")
int_num_1 = int(num_1)
# or
int_num_1 = int(input("enter no: "))

print(int_num_1, type(int_num_1))

# Write a program to get inputs from user and perform additino, sub and multiplication.
num_1 = float(input('Enter no'))
num_2 = float(input('Enter no'))

print( num_1 + num_2 )
print( num_1 - num_2 )
print( num_1 * num_2 )

# how does brackets work:
result = 10 * (20 / (5 -2))
print(result)