#!/usr/bin/env python3

ll = list()

with open('sonnet47.txt','r') as infile:
    for line in infile:
        ll.append(line.strip()+" ")
    infile.close()

ls = ''.join(ll)

print(ls)

print(len(ls.split(" ")))


cleaned_list = ls.split(" ")[::]

badchars = "!@#$%^&*()_+-={}[]|\:\";'<>?,./"

for x,word in enumerate(cleaned_list):
    for bc in badchars:
        while bc in word:
            word.replace(bc,"")
    cleaned_list[x] = word

print(" ".join(cleaned_list))

