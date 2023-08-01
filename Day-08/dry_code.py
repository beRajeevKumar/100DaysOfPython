# My DRY Code is here:

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def ceaser(plain_text, shift_amount):
#   cipher_text=""
#   for letter in plain_text:
#       position = alphabet.index(letter)
#       if direction == "encode":
#           new_position = (position + shift_amount) % len(alphabet)
#           cipher_text += alphabet[new_position]         
#       elif direction == "decode":
#           new_position = position - shift_amount
#           cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}.")

# ceaser(text,shift)


# But the Teacher code is here:
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction == "decode":
            shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}.")

ceaser(start_text= text,shift_amount=shift,cipher_direction=direction)    