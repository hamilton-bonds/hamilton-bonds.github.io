import subprocess
from os import listdir
from os.path import isfile, join
from threading import Thread

filenames = [f for f in listdir("./") if isfile(join("./", f))]

def process(filename):
    print("Processing filename {}...".format(filename))
    ps = subprocess.Popen(('./{}'.format(filename)), stdout=subprocess.PIPE)
    try:
        stdout,stderr = ps.communicate(timeout=1)
        if "Passphrase" not in stdout.decode('ascii'):
            print("****Potential entry point found at filename: {}".format(filename))
            with open("output.txt","w+") as outfile:
                outfile.write("./{}".format(filename))
                outfile.close()
        print("Killing...")
        ps.kill()
    except:
        print("Killing...")
        ps.kill()
    
if __name__ == '__main__':
    for filename in filenames:
        ft = Thread(target=process,args=(filename,))
        ft.start()
    ft.join()
