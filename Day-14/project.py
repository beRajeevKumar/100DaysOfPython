from art import vs_logo
from art import game_logo
from random import randint
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    }
]


data1 = data[randint(0, len(data)-1)]
data2 = data[randint(0, len(data)-1)]

winners = {}
keys = ["name", "follower_count", "description", "country"]
values = [data1["name"], data1["follower_count"],
          data1["description"], data1["country"]]
for i in range(len(data)):
    winners[keys[i]] = values[i]


def follower_counter(dict):
    return dict["follower_count"]


print(game_logo)


def account1(name, description, country):
    print(f"Compare A: {name}, a {description}, from {country}.")


account1(data1["name"], data1["description"], data1["country"])


def account2(name, description, country):
    print(f"Against B: {name}, a {description}, from {country}.")


print(vs_logo)
account2(data2["name"], data2["description"], data2["country"])

user_guess = input("Who has more followers? Type 'A' or 'B': ")


def compare(followers_1, followers_2):
    if followers_1 > followers_2:
        return followers_1
    else:
        return followers_2


if user_guess == "A" or "a":
    compare(follower_counter(), follower_counter())
elif user_guess == "B" or "b":
    print("")
