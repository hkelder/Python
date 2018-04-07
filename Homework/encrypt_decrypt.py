# Encrypt a text file using the Caesar cipher (shift 5).
#
# 1. Write the program to encrypt the text file (case insensitive) into cipher text
# 2. Write the program to decrypt the cipher text to plain text(normal text- case insensitive)

plainText = input("Enter a some text:")
shift = 5


def caesar(plainText, shift):
    """Encrypt inputted text via Caesar cipher (shift by 5).

    Keyword arguments:
    plainText -- user inputted text
    shift -- 5

    returns string

    """

    cipherText = ""
    for character in plainText:
        if character.isalpha():
            alphabet = ord(character) + shift
            if alphabet > ord('z'):
                alphabet -= 26
            finalLetter = chr(alphabet)
            cipherText += finalLetter

    print(cipherText)
    return cipherText


caesar(plainText, shift)


def decryption():

    encryptedText = input("Enter your encrypted text:")
    encryptionShift = 5

    encrypText = ""
    for character in encryptedText:
        if character.isalpha():
            alphabet = ord(character) - encryptionShift
        if alphabet > ord('z'):
            alphabet += 26
        finalLetter = chr(alphabet)
        encrypText += finalLetter

    print(encrypText)
    return encrypText


decryption()
