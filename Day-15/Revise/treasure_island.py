print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("Choose Left(L) or Right(R): ").lower()
if choice1 == 'l':
    choice2 = input("Choose Wait(W) or Swim(S): ").lower()
    if choice2 == 'w':
        choice3 = input("Choose color Red(R) or Green(G) or Blue(B): ").lower()
        if choice3 == 'r':
            print("It's a room full of fire. Game Over.")
        elif choice3 == 'b':
            print("You enter a room of beasts. Game Over.")
        elif choice3 == 'g':
            print("You found the treasure! You Win!")
        else:
            print("Invalid Color!")
    else:
        print("Game Over")
else:
    print("Game Over")
