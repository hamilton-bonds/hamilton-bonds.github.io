#!/usr/bin/python3
#~~~~% OF THE HIGHEST SECRECY OF THE ATROPIAN GOVERNMENT %~~~~#
#~~~~% ATROPIAN ENCRYPTION ALGORITHM - NO FOREIGNERS!!!! %~~~~#

import random as rand
import os
import sys

rand.seed()
r = rand.SystemRandom()

keylen = 16 # in bytes

def encryptFile(hc):
    '''Encrypts using gpg'''
    os.system("gpg --yes --batch --passphrase={} -c encthis.txt".format(hc))

def decryptFile(hc):
    '''Decrypts using gpg (import this to your code)'''
    os.system("gpg --yes --batch --passphrase={} -o flag.txt --decrypt encthis.txt.gpg".format(hc))
    os.system("cat flag.txt")

def makeButtonSet():
    '''Generates all possible combinations of buttons on the 16x16 board'''
    buttonArray = list()
    for i in range(256):
        h = hex(i)[2:]
        if len(h) < 2:
            h = "0" + h
        buttonArray.append(h)
    return set(buttonArray)

def generateButtonComboHash(buttonSet):
    '''Generates the initial button combo and its initial encoding.'''
    buttonComboHash = ''
    buttonArray = list(buttonSet)
    encodedButtonCombo = list()
    expectedButtonCombo = list()
    for x in range(keylen):
        ba_copy = buttonArray[:]
        button = ba_copy[rand.randint(0,255)]
        expectedButtonCombo.append(button)
        ba_copy.remove(button)
        encodedButtonCombo.append(rand.choice(ba_copy))
    return ''.join(encodedButtonCombo),''.join(expectedButtonCombo)

def forgotPassword(expectedButtonCombo,buttonSet):
    '''Produces another encoded combo in case you forgot the first.'''
    a = 0
    ba_copy = list(buttonSet)
    encodedButtonCombo = list()
    for b in range(2,(keylen*2)+1,2):
        examineButton = expectedButtonCombo[a:b]
        choice = findNotButton(examineButton,encodedButtonCombo)
        encodedButtonCombo.append(choice)
        a = b
    ebcstring = ''.join(encodedButtonCombo)
    if len(ebcstring) == keylen*2:
        print(ebcstring)
    else:
        forgotPassword(expectedButtonCombo,buttonSet)

def findNotButton(examineButton,ba_copy):
    '''Aids in the creation of a key. See forgotPassword'''
    chosen_hex = hex(rand.randint(0,255))[2:]
    if chosen_hex != examineButton:
        choice = chosen_hex
    else:
       choice = findNotButton(examineButton,ba_copy)
    return choice

def processOptions(opt_list,guess):
    '''Takes user input (guess) and pits it against the expected value'''
    bas = makeButtonSet()
    enbc,exbc = generateButtonComboHash(bas)
    encryptFile(exbc)
    tries = 0
    #print(exbc) #Uncomment to receive feedback in the ns_solution.py commented section
    while True:
        if tries == 0:
            pass
        elif tries == 3:
            tries = 0
            print("ATTEMPTS RESET")
        for opt in opt_list:
            if opt in "Yy":
                tries += 1
                comparison = processGuess(guess,exbc)
                if comparison == '1111111111111111':
                    decryptFile(exbc)
                return comparison
            elif opt in "Nn":
                return "QUITTING..."
            elif opt in "Ff":
                forgotPassword(exbc,bas)
            else:
                print("INVALID OPTION")
    return "QUITTING..."

# OPTIONAL functions
def processGuess(inputted,expectedButtonCombo):
    '''Processes keylen*8-bit user input and expectedButtonCombo'''
    if len(inputted) == (keylen*2):
        inlist = list(inputted)
        exlist = list(expectedButtonCombo)
        ilist = list()
        elist = list()
        for n in range(keylen):
            inx = ''
            enx = ''
            inx += inlist.pop(0)
            inx += inlist.pop(0)
            enx += exlist.pop(0)
            enx += exlist.pop(0)
            ilist.append(inx)
            elist.append(enx)
        return compareHex(ilist,elist)
    else:
        print("I'll stop you right there, that's just plain wrong to begin with.")

def compareHex(inlist,exlist):
    '''Gives the operator feedback on correctly guessed bytes'''
    retbin = ''
    for a,b in zip(inlist,exlist):
        if a == b:
            retbin += '1' # Correctly-guessed byte
        else:
            retbin += '0' # Incorrectly-guessed byte
    return retbin

######### MAIN PROGRAM #########
if __name__ == '__main__':
    ''' USAGE: ./nuclearsavior.py "opt1:opt2" "guess" '''
    opt_list = sys.argv[1].split(':')
    guess = sys.argv[2]
    response = processOptions(opt_list,guess)
    print(response)
