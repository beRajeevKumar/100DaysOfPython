import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
             'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
characters = ["!", "@", "#", "$", "%", "^",
              "&", "*", "(", ")", "_", "-", "+", "=", "/"]

print("Welcome to the PyPassword Generator!")
total_letters = int(input("How many letters would you like to your password?\n"))
total_characters = int(input("How many characters would you like? \n"))
total_numbers = int(input("How many numbers would you like? \n"))

only_letters = total_letters - (total_characters + total_numbers)

# Easy Level
password_easy = ""

for char in range(0, total_letters):
    password_easy += random.choice(alphabets)

for char in range(0, total_characters):
    password_easy += random.choice(characters)

for char in range(0, total_numbers):
    password_easy += random.choice(numbers)

print(password_easy)

# Hard Level
password_hard_list = []

for char in range(0, only_letters):
    password_hard_list.append(random.choice(alphabets))

for char in range(0, total_characters):
    password_hard_list.append(random.choice(characters))

for char in range(0, total_numbers):
    password_hard_list.append(random.choice(numbers))

print(password_hard_list)
random.shuffle(password_hard_list)
print(password_hard_list)
password_hard = ""
for char in password_hard_list:
    password_hard += char
print(f"Here is the new password: {password_hard}")
