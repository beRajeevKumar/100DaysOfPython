import random

# Now you can use functions from the random module
# print(random.randint(1, 10))

# print(round(random.random()*5))

random_value=random.randint(0, 1)
if random_value == 0:
    print("Tails")
else:
    print("Heads")