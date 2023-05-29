
# OBSERVATIONS
'''
- Block sizes are 16
- Leak is [encrypted blocks[r], encrypted blocks[r+1]]
- Oracle is 'HTB'
'''

# MODULES
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random, os
import binascii as ba
from output import *

# VARIABLES

# CLASSES

# FUNCTIONS
def blockify(message, size):
    return [message[i:i + size] for i in range(0, len(message), size)]

def dehex(string):
    dehexed = ""
    for i in range(0,len(string),2):
        dehexed += chr(int(string[i:i+2],16))
    return dehexed

def hex_range(start, end):
    return ['{:08X}'.format(i) for i in range(int(start, 16), int(end, 16))]


def xor(a, b):
    xord_bytes = list()
    for a_item,b_item in zip(a,b):
        for i in range(0,len(a_item),2):
            a_term,b_term = a_item[i:i+2],b_item[i:i+2]
            a_xor_b = int(a_term,16) ^ int(b_term,16)
            xord_bytes.append(hex(a_xor_b)[2:].zfill(2))
    return ''.join(xord_bytes)

# MAIN FUNCTION
def main():
    '''Break the AES ECB Mode.'''
    size = 32
    ct_blocks = blockify(ct,size)
    
    

######## MAIN ########
if __name__ == '__main__':
    main()
