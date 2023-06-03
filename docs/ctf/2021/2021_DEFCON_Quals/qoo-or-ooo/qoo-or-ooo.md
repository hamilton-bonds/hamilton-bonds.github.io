## QOO or OOO?

### Prompt:
This is another QOO's challenge. Wait, is this QOO or OOO?

qoo-or-ooo.challenges.ooo 5000

Files:

- [backend.py](https://rbf-shadowhunter.github.io/ctf/2021_DEFCON_QUALS/qoo-or-ooo/backend.py) f34c0ad16638ed67930893b8fc61abc50b98c8b00d761766cc8afb3525ae6a4d
- [coin.py](https://rbf-shadowhunter.github.io/ctf/2021_DEFCON_QUALS/qoo-or-ooo/coin.py) 4e812503ab73aaf7dd66e6302e01202845f8f1307232761f03baedbe3bc34cba
- [game.py](https://rbf-shadowhunter.github.io/ctf/2021_DEFCON_QUALS/qoo-or-ooo/game.py) 3d9158498c4272761e82e6f9fa9192cfa884d3d350ec01a2bb3873e46b0e3058
- [players.py](https://rbf-shadowhunter.github.io/ctf/2021_DEFCON_QUALS/qoo-or-ooo/players.py) 635db715b498511ebaf305a242cd3ca095235813189be095734721f64d568f12
- [service.py](https://rbf-shadowhunter.github.io/ctf/2021_DEFCON_QUALS/qoo-or-ooo/service.py) ff1f96ec1158cc9118ba0fad9142f18f92ed288b9659b1826d1006c1a2c26ff2


### Initial Analysis:
After downloading and examining each file, the first thing to realize if it wasn't evident from the title is that the programs are a game-ified combination of Quantum Key Distribution and quantum coin flipping.

In general, each of the above programs function as such:

- backend.py - manage chat connections, starts and stops "games" (QKD iterations)
- coin.py - a code-based representation of quantum coin-flipping
- game.py - interfaces with client connections and inputs and contains the Game class.
- players.py - performs qubit generation, measurement, and modification according to some quantum protocol (we'll discuss in a second) and contains the Player, Zardus, Adamd, and Hacker classes.
- service.py - manages win and loss results (this is where the game starts)

**Terminology.**
Some quick crypto and QKD terminology:
- Alice: the sender
- Bob: the receiver
- Eve: the evesdropper, usually some entity attempting to view information

- qubit: quantum bit (0 or 1)
- basis: pairs of orthogonal (rays at a 90-degree angle) states
- eigenstate: a vector in a Hilbert space representative of a well-defined momentum with a quantum uncertainty of 0.  The four states of BB84 are `{|↑⟩,|→⟩,|↗⟩,|↘⟩}`.  For this problem, that means there's no doubt of a polarization measurement.
- rectilinear: a basis combination of 0 and 90 degrees
- diagonal: a basis combination of 45 and 135 degrees
- true randomization: quantum random number generation (QRNG) that produces a random number based on wholly indeterminate physical information of quantum states.

**Overview of QKD.**
Closer examination of players.py reveals that the QKD protocol is akin to BB84, one of the simplest and oldest of QKD protocols.  BB84 polarizes photons to transmit information.  The summary of the BB84 process is below:
- Alice generates two strings of n bits
- Alice encodes each bit with a basis.  The encoding works as follows.  For a rectilinear eigenstate, a qubit value of 0 corresponds to a 0-degree polarization and a 1 corresponds to a 90-degree polarization.  For a diagonal eigenstate, qubit value 0 is encoded with 45 degrees while 135 degrees represents a 1.  These bit-basis combinations can be represented like so in bra-ket notation:
1. |Phi_00⟩ = Basis 0, Bit 0 = |0⟩
2. |Phi_10⟩ = Basis 1, Bit 0 = |1⟩
3. |Phi_01⟩ = Basis 0, Bit 1 = |+⟩
4. |Phi_11⟩ = Basis 1, Bit 1 = |-⟩

NOTE: Alice must select a polarization.  The basis cannot be both 0 and 90 or 45 and 135.
- Alice transmits the string of bits one photon at a time to Bob with the encoded information over the quantum channel.
- Bob, unaware of how Alice modified the photon, randomly selects a measurement basis.
- If Bob guesses right, he measures the polarized state and records the qubit value.  If he guesses wrong, both Alice and Bob discard the bit.
- Bob and Alice communicate the results over a classical channel and store their shared keys.
- This process is repeated for each photon until they develop a shared key as a percentage (threshold) of n bits.  This threshold is generally high, for this problem about 85% (represented by the amount of "wins" we get in the betting game).

While this explanation is grossly oversimplified, it is the best fit for answering the problem.  Now, the question arises - how are we going to hack this protocol?  Luckily, 4 guys in 1969 already did this (Reference D) as a complement to Bell's work.  It pains to reduce such an interesting experiment to a mere sentence, but the gist is that if we take a quantum approach to this game, we can win around 85% of the time - exactly what we need (Reference C).

We find that the flag is encoded in the player Adamd not only with BB84, but with AES in EAX mode, and Zardus and Adamd communicate the secret key and the flag.  Let's identify how we get from interacting with the game in game.py to being sent the AES-encrypted flag.

Two more things looking at the source code.
1. A rough workflow is service.py > backend.py > [repeat this sequence for every iteration] service.py > game.py > players.py > game.py > coin.py > game.py > service.py
2. Adamd's secret key is the same as each of the bets that Zardus makes when he and the Hacker (we) win.  Keep reading to see how to find that information.

Now, we know we'll need to code a way to interface with qoo-or-ooo.challenges.ooo on port 5000, so we'll create a script that interacts with the challenge (where the flag is stored) and parses the output.  But before we do...

**Getting to the Win.**
When interacting with the server, we can identify quickly that the server b

game.py takes you through 1 or 2 prompts, depending on your first choice.  Prompt 1 asks you what you want to bet (0 or 1) or if you want to use your "magic qoin" (quantum coin flip).  If you select the qoin (option 2), then you get a second prompt: "Do you want to rotate your qoin before flipping?" and are presented with "0. No, do not rotate my qoin", "1. Yes, rotate left", and "2. Yes, rotate right".

Rotating invokes the rotate functions in the Coin class in coin.py.
```
class Coin(object):
    def __init__(self, id):
        self.id = id
        self.qubit = secret(id)

    def rotate_left(self):
        self.qubit.ry(-2.0 * math.pi / 8.0)

    def rotate_right(self):
        self.qubit.ry(2.0 * math.pi / 8.0)

    def flip(self, referee):
        res = self.qubit.measure(non_destructive=True)
        return res
```
After 1 or 2 prompts, you're presented with a "Win!" or "Lose!" response.  This is decided by the `play` function from game.py:
```
    def play(self, p1_bet, p2_bet):
        if p1_bet ^ p2_bet == self.competitor_bet1 * self.competitor_bet2:
            print(WIN_MSG)
            return WIN
        else:
            print(LOSE_MSG)
            return LOSE
```
We're p1 and Zardus is p2 (game.py Line 36).
```
class Game(object):
    def __init__(self, hacker, zardus, id):
        self.player1 = hacker
        self.player2 = zardus
        self.competitor_bet1 = random.randint(0, 1)
        self.competitor_bet2 = random.randint(0, 1)
        self.player2_bet = self.player2.bet(id, self.competitor_bet2)
        self.coin = Coin(id)
        self.id = id
```
Both competitors will pick a random integer.  This will be given to us in stdout and will be important later for determining the secret_key, which will give us the flag.

In the beginning, we're given our competitor's bet (`self.competitor_bet1`): `[Round 0]: Your competitor bets on <somenumberhere>`.

After we place our bet, we're shown the output:
```
[Round 0]: zardus's competitor bets on <self.competitor_bet2>, you bet on <p1_bet>
<Win/Loss Message>
```
Zardus' bet is based off of his corresponding competitor's bet, `self.competitor_bet2`.

So, in effect, if `(our_bet XOR zardus_bet) EQUALS random_integer1 * random_integer2`, we win.

Zardus' betting function in players.py is
```
    def bet(self, gameid, referee):
        qubit = self.qubits[gameid]
        if referee == 1:
            qubit.H()
            res = qubit.measure(non_destructive=True)
            qubit.H()
        else:
            res = qubit.measure(non_destructive=True)
        self.bases.append(referee)
        return res
```
which tells us two things: 1) Zardus' basis will always equal the competitor's bet, and 2) a basis (competitor_bet2) value of 1 will prompt a Hadamard transform of the given qubit.

Without getting too in the weeds of how a Hadamard gate works, the relevant results of the Hadamard transform is
```
H(|0⟩) = |+⟩ == H(Basis 0, Bit 0) = Basis 0, Bit 1
H(|1⟩) = |-⟩ == H(Basis 1, Bit 0) = Basis 1, Bit 1
H(|+⟩) = |0⟩ == H(Basis 0, Bit 1) = Basis 0, Bit 0
H(|-⟩) = |1⟩ == H(Basis 1, Bit 1) = Basis 1, Bit 0
```
which represents entanglement.

In any case of a Hadamard transform, the original qubit value is flipped - a 1 to a 0 and vice versa.  It is important to note that Zardus changes the bit back once he's recorded the result (res) to return.

Remember that according to service.py, we have to win 85% of 30 plays, which is 26 times (25.5 rounded up).
```
PLAYS = 30
THRESHOLD = 0.85
```
Rotating left when our competitor bets 0 and rotating right when our competitor bets 1 should give us an 85% win rate.  This strategy is called the CHSH Game.  See Reference C for more information.  In the interest of time, I never rotated my qoin, but later on in the CTF, we'll need to be more precise.

Last part of our analysis is the method by which we'll get the solution.
    1. Interact with the server
    2. Process the results to record hacker_bet, competitor1_bet, competitor2_bet, and the win/loss result
    3. Calculate zardus_bet for each "Win!" result.  Record zardus_bet as a string.
    4. Follow the same method for setting up AES EAX Mode that Adamd followed, only use the decrypt function.  We'll get the flag this way.

### Solution:
Quick aside: while I was compiling this write-up, I was tempted to clean up my interaction code, but I decided against that.  My reasoning is that I hope that I can reassure any individuals new to CTF problems like this that even though I have experience with QKD, I still produce a lot of junk before coming to a solution - it's not always a clean path to the flag.  Keep nugging away at CTF problems, set them down if you get swamped, then come back to them with a renewed spirit.  Okay, back to the write-up.

Interacting with the server is a dance, so you'll need to build a socketing program that keeps the connection open after one interaction.  Not only that, the program must be ready to write the results to an output file.  This is good practice to avoid those moments when you can't scroll any higher in your terminal or you need more efficient access to the information.

- [interact.py](https://rbf-shadowhunter.github.io/ctf/2021_DEFCON_QUALS/qoo-or-ooo/interact.py)
- [output.txt](https://rbf-shadowhunter.github.io/ctf/2021_DEFCON_QUALS/qoo-or-ooo/output.txt)

One hint for any CTF is to ensure you can always access the challenge by hostname, as IP's can change.  See the line in interact.py `IPADDR = socket.gethostbyname('qoo-or-ooo.challenges.ooo')`.

Now that we have our output, let's take the first round as an example to calculate zardus' bet.
```
[Round 0]: Your competitor bets on 1
0. Bet for 0
1. Bet for 1
2. Use your magic qoin

2
<You>2
Do you want to rotate your qoin before flipping?
0. No, do not rotate my qoin
1. Yes, rotate left
2. Yes, rotate right

0
0: ['2', '0', None]
<You>0
[Round 0]: zardus's competitor bets on 1, you bet on 1
Win!
```
Since our bet is 1, our competitor (competitor1)'s bet is 1, zardus' competitor (competitor2)'s bet is 1, and the result is a "Win!", we can use the XOR table in Annex A to determine that Zardus must have bet a 0.

This is because 1 ^ zardus_bet == 1 * 1.  Therefore zardus_bet == 0.

Rather than manually calculate this for the remaining 29 iterations, let's develop a program that will process the results.

Process file: [process.py](https://rbf-shadowhunter.github.io/ctf/2021_DEFCON_QUALS/qoo-or-ooo/process.py)

The first part of this file parses the information in output.txt
```
from Crypto.Cipher import AES
import hashlib
import sys
from time import sleep

filename = "output.txt"

competitor1_text = ": Your competitor bets on "
competitor2_text = ": zardus's competitor bets on "
hacker_text = ", you bet on "
adamd_text = "zardus receives from adamd: "

competitor1_bet_list = list()
competitor2_bet_list = list()
hacker_bet_list = list()
zardus_bet_list = list()
expected_qubit_list = list()
adamd_bases = ""

def convert2stringlist(intlist):
    stringlist = list()
    for i in intlist:
        stringlist.append(str(i))
    return stringlist

def key_array_to_key_string(key_list):
    key_string_binary = b''.join([bytes([x]) for x in key_list])
    return hashlib.md5(key_string_binary).digest()

filedict = dict()
x = 0
with open(filename,'r') as infile:
    for line in infile:
        filedict[x] = line.strip()
        x += 1
    infile.close()
    
for lineno in filedict:
    if lineno < len(filedict):
        l = filedict[lineno]
        if competitor1_text in l:
            competitor1_bet = int(l.split(competitor1_text)[1])
            competitor1_bet_list.append(competitor1_bet)
        elif competitor2_text in l:
            competitor2_bet,hacker_bet = int(l.split(competitor2_text)[1].split(hacker_text)[0]),int(l.split(competitor2_text)[1].split(hacker_text)[1])

            if filedict[lineno+1] == "Win!":
                if (competitor1_bet * competitor2_bet == 1) and (hacker_bet == 0):
                    zardus_bet = 1
                elif (competitor1_bet * competitor2_bet == 1) and (hacker_bet == 1):
                    zardus_bet = 0
                elif (competitor1_bet * competitor2_bet == 0) and (hacker_bet == 0):
                    zardus_bet = 0
                elif (competitor1_bet * competitor2_bet == 0) and (hacker_bet == 1):
                    zardus_bet = 1
            elif filedict[lineno+1] == "Lose!":
                if (competitor1_bet * competitor2_bet == 1) and (hacker_bet == 0):
                    zardus_bet = 0
                elif (competitor1_bet * competitor2_bet == 1) and (hacker_bet == 1):
                    zardus_bet = 1
                elif (competitor1_bet * competitor2_bet == 0) and (hacker_bet == 0):
                    zardus_bet = 1
                elif (competitor1_bet * competitor2_bet == 0) and (hacker_bet == 1):
                    zardus_bet = 0
            else:
                print("LINE 40 ERROR!")
            if (competitor2_bet == 1) and (zardus_bet == 0):
                expected_qubit = 1
            elif (competitor2_bet == 1) and (zardus_bet == 1):
                expected_qubit = 0
            elif competitor2_bet == 0:
                expected_qubit = zardus_bet
            
            competitor2_bet_list.append(competitor2_bet)
            hacker_bet_list.append(hacker_bet)
            zardus_bet_list.append(zardus_bet)
            expected_qubit_list.append(expected_qubit)
            
            c2bl = convert2stringlist(competitor2_bet_list)
            eql = convert2stringlist(expected_qubit_list)
            zbs = convert2stringlist(zardus_bet_list)
            
            zardus_bets = ''.join(zbs)
            zardus_bases = ''.join(c2bl)
            zardus_qubits = ''.join(eql)
            
        elif adamd_text in l:
            if "-" not in l:
                adamd_bases += l.split(adamd_text)[1].split(":")[1]
            else:
                if "-1" in l:
                    nonce = l.split(adamd_text)[1].split(":")[1]
                elif "-2" in l:
                    ciphertext = l.split(adamd_text)[1].split(":")[1]
```
Once we have each component of the equation `hacker_bet ^ zardus_bet == competitor1_bet * competitor2_bet` and have calculated zardus' bet, we can then compare all of the bases that adamd guessed correctly (see the BB84 protocol) to determine which of zardus' bets adamd kept to make his secret key.
```
secret_key = ""
for zbet,zq,zb,ab in zip(list(zardus_bets),list(zardus_qubits),list(zardus_bases),list(adamd_bases)):
    if zb == ab:
        secret_key += zbet

print("SECRET_KEY:\t{}\nINTEGER:\t{}\n".format(secret_key,int(secret_key,2)))
```
After that, we need to recreate the AES EAX instance using the given key and nonce.
```
ciphertext_bytes = bytes.fromhex(ciphertext)

skl = [int(x) for x in secret_key]
key = key_array_to_key_string(skl)
cipher = AES.new(key, AES.MODE_EAX, nonce=bytes.fromhex(nonce))
plaintext_bytes = cipher.decrypt(ciphertext_bytes)
try:
    plaintext = plaintext_bytes.decode('ascii')
except:
    plaintext = "INCORRECT"

if plaintext != "INCORRECT": #This will show the flag.
    print("KEY:  {}".format(key))
    print("FLAG: {}".format(plaintext))
    sys.exit()

print("{}.  TRY AGAIN.".format(plaintext))
```
This gives us the flag!

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
