from Crypto.Cipher import AES
import hashlib
import sys
from time import sleep

filename = "game_result.txt"

competitor1_text = ": Your competitor bets on "
competitor2_text = ": zardus's competitor bets on "
hacker_text = ", you bet on "
adamd_text = "zardus receives from adamd: "

competitor1_bet_list = list()
competitor2_bet_list = list()
hacker_bet_list = list()
zardus_bet_list = list()
expected_qubit_list = list()
adamd_bases = ""

def convert2stringlist(intlist):
    stringlist = list()
    for i in intlist:
        stringlist.append(str(i))
    return stringlist

def key_array_to_key_string(key_list):
    key_string_binary = b''.join([bytes([x]) for x in key_list])
    return hashlib.md5(key_string_binary).digest()

filedict = dict()
x = 0
with open(filename,'r') as infile:
    for line in infile:
        filedict[x] = line.strip()
        x += 1
    infile.close()
    
for lineno in filedict:
    if lineno < len(filedict):
        l = filedict[lineno]
        if competitor1_text in l:
            competitor1_bet = int(l.split(competitor1_text)[1])
            competitor1_bet_list.append(competitor1_bet)
        elif competitor2_text in l:
            competitor2_bet,hacker_bet = int(l.split(competitor2_text)[1].split(hacker_text)[0]),int(l.split(competitor2_text)[1].split(hacker_text)[1])

            if filedict[lineno+1] == "Win!":
                if (competitor1_bet * competitor2_bet == 1) and (hacker_bet == 0):
                    zardus_bet = 1
                elif (competitor1_bet * competitor2_bet == 1) and (hacker_bet == 1):
                    zardus_bet = 0
                elif (competitor1_bet * competitor2_bet == 0) and (hacker_bet == 0):
                    zardus_bet = 0
                elif (competitor1_bet * competitor2_bet == 0) and (hacker_bet == 1):
                    zardus_bet = 1
            elif filedict[lineno+1] == "Lose!":
                if (competitor1_bet * competitor2_bet == 1) and (hacker_bet == 0):
                    zardus_bet = 0
                elif (competitor1_bet * competitor2_bet == 1) and (hacker_bet == 1):
                    zardus_bet = 1
                elif (competitor1_bet * competitor2_bet == 0) and (hacker_bet == 0):
                    zardus_bet = 1
                elif (competitor1_bet * competitor2_bet == 0) and (hacker_bet == 1):
                    zardus_bet = 0
            else:
                print("LINE 40 ERROR!")
            if (competitor2_bet == 1) and (zardus_bet == 0):
                expected_qubit = 1
            elif (competitor2_bet == 1) and (zardus_bet == 1):
                expected_qubit = 0
            elif competitor2_bet == 0:
                expected_qubit = zardus_bet
            
            competitor2_bet_list.append(competitor2_bet)
            hacker_bet_list.append(hacker_bet)
            zardus_bet_list.append(zardus_bet)
            expected_qubit_list.append(expected_qubit)
            
            c2bl = convert2stringlist(competitor2_bet_list)
            eql = convert2stringlist(expected_qubit_list)
            zbs = convert2stringlist(zardus_bet_list)
            
            zardus_bets = ''.join(zbs)
            zardus_bases = ''.join(c2bl)
            zardus_qubits = ''.join(eql)
            
        elif adamd_text in l:
            if "-" not in l:
                adamd_bases += l.split(adamd_text)[1].split(":")[1]
            else:
                if "-1" in l:
                    nonce = l.split(adamd_text)[1].split(":")[1]
                elif "-2" in l:
                    ciphertext = l.split(adamd_text)[1].split(":")[1]
            
secret_key = ""

for zbet,zq,zb,ab in zip(list(zardus_bets),list(zardus_qubits),list(zardus_bases),list(adamd_bases)):
    if zb == ab:
        secret_key += zbet

print("SECRET_KEY:\t{}\nINTEGER:\t{}\n".format(secret_key,int(secret_key,2)))

ciphertext_bytes = bytes.fromhex(ciphertext)

skl = [int(x) for x in secret_key]
key = key_array_to_key_string(skl)
cipher = AES.new(key, AES.MODE_EAX, nonce=bytes.fromhex(nonce))
plaintext_bytes = cipher.decrypt(ciphertext_bytes)
try:
    plaintext = plaintext_bytes.decode('ascii')
except:
    plaintext = "INCORRECT"

if plaintext != "INCORRECT": #This will show the flag.
    print("KEY:  {}".format(key))
    print("FLAG: {}".format(plaintext))
    sys.exit()

print("{}.  TRY AGAIN.".format(plaintext))
