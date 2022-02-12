'''
The following speech section was found in a addition to this series of numbers. Can you figure out the hidden message.
'''
speech = "Our democratic republican government is based on the idea of the natural right of each individual member thereof to a voice and a vote in making and executing the laws. We assert the province of government to be to secure the people in the enjoyment of their unalienable rights. We throw to the winds the old dogma that governments can give rights. Before governments were organized no one denies that each individual possessed the right to protect his own life, liberty, and property. And when one hundred or one million people enter into a free government, they do not barter away their natural rights, they simply pledge themselves to protect each other in the enjoyment of them through prescribed judicial and legislative tribunals. They agree to abandon the methods of brute force in the adjustment of their differences and adopt those of civilization. - Susan B Anthony 3 APRIL 1873"

numlist = [ 86, 24, 89, 21, 95, 4]
'''
WALKTHROUGH: This problem is a very CIA-like word-crypto challenge (not like your traditional crypto challenges).  It is deceptive in how involved it forces you to be, as evident in the first code below:

# Attempt 1
print(numlist)
for x,word in enumerate(speech.split(' ')):
    if x in numlist:
        print("{}: {}".format(x,word))


WALKTHROUGH: So naturally, the next instinct is to try to piece together every num in numlist word.  This has no discernable flag.  Code is below.

# Attempt 2
print(numlist)
numdict = dict()
for num in numlist:
    numdict[num] = list()
    for x,word in enumerate(speech.split(' ')):
        if x % num == 0:
            numdict[num].append(word)
    print(numdict[num])

WALKTHROUGH: Maybe it is every <num>-th letter?  Nope.

# Attempt 3A
print(numlist)
for x,char in enumerate(speech):
    if x in numlist:
        print("{}: {}".format(x,char))

# Attempt 3B
print(numlist)
numdict = dict()
for num in numlist:
    numdict[num] = ""
    for x,char in enumerate(speech):
        if x % num == 0:
            numdict[num] += char
    print(numdict[num])

WALKTHROUGH: After beating my head against the wall (because I often overthink things), I thought of the solution: maybe, just maybe, normal people start counting from 1, not 0.  Oh, and remember that democratic-republican is two separate words.
'''

# Attempt 1, but different and not the stupid way I tried at first
#print(numlist)
numdict = dict()
for num in numlist:
    for x,word in enumerate(speech.split(' ')):
        x = x + 1
        if x in numlist:
            numdict[x] = word

stringlist = list()
for num in numlist:
    stringlist.append(numdict[num])

print("FLAG: {}".format(' '.join(stringlist))) # QED
