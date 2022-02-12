#!/usr/bin/python3
from datetime import datetime

'''
enumeration-201
~~~~~~~~~~~~~~~~~~~~~~~~
Different flags were hidden within the attached database file. The first one can be identified when you remove all the separators and the resulting text is exactly the same backwards and forwards.

The flag will be the four columns concatenated together with no spaces, e.g. onetwothreefour.
'''

def enum201(filename):
    with open(filename,'r') as infile:
        for line in infile:
            ll = line.strip().split(',')
            ls = ''.join(ll)
            if ls == ls[::-1]: #palindrome string
                return ls
            elif ll == ll[::-1]: #palindrome list
                return ''.join(ll)
        infile.close()

#print(enum201('enum-flags.csv'))

def enum202(filename):
    firsts_list = list()
    seconds_list = list()
    thirds_list = list()
    fourths_list = list()
    with open(filename,'r') as infile:
        for line in infile:
            ll = line.strip().split(',')
            firsts_list.append(ll[0])
            seconds_list.append(ll[1])
            thirds_list.append(ll[2])
            fourths_list.append(ll[3])
        infile.close()
    counter = 0
    for firsts in firsts_list:
        if (firsts in seconds_list) and (firsts in thirds_list) and (firsts in fourths_list):
            flag = firsts
    ind = firsts_list.index(flag)
    return firsts_list[ind]+seconds_list[ind]+thirds_list[ind]+fourths_list[ind]

#print(enum202('enum-flags.csv'))

def enum206(filename):
    oldcounter = 0
    with open(filename,'r') as infile:
        for x,line in enumerate(infile):
            change = 0
            if x != 0:
                line = line.strip()
                dt = datetime.fromtimestamp(int(line))
                if 
                dtl = dt.split(' ')[0].split('-')
                dtt = dt.split(' ')[1].split(':')
                if int(dtl[0]) == 2019:
                    if int(dtl[1]) == 8:
                        if int(dtl[2]) == 8:
                            if int(dtt[1]) == 19:
                                pass
                            elif int(dtt[1]) < 19:
                                change = 1
                        elif int(dtl[2]) < 8:
                            change = 1
                    elif int(dtl[1]) < 8:
                        change = 1
                elif int(dtl[0]) < 2019:
                    change = 1
                if change == 1:
                    oldcounter += 1
        infile.close()
    return oldcounter
enum206('enum-dates.csv')
