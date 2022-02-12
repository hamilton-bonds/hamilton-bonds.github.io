import os

account_list = ["root","andrew","matthew","philip","simon","thomas","nate","emma","madison","abigail","olivia","isabella","hannah"]

ip_list = ["101","102","103","104","105","106","107","108"]
port_list = ["80","23","53","443","125","223"]

#test TELNET

#for port in port_list:
#    for ip in ip_list:
#        print("PORT: ",port)
#        command = "telnet 10.10." + ip + ".15 " + port
#        os.system(command)
#        command = "telnet 10.10." + ip + ".20 " + port
#        os.system(command)

#test SSH

for user in account_list:
    for ip in ip_list:
        command = "ssh " + user + "@10.10." + ip + ".15"
        os.system(command)
        command = "ssh " + user + "@10.10." + ip + ".20"
        os.system(command)
