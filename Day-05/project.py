import random
print("Welcome to the PyPassword Generator!")
total_chars = int(input("How many letters would you like in your password?\n"))
no_of_symbols = int(input("How many symbols would you like?\n"))
no_of_numbers = int(input("How many numbers would you like to numbers?\n"))

no_of_alphabets = total_chars-(no_of_symbols+no_of_numbers)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
characters = ["!", "@", "#", "$", "%", "^",
              "&", "*", "(", ")", "_", "-", "+", "=", "/"]

# //////////////////////////////////////////////////////////////////

# password = ""
# pass_value = [alphabets[random.randint(0, len(alphabets)-1)], characters[random.randint(
#     0, len(characters)-1)], numbers[random.randint(0, len(numbers)-1)]]

# # print(random.randint(0, pass_value))
# print(pass_value[random.randint(0, len(pass_value)-1)])
# for i in range(0, total_chars):
#     password += pass_value[random.randint(0, len(pass_value)-1)]

# print(f"Here is your password: {password}")


# //////////////////////////////////////////////////////////////////
password_list = []

for i in range(0, no_of_alphabets):
    password_list += alphabets[random.randint(0, len(alphabets)-1)]
    # password_list.append(random.choice(alphabets))  We also can write it as.
for i in range(0, no_of_symbols):
    password_list += characters[random.randint(0, len(characters)-1)]
for i in range(0, no_of_numbers):
    password_list += numbers[random.randint(0, len(numbers)-1)]

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Here is your password: {password}")
