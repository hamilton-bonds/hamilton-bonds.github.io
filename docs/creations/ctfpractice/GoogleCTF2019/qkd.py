import requests,json,random
#import itertools as it
url="https://cryptoqkd.web.ctfcompetition.com/qkd/qubits"

def qkd():
    bitlist = list()
    for i in range(512):
        qd = dict()
        qd['real'] = complex().real
        qd['imag'] = complex().imag
        bitlist.append(qd)
    # QUANTUM CODE
    return bitlist

def createPayload(basis,qubits):
    baselist = list()
    for b in basis:
        baselist.append(b)
    return {'basis':baselist,'qubits':qubits}

######## MAIN PROGRAM ########
if __name__ == '__main__':
    print("GETTING QUBITS...")
    q = qkd()
    print("DONE! [1]")
    b = ""
    print("GETTING BASIS...")
    for i in range(512):
        decideri = random.choice([0,1])
        if decideri == 1:
            b += "x"
        else:
            b += "+"
    bitlist = list()
    for k in range(512):
        qd = dict()
        deciderk = random.choice([0,1])
        if deciderk == 1:
            qd['real'] = 0
            qd['imag'] = 1
        else:
            qd['real'] = 1
            qd['imag'] = 0
        bitlist.append(qd)
    q = bitlist
    print("DONE! [2]")
    print("CRAFTING PAYLOAD...")
    payload = createPayload(b,q)
    print("DONE! [3]")
    print("POSTING DATA TO QKD SITE...")
    r = requests.post(url,json=payload)
    response = r.text
    statuscode = r.status_code
    print("DONE! [4]")
    print(response)
    print(statuscode)
    rl = response.split(" ")
    if '"announcement":' in rl:
        ans = rl[rl.index('"announcement":')+1]
        ans = ans[1:len(ans)-2]
    else:
        ans = "ERROR'D OUT"
    print(ans)
