import random
word_list = ['abruptly', 'absurd', 'abyss',]
word = random.choice(word_list)

display = []
for _ in range(len(word)):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ")
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            display[position] = letter

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You Win.")
