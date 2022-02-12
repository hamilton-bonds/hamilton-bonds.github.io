#!/usr/bin/python3
'''
Decode the Secret Cow's Message: pmoorBmomoooMnErxDBKuDnLxF0nlxwKHOrAnL2Omooouj
'''
import itertools as it

decodeme = 'pmoorBmomoooMnErxDBKuDnLxF0nlxwKHOrAnL2Omooouj'
alphabet = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

class Cow():
    def __init__(self,cowkey="moo",totalcows=5,message=""):
        self.ckey = cowkey
        self.cows = totalcows
        self.msg = message

    def RshiftCow(self):
        shift = len(self.msg)//2
        self.msg = self.msg[shift:] + self.msg[:shift]

    def RrotateCow(self):
        rotate = len(self.msg)//4
        newstr = ""
        for char in self.msg:
            newindex = alphabet.index(char)+rotate
            if newindex > len(alphabet)-1:
                newindex -= 52
            newstr += alphabet[newindex]
        self.msg = newstr

    def RreplaceCow(self):
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

    def RaddCow(self):
        loc = (len(self.msg)-len(self.ckey))//self.cows
        print(loc)
        self.msg = self.msg[:loc] + self.msg[loc+len(self.ckey):]
        print("RaddCow:\t",self.msg)

    def decrypt(self,enc_msg):
        self.msg = enc_msg
        self.RaddCow()
        self.RreplaceCow()
        self.RshiftCow()
        self.RrotateCow()


if __name__ == '__main__':
    flagCow = Cow()
    print("ORIGINAL:\t",decodeme)
    flagCow.decrypt(decodeme)
    print(flagCow.msg)
