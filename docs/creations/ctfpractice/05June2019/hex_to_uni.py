#This python program will convert hex to unicode (utf-8)

def hexToUni(filename):
    with open(filename,'r') as infile:
        for x,line in enumerate(infile):
            if x != 0:
                print(line.decode('utf-16be',errors='ignore'))
    return 0
    pass

if __name__ == '__main__':
    fil = input("Filename: ")
    uniout = hexToUni(fil)
    print(uniout)
