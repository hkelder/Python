# Encrypt a text file using the Caesar cipher (shift 5).
#
# 1. Write the program to encrypt the text file (case insensitive) into cipher text
# 2. Write the program to decrypt the cipher text to plain text(normal text- case insensitive)

MAX_SHIFT_SIZE = 26


def decryptionMode():
    while True:
        print("Do you wish to encrypt or decrypt?")
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return mode
        else:
            print("Enter one of the following: encrypt, e, decrypt, d")


def userMessage():
    print("Enter your message:")
    return input()


def caesarShift():
    shift = 0
    while True:
        print("Enter the shift number (1-%s)" % MAX_SHIFT_SIZE)
        shift = int(input())
        if shift >= 1 & shift <= MAX_SHIFT_SIZE:
            return shift


def caesarsMessage(mode, message, shift):
    if mode[0] == 'd':
        shift = -shift
    translated = ''

    for character in message:
        if character.isalpha():
            asciiNumber = ord(character)
            asciiNumber += shift

            if character.isupper():
                if asciiNumber > ord('Z'):
                    asciiNumber -= 26
                elif asciiNumber < ord('A'):
                    asciiNumber += 26
            elif character.islower():
                if asciiNumber > ord('z'):
                    asciiNumber -= 26
                elif asciiNumber < ord('a'):
                    asciiNumber += 26

            translated += chr(asciiNumber)
        else:
            translated += character
    return translated


mode = decryptionMode()
message = userMessage()
shift = caesarShift()

print("Your translated text is:")
print(caesarsMessage(mode, message, shift))
