import smtplib

i=0
user_list = []
ip_list = ["102","103","104","105","106","107","108"]

with open("userlist.txt","r") as infile:
    for line in infile:
        user_list.append(line.strip())
    infile.close()

while True:
    for ip in ip_list:
        newip = "10.10." + ip + ".25"
        print("Trying ",newip)
        server = smtplib.smtp(host=newip,port=25)
        server.starttls()

        for user in user_list:
            print("Trying user ",user)
            sender = "sh@example.com"
            receiver = user + "@halcorp.biz"

        message = "\nProperty of the Red Team!"
        server.sendmail(sender,receiver,message)
        print("EMAILS ATTEMPTED: ",i)
        i += 1

