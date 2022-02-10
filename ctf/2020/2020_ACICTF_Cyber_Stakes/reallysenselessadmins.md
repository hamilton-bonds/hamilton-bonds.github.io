## [35] Really Senseless Admins (Cryptography)

### Prompt:
We fired Julius, but the new guy apparently misplaced the file with our pivate key. All he could find was the encrypted flag and some file labeled 'params'. flag.enc params.txt

### Initial Analysis:
We see the following content inside of params.txt:

```
$cat params.txt 
p = 254937310238208291646070756202860841079050569358962531263386166539215047822636688779860990409771843546565149125185655063576840655394994646211935067246465030325112235680733783798964511566995937259426508073269564816311010485486428777916419188356641278309495831305670847530259907034629302646895577541520415984667
q = 201527490583048374118399563067551781909214089147418803365066217013094917936585644189639597827127551746357691085065660000107897994151501253043547182809049438725535695589118056707580132966560406675561187564662424545560984591448339586890655239830605409553807738203732500983321821330530783341354047239347065201911
e = 82673630939154540737332448962792509162965479788901382135850578191063941371117
```

Hooray, it's RSA!

Not only that, it's a relatively small number.

RSA leverages properties of prime numbers to institute simple and unique encryption.  Its math is explained below:

Given two distinct primes, _p_ and _q_, **_n_ = _p_ x _q_** [Eq. 1] and the totient is **_phi_ = (_p_-1)(_q_-1)** [Eq. 2].  Also, _e_ is the public key exponent integer chosen where **1 < e < phi** such that gcd(e,phi) == 1 and _d_ is the private key exponent integer chosen where **1 < d < phi** such that **e x d == 1 % phi**.

Additionally, since **_cipher_ = _plaintext_ ^ _e_ % _n_** [Eq. 3] then one may decrypt with the private key as such **_plaintext_** = _cipher_^_d_ % _n_** [Eq. 4].

### Solution:
Now, there's a philosophy I think is important with cryptography: never use your own processing power if you don't have to.
Simply searching the Internet for "decrypt RSA online", the first link we should come across that allows manual entry of p, q and e values is [this](https://www.cryptotool.org/rsa-step-by-step).  This is the quickest route to the flag.

If, however, you feel like braving the computing elements on your own, prepare to wait a substantial amount of time.  This is all you need to do:

Compute d, then execute Equation 4 with the ciphertext number in flag.enc.  Convert the number to hex, then to raw, and you have the flag.

END
