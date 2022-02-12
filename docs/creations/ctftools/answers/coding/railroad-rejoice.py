'''
One of your team members intercepted this encoded message

l96s42496sg7so62hgfksaks369af5sl96s3dm6s3mad5af8

Luckily, they were previously able to intercept the algorithm used for encoding the original method (apparently this member never learned that it's not smart to create your own "encryption" method).

Using an alphabet of only these characters in this order':' "0123456789abcdefghijklmnopqrstuvwxyz ”, the algorithm does these things':'

1    If the position of the character in the string (with the first character in the string being in position 1) was divisible by 5, move the character forward 10 positions in his alphabet (wrapping around the alphabet if the end of the string was hit).
2    If the position of the character in the string was divisible by 9, move the character back 4 position in his alphabet (wrapping around to the other side of the alphabet if needed).
3    If the position of the character of the string had a remainder of 2 when dividing by 7, move the character forward 13 positions in his alphabet.
4    If the position of the character was even, move the character back 12 positions in his alphabet.
5    If the position of the character of the string had a remainder of 2 when dividing by 3, move the character forward 6 positions in his alphabet.
6    If the position of the character was odd, move the character forward 29 positions in his alphabet.

Do those manipulations in that order, and do as many as fit each character position.

Can you decode the text and find the original message, which we believe will help tell us where a cache of weapons are hid?
'''

chars = "0123456789abcdefghijklmnopqrstuvwxyz "
base_chars = chars

starting = 'l96s42496sg7so62hgfksaks369af5sl96s3dm6s3mad5af8'
#starting = "0123456789abcdefghijklmnopqrstuvwxyz "
ending = 'l96s42496sg7so62hgfksaks369af5sl96s3dm6s3mad5af8'

def move_forwards(i,star,chars,divisor,expected,move_distance):
    if i % divisor == expected:
        count = 0
        while count != move_distance:
            pos_in_chars = chars.index(star)
            next_pos = pos_in_chars + 1
            chars = chars[:pos_in_chars] + chars [next_pos:]
            new_chars = chars[:next_pos] + star + chars[next_pos:]
            print(new_chars)
            chars = new_chars
            count += 1
    return chars

def move_backwards(i,star,chars,divisor,expected,move_distance):
    if i % divisor == expected:
        count = 0
        while count != move_distance:
            pos_in_chars = chars.index(star)
            next_pos = pos_in_chars - 1
            chars = chars[:pos_in_chars] + chars [pos_in_chars+1:]
            new_chars = chars[:next_pos] + star + chars[next_pos:]
            print(new_chars)
            chars = new_chars
            count += 1
    return chars

def decipher(starting,chars):
    msg = str()
    for star in starting:
        pos_in_chars = chars.index(star)
        base_letter = base_chars[pos_in_chars]
        msg = msg + base_letter
    return msg

if __name__ == '__main__':
    for i,star in enumerate(starting):
#        print("\nSTEP 1\n")
        #STEP 1
#        chars = move_forwards(i,star,chars,5,0,10)
#        print("\nSTEP 2\n")
        #STEP 2
#        chars = move_backwards(i,star,chars,9,0,4)
#        print("\nSTEP 3\n")
        #STEP 3
#        chars = move_forwards(i,star,chars,7,2,13)
#        print("\nSTEP 4\n")
        #STEP 4
#        chars = move_backwards(i,star,chars,2,0,12)
#        print("\nSTEP 5\n")
        #STEP 5
#        chars = move_forwards(i,star,chars,3,2,6)
#        print("\nSTEP 6\n")
        #STEP 6
#        chars = move_forwards(i,star,chars,2,1,29)
        print("\nSTEP 6\n")
        #STEP 6
        chars = move_backwards(i,star,chars,2,1,29)
        print("\nSTEP 5\n")
        #STEP 5
        chars = move_backwards(i,star,chars,3,2,6)
        print("\nSTEP 4\n")
        #STEP 4
        chars = move_forwards(i,star,chars,2,0,12)
        print("\nSTEP 3\n")
        #STEP 3
        chars = move_backwards(i,star,chars,7,2,13)
        print("\nSTEP 2\n")
        #STEP 2
        chars = move_forwards(i,star,chars,9,0,4)
        print("\nSTEP 1\n")
        #STEP 1
        chars = move_backwards(i,star,chars,5,0,10)
    #DECIPHER
    msg = decipher(ending,chars)
    print(msg)
