#This program is designed to map IPs in a traceroute and nmap each IP along the route.

import os

ip_list = []
count = 1

def trace(ip):
    command = "traceroute " + ip + " > trace.txt"
    os.system(command)

def breakupip():
    with open("trace.txt","r") as infile:
        for line in infile:
            line_list = line.strip().split(" ")
#            print(line_list)
            for part in line_list:
                if "(" in part:
                    if part not in ip_list:
                        ip_list.append(part[1:len(part)-1])
            for ip in ip_list:
                if "(" in ip:
                    ip = ip[1:len(ip)]
                elif ")" in ip:
                    ip = ip[0:len(ip)-1]
        print(ip_list)

def repeat():
    print("Processing IP ",count)
    for ip in ip_list:
        trace(ip)
        breakupip()
    repeat()

if __name__ == '__main__':
    start_ip = input("Enter traceroute IP: ")
    trace(start_ip)
    breakupip()
    repeat()
    print("DONE!")
