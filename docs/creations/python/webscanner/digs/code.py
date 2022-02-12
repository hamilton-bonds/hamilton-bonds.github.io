#Code created by ShadowHunter
#
#Follow the steps below:
#  1. Define the starting DNS.
#  2. Generate IP list(s) from RRs
#  3. Structure RR matrix as so:
#     a. [A,CNAME,NS root,NS (if it is a NS)]

#Find an alternative to import os later.  Unsecure.
import os

global_results = []
searched_results = []

def start():
    start_dns = input("Type the starting DNS in dotted decimal notation: ")
    return start_dns

def dig(ip):
    command = "dig @" + ip + " > dig.txt"
    os.system(command)

def main():
    ref_list = []
    with open("dig.txt","r") as infile:
        for line in infile:
            line_list = line.strip().split("\t")

            #Adds nameserver and IPs to a list to search.
            if "NS" in line_list:
                ns = line_list.pop()
                if ns not in global_results:
                    if ns not in searched_results:
                        global_results.append(ns)
            elif "A" in line_list:
                ip = line_list.pop()
                if ip not in global_results:
                    if ip not in searched_results:
                        global_results.append(ip)

        #Cleans the list for any non-ip or non-ns listings.
        while "NS" in global_results:
            global_results.remove("NS")
        while "A" in global_results:
            global_results.remove("A")
    infile.close()
    return global_results

def repeat(global_results):
    print(len(searched_results)," searched.")
    for item in global_results:
        dig(item)
        pop = global_results.pop(0)
        if pop not in searched_results:
            searched_results.append(pop)
        ref_list = main()
        print("GLOBAL: ",global_results)
        print("SEARCHED: ",searched_results)
        repeat(ref_list)



if __name__ == '__main__':
    start_ip = start()
    dig(start_ip)
    references = main()
    repeat(references)
    print("DONE!")
