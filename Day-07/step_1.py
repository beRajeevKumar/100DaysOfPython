# Step 1 to solve the Hangman Game.

import random
word_list = ["ardvark", "baboon", "camel"]
random_word = random.choice(word_list)

guess = input("Guess A Letter: ").lower()
# if len(guess) > 1:
#     print("You should choose only single letter")
#     input("Please guess single letter: ").lower()

for letter in random_word:
    if guess == letter:
        print("Right")
    else:
        print(f"Wrong")
