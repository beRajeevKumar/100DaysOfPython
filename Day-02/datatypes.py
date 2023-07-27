# Datatypes in Python

# # String Datatype
# print("Hello"[0])
# print("Hello"[4])
# print("Hello"[len("Hello") - 1])
# # Concationation of strings
# print("123" + "345")

# # Integer Datatype

# print(123 + 345)
# print(123_456_789) # This is a valid syntax in Python like 123,456,789

# # Float Datatype
# print(3.14159)

# # Boolean Datatype
# True
# False

# Type Error, Type Checking and Type Conversion
# num_char = len(input("What is your name? "))
# # print("Your name has " + num_char + " characters.") # This will throw a type error

# print("Your name has " + str(num_char) + " characters.") # This will work

# # Type Checking
# print(type(num_char))  # This will print the type of the variable which is int type of int class.

# # Type Conversion
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.") # This will work

# print(50 + float(20.5))

# print(20 + bool(False)) 

# print(str(100) + str(490), type(str(100) + str(490))) # This will print the


# Excercise - 01
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
input_str = input("Enter a number: ")
# print(type(input_str))
# print(input_str[0], input_str[1])
input_sum=int(input_str[0])+int(input_str[1])
print(type(input_sum))