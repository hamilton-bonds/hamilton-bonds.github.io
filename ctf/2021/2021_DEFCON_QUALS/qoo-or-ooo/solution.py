# qoo-or-ooo solution
# ShadowHunter

def importFile(filename):
    results = dict()
    you_ct = 0
    with open(filename,'r') as infile:
        for line in infile:
            if "<You>" in line:
                you_ct += 1
                if you_ct % 2 == 0:
                    rot_opt = line.strip().split("<You>")[1] #str()
            elif "Your competitor bets on " in line:
                c1_bet = line.strip().split("Your competitor bets on ")[1] #str()
            elif "zardus's competitor bets on " in line:
                c2_bet = line.strip().split("zardus's competitor bets on ")[1].split(",")[0]
                p1_bet_hacker = line.strip().split("you bet on ")[1]
                q_i = line.strip().split("Round ")[1].split("]")[0]
            elif "Win!" in line:
                a
            elif "Lose!" in line:
