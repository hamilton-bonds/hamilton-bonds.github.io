#!/usr/bin/python3

import socket,sys,time
import random as rand
import base64 as b64
from threading import Thread

def base64encode():
    alphanum = "0123456789abcdefghijklmnopqrstuvwxyz"
    expected = str()
    for i in range(20):
        expected += rand.choice(list(alphanum))
    tosend = b64.b64encode(expected.encode('ascii'))
    return expected,tosend

def mainLoop():
    PORT = rand.randint(1024,65535)
    print("Server will send to port {}.".format(PORT))
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        count = 0
        for m in mts:
            #for fourth_octet in range(1..254):
            if True:
                #fourth_octet = 1 #Uncomment to run on 127.0.0.1
                #ADDR = sys.argv[1] + '.' + str(fourth_octet)
                ADDR = '0.0.0.0'
                try:
                    s.connect((ADDR,PORT))
                    s.send(m.encode('ascii'))
                    if count == len(mts)-1:
                        s.send(order.encode('ascii'))
                    s.close()
                    print("Sent to {}:{}!".format(ADDR,PORT))
                    count += 1
                except:
                    continue

def accept_incoming_connections():
    while True:
        conn,addr = s.accept()
        print("{} connected at {}:{}".format(conn,addr[0],addr[1]))
        addresses[conn] = addr
        conn.send(message.encode('ascii'))
        Thread(target=handle_client,args=(conn,addr)).start()

def handle_client(conn,addr):

    sentence,tosend = base64encode()

    clients[conn] = addr

    num_trials = 10
    trials = [list(base64encode()) for i in range(num_trials)]
    for x,trial in enumerate(trials):
        [expected,tosend] = trial
        conn.send(tosend)
        resp = conn.recv(BUFFER).decode('ascii')
        print("Expected response: {}".format(expected))
        print("{} replied with {}".format(addr,resp))
        if resp == expected + "\n":
            print("{} is correct!  {} / {}".format(addr,x+1,num_trials))
            CORRECT = "Correct!  {} / {}\n".format(x+1,num_trials)
            conn.send(CORRECT.encode('ascii'))
            if x == num_trials-1:
                x = num_trials
        else:
            print("{} is incorrect!  {} / {}".format(addr,x+1,num_trials))
            INCORRECT = "Incorrect!  {} / {}\n".format(x+1,num_trials)
            conn.send(INCORRECT.encode('ascii'))
            break
    if x == num_trials:
        flag_msg = "Good job!  Here's the flag: {}".format(flag)
        conn.send(flag_msg.encode('ascii'))
    else:
        fail_msg = "Sorry!  Try again by reconnecting."
        conn.send(fail_msg.encode('ascii'))
    print("Terminating connection with {}".format(addr))
    conn.close()
    

if __name__ == '__main__':
    global message
    global clients
    global addresses
    global sentence
    global flag
    
    global BUFFER
    BUFFER = 1024

    message = "Beginner 1: Create your very own Base64 decoder!  Use any language, but don't use modules or commands specifically designed to decode base64. Send the output back to the server to get the flag.\n"
    clients = dict()
    addresses = dict()
    
    flag = "RTD{QmFzZTY0IElzIEF3ZXNvbWUh}"

    ########## NET ###########
    print("Starting server socket...")
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    if len(sys.argv) != 3:
        print("Correct usage:  ./beginner_1.py <server ip> <server port>")
        exit()
    SADDR = str(sys.argv[1])
    SPORT = int(sys.argv[2])
    s.bind((SADDR,SPORT))
    s.listen(20)
    print("Done!")
    client_list = list()
    print("Waiting for connections...")

    #### MAIN SERVER LOOP ####
    newthread = Thread(target=accept_incoming_connections)
    newthread.start()
    newthread.join()

    print("Exiting...")
    s.close()
