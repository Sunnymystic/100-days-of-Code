#Encryption
#Shift 
# Uppercase letters 65 to 90.
# Lowercase letters 97 - 122

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
#            print("Hello")   
#            print(f"encrpyted_list : + {encrpyted_list}")
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
#            print("Hello")   
#            print(f"encrpyted_list : + {encrpyted_list}")
    decry_mesg = ''.join(decrpyted_list)
    print(f"Here's the decoded result: {decry_mesg}")

times = "yes"
while times == "yes":
    operation = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    input_message = input("Type your message:\n").lower()
#    print(input_message)
    shift = int(input("Type the shift number:\n"))
    if operation == 'encode':
        encrypt(input_message,shift)
    elif operation == 'decode':
        decrpyt(input_message,shift)
    times = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    


