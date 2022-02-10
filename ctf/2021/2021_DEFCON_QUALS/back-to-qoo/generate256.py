import random as rand

opt1 = '2'

with open('256.txt','w+') as outfile:
    for i in range(256):
        if i % 2 == 0:
            outfile.write(opt1+"\n")
        else:
            outfile.write(str(rand.choice([0,0,0,0,0,0,0,0,1,2]))+"\n")
    outfile.close()

print("DONE!")
