## [75] Move ZIG (Miscellaneous)

### Prompt:
CATS is back at it on challenge.acictf.com:47912. Only this time he's throwing 500 problems at you. If you didn't use a program to solve the last one, you'll probably want this...

### Initial Analysis:
This is the same problem as [All Your Base Are Belong To Us - 50](https://rbf-shadowhunter.github.io/ctf/2020_ACICTF_Cyber_Stakes/allyourbase.html)

Except, we need to change a few things...(changes have [CHANGE] in comments)  I included the All Your Base writeup for convenience.

### Solution:
We'll be using the following setup before diving into the program:
```
import socket
import binascii as ba
import base64

ipaddr = '160.1.153.245'
port = 47912 #[CHANGE] port number

delimiter = '------------------------------------------------------------------------------'
```

Let's build the client first.

```
if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ipaddr,port))
    global f
    f = sock.makefile()
```

Then, we should focus on how to iterate through problems.  We want to cut up the text so that we have the right information.  Comments explain how the code divides the server's response.

```
if __name__ == '__main__':
...
    question_amount = 500 #[CHANGE] We now have to answer 500 questions correctly.
    counter = 0
    while counter <= question_amount:
        f = sock.recv(4096)
        print("PROBLEM #{}".format(counter+1))
        line = f.decode('ascii').strip()
        print("~~~\n\n{}\n\n~~~\n".format(line))
        question = line.split(delimiter)[1] # We want the part of the response that contains the bases
        start = question.split(' -> ')[0].strip() # FROM base
        end = question.split(' -> ')[1][:3].strip() # TO base
        base_text = question.split(' -> ')[1][3:] # This is the information that the server wants you to convert.
        conversion = main(base_text,start,end)
        conversion += "\n"
        sock.send(bytes(conversion.encode('ascii')))
        print("SENT {}.".format(conversion))
        counter += 1
...
```

From here, let's build our conversion functions, keeping in mind that we chose hex as our default base:

```
def raw2hex(base_text):
    base_text = base_text.strip()
    hc = ba.hexlify(base_text.encode('ascii'))
    return hc
    
def raw2bin(base_text):
    return ''.join(format(ord(i),'b') for i in base_text)
    
def hex2raw(hc):
    conversion = str(ba.unhexlify(hc),'ascii')
    return conversion
    
def b642hex(base_text):
    data = base64.b64decode(base_text)
    hc = raw2hex(str(data,'ascii'))
    return hc

def hex2b64(hc):
    data = hex2raw(hc)
    conversion = base64.b64encode(data.encode('ascii')).decode('ascii')
    return conversion

def raw2b64(raw):
    conversion = base64.b64encode(raw.encode('ascii')).decode('ascii')
    return conversion

def dec2hex(base_text):
    hc = hex(int(base_text))[2:]
    return hc
    
def hex2dec(hc):
    conversion = int(hc,16)
    return conversion
    
def oct2hex(base_text):
    hc = hex(int(base_text,8))[2:]
    return hc

def hex2oct(hc):
    conversion = oct(int(hc,16))[2:]
    return conversion
    
def bin2hex(base_text):
    hc = hex(int(base_text,2))[2:]
    return hc

def hex2bin(hc):
    conversion = bin(int(hc,16))[2:]
    return conversion
```

(As a quick aside, I had to Frankenstein some extraneous conversion functions for on-the-fly debugging.  Try to package this a lot better than I did.)

Additionally, we paired base conversions for quicker reference in case of debugging.

Finally, let's build the main function to handle the parsed server response and output a conversion answer.

```
def main(base_text,start,end):
    if start == 'raw':
        ''' # This is where I had to 'Frankenstein' my main
        if end == 'b64':
            conversion = raw2b64(base_text)
        elif end == 'bin':
            conversion = raw2bin(base_text)
        else:
            hc = raw2hex(base_text)
        '''
        hc = raw2hex(base_text)
    elif start == 'b64':
        hc = b642hex(base_text)
    elif start == 'dec':
        hc = dec2hex(base_text)
    elif start == 'oct':
        hc = oct2hex(base_text)
    elif start == 'bin':
        hc = bin2hex(base_text)
    elif start == 'hex':
        hc = bytes(base_text.strip().encode('ascii'))
    if len(hc) % 2 != 0:
        hc = '0' + hc
    if end == 'raw':
        conversion = hex2raw(hc)
    elif end == 'b64':
        conversion = hex2b64(hc)
    elif end == 'dec':
        conversion = hex2dec(hc)
    elif end == 'oct':
        conversion = hex2oct(hc)
    elif end == 'bin':
        conversion = hex2bin(hc)
    elif end == 'hex':
        if type(hc) == type(bytes()):
            conversion = hc.decode('ascii')
        else:
            conversion = hc
    elif start == 'raw' and end == 'b64':
        conversion = raw2b64(base_text)
    elif start == 'raw' and end == 'bin':
        conversion = raw2bin(base_text)
    return str(conversion)
```

See, there's some value in writing code to automate the process!  After answering all questions correctly, you get the flag!

END
