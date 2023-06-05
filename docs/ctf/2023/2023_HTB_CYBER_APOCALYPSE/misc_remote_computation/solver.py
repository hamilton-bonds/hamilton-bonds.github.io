import ast
import operator as op
import socket

IPADDR = '138.68.162.218'
PORT = 32166
BUFFER = 2048

operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((IPADDR,PORT))

"""
* Divide by 0:                                                                                                                                                                                                      
This may be alien technology,                                                                                                                                                                                       
but dividing by zero is still an error!                                                                                                                                                                             
Expected response: DIV0_ERR                                                                                                                                                                                         
                                                                                                                                                                                                                    
* Syntax Error                                                                                                                                                                                                      
Invalid expressions due syntax errors.                                                                                                                                                                              
ex. 3 +* 4 = ?                                                                                                                                                                                                      
Expected response: SYNTAX_ERR                                                                                                                                                                                       
                                                                                                                                                                                                                    
* Memory Error                                                                                                                                                                                                      
The remote machine is blazingly fast,                                                                                                                                                                               
but its architecture cannot represent any result                                                                                                                                                                    
outside the range -1337.00 <= RESULT <= 1337.00                                                                                                                                                                     
Expected response: MEM_ERR 
"""

def eval_expr(expr):
    """https://stackoverflow.com/questions/2371436/evaluating-a-mathematical-expression-in-a-string"""
    try:
        send = eval_(ast.parse(expr, mode='eval').body)
    except Exception as e:
        #print("ERROR: ",e)
        send = 0.0
        if "syntax" in str(e):
            err_code = 2
        else:
            err_code = 1
        #print(expr)
        return send,err_code
    
    try:
        float(send)
    except:
        return 0.0,1
        
    if -1337.00 <= float(send) <= 1337.00:
        check_3 = True
    else:
        return send,3
    
    return send,0
    

def eval_(node):
    try:
        if isinstance(node, ast.Num): # <number>
            return node.n
        elif isinstance(node, ast.BinOp): # <left> <operator> <right>
            return operators[type(node.op)](eval_(node.left), eval_(node.right))
        elif isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
            return operators[type(node.op)](eval_(node.operand))
        else:
            raise TypeError(node)
    except Exception as e:
        return e

resp = s.recv(BUFFER)
print(resp.decode('ascii'))
r1 = "1\n"
r2 = "2\n"
r3 = "3\n"
print(r1)
s.send(r1.encode('ascii'))

DIV0_ERR = b"DIV0_ERR\n"
SYNTAX_ERR = b"SYNTAX_ERR\n"
MEM_ERR = b"MEM_ERR\n"

ERRORS = [b"NO_ERR",DIV0_ERR,SYNTAX_ERR,MEM_ERR]

ctr = 1
while True:
    if ctr == 501:
        break
        
    print("STDOUT: Evaluating {}...".format(ctr))
    resp = s.recv(BUFFER)
    if b"Incorrect response" in resp:
        #print("Incorrect response.  Quitting...")
        break
        
    #print(resp.decode('ascii'))
    
    resp_list = resp.decode('ascii').split("\n")
    
    try:
        problem = resp_list[-2].split(":")
        num,expr = problem[0],problem[1].split("=")[0].replace(" ","")
    except:
        encoded_send = SYNTAX_ERR
        s.send(encoded_send)
        ctr += 1
        continue
    
    send,err_code = eval_expr(expr)
    if err_code == 0:
        rounded_send = round(send,2)
        encoded_send = '{}{}'.format(str(rounded_send),"\n").encode('ascii')
    else:
        encoded_send = ERRORS[err_code]
    
    #print("{}".format(encoded_send))
    
    s.send(encoded_send)
    ctr += 1
    
print(resp.decode('ascii'))
print(s.recv(BUFFER).decode('ascii'))
quit()
