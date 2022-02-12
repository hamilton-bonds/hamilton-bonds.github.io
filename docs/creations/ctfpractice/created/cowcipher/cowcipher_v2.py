#!/usr/bin/python3
'''
Decode the Secret Cow's Message.  This program encodes the message.
'''
import itertools as it

alphabet = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
alphahex = dict()

for char in alphabet:
    alphahex[char] = hex(ord(char))[2:]

class Cow():
    def __init__(self,cowkey="moo",totalcows=5,message=""):
        self.ckey = cowkey
        self.cows = totalcows
        self.msg = message
        self.mhl = list()

    def hexxit(self):
        self.mhl = [alphahex[x] for x in self.msg]
        return 0

    def shiftCow(self):
        shift = len(self.msg)//2
        self.msg = self.msg[shift:] + self.msg[:shift]
        return 0

    def rotateCow(self):
        rotate = len(self.msg)//4
        rotmap = [[orig,rot] 
        newstr = ""
        for char in self.msg:
            newindex = alphabet.index(char)+rotate
            if newindex > len(alphabet)-1:
                newindex -= 52
            newstr += alphabet[newindex]
        self.msg = newstr

    def replaceCow(self):
        letterlist = list(self.msg)
        message_len = len(self.msg)
        for i in range(message_len):
            if (i % totalcows == 0) and (i != 0):
                hexlist[i] = self.ckey

    def addCow(self):
        loc = len(self.msg)//self.cows
        self.msg = self.msg[:loc] + self.ckey + self.msg[loc:]

    def encrypt(self,message):
        self.msg = message
        self.rotateCow()
        self.shiftCow()
        self.replaceCow()
        self.addCow()

    def decrypt(self):
        pass

if __name__ == '__main__':
    flagCow = Cow()
    flag = "ReconByFireCTF flag is DeviousBlueCow"
    flagCow.encrypt(flag)
    print(flagCow.msg)
