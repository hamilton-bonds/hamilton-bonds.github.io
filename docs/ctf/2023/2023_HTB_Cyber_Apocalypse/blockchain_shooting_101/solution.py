# Must update version to 10 inside function 'updateSensors' inside Unknown() object
# so ... TARGET.updateSensors(10)?

# URL1 = 165.232.100.46:31385 #RPC
# URL2 = 165.232.100.46:32543 #TCP

import web3
from eth_account import *
from solcx import compile_source

private_key = "0xed67f80935cb860aa5a25ba3b6560b6bab7e7cf2b9cbedff191a1c95bd519e68"
address = "0x1A5dB6C90864A1204472C89C429E811e4e8F3Cd3"
target_contract = "0xf5BDEB2f8cbaB053C69E1f1195e88Fbe651e6658"
setup_contract = "0x6bbC1CBcaAC88d82036C2ea47059c5255f63Df0A"

infura_url = "http://165.232.100.46:31385"

#########
imported_ShootingArea_sol = """pragma solidity ^0.8.18;

contract ShootingArea {
    bool public firstShot;
    bool public secondShot;
    bool public thirdShot;

    modifier firstTarget() {
        require(!firstShot && !secondShot && !thirdShot);
        _;
    }

    modifier secondTarget() {
        require(firstShot && !secondShot && !thirdShot);
        _;
    }

    modifier thirdTarget() {
        require(firstShot && secondShot && !thirdShot);
        _;
    }

    receive() external payable secondTarget {
        secondShot = true;
    }

    fallback() external payable firstTarget {
        firstShot = true;
    }

    function third() public thirdTarget {
        thirdShot = true;
    }
}"""
compiled_ShootingArea_sol = compile_source(imported_ShootingArea_sol,output_values=['abi','bin'])
#########
#########
imported_Setup_sol = """pragma solidity ^0.8.18;

import {ShootingArea} from "./ShootingArea.sol";

contract Setup {
    ShootingArea public immutable TARGET;

    constructor() {
        TARGET = new ShootingArea();
    }

    function isSolved() public view returns (bool) {
        return TARGET.firstShot() && TARGET.secondShot() && TARGET.thirdShot();
    }
}"""
compiled_Setup_sol = compile_source(imported_Setup_sol,output_values=['abi','bin'])
#########

w3 = web3.Web3(web3.Web3.HTTPProvider(infura_url))
res = w3.is_connected()
print("CONNECTED: {}".format(res))

contract_id_shooting,contract_interface_shooting = compiled_ShootingArea_sol.popitem()
contract_id_setup,contract_interface_setup = compiled_Setup_sol.popitem()

#w3.eth.default_account = w3.eth.accounts[0]

account = w3.eth.account.from_key(private_key)

abi_TARGET = contract_interface_shooting['abi']
print("TARGET ABI: {}".format(abi_TARGET))
TARGET = w3.eth.contract(address=target_contract,abi=abi_TARGET)

#txn_TARGET = TARGET.functions.updateSensors(10).build_transaction({
#                                                                   'chainId':0,
#                                                                   'from':account.address,
#                                                                   'nonce':nonce
#                                                                  })

false = "false"
true = "true"

# firstTarget 000
nonce = w3.eth.get_transaction_count(account.address)
txn_TARGET = TARGET.functions.receive().build_transaction({'nonce':nonce})
signed_txn_TARGET = w3.eth.account.sign_transaction(txn_TARGET,private_key=private_key)
print(signed_txn_TARGET.hash)

# secondTarget 100
nonce = w3.eth.get_transaction_count(account.address)
txn_TARGET = TARGET.functions.fallback().build_transaction({'nonce':nonce})
signed_txn_TARGET = w3.eth.account.sign_transaction(txn_TARGET,private_key=private_key)
print(signed_txn_TARGET.hash)

# thirdTarget 110
nonce = w3.eth.get_transaction_count(account.address)
txn_TARGET = TARGET.functions.third().build_transaction({'nonce':nonce})
signed_txn_TARGET = w3.eth.account.sign_transaction(txn_TARGET,private_key=private_key)
print(signed_txn_TARGET.hash)

#TARGET.functions.updateSensors(10).call()

#w3.eth.send_raw_transaction(signed_txn_TARGET.rawTransaction)

print("UPDATED: {}".format(TARGET.functions.updated().call()))

abi_SETUP = contract_interface_setup['abi']
#abi_SETUP = [{'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'updateSensors', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'updated', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}]
print("SETUP ABI: {}".format(abi_SETUP))
SETUP = w3.eth.contract(address=setup_contract,abi=abi_SETUP)
#nonce = w3.eth.get_transaction_count(account.address)
txn_SETUP = SETUP.functions.updateSensors(10).build_transaction({'nonce':nonce})
#print(SETUP.functions.isSolved().call())
#SETUP.functions.updateSensors(10).call()
signed_txn_SETUP = w3.eth.account.sign_transaction(txn_SETUP,private_key=private_key)
w3.eth.send_raw_transaction(signed_txn_SETUP.rawTransaction)
print("UPDATED: {}".format(SETUP.functions.updated().call()))
