# from hangman_words import word_list
import random
word_list = ['abruptly', 'absurd', 'abyss',]
word = random.choice(word_list)

display = []
for _ in range(len(word)):
    display += "_"

# till_end = False

guess = input("Guess a letter: ")
print(display)
for position in range(len(word)):
    letter = word[position]
    if letter == guess:
        display[position] = letter


# How to use fleg variable in while loop.
# end_game = False
# i = 1
# while not end_game:
#     print(i)
#     i += 1
#     if i == 11:
#         end_game = True


# Or we can use fleg variable in this way in while loop
# end_game = True
# i = 1
# while end_game:
#     print(i)
#     i += 1
#     if i == 11:
#         end_game = False
