print(12+14)
print(12-10)
print(12*10)
print(20/10)
print(2 ** 4) #16 

# The concept of calculating the operator is PAMDASLR
# ()   P FOR Parenthesis
# **   E for Exponent
# * /  M for Multiplication, D for Division
# + -  A for Addition, S for Subtraction
# LR   for Left to Right value evolution.
 
print(3*3+3/3-3) # The output will be 7.0 a float value.

# Excercise - 02 (BMI Calculator)

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Write your code below this line 👇
print(float(weight)/float(height)**2)