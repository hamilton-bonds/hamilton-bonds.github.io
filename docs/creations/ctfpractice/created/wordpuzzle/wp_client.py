#!/usr/bin/python3

# TEST CLIENT
import socket
from threading import Thread

'''
def main():
    message = s.recv(1024).decode('ascii')
    while True:
        message = receive()
        print(message)

def receive():
    while True:
        try:
            message = s.recv(1024).decode('ascii')
        except:
            continue
    return message
'''

def testloop():
    s.send(bytes('testclient','ascii'))
    welcome = s.recv(1024).decode('ascii')
    print(welcome)
    while True:
        message = s.recv(1024).decode('ascii')
        print(message)

if __name__ == '__main__':
    SADDR = '127.0.0.1'
    SPORT = 18543

    global s

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((SADDR,SPORT))

    testloop()

    #receive_thread = Thread(target=main)
    #receive_thread.start()
    #s.close()
