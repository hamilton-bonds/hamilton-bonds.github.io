import os

starting = 0
check_list = []
searched_list = []

initialip = "192.168.1.1"

def dig(dug):
    command = "dig @"+str(dug)+" > dig.txt"
    record = os.system(command)

def findipns(start):
    dig(start)
    search_list = []
    with open("dig.txt","r") as out:
        for line in out:
            newline_list = line.strip().split("\t")
            if "NS" in newline_list:
                for i,p in enumerate(newline_list):
                    print("")
                new_ns = newline_list[i]
                print(newline_list,"\nINDEX: ",i,"\nNEW_NS: ",new_ns)
#                input("")
                if new_ns not in check_list:
                    check_list.append(new_ns)
                print(check_list)
            elif "A" in newline_list:
                for j,q in enumerate(newline_list):
                    print("")
                new_ip = newline_list[j]
                print(newline_list)
#                input("")
                if new_ip not in check_list:
                    check_list.append(new_ip)
                print(check_list)

    return check_list

def check_ip_list(ip_list):
    for ip in ip_list:
        out = findipns(ip)
    print(out)
        
    

if __name__ == '__main__':
    findipns(initialip)
    check_ip_list(check_list)
