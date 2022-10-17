#caesar-cipher
from base64 import decode
from operator import indexOf
from turtle import position
from art import caesar_cipher_logo

print(caesar_cipher_logo)
#Encryption
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%26
    def caesar(old_text, shift_amount, direction_type):
        new_text = ''
        if direction== 'decode':
                shift_amount *= -1
        for letter in old_text:
            if letter in alphabet:
                old_position = alphabet.index(letter)
                new_position = old_position+shift_amount
                new_letter = alphabet[new_position]
                new_text += new_letter
            else:
                new_text += letter
        print(f"The {direction}d text is {new_text}")

    caesar(old_text=text, shift_amount=shift, direction_type=direction)
    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no'. : ")
    if user_input == 'no':
        should_continue = False
        print("Good Bye")




#Encryption
'''def encrypt(plain_text, shift_amount):
    cipher_text = ''
    for letter in plain_text:
        #print(letter)
        position = alphabet.index(letter)
        #print(position)
        new_position = position+shift_amount
        #print(new_position)
        new_letter = alphabet[new_position]
        #print(new_letter)
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

#decryption
def decrypt(cipher_text, shift_amount):
    plain_text = ''
    for letter in cipher_text:
        #print(letter)
        position = alphabet.index(letter)
        #print(position)
        new_position = position-shift_amount
        #print(new_position)
        new_letter = alphabet[new_position]
        #print(new_letter)
        plain_text += new_letter
    print(f"The decoded text is {plain_text}")

if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_amount=shift)'''

