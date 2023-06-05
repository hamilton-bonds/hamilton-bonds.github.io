#!/usr/bin/env python3

#### #### #### #### #### #### #### ####
# Python TCP Client                   #
#    filename: python_tcp_client.py   #
#  created on: 2019-03-27             #
#  created by: ShadowHunter           #
# modified on: 2023-05-26             #
# modified by: ShadowHunter           #
#### #### #### #### #### #### #### ####

from sys import argv
import socket
from time import sleep

USAGE = """Usage: ./python_tcp_client.py [TARGET_IP | TARGET_HOSTNAME] [TARGET_PORT]"""

BUFFER = 2048 # bytes
TIMEOUT = 10 # seconds

try:
    #HOST,PORT = argv[1],argv[2]
    HOST = "welcome-to-quals-vfnva65rlchqk.shellweplayaga.me"
    PORT = 10001
    PORT = int(PORT)
except:
    print(USAGE)
    quit()

TICKET = "ticket{OwnershipRemodel1982n23:SFlwnzNby2IAG3ERymyFZIZAyXxET1z5sbDOv-ACAjIHFbOv}\r"

def validate_host(HOST):
    print("\t[o] Validating host {}...".format(HOST))
    if HOST.count(".") == 3:
        try:
            socket.inet_aton(HOST)
            IPADDR = HOST
            print("\t[+] Successfully validated IPv4 address: {}".format(HOST))
        except socket.error:
            print("\t[-] Not a valid IPv4 address: {}.  Quitting...".format(HOST))
            quit()

    else:
        try:
            IPADDR = socket.gethostbyname(HOST)
            print("\t[+] Successfully validated hostname {} at IPv4 address {}.".format(HOST,IPADDR))
        except socket.error:
            print("\t[-] Not a valid hostname: {}.  Quitting...".format(HOST))
            quit()

    return True,IPADDR

def connect_to_host(IPADDR,PORT):
    print("\t[o] Setting up socket.  Connecting to {}:{}...".format(IPADDR,PORT))
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)
    try:
        s.connect((IPADDR,PORT))
        print("\t[+] Connection successful.")
    except Exception as e:
        print("\t[-] Something went wrong connecting to {}:{}.  See output below:\n{}\n  Quitting...".format(IPADDR,PORT,e))
        quit()

    return s

######## MAIN FUNCTION ########
def main(s):
    '''
    Rot 13 until you get shell
    '''

    while True:
        server_resp = s.recv(BUFFER) # The script will hang here if the server does not send anything to you or it quits.
        print("\t[o] Server response:\n")
        print("="*32)
        print(server_resp.decode('utf-8'))
        print("="*32)
        print("\t[o] End server response.")
        
        if "Ticket please" in server_resp.decode('utf-8'):
            user_msg = TICKET
        elif "Hello challenger" in server_resp.decode('utf-8'):
            user_msg = "/ova/onfu\r"
        else:
            user_msg = "\r"

        sleep(0.05)

        print("\t[o] Sending this message:\n")
        print("="*32)
        print(user_msg)
        print("="*32)
        print("\t[o] End user message.")
        
        s.send(user_msg.encode('utf-8'))
        
        sleep(0.05)

    s.close()
    return 0

######## MAIN ROUTINE ########
if __name__ == '__main__':
    validated,IPADDR = validate_host(HOST)
    s = connect_to_host(IPADDR,PORT)
    main(s)
