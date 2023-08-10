import random
from hangman_words import word_list
from hangman_life import stages
from art import logo
print(logo)

word = random.choice(word_list)
print(word)
end_of_game = False
lives = 6
display = []
for _ in range(len(word)):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You have already guessed a letter")
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            display[position] = letter

    if guess not in word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win.")

    print(stages[lives])
