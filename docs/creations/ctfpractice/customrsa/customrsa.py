#!/usr/bin/python3

import random as rand
import binascii as ba

def isPrime(num):
    for n in range(2,num):
        if num % n == 0:
            return False
    return True

def choosePrimes(start,end,amount):
    ps = [p for p in range(start,end) if isPrime(p)]
    plist = list()
    for i in range(amount):
        plist.append(rand.choice(ps))
    return plist

def totient(numa,numb):
    return ((numa-1)*(numb-1))

def rsa(start,end):
    plist = choosePrimes(start,end,2)
    pna = plist[0]
    pnb = plist[1]
    n = pna * pnb
    phi_n = totient(pna,pnb)
    elist = choosePrimes(2,phi_n,1)
    e = elist[0]
    return (e,n)

def genPrivateKey(pubkey):
    e = pubkey[0]
    n = pubkey[1]
    dlist = list()
    for i in range(2,n):
        if ((i*e) % n) == 1:
            dlist.append(i)
    try:
        d = rand.choice(dlist)
    except IndexError:
        print('dlist is empty')
    return (d,n)

def encrypt(m,pubkey):
    e = pubkey[0]
    n = pubkey[1]
    return ((m**e) % n)

def decrypt(c,privkey):
    d = privkey[0]
    n = privkey[1]
    return ((c**d) % n)

if __name__ == '__main__':
    global pubkey
    pubkey = rsa(100,200)
    privkey = genPrivateKey(pubkey)
    msg = ""
    while msg != "/exit":
        msg = input("Type message: ")
        rsa = ""
        for char in msg:
            ic = int(ba.hexlify(char.encode('ascii')),16)
            ac = ba.unhexlify(hex(ic))
            nc = ac.decode('ascii')
            rsa += nc
        print("MSG: ",msg)
        print("RSA: ",rsa)
