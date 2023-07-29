import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# MY SOLUTION

user_input= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_chance= random.randint(0,2)
print(f"Computer also choose {computer_chance}")

if user_input==0:
    print(rock)
    if computer_chance == 0:
        print(rock)
        print("Game Draw!")
    elif computer_chance == 1:
        print(paper)
        print("You Loose!")
    elif computer_chance == 2:
        print(scissors)
        print("You Win!")
elif user_input==1:
    print(paper)
    if computer_chance == 0:
        print(rock)
        print("You Win!")
    elif computer_chance == 1:
        print(paper)
        print("Game Draw!")
    elif computer_chance == 2:
        print(scissors)
        print("You Loose!")
elif user_input== 2:
    print(scissors)
    if computer_chance == 0:
        print(rock)
        print("You Loose!")
    elif computer_chance == 1:
        print(paper)
        print("You Win!")
    elif computer_chance ==2:
        print(scissors)
        print("Game Draw!")


# ////////////////////////////////////////
# TEACHER SOLUTION

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")