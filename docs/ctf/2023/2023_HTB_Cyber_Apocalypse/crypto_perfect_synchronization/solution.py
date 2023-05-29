
# OBSERVATIONS
'''
- 1478 lines
'''


# MODULES
from os import urandom
from Crypto.Cipher import AES

# VARIABLES
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPECIAL = "{_} "
KNOWN = "HTB{"

# CLASSES
class Cipher:

    def __init__(self):
        self.salt = urandom(15)
        key = urandom(16)
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, message):
        return [self.cipher.encrypt(c.encode() + self.salt) for c in message]


# FUNCTIONS

# MAIN FUNCTION
def main():
    '''Deconstructing AES ECB.'''
    cipher = Cipher()
    MESSAGE = KNOWN
    encrypted = cipher.encrypt(MESSAGE)
    encrypted = "\n".join([c.hex() for c in encrypted])
    print(encrypted)

######## MAIN ########
if __name__ == '__main__':
    main()
