#  Best Cyber Warrior 2022 - US » SONNET 47

## Prompt
Category: Cryptography
Level: easy
Points: 50
Description

Our intelligence team intercepted a strange stream of data, can you help us to understand what is it?
0110101100001000000101000100100001000000011000001000111000000110000110001001011001101100111000001010010000010100100

## Analysis
In my analysis, I searched for Shakespeare's Sonnet 47:
```
47

Betwixt mine eye and heart a league is took,
And each doth good turns now unto the other.
When that mine eye is famished for a look,
Or heart in love with sighs himself doth smother,
With my love’s picture then my eye doth feast
And to the painted banquet bids my heart.
Another time mine eye is my heart’s guest
And in his thoughts of love doth share a part.
So, either by thy picture or my love,
Thyself away are present still with me;
For thou no farther than my thoughts canst move,
And I am still with them, and they with thee;
Or, if they sleep, thy picture in my sight
Awakes my heart to heart’s and eye’s delight.
```

However, following this path to its apparent solution is a dead end.  I had attempted every breakup of bits and bytes in the data stream to splice characters from the sonnet to make a message to no avail.  Then, I went back to the drawing board for a better solution.  I typed in "Shakespeare Cipher" and the first result on DuckDuckGo was "Bacon's cipher".  Scrolling through the Wikipedia page, the cipher seemed to make use of alternating sequences of A's and B's to form a message.

## Solution
I ran the stream through Python:
```
Python 3.9.12 (main, Mar 24 2022, 13:02:21) 
[GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> binary = "0110101100001000000101000100100001000000011000001000111000000110000110001001011001101100111000001010010000010100100"
>>> for b in binary:
...     a
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'a' is not defined
>>> ab = ""
>>> ba = ""
>>> for b in binary:
...     if b == "0":
...         ab += "A"
...         ba += "B"
...     else:
...         ab += "B"
...         ba += "A"
... 
>>> ab
'ABBABABBAAAABAAAAAABABAAABAABAAAABAAAAAAABBAAAAABAAABBBAAAAAABBAAAABBAAABAABABBAABBABBAABBBAAAAABABAABAAAAABABAABAA'
```

This translates to the flag content: `ONEBITCANCHANGEYOURLIFE`
