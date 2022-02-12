#!/usr/bin/python3

import binascii as ba
import random as rand

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
    print("Generating private key...")
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

def egcd(a,b):
    x,y,u,v = 0,1,1,0
    while a != 0:
        q,r = b//a, b%a
        m,n = x-u*q, y-v*q
        b,a,x,y,u,v = a,r,u,v,m,n
        gcd = b
    return gcd,x,y

if __name__ == '__main__':
    p = '0x00e0f26fc8aa4fcae7fb977c41c6b3e926a92746808703f3b92a3bdf80958f25eb4a6f5e19240e3affbf2546924b314d07baf7750c6f9a506133b8a0619b6af1c3'
    q = '0x00caab5cc90313f39293bcfb2bdee1351ee111d682cf397a04604980744bd764c565ca7a4ad47839b945e59153afacf3e4e902d3b7fbc4de7bc662c33406fee147'
    p = int(p[2:],16)
    q = int(q[2:],16)
    print(p,'\n',q)
    n = p * q
    phi_n = totient(p,q)
    attempt = 1
    while True:
        print("ATTEMPT {}...".format(attempt))
        attempt += 1
        print("Generating public key...")
        #elist = choosePrimes(2,phi_n,1)
        e = 4
        while not isPrime(e):
            e = rand.choice(range(2,65535))
        print("DONE!")
        pubkey = (e,n)
        #privkey = genPrivateKey(pubkey)
        i = 1
        while ((i*e) % n) != 1:
            i = rand.choice(range(2,65535))
        d = i
        privkey = (d,n)
        print("DONE!")
        if 31 < ((259**privkey[0]) % n) < 127:
            print("GOOD PRIVATE KEY FOUND!")
            break
        print("BAD PRIVATE KEY.  RETRYING...")

    decoded_string = ""
    with open('flag.txt','r') as infile: # Raw hex
        hexstring = ""
        for line in infile:
            hexstring += line.strip()
        infile.close()
        h = 0
        for i in range(2,len(hexstring)+2,2):
            print("INPUT: {}\nOUTPUT: {}".format(int(hexstring[h:i],16),decrypt(int(hexstring[h:i],16),privkey)))
            #decoded_string += chr(decrypt(int(hexstring[h:i],16),privkey))
            h = i
    print(decoded_string)
    '''
    #elist = choosePrimes(2,phi_n,1)
    #e = elist[0]
    # Will have to brute force e...
    #cont = input("Press ENTER to continue...")
    #elist = [p for p in range(2,65535) if isPrime(p)]
    #ct = int('018a978ac5b97b23e7a3f8277d0945de6b2a5c10b7e23ef8f908a6da6328a4ab8cd572e3417d70465ad4754a15b17366761eee47e52fae9911fb0a39020385571191d4fec2e86c108244b962403bc6918179614870680a2a5ad31a7631c10097957065112d8b176b9098a239bb386a93ca6af4c7083f3732a994f838bd546c52',16)
    for e in elist:
        gcd,a,b = egcd(e,phi_n)
        d = a
        #print("n: " + str(d))
        pt = pow(ct,d,n)
        print("pt: " + str(pt))
    '''
    '''
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
    '''
