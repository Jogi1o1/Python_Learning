#Caeser Cipher
from encryption import encrypt
from decryption import decrypt
from diagram import logo

print(logo)
repeat = "yes"
while repeat == "yes":
    enc_dec = input("Do you want to encrypt or decrypt?, for encryption type 'encrypt' for decryption type 'decrypt'\n")
    user_input = input("Please provide the string\n")
    shifting_number = int(input("Please provide the shift number\n"))

    if enc_dec == "encrypt":
        encrypt(user_input,shifting_number)
    else:
        decrypt(user_input,shifting_number)
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")

