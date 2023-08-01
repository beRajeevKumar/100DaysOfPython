alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    encoded_text=""
    for i in range(0, len(text)):
        if not text[i] in alphabet:
            encoded_text += text[i]
        else:
            index_of_letter = alphabet.index(text[i])
            encoded_text+=alphabet[index_of_letter+shift]
    print(f"The encoded text is {encoded_text}")

def decrypt(text, shift):
    decoded_text=""
    for i in range(0, len(text)):
        if not text[i] in alphabet:
            decoded_text+=text[i]
        else:
            index_of_letter = alphabet.index(text[i])
            decoded_text+=alphabet[index_of_letter-shift]
    print(f"The decrypted text is {decoded_text}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print(f"Unknown direction")  

play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
while not play_again == "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Unknown direction")

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 