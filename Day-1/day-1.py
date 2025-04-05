# Data types:
# intiger, float, sets, char, string, boolean, list, tupple, dict , 


# What is variable?
#           name	                --=> Variable						
# a	 s	h	u	t	o	s	h       --> values
# 0	 1	2	3	4	5	6	7       --> Indexes
# Allowd: Name, name, lastName, age, password33 , user_1, user_2, 
# Not acceptyed: " ", 123_name, special chars, __, 1user


# # String: "" / ''
# name= 'nare3ndra'
# last_name =  "modi"
# address= 'nare3ndra\'s house -1'
# address= "nare3ndra's house - 2"
address= 'nare3ndra"s house -3'
# age = 30
# is_true = False
# print(address)
# print(type(address))

# # len:
# sentence = "Hello World"
# print(len(sentence))


# Indexing and Slicing: []
sentence = "My name is nare3ndra"
#           0123456789... incraseing
#                        -3 -2 -1  decreasing
# print(sentence[11])


# print(sentence[3:7]) # name
# print(sentence[0:7])
# print(sentence[:7])
# print(sentence[11:])
# print(sentence[:])

# print(sentence[-20]) # reverse
# print(sentence[-5]) 
# print(sentence[::])
# print(len(sentence))

# step1:  print(len("My name is nare3ndra"))
# step2 : print(20)
# step 3: 20


# Methods: 
# name = "aashutoshaa"
# # print(name.upper())
# print(name.capitalize())
# print(name.count("sh"))
# print(name.index("as"))

# print(dir(name))

# wahat is difference between method and funtion in python?
# Implement join and split method



# String concatination:
name = "ashu"
lastName = "patil"

completeName = "User name is: {} {}".format(name, lastName)
print(completeName)
completeName = f"User name is: {name} {lastName}"
print(completeName)

print(name + " " + lastName)
# print("User name is:", name, lastName)
# print(completeName)

print("4 - ", 4*4)
print("4 - " + str(4*4))
print(f'4 - {4*4}')
print(4,"-",4*4)

# num_1 = 20
# num_2 = "5"
# print(f"{num_1} \n {num_2}")