#!/usr/bin/python3

# MODULES
from scapy.all import *
from threading import Thread
import socket,sys,traceback

def send_ICMP(ip_dst):
    flag="DSC{8c27f0ca74e8adb32c6fed86523d408f}"
    sr1(IP(dst=ip_dst)/ICMP()/Raw(load=flag))

def receive_input(conn,ip,port,max_buffer_size):
    client_input = conn.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)
    if client_input_size > max_buffer_size:
        print("Larger input than buffer from {}:{}".format(ip,port))
        return None
    else:
        return client_input

def client_thread(message,conn,ip,port,max_buffer_size=5120):
    is_active = True
    conn.sendall(message + "\n.../pet me...\n  >>>".encode('ascii'))
    while is_active:
        client_input = receive_input(conn,ip,port,max_buffer_size).decode()
        if "/quit" in client_input.split('\n')[0]:
            print("{}:{} is exiting...".format(ip,port))
            conn.close()
            is_active = False
        elif "/pet" in client_input.split('\n')[0]:
            print("Received data from {}:{}".format(ip,port))
            conn.sendall("Thank you!  Goodbye.".encode('ascii'))
            #Send the ICMP packet with the flag.
            send_ICMP(ip)
            is_active = False
    conn.close()

def server():
    global messageA
    global messageB
    messageA = "I've seen you before! Woof! Woof! *sniff* *sniff*".encode('ascii')
    messageB = "I've never met you! Bark! Bark! *ping* *ping*".encode('ascii')
    ip = '0.0.0.0'
    port = 1337

    srv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    srv.bind((ip,port))
    print("Server started at {}:{}".format(ip,port))
    srv.listen(8)

    seen = set()
    while True:
        conn,addr = srv.accept()
        ip,port = (addr[0],addr[1])
        print("Connection from {}:{}".format(ip,port))
        if ip not in seen:
            seen.add(ip)
            message = messageB
        else:
            seen.remove(ip)
            message = messageA
        try:
            Thread(target=client_thread,args=(message,conn,ip,port)).start()
        except:
            print("Thread did not start with {}:{}".format(ip,port))
            traceback.print_exc()
    srv.close()
    print("Server closed.")

if __name__ == '__main__':
    ans = True
    while ans == True:
        server()
