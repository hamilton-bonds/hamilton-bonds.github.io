'''
CAESAR CYPHER
 1. Takes an string input from user
 2. Takes an offset value as input
 3. Performs the operation on the string user input
 4. Returns the CCypher'd text
'''

def caesarEncode(string,offset=13):
    caesare = ''
    al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    if offset >= 52:
        while offset >= 52:
            offset -= 52
    newal = al[offset:] + al[:offset]
    for char in string:
        caesare = caesare + newal[al.index(char)]
    return caesare

def caesarDecode(string,offset=13):
    caesard = ''
    al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    if offset >= 52:
        while offset >= 52:
            offset -= 52
    newal = al[offset:] + al[:offset]
    for char in string:
        caesard = caesard + al[newal.index(char)]
    return caesard

if __name__ == '__main__':
    st = input("What do you want to encode? ")
    ce = caesarEncode(st)
    print(ce)
    cd = caesarDecode(ce)
    print(cd)
