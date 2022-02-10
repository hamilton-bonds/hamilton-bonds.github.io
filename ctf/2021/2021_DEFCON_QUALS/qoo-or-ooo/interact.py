import binascii as ba
import itertools as it
import random as rand
import select
import socket
import subprocess
import sys
#from subprocess import Popen,PIPE,STDOUT
from time import sleep

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IPADDR = socket.gethostbyname('qoo-or-ooo.challenges.ooo')
PORT = 5000

s.connect((IPADDR,PORT))

while True:
    sockets_list = [sys.stdin,s]
    read_sockets,write_socket,error_socket = select.select(sockets_list,[],[])
    
    q_track = dict()
    iters = 0
    for socks in read_sockets:
        if socks == s:
            ''' Attempt at automation #1
            print(s.recv(4096).decode('utf-8'))
            iters += 1 
            messageA = '2'
            if messageA == '0':
                 bit = '0'
            elif messageA == '1':
                bit = '1'
            elif messageA == '2':
                bit = 'qbit'
            messageB = str(rand.randint(1,3))
            if messageB == '1':
                basis = 'rectilinear'
            else:
                basis = 'diagonal'
            sys.stdout.write("<Python Input> Sending bit {} of basis {}\n".format(bit,basis))
            q_track[iters] = [bit,basis,None]
            s.send(messageA.encode('utf-8'))
            responseA = socks.recv(4096).decode('utf-8')
            print("Sent. Sleep(2).")
            sleep(2)
            print(responseA)
            s.send(messageB.encode('utf-8'))
            responseB = socks.recv(4096).decode('utf-8')
            print(responseB)
            print("Sent. Sleep(2).")
            sleep(2)
            if "Win!" in responseB:
                q_track[iters][2] = q_track[iters][0] # Shared key
            elif "Lose!" in responseB:
                q_track[iters][2] = None # Throw away
            sys.stdout.flush()
            ''' # Attempt at automation #1
        #''' Manual #1
            iters = 0
            tracker = dict()
            message = socks.recv(4096).decode('utf-8')
            print(message)
            if len(message) <= 1:
                sys.exit()
        else:
            if 'bet' in message:
                disp = 'bit'
                iters += 1
            elif 'rotate' in message:
                disp = 'basis'
            elif 'Win!' in message:
                disp = bit
            elif 'Lose!' in message:
                disp = 'NONE'
            message = sys.stdin.readline()
            if disp == 'bit':
                bit = message[0]
            elif disp == 'basis':
                basis = message[0]
            elif disp == bit:
                tracker[iters][2] = bit
            elif disp == 'NONE':
                tracker[iters][2] = 'NONE'
            try:
                tracker[iters] = [bit,basis,None]
            except:
                a = 1 # Do nothing
            for track in tracker:
                print("{}: {}".format(track,tracker[track]))
            #message += "\n"
            s.send(message.encode('utf-8'))
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
        #''' # Manual #1
                
server.close()
