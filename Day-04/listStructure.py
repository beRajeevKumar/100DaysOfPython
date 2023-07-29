# Programming is like an open book exam.
# https://www.askpython.com/python/data-structures-in-python

# Exercise 2 - Banker Roulette 
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(f"{names[random.randint(0, len(names))]} is going to buy the meal today!")
# ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']