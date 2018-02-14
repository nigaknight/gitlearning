from __future__ import print_function
# The Caesar Cipher Algorithm

def main():
    message = input("Enter message: ")
    key     = int(input("Key [1-26]: "))
    mode    = input("Encrypt or Decrypt [e/d]: ")

    if mode.lower().startswith('e'):
        mode = "encrypt"
    elif mode.lower().startswith('d'):
        mode = "decrypt"

    translated = encdec(message, key, mode)
    if mode ==   "encrypt":
        print(("Encryption:", translated))
    elif mode == "decrypt":
        print(("Decryption:", translated))
        
def encdec(message, key, mode):
    message    = message.upper()
    translated = ""
    LETTERS    = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode ==   "encrypt":
                num = num + key
            elif mode == "decrypt":
                num = num - key

            if num >= len(LETTERS):
                num -= len(LETTERS)
            elif num < 0:
                num += len(LETTERS)

            translated += LETTERS[num]
        else:
            translated += symbol
    return translated

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
