# Step 2 to solve the Hangman Game.

import random
word_list = ["ardvark", "baboon", "camel"]
random_word = random.choice(word_list)
print(random_word)
guess = input("Guess A Letter: ").lower()

display = []
# for letter in random_word:
#     display.append("_")

for _ in range(len(random_word)):
    display += "_"

# for letter in random_word:
#     if letter == guess:
#         position = random_word.index(letter)
#         display[position] = letter
# This loop prints letters of a string but we need position of that letter, so we use range funcion loop.


for position in range(len(random_word)):
    letter = random_word[position]
    if letter == guess:
        display[position] = letter
print(display)
