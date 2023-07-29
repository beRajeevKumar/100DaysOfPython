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