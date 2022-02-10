zardus_bases = dict()
adamd_bases = dict()
c1 = list()
c2 = list()
z2 = list()
a = list()
h1 = list()
wl_dict = dict()
with open('output.txt','r') as infile:
    for line in infile:
        l = line.strip()
        if "Your competitor bets on " in l:
            c1.append(int(l.split("Your competitor bets on ")[1]))
        elif "zardus's competitor" in l:
            ll = l.split(',')[0].split("bets on ")
            zardus_basis = int(ll[1])
            c2.append(zardus_basis)
            #z2.append(".") #Placeholder
            rnd = int(ll[0].split(']')[0].split(' ')[1])
            zardus_bases[rnd] = zardus_basis
        elif "from adamd" in l:
            its = l.split(': ')[1]
            it = int(its.split(':')[0])
            adamd_basis = its.split(':')[1]
            if it >= 0:
                adamd_basis = int(adamd_basis)
            adamd_bases[it] = adamd_basis
        if "Win!" in l:
            wl_dict[rnd] = 'W'
        elif "Lose!" in l:
            wl_dict[rnd] = 'L'
        if "you bet on " in l:
            h1.append(int(l.split("you bet on ")[1]))
    infile.close()

zn_ct = 0
eq_ct = 0
bases = list()
indices = list()
print("Z:A")
for i in range(128):
    try:
        z = zardus_bases[i]
        a = adamd_bases[i]
    except:
        z = None
        a = adamd_bases[i]
    if z == None:
        zn_ct += 1
    if z == a:
        eq_ct += 1
        if z == 1:
            bases.append("1")
            indices.append(eq_ct)
        elif z == 0:
            bases.append(str(z))
    else:
        bases.append(" ")
    print("{}\t| {}:{} | {}".format(i,z,a,z==a))

print(len(indices))

'''[Round 0]: Your competitor bets on 0
0. Bet for 0
1. Bet for 1
2. Use your magic qoin
Do you want to rotate your qoin before flipping?
0. No, do not rotate my qoin
1. Yes, rotate left
2. Yes, rotate right
[Round 0]: zardus's competitor bets on 0, you bet on 1
Win!
'''

c1c2 = list()
for x1,x2 in zip(c1,c2):
    c1c2.append(str(int(x1)*int(x2)))

wl_list = list()
for key in wl_dict:
    wl_list.append(wl_dict[key])
    
# Using z2's list
h_hat_z = list()
for h,wl,c12 in zip(h1,wl_list,c1c2):
    '''
    RULES OF XOR
    A B | Q
    --------
    0 0 | 0
    0 1 | 1
    1 0 | 1
    1 1 | 0
    
    p1_bet ^ p2_bet =? c1_bet * c2_bet
    '''
    h = int(h)
    c12 = int(c12)
    if wl == "W":
        if c12 == 0 and h == 0:
            zq = 0
        elif c12 == 0 and h == 1:
            zq = 1
        elif c12 == 1 and h == 0:
            zq = 1
        elif c12 == 1 and h == 1:
            zq = 0
        h_hat_z.append(str(c12))
    elif wl == "L":
        if c12 == 0 and h == 0:
            zq = 1
        elif c12 == 0 and h == 1:
            zq = 0
        elif c12 == 1 and h == 0:
            zq = 0
        elif c12 == 1 and h == 1:
            zq = 1
        if c12 == 0:
            h_hat_z.append('1')
        elif c12 == 1:
            h_hat_z.append('0')
    z2.append(zq)

qubits = list()
for zbets,bss in zip(z2,bases):
    print("Z: ",zbets)
    print("B: ",bss)
    if bss != ' ':
        if int(bss) == 0:
            qubits.append(str(zbets))
        elif int(bss) == 1:
            qubits.append('?')
    else:
        qubits.append(' ')
        
qubits_abbv = list()
qunk = 0
for q in qubits:
    if q.isalnum():
        qubits_abbv.append(str(q))
    elif q == '?':
        qunk += 1
        qubits_abbv.append(str(q))
qubits_extended = list()
for u,qa in enumerate(list(qubits_abbv)):
    if qa == '?':
        qubits_extended.append(str(z2[u]))
    else:
        qubits_extended.append(str(qa))
        
print("UNKNOWNS: {}".format(zn_ct))
print("KNOWNS  : {}".format(eq_ct))

c1 = [str(a) for a in c1]
c2 = [str(b) for b in c2]
h1 = [str(c) for c in h1]
z2 = [str(d) for d in z2]

print(indices)

print("          0       1       2       3       4       5       6       7       8       9       10      11      12      13      14      15      ")
print("          01234567012345670123456701234567012345670123456701234567012345670123456701234567012345670123456701234567012345670123456701234567")
print("C1 Bets : {}".format(''.join(c1)))
print("C2 Bets : {}".format(''.join(c2)))
print("------------------------------------------------------------------------------------------------------------------------------------------")
print("C1 * C2 : {}".format(''.join(c1c2)))
print("==========================================================================================================================================")
print("RESULTS : {}".format(''.join(wl_list)))
print("==========================================================================================================================================")
print(" H ^ Z  : {}".format(''.join(h_hat_z)))
print("------------------------------------------------------------------------------------------------------------------------------------------")
print(" Z Bets : {}".format(''.join(z2)))
print(" H Bets : {}".format(''.join(h1)))
print("  Bases : {}".format(''.join(bases)))
print("------------------------------------------------------------------------------------------------------------------------------------------")
print(" Qubits : {}".format(''.join(qubits)))
print(" Qb_abbv: {}".format(''.join(qubits_abbv)))
print(" Qb_unk : {}".format(qunk))
print(" Qb_ext : {}".format(''.join(qubits_extended)))
