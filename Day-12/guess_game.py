import random
from art import logo
print(logo)


def guess_checker(no_of_attempts):
    for i in range(1, no_of_attempts + 1):
        print(
            f"You have {no_of_attempts-i+1} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it! The answer was {guess}.")
            break
        elif guess > random_number:
            print("Too High.")
        else:
            print("Too Lose.")
    else:
        print(f"Game over! The number was {random_number}.")


random_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {random_number}")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == "easy":
    guess_checker(10)
elif level == "hard":
    guess_checker(5)
else:
    print("Invalid Level!")

