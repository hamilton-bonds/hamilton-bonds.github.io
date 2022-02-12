'''
crypto-204.py
In a review of network traffic, the following string was found to be sent across the wire.
'''
string = 'NDkiIR0/LnoVLy56OzQ+egw1Lj8nUA=='
#string = '4e446b694952302f4c6e6f564c7935364f7a512b656777314c6a386e55413d3d0a'
'''
Decrypt the string to determine the secret message.
'''

'''
WALKTHROUGH:  When you run this command echo 'NDkiIR0/LnoVLy56OzQ+egw1Lj8nUA==' | base64 -d, nothing significant shows up, especially not a flag.  Even if you tried all ROT combos of this string, no flag.

At first glance, there's not much to see, but one quick and easy method to test is a string that was base64-encoded after undergoing single-character XOR.
'''

import os

def base64dToFile(input_filename,output_filename):
    '''Decodes the base64 string from a file and puts the output into another file'''
    with open(input_filename,'r') as infile:
        for line in infile:
            os.system('echo {} | base64 -d > {}'.format(line.strip(),output_filename))
        infile.close()
    return "Base64 Decode Complete."

def processDataIntoHex(input_filename):
    '''Takes the raw data and turns it into a hex string'''
    with open(input_filename,'r') as infile:
        for line in infile:
            line = line.strip()
            linehex = ""
            for char in line:
                linehex += hex(ord(char))[2:].zfill(2)
        infile.close()
    return linehex

def singleCharXOR(hex_encoded_data):
    '''Decode a XOR with a XOR!  XOR each byte in hex_encoded_data with a single character'''
    decoded_options_list = list()
    print(hex_encoded_data)
    for a in alphanum:
        h = 0
        result_string = ""
        for i in range(2,len(hex_encoded_data)+2,2):
            hed = hex_encoded_data[h:i]
            result_string += chr(int(hed,16) ^ ord(a))
            h = i
        decoded_options_list.append(result_string)
    return decoded_options_list

if __name__ == '__main__':
    global alphanum
    alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    input_filename = 'crypto-204.txt'
    output_filename = 'crypto-204-base64d.txt'
    print(base64dToFile(input_filename,output_filename))
    input_filename = output_filename
    hex_string = processDataIntoHex(input_filename)
    print("Hex Conversion Complete.")
    decoded_options_list = singleCharXOR(hex_string)
    for dol in decoded_options_list:
        if (("{" in dol) and ("}" in dol)) and ((dol.count("{") == 1) and (dol.count("}") == 1)):
            print("\nFLAG: {}\n".format(dol)) #QED
