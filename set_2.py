def shift_letter(letter, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter = str(letter)
    shift = int(shift)
    
    if letter == " ":
        new_letter = " "
    else:
        new_position = (alphabet.rfind(letter) + shift) % 26 
        new_letter = alphabet[new_position]
    
    return new_letter

def caesar_cipher(message, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = str(message).upper()
    shift = int(shift)
    new_list = []
    
    for i in message:
        if i == " ":
            new_letter = " "
        else:
            letter = alphabet.rfind(i)
            new_position = (letter + shift) % 26
            new_letter = alphabet[new_position]
        
        new_list.append(new_letter)

    new_message = ''.join(new_list)
    return new_message
        
def shift_by_letter(letter, letter_shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter = str(letter.upper())
    letter_shift = str(letter_shift.upper())

    if letter == " ":
        new_letter = " "

    else:
        new_letter_position = (alphabet.rfind(letter) + alphabet.rfind(letter_shift))%26
        new_letter = alphabet[new_letter_position]

    return new_letter

def vigenere_cipher(message, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = list(message.upper())
    key = list(key.upper())
    new_key = []
    new_list = []

    while len(message) > len(new_key):
        new_key = new_key + key

    while len(new_key) != len(message):
        new_key.pop()

    for i in range(0,len(message)):
        if message[i] == " ":
            new_list.append(" ")
            
        else:
           m = alphabet.rfind(message[i])
           k = alphabet.rfind(new_key[i])
           position = (m + k) % 26
           new_list.append(alphabet[position])
        
    new_message = ''.join(new_list)
    return new_message

def scytale_cipher(message, shift):
    message = str(message)
    shift = int(shift)
    new_message = []


    if len(message) % shift == 0:
        message = message
    else:
        while (len(message) % shift) != 0:
            message = message + "_"

    for i in range(0,len(message)):
        position = (i // shift) + (len(message) // shift) * (i % shift)
        letter = message[position]
        new_message.append(letter)

    encoded = ''.join(new_message)
    return encoded 

def scytale_decipher(message, shift):
    message = str(message)
    shift = int(shift)
    old_message = []
    i = 0
    col = len(message)/shift

    for i in range(0,shift):
        m = 0
        while m < col:
            n = shift*m + i
            old_message.append(message[n])
            m = m + 1
        
    decoded = ''.join(old_message)
    return decoded
