#!/usr/bin/python3
'''
Decode the Secret Cow's Message: pmoorBmomoooMnErxDBKuDnLxF0nlxwKHOrAnL2Omooouj
'''
import itertools as it

alphabet = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

class Cow():
    def __init__(self,cowkey="moo",totalcows=5,message=""):
        self.ckey = cowkey
        self.cows = totalcows
        self.msg = message

    def shiftCow(self):
        shift = len(self.msg)//2
        self.msg = self.msg[shift:] + self.msg[:shift]

    def rotateCow(self):
        rotate = len(self.msg)//4
        newstr = ""
        for char in self.msg:
            newindex = alphabet.index(char)+rotate
            if newindex > len(alphabet)-1:
                newindex -= 52
            newstr += alphabet[newindex]
        self.msg = newstr

    def replaceCow(self):
        letterlist = list(self.msg)
        while True:
            if "m" in letterlist:
                letterlist.remove("m")
            elif "o" in letterlist:
                letterlist.remove("o")
            else:
                break
        chosen = self.msg[len(self.msg)//8]
        while chosen in self.msg:
            self.msg = self.msg[:self.msg.index(chosen)] + self.ckey + self.msg[self.msg.index(chosen)+1:]

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
