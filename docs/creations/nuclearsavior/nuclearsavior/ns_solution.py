#!/usr/bin/python3
'''
You may have to run this program a few times to get the flag.
'''
import sys
import subprocess as sp
import itertools as it
import numpy as np
from nuclearsavior import decryptFile

keylen = 16 # in bytes

def makeButtonSet():
    '''Generates all possible combinations of buttons on the 16x16 board'''
    buttonArray = list()
    for i in range(256):
        h = hex(i)[2:]
        if len(h) < 2:
            h = "0" + h
        buttonArray.append(h)
    return set(buttonArray)

def interactWithButtonPanel():
    '''Reads the printed response of stdout and formats into list of responses'''
    num_forgotPass = int(sys.argv[1])
    options = "F:" * num_forgotPass + "N"
    guess = ""

    proc = sp.Popen(["./nuclearsavior.py","{}".format(options),"{}".format(guess)],stdout=sp.PIPE)
    out = proc.communicate()[0]
    decoded_out = out.decode("utf-8")
    do_list = decoded_out.split('\n')
    do_list.pop()
    do_list.pop()
    return do_list

def interactWithResults(do_list):
    '''Aggregates the many forgotPassword responses and formats them for processing'''
    """
    # For testing only:
    solution = do_list[0]
    do_list = do_list[1:]
    """

    buttonDict = dict()
    for i in range(keylen):
        buttonDict[i] = [set(),set()]

    for x,do in enumerate(do_list):
        print(do)
        a = 0
        for b in range(2,(keylen*2)+1,2):
            buttonDict[a//2][0].add(do[a:b])
            a = b
    """
    print("\n\n###################################\n\n")
    print("sol:\t",solution)
    print("\n\n###################################\n\n")
    """
    totalcombos = 1
    for key in buttonDict:
        for b in bs:
            if b not in buttonDict[key][0]:
                buttonDict[key][1].add(b)
        #print(key,":\t",' '.join(list(buttonDict[key][1])))
        buttonDict[key][1] = list(buttonDict[key][1])
    result = dnm(buttonDict)
    return result

def combos(subject,additive,expected_len):
    newsubject = dict()
    nextsubject = dict()

    newkey = 0
    for key in subject:
        sstr = subject[key]
        for astr in additive:
            if astr not in sstr:
                sstr.append(astr)
                sstr_copy = sstr[:]
                newsubject[newkey] = sstr_copy
                sstr.remove(astr)
                newkey += 1

    newerkey = 0
    for nslkey in newsubject:
        nsl = newsubject[nslkey]
        if len(nsl) == expected_len:
            nextsubject[newerkey] = nsl
            newerkey += 1
    return nextsubject

def dnm(buttonDict):
    probmat = list()
    for key in buttonDict:
        probmat.append(buttonDict[key][1])
    cartmat = setter(probmat)
    attemptDecrypt(cartmat)

def setter(matrix):
    nl = list()
    bl = list()
    maxlen = 0
    for row in matrix:
        if len(row) > maxlen:
            maxlen = len(row)
    for row in matrix:
        if len(row) == maxlen:
            for col in row:
                lcol = list()
                lcol.append(col)
                if (lcol not in bl) and (lcol not in nl):
                    nl.append(lcol)
                elif (lcol not in bl) and (lcol in nl):
                    nl.remove(lcol)
                    bl.append(lcol)
        else:
            nl.append(row)
    newerl = list(it.product(*nl))
    newestl = list()
    for newl in newerl:
        newestl.append(''.join(list(newl)))
    return newestl

def attemptDecrypt(probmat):
    for prob in probmat:
        if len(prob) == (keylen*2):
            decryptFile(prob)

######### MAIN PROGRAM #########
if __name__ == '__main__':
    bs = makeButtonSet()
    do_list = interactWithButtonPanel()
    interactWithResults(do_list)
