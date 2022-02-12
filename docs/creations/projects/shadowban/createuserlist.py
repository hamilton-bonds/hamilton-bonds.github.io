words = list()
users = list()

with open("tempcurl.txt","r") as infile:
    for line in infile:
        for word in line:
            if "@" in word:
                words.append(word)
    for item in words:
        if item.index("@") == 0:
            users.append(item)
    infile.close()

with open("userlist.txt","w") as outfile:
    for user in users:
        print(user,"\n")
    outfile.close()
