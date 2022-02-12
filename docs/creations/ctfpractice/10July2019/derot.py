
import os
filename = "example.txt"
badalpha = 'ghijklmnopqrstuvwxyz'

goodhex = list()
with open(filename,"r") as infile:
    for line in infile:
        bad = 0
        for b in badalpha:
            if b in line:
                bad = 1
        if bad != 1:
            goodhex.append(line.strip())

for g in goodhex:
    cmd = "echo '{}' | xxd -r -p -o /path/to/file && cat /path/to/file".format(g)
    os.system(cmd)
