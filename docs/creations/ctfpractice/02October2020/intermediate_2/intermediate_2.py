#!/usr/bin/python3

import socket,sys,time
import random as rand
from threading import Thread

def chooseOrder():
    indlist = list()
    for x in range(len(message)):
        indlist.append(x)
    rand.shuffle(indlist)
    randmsg = ""
    for y,ind in enumerate(indlist):
        randmsg += message[ind]
        indlist[y] = str(ind)
    return randmsg,','.join(indlist)

def mainLoop():
    PORT = rand.randint(2000,6000)
    print("Server will send to port {}.".format(PORT))
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        count = 0
        print("Choosing order...")
        mts,order = chooseOrder()
        for m in mts:
            #for fourth_octet in range(1..254):
            if True:
                fourth_octet = 1 #Uncomment to run on 127.0.0.1
                ADDR = sys.argv[1] + '.' + str(fourth_octet)
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
        #conn.send(bytes('Public Key: {}','ascii'))
        addresses[conn] = addr
        Thread(target=handle_client,args=(conn,addr)).start()

def handle_client(conn,addr):

    mts,order = chooseOrder()

    clients[conn] = addr

    while True:
        for x,m in enumerate(mts):
            conn.send(m.encode('ascii'))
            time.sleep(1)
            if x == len(mts)-1:
                conn.send(str(order).encode('ascii'))
                conn.send(b'\n')

'''
def respond(message,conn):
    try:
        conn.send(mts,order)
    except:
        conn.close()
'''

if __name__ == '__main__':
    global message
    global clients
    global addresses

    message = "UmVjb25CeUZpcmVDVEYgfCBmbGFnPXsgSGVhdnlMb2FkZWREaWNlIH0K"
    clients = dict()
    addresses = dict()

    ########## NET ###########
    print("Starting server socket...")
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    if len(sys.argv) != 3:
        print("Correct usage:  ./wordpuzzle.py <server ip> <server port>")
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
