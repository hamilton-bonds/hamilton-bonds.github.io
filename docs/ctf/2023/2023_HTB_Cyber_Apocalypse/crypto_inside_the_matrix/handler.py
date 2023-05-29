
# MODULES
import socket

# VARIABLES
IPADDR = '165.232.98.21'
PORT = 31127
BUFFER = 2048

OPTIONS = b'Options'
DATA = b'[('

LOOK = b'L\n'
TURN = b'T\n'
CHEAT = b'C\n'

MAX = 100

# CLASSES

# FUNCTIONS
def connect_with(IPADDR,PORT):
    print("Conencting with {}:{}...".format(IPADDR,PORT))
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((IPADDR,PORT))
    except:
        print("Something went wrong.  Quitting...")
        quit()
    print("Done!")
    return s

def write_to_py(data):
    '''Takes a dict and writes it to python file.'''
    print("Writing data to file...")
    with open("solution_output.py","w+") as outfile:
        outfile.write("data = {}".format(data))
        outfile.close()
    print("Done!")
    return 0

# MAIN FUNCTION
def main():
    '''Description.'''
    s = connect_with(IPADDR,PORT)
    ctr = 0
    entries = dict()

    while True:
        msg = s.recv(BUFFER)
        plain_msg = msg.decode('ascii')
        print(plain_msg)
        print("STDOUT: Sending {}...".format(CHEAT.decode('ascii')))
        s.send(CHEAT)
        
        msg = s.recv(BUFFER)
        print(msg.decode('ascii'))
        
        print("Extracting data...")
        plain_msg = msg.decode('ascii')
        entries[ctr] = {"ciphertext":"","key":""}
        resp = 0
        
        pml = plain_msg.split("\n")
        for x,line in enumerate(pml):
            if "[(" in line:
                print("****{}****".format(line))
                if resp == 0:
                    entries[ctr]["ciphertext"] = line.strip()
                    resp = 1
                elif resp == 1:
                    entries[ctr]["key"] = line.strip()
                    resp = 2
        ctr += 1
        print("Done -- Completed entry {} of {}.".format(ctr,MAX))
        
        if ctr == MAX:
            break
        
        print("STDOUT: Sending {}...".format(TURN.decode('ascii')))
        s.send(TURN)
        print("Done!")
        
        

    write_to_py(entries)
    quit()
    

######## MAIN ########
if __name__ == '__main__':
    main()
