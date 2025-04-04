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

# number = -1.123
# print(type(number))

# # # convert float to integer:
# number = 99.95                              # FLoat value
# number = int(number)                        #type casting
# print(number) 
# print(type(number))                     


# num_1 = 10.0
# num_2 = 90

# print(int(num_1 + num_2))
# print(int(num_1 - num_2))
# print(int(num_1 * num_2))
# print(int(num_2 / num_1))

# # int and flaot --> float
# # int and int --> int (except for div)
# # float and float --> float


# num_1 = 56
# num_2 = 9

# remender = num_1 % num_2
# quot = num_1 // num_2

# print(f'remender is: {remender} quotient is: {quot}')

# # # 92 / 9 --> 10 quotient ,  2 remender
# # # 77 / 7 --> 11 quotient , 0 remender
# # # 56 / 9 --> 6 quotient , 2 remender


# # 3^2 = 3*3 
# # 5^2 = 5*5
# # 9^3 = 9*9*9
# print(3 ** 2)
# print(5 ** 2)
# print(9 ** 3)


####################################

# num = 50
# # increment num by 10 and store its value in num 
# num = num + 10    #  num += 10
# num += 10
# print(num)

# num = 30
# num += 20 
# print(num)

# num = 50
# # multiply num by 2 and store its result in num
# # num = num*2
# num //=2 
# print(num)

# num += 2 
# num *= 2 
# num -= 2 
# num /= 2 
# num //=2 
# num %=2 
# num **=2 


####################################
# # Comparison  operator 
# Operator	    Name	                    Example	Try it
# ==	        Equal	                    x == y	
# !=	        Not equal	                x != y	
# >	            Greater than	            x > y	
# <	            Less than	                x < y	
# >=	        Greater than or equal to	x >= y	
# <=	        Less than or equal to	    x <= y

# num_1 = 100
# num_2 = 20
# print(num_1 == num_2)
# print(num_1 != num_2)
# print(num_1 <= num_2)


####################################
# # Type casting:
# num_1 = input("enter no: ")
# int_num_1 = int(num_1)
# # or
# int_num_1 = int(input("enter no: "))
# print(int_num_1, type(int_num_1))
# num_1 = input(int('Enter no'))
# num_2 = int(input('Enter no'))

# print( num_1 + num_2 )
# print( num_1 - num_2 )
# print( num_1 * num_2 )



#####################

# result = 10 * (20 / (5 -2))
# print(result)