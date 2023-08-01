# import art
# print(art.logo)

from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction == "decode":
            shift_amount *= -1
    for letter in start_text:
        if not letter in alphabet:
             end_text += letter
        else:
            end_text += alphabet[(alphabet.index(letter) + shift_amount)%len(alphabet)]
    print(f"The {cipher_direction}d text is {end_text}.")

should_end=False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    ceaser(start_text= text,shift_amount=shift,cipher_direction=direction)
    
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if again == "no":
         should_end = True
         print("Goodbye!")
         

