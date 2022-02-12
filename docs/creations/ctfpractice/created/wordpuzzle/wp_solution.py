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
    start = 0
    om = ""
    while True:
        message = s.recv(1024).decode('ascii')
        print(message)
        if start == 1:
            ms += message
            if len(message) > 1:
                print("Starting to build the message...")
                order_list = message.strip().split(',')
                nm = ""
                for x,order in enumerate(order_list):
                    if '\n' in order:
                        order = order[:order.index('\n')]
                    order_list[x] = int(order)
                mn = max(order_list)
                word_dict = dict()
                for char,order in zip(list(ms),order_list):
                    word_dict[order] = char
                for r in range(mn):
                    nm += word_dict[r]
                print("OLD MESSAGE: ",om)
                print("NEW MESSAGE: ",nm)
        else:
            om += message
        if len(message) > 1:
            ms = ""
            if start == 0:
                om = ""
            start = 1


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
