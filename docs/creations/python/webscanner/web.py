#This scans dns servers and web pages for SQL databases.
#Created by shadowhunter 03/30/2018

import os

#Create Octet list

octs = [0,0,0,0]

def getips():
    finished = 0
    while finished == 0:
        first = octs[0]
        second = octs[1]
        third = octs[2]
        fourth = octs[3]
        while octs[0] != 256:
            while octs[1] != 256:
                while octs[2] != 256:
                    while octs[3] != 256:
                        ipold = str(octs[0])+"."+str(octs[1])+"."+str(octs[2])+"."+str(octs[3])
                        ipaddr = ipold.strip()
                        command = "dig " + ipaddr
                        os.system(command)
                        octs[3] += 1
                    octs[3] = 0
                    octs[2] += 1
                octs[2] = 0
                octs[1] += 1
            octs[1] = 0
            octs[0] += 1
        finished = 1

if __name__ == '__main__':
    getips()
