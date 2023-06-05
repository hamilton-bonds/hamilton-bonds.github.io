import subprocess
from os import listdir
from os.path import isfile, join
from threading import Thread

filenames = [f for f in listdir("./") if isfile(join("./", f))]

first_file = filenames[0]

def process(filename):
    ps = subprocess.Popen(('./{}'.format(filename)), stdout=subprocess.PIPE)
    try:
        stdout,stderr = ps.communicate(timeout=5)
        print(stdout.decode('ascii'))
        quit()
        if "Passphrase" in stdout.decode('ascii'):
            print("Sending {}...".format(filename))
            stdout,stderr = ps.communicate(input="{}\r".format(filename),timeout=1)
            if len(stdout.decode('ascii').strip()) > 0:
                print("****Potential password: {}".format(filename))
                with open("output.txt","w+") as outfile:
                    outfile.write("{}\n".format(filename))
                    outfile.close()
        print("Killing...")
        ps.kill()
    except:
        print("Killing...")
        ps.kill()
    
if __name__ == '__main__':
    print("Processing password for {}".format(first_file))
    for filename in filenames:
        ft = Thread(target=process,args=(filename,))
        ft.start()
        quit()
    ft.join()
