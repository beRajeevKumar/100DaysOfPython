from random import randint
player_guess = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))

computer_turn = randint(0, 2)
print(computer_turn)
if player_guess == computer_turn:
    print("Draw")
elif player_guess == 0:
    if computer_turn == 1:
        print("You Loose")
    elif computer_turn == 2:
        print("You Win")
elif player_guess == 1:
    if computer_turn == 0:
        print("You Loose")
    elif computer_turn == 2:
        print("You Win")
elif player_guess == 2:
    if computer_turn == 0:
        print("You Loose")
    elif computer_turn == 1:
        print("You Win")


if player_guess >= 3 and player_guess < 0:
    print("You typed an invalid number, you lose!")
elif player_guess == 0 and computer_turn == 2:
    print("You Win")
elif player_guess == 2 and computer_turn == 0:
    print("You Loose")
elif computer_turn > player_guess:
    print("You Loose")
elif computer_turn < player_guess:
    print("You Win")
else:
    print("Its a Draw")
