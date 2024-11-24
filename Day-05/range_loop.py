# Sum of the numbers from 1 to 100 by using range function.
# total = 0
# # Here we use range from 0 to 101 because 0 is inclusive but 101 is exclusive.
# for number in range(0, 101):
#     total += number
# print(total)

# # Exercise 3 - Adding Even Numbers

# total = 0
# # Here I use third parameter for jumps in between the range of first two parameters.
# for number in range(2, 101, 2):
#     total += number
# print(total)

# Exercise 4 - FizzBuzz Game

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
