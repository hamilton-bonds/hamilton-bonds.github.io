from Crypto.Cipher import AES
import hashlib
import itertools as it
import random as rand
import sys
from time import sleep
import numpy as np

ciphertext = 'c81d34b91162a8b488cd4a923370d8d887daba3367d1fce6617e2fb1a681d4e21bff2e82350a0b04930c89e85dff0ab1aaf365'
nonce = '820be17b5cb8fe3c5c02963fc35de8ff'
#secret_key = '100010000000001000011010101110'

#skl = [int(x) for x in secret_key]
ciphertext_bytes = bytes.fromhex(ciphertext)

indices = [7, 8, 9, 10, 13, 14, 15, 17, 23, 24, 25, 26, 27, 29, 30, 33, 34, 35, 36, 37, 38, 44, 46, 48, 49, 51, 52, 53, 55, 56, 57, 59, 61, 62, 69, 70, 73, 74]

def key_array_to_key_string(key_list):
    key_string_binary = b''.join([bytes([x]) for x in key_list])
    return hashlib.md5(key_string_binary).digest()

def decrypt(n):
    print("Evaluating n={}...".format(n))
    secret_key = str()
    all_nums = set()
    hb = 2**(n+1)
    x = 0
    samples = set()
    while x != hb:
        x += 1
        #an = rand.randint(0,hb)
        #secret_key = str()
        #for i in range(n):
        #    secret_key += rand.choice(['0','1'])
        pct = round((x/hb)*100,2)
        #secret_key = bin(an)[2:].zfill(n)
        #print("Evaluating [{}]\t| {}\t| {}".format(pct,an,secret_key),end='\r')
        #secret_key_base = '0000111011011100000001001000011000010011011110100101000100101100101111011011'
        secret_key_base = '0000111000011010000001110000101000000011011110101111100010100100101100010011'
        skbl = list(secret_key_base)
        #for g,skb in enumerate(skbl):
        #    if skb == '?':
        #        skbl[g] = rand.choice(['0','1'])
        #for rs in range(12):
        #    indl = list(it.product(indices,indices,repeat=rs))
        #    for ind in indl:
        #        for part in ind:
        #            i = part
        #            if skbl[i] == '0':
        #                skbl[i] = '1'
        #            elif skbl[i] == '1':
        #                skbl[i] = '0'
        samp_list = None
        
        while samp_list == None:
            samp_list = sorted(rand.sample(indices,rand.randint(1,38)))
            sample = ':'.join([str(x) for x in samp_list])
            if sample not in samples:
                samples.add(sample)
            else:
                samp_list = None
        for samp in samp_list:
            i = int(samp) - 1
            if skbl[i] == '0':
                skbl[i] = '1'
            elif skbl[i] == '1':
                skbl[i] = '0'
            print("Modified: {}\t\t| Total Samples: {}".format(len(samp_list),len(samples)))
            if True:
                print("Evaluating [{}]\t| {}".format(pct,secret_key),end='\n')
                secret_key = ''.join(skbl)
                #secret_key = '0000111011011100000001001000011000010011011110100101000100101100101111011011'
                skl = [int(x) for x in secret_key]
                key = key_array_to_key_string(skl)
                cipher = AES.new(key, AES.MODE_EAX, nonce=bytes.fromhex(nonce))
                plaintext_bytes = cipher.decrypt(ciphertext_bytes)
                try:
                    plaintext = plaintext_bytes.decode('ascii')
                except:
                    plaintext = "SKIPPED"
                if plaintext != "SKIPPED": #This will show the flag.
                    print("KEY:  {}".format(key))
                    print("FLAG: {}".format(plaintext))
                    sleep(10)
                    sys.exit()
    sys.exit()
    return 0

if __name__ == '__main__':
    m = 76
    n = 77
    decrypt(38)
    #decrypt(n)
            
    sys.exit()
