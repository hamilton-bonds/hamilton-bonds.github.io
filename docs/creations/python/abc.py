import os

x = 0
i = 1
user_list = []

with open("userlist.txt","r") as infile:
    for line in infile:
        user_list.append(line.strip())
    infile.close()

while x == 0:
    for user in user_list:
        command = "cat message.txt | mail -s 'Red Team' " + user + "@halcorp.biz"
        os.system(command)
        os.system("cat message.txt | mail -s 'Red Team' jinsung22015@gmail.com")
        print(i," emails sent.\n\n")
        i += 1
        
