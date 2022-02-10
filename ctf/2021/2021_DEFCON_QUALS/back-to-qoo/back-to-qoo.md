## BACK TO QOO

### Prompt:
You are pulled back to QOO again. QOO or OOO? Whatever.

back-to-qoo.challenges.ooo 5000

Files:

- [backend.py](https://rbf-shadowhunter.github.io/ctf/2021_DEFCON_QUALS/back-to-qoo/backend.py) f34c0ad16638ed67930893b8fc61abc50b98c8b00d761766cc8afb3525ae6a4d
- [coin.py](https://rbf-shadowhunter.github.io/ctf/2021_DEFCON_QUALS/back-to-qoo/coin.py) 9b0a37309482c2e506d16bbd228af4c79884318f2b00c1da1c9b05ec246db9b7
- [game.py](https://rbf-shadowhunter.github.io/ctf/2021_DEFCON_QUALS/back-to-qoo/game.py) c3eb4d4aef967091023a66f7db6785356543c96639b3687ef1433b09e2fd39b1
- [players.py](https://rbf-shadowhunter.github.io/ctf/2021_DEFCON_QUALS/back-to-qoo/players.py) 205c1aaf464011edb413b8237e61050178ded9bbaf0891e1f7e7bd39da84645a
- [service.py](https://rbf-shadowhunter.github.io/ctf/2021_DEFCON_QUALS/back-to-qoo/service.py) 12923244ae4e66fc3d23c0b276bb47618eca26d91075f7020e7c7a7ce6b35f58

### Initial Analysis:
After downloading and examining each file, we quickly realize that there's not much difference between this problem and [qoo-or-ooo](https://rbf-shadowhunter.github.io/ctf/2021_DEFCON_QUALS/qoo-or-ooo/qoo-or-ooo.html).  Review that problem for the rest of the analysis.

### Solution:
Of course, you could use the same methods as in qoo-or-ooo and achieve the same results, but what if you have no clue where to start?  Before we get going, here's the full files used for the solution.

- [interact.py](https://rbf-shadowhunter.github.io/ctf/2021_DEFCON_QUALS/back-to-qoo/interact.py)
- [output.txt](https://rbf-shadowhunter.github.io/ctf/2021_DEFCON_QUALS/back-to-qoo/output.txt)
- [process.py](https://rbf-shadowhunter.github.io/ctf/2021_DEFCON_QUALS/back-to-qoo/process.py)

Suppose you come into the problem with no well-defined method for approaching this problem (like selecting a rotation based on our competitor's bet), what do you try next?

Now, according to the rules of the CTF, you can't just brute-force spam/scan, so this makes your job much more time-consuming, but you can feed a pre-determined set of answers, line-by-line into netcat.  If you know what options you want to choose ahead of time (2 for qoin and 0,1, or 2 for type of rotation or no rotation), you can place them in a file as such:
```
2
0
2
1
2
0
2
2
...
```
for as many iterations as you want.  Then, you run the command `nc back-to-qoo 5000 < myinputs.txt`.

This is inefficient, as you won't know how to manipulate your qoin to achieve an 85% win rate - you'll have to get lucky.  If you leave this program up and sleep (bash: sleep) between iterations to avoid spamming the CTF problem, you can work on other things and eventually (or not) get a win.  If you do, you'll still need to use process.py to find the flag.  Happy hunting!

## Annexes
### Annex A: XOR bit map
```
+---+---+---+
|    XOR    |
+---+---+---+
| A | B | X |
+---+---+---+
| 0 | 0 | 0 |
+---+---+---+
| 0 | 1 | 1 |
+---+---+---+
| 1 | 0 | 1 |
+---+---+---+
| 1 | 1 | 0 |
+---+---+---+
```

## References
- A. https://tqsd.github.io/QuNetSim/examples/quantum_coin_flipping.html
- B. https://tqsd.github.io/QuNetSim/examples/QKD.html
- C. https://tqsd.github.io/QuNetSim/examples/chsh.html
- D. https://en.wikipedia.org/wiki/CHSH_inequality

END
