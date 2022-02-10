---
title: "[50] All Your Base Are Belong To Us (Miscellaneous)"
layout: template
filename: allyourbase.md
---

## [50] All Your Base Are Belong To Us (Miscellaneous)

### Prompt:
In honor of 30 years of terrible translations, we figured we'd give you a try at a series of (easier) translation problems. All you have to do is to translate bases by connecting to challenge.acictf.com:55350. In case you're new to network programs, we even have some Python starter code you can use. (NOTE: Your port may be different)

### Initial Analysis:
We are tasked to convert between the following bases (nc 160.1.153.245 55350):
```
...
          raw = the unencoded ASCII string (contains only printable characters
                    that are not whitespace)
          b64 = standard base64 encoding (see 'base64' unix command)
          hex = hex (base 16) encoding (case insensitive)
          dec = decimal (base 10) encoding
          oct = octal (base 8) encoding
          bin = binary (base 2) encoding (should consist of ASCII '0' and '1')
...
```

This means we'll have to account for all 2**6 (64) combinations of conversions, which can is easily accomplished if we choose a default base and just convert to any base from there.  Let's choose hex as our default base.  Also, we're going to automate the process because it avoids timeouts and is more efficient.

### Solution:
We'll be using the following setup before diving into the program:
```
import socket
import binascii as ba
import base64

ipaddr = '160.1.153.245'
port = 55350

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
    question_amount = 5 # We only have to answer 5 questions correctly.
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

After answering all questions correctly, you get the flag!

END
