# # Part 1: String Methods & Transformations
# # Create a variable text and assign it any paragraph of your choice (at least 3 sentences).
# # comment : ctl + /


# my_para = "My name is Superman. I am 30yr old and I live in Thailand. I work at Google"

# # Convert the entire text to uppercase and lowercase.
# print(my_para.upper())
# print(my_para.lower())

# # Reuse
# upper_my_para = my_para.upper()
# # OR
# my_para = my_para.upper()
# print(my_para)



# # Capitalize only the first letter of the text.
# print(my_para.capitalize())
# print("Count of Capital letter I in my strting: ", my_para.count("I"))
# print(my_para.replace("I","You"))
# print(my_para.replace(" ", ""))
# print(my_para.startswith("z")) 
# print(my_para.endswith("e")) 
# print( my_para.split("I"))


# # Part 2: String Concatenation & Manipulation
# first_name = "john"
# last_name = "wick"
# full_name = "john" +" " + "wick"  # Option 1
# full_name = f"{first_name} {last_name}"  # option 2
# print(full_name.upper())

# # Swap the first and last names and print the result.
# swap_val = first_name               # swap_val = "john"
# first_name = last_name              # first_name  = "wick"
# last_name = swap_val                # last_name = "john"
# full_name = first_name +" " + last_name
# print(full_name)

# # Create a new string where the first name is reversed and the last name is in title case.
# first_name = first_name[::-1]       # string reversal
# last_name = last_name.capitalize()

# print(first_name, last_name)
# # OR
# print(first_name +" "+ last_name)
# # OR
# print(f"{first_name} {last_name}")



# # Part 3: String Formatting & Dynamic Input
# name = input("Enter your Name: ").strip(" ").capitalize()
# age = input("Enter your age: ")
# language = input("Enter your favorite programming language: ")
# # print(name, age, language)
# print( f"Hello, my name is {name}, I am {age} years old, and I love {language}." )
# print( "Hello, my name is {}, I am {} years old, and I love {}.".format(name, age, language) )


# # Part 4: Indexing, Slicing & Reversing
# phrase = "Mastering Python is Fun!" # -> Mseig
# print(phrase[-1])
# print(phrase[9:16])
# print(phrase[9:16])
# print(phrase[0:9])
# print(phrase.index("Python"))

# phrase = "Mastering Python is Fun!" # Mastering is Fun!
# # print(phrase.replace("Python ", ""))
# phrase = phrase.split(" ")
# phrase.remove("Python")
# print(" ".join(phrase))