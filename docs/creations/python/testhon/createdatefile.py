with open("dates.txt","a") as newfile:
    i = 1
    while i < 366:
        newfile.write(str(i))
        i += 1
