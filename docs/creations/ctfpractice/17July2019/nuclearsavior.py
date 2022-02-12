#~~~~% OF THE HIGHEST SECRECY OF THE ATROPIAN GOVERNMENT %~~~~#
#~~~~% ATROPIAN ENCRYPTION ALGORITHM - NO FOREIGNERS!!!! %~~~~#
'''DEV NOTES, MUST PRODUCE: 4174726f7069615375706572696f720a'''
expected = "4174726f7069615375706572696f720a"

import random as rand
import os

def encryptFile(hc):
    os.system("gpg --yes --batch --passphrase={} -c flag.txt".format(hc))

def decryptFile(hc):
    os.system("gpg --yes --batch --passphrase={} -d flag.txt.gpg".format(hc))
    os.system("cat flag.txt")

def makeButtonArray():
    buttonArray = list()
    for i in range(256):
        h = hex(i)[2:]
        if len(h) < 2:
            h = "0" + h
        buttonArray.append(h)
    return buttonArray

def generateButtonComboHash(buttonArray):
    buttonComboHash = ''
    encodedButtonCombo = list()
    expectedButtonCombo = list()
    for x in range(16):
        ba_copy = buttonArray[:]
        button = ba_copy[rand.randint(0,255)]
        expectedButtonCombo.append(button)
        ba_copy.remove(button)
        encodedButtonCombo.append(rand.choice(ba_copy))
    return ''.join(encodedButtonCombo),''.join(expectedButtonCombo)

def getIO(inputted,expected):
    '''Processes 128-bit user input'''
    try len(inputted) == 32:
        inlist = list(inputted)
        exlist = list(expected)
        ilist = list()
        elist = list()
        for n in range(16):
            inx = ''
            enx = ''
            inx += inlist.pop(0)
            inx += inlist.pop(0)
            enx += exlist.pop(0)
            enx += exlist.pop(0)
            ilist.append(inx)
            elist.append(enx)
    except lengthError:
        print("I'll stop you right there, that's just plain wrong to begin with.")

def compareHex(inlist,exlist):
    '''Gives the operator feedback on correctly guessed bytes'''
    retbin = ''
    for a,b in zip(inlist,exlist):
        if a == b:
            retbin += '1'
        else:
            retbin += '0'
    return retbin
###ISSUES:  Starting out with flag.txt.gpg...and letting the program deal with it without giving away the answer.
def processGuess(guess,expectedButtonCombo):
    ba = makeButtonArray()
    enbc,exbc = generateButtonComboHash(ba)
    tries = 0
    while tries < 3:
        pass
    print(ans)
