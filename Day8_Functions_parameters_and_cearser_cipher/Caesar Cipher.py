# Caesar Cipher Game Rules:
# 1. Choose to 'encode' (encrypt) or 'decode' (decrypt) a message.
# 2. Enter your message in lowercase — numbers and spaces are kept as-is.
# 3. Choose a shift number (e.g. 3 shifts 'a' to 'd').
# 4. Only lowercase letters are shifted; all other characters remain unchanged.
# 5. Shifting wraps around the alphabet (e.g. 'z' + 1 = 'a').
# 6. To decode a message, use the same shift number that was used to encode it.
# 7. Type 'yes' to go again or 'no' to exit.
from caesar_cipher_art import logo
print(logo)

def encrypt(input_message,shift):
    encrpyted_list = []
    for letter in input_message:
        if (ord(letter) + shift) <= 122 and (ord(letter) + shift) >= 97:
            encrpyted_letter = chr(ord(letter) + shift) 
        elif((ord(letter) + shift) > 122):
            encrpyted_letter = chr((ord(letter) + shift) - 26)
        else:
            encrpyted_letter = letter
        encrpyted_list.append(encrpyted_letter)
    encry_mesg = ''.join(encrpyted_list)
    print(f"Here's the encoded result: {encry_mesg}")

def decrpyt(input_message,shift):
    decrpyted_list = []
    for letter in input_message:
        if (ord(letter) - shift) <= 122 and (ord(letter) - shift) >= 97:
            decrpyted_letter = chr(ord(letter) - shift) 
        elif(letter.isalpha() and (ord(letter) - shift) < 97):
            decrpyted_letter = chr((ord(letter) - shift) + 26)
        else:
            decrpyted_letter = letter
        decrpyted_list.append(decrpyted_letter)
    decry_mesg = ''.join(decrpyted_list)
    print(f"Here's the decoded result: {decry_mesg}")

times = "yes"
while times == "yes":
    operation = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    input_message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if operation == 'encode':
        encrypt(input_message,shift)
    elif operation == 'decode':
        decrpyt(input_message,shift)
    times = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    


