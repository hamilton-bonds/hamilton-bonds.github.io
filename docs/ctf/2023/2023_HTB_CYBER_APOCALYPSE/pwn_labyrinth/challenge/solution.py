import subprocess

from time import sleep

def main():
    print("Starting solution script.")
    success = []
    i = 1
    MAX = 10001
    it = 0
    log = dict()
    while i != MAX:
        print("Iteration {}".format(it))
        command = ["./labyrinth"]
        s = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        door = str(i).zfill(3)
        if len(success) == 0:
            send = door
        else:
            send = "{}\n{}".format("\n".join(success),door)
            
        doors = send.encode('ascii')
        
        stdout,stderr = s.communicate(input=doors)
        stdout_decoded = stdout.decode('utf-8')
        print(stdout_decoded + "--------")
        
        log[it] = [i,stdout_decoded]

        if stdout.decode('utf-8').count(">") == 4 + (2 * len(success)):
            success.append(door)
            print(success)
            i = 0
            sleep(2)
        i += 1
        it += 1
        
    print(success)
    print("Iteration final: {}".format(it))
    
    with open("log.txt","w+") as outfile:
        for l in log:
            print(log[l])
            #outfile.write("{}:{}:{}\n".format(l,log[l][0],log[l][1]))
        outfile.close()

if __name__ == '__main__':
    main()
    print("Done executing solution script")
    quit()
