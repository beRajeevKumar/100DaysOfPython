enemies = 1


def increase_enemies():
    global enemies
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# """If we create a variable in a function so it will be available in that function but if we create a variable inside a block like if block else block or any kind of block like while loop or for loop so then we can access that variable outside the block of that block(if, else, while, for)"""

# game_level = 3


# def create_enemy():
#     enemies = ["Skleton", "Zombie", "Ghost", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[2]
#     print(new_enemy)


# create_enemy()
