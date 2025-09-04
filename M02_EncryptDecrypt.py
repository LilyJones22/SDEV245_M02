import random

letters_ordered = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # used for encryption scrambling
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def scramble(): # scrambles letters to simulate encryption
    letters_scramble = []

    while len(letters_scramble) < 26: # checks if list is full
        val = random.choice(letters_ordered) # randomly selecting a letter
        if val not in letters_scramble:
            letters_scramble.append(val) # adds new letter to list
        else: 
            continue # if random letter already is in list, it skips to making a new one

    return letters_scramble

def gen_key(): # simulates generating a key
    key = "" # instalizing variables
    i = 0 
    
    while i < 4: # generating a random 4 digit number
        val = random.choice(nums)
        key = key + val
        i += 1

    return key


def encrypt(code, message): # simulates message encryption
    new = "" # instalizing new message

    for char in message: # cycles throguh each character of message

        if char.isalpha(): # checks if character is a letter
            char_fix = char.lower() # lowercases for simplicity

            index = letters_ordered.index(char_fix) # gets index of letter from original list

            temp = code[index] # converts letter of original message using scrambled code

            if char.isupper():
                temp = temp.upper() # capitalizes letter of encrypted message if original is capitalized

            new = new + temp

        else: # adds character as-is if it is not a letter

            new = new + char

    return new

def decrypt(code, message): # simulates message decryption

    new = "" # instalizing new message

    for char in message: # cycles through each character of message

        if char.isalpha(): # checks if character is a letter
            char_fix = char.lower() # lowercases for simplicity

            index = code.index(char_fix) # gets index of letter from scrambled code

            temp = letters_ordered[index] # converts letter of scrambled message back to its original

            if char.isupper():
                temp = temp.upper() # capitalizes letter of decrpyed message if it was capatlized

            new = new + temp

        else: # adds character as-is if it is not a letter

            new = new + char

    return new        


message = input("Enter your message: ") # user enters a message
    
while True:
    try:
        crypt_type = input("Enter encrption type. Symmetric (S) or Asymmetric (A): ") # user selects encryption type, since both are asked of assignment

        crypt_type = crypt_type.upper() # allows lowercase versions of letters to also be accepted, for ease of use


        if crypt_type == "A" or crypt_type == "S":
            break
        else:
            raise ValueError # simple error handling for encryption choice
    
    except ValueError:
        print("Not an accepted input. Please try again. \n")
        continue



if crypt_type == "S": # simulating symmetric key encryption
    code = scramble() 
    message_mixed = encrypt(code, message)
    key = gen_key() 
    message_fixed = decrypt(code, message_mixed) 

    print("")
    print(f"Sending message \" {message_mixed} \"")
    print(f"Inform reciever of secret key \"{key}\" to decrypt")

    print("")
    print("--" * 10)
    print("")

    print("---New Message Recieved---")
    print("Enter key to decrypt")
    attempt = input()

    while True: # requires user to enter proper key to access message
        if attempt == key:
            break
        else:
            print("Incorrect. Please try again.")
            attempt = input()
            continue

    print("Happy to confirm this is for you")
    print(f"Message: {message_fixed}")



if crypt_type == "A": # simmulating asymmetric key encryption
    code = scramble()
    private_key = gen_key()
    public_key = gen_key()
    message_mixed = encrypt(code, message)
    message_fixed = decrypt(code, message_mixed)

    print("")
    print(f"Using reciever's public key of \"{public_key}\" to encrypt")
    print(f"Sending message \" {message_mixed} \"")

    print("")
    print("--" * 10)
    print("")

    print("REMINDER")
    print(f"Your private key is \"{private_key}\"")
    print("")
    print("---New Message Recieved---")
    print("It was encrypted with your public key. Please use your private key to decrypt")

    attempt = input()
    
    while True: # requires user to enter proper key to access message
        if attempt == private_key:
            break
        else:
            print("Incorrect. Please try again")
            attempt = input()
            continue

    print("Happy to confirm this is for you")
    print(f"Message: {message_fixed}")