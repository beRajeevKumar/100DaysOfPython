from art import vs_logo, game_logo
from game_data import data
import random

def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}."


def check_answer(guess, first_account, second_account):
    """Take the user guess and follower counts and returns if they got it right"""
    if first_account > second_account:
        return guess == "a"
    elif second_account > first_account:
        return guess == "b"


print(game_logo)
score = 0
game_should_continue = True
second_account = random.choice(data)

while game_should_continue:
    first_account = second_account
    second_account = random.choice(data)

    while first_account == second_account:
        second_account = random.choice(data)

    print(
        f"Compare A: {format_data(first_account)}")
    print(vs_logo)
    print(
        f"Against B: {format_data(second_account)}")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    first_follower_count = first_account["follower_count"]
    second_follower_count = second_account["follower_count"]

    is_correct = check_answer(
        user_guess, first_follower_count, second_follower_count)

    if is_correct:
        score += 1
        print(f"You're right!, Current score: {score}.")
    else:
        game_should_continue = False
        print(f"You're wrong!, Final score: {score}.")

