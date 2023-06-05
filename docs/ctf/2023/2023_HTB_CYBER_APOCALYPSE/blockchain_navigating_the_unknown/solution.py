# Must update version to 10 inside function 'updateSensors' inside Unknown() object
# so ... TARGET.updateSensors(10)?

# URL1 = 178.62.9.10:30542 #RPC
# URL2 = 178.62.9.10:32284 #TCP

import web3
from eth_account import *
from solcx import compile_source

private_key = "0x297eb2aa0d0ab13bee52bd1ad7ba74cf63b9fe91be38406cc57ec77f004f1620"
address = "0x1dCFf7272D02bf1364B34cb979943aB416B3bD30"
target_contract = "0xc48e2C83747a0BF40b053334C4cd3DcA8F89aBf4"
setup_contract = "0xF86Feb32756be04Ed7729405EE3FcbD76822205D"

infura_url = "http://178.62.9.10:30542"

#########
imported_Unknown_sol = """pragma solidity ^0.8.18;


contract Unknown {
    
    bool public updated;

    function updateSensors(uint256 version) external {
        if (version == 10) {
            updated = true;
        }
    }

}"""
compiled_Unknown_sol = compile_source(imported_Unknown_sol,output_values=['abi','bin'])
#########
#########
imported_Setup_sol = """pragma solidity ^0.8.18;

import {Unknown} from "./Unknown.sol";

contract Setup {
    Unknown public immutable TARGET;

    constructor() {
        TARGET = new Unknown();
    }

    function isSolved() public view returns (bool) {
        return TARGET.updated();
    }
}"""
compiled_Setup_sol = compile_source(imported_Setup_sol,output_values=['abi','bin'])
#########

w3 = web3.Web3(web3.Web3.HTTPProvider(infura_url))
res = w3.is_connected()
print("CONNECTED: {}".format(res))

contract_id_unknown,contract_interface_unknown = compiled_Unknown_sol.popitem()
contract_id_setup,contract_interface_setup = compiled_Setup_sol.popitem()

#w3.eth.default_account = w3.eth.accounts[0]

account = w3.eth.account.from_key(private_key)

abi_TARGET = contract_interface_unknown['abi']
#abi_TARGET = [{'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'updateSensors', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'updated', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'edit', 'view': 'function'}]
print("TARGET ABI: {}".format(abi_TARGET))
TARGET = w3.eth.contract(address=target_contract,abi=abi_TARGET)
nonce = w3.eth.get_transaction_count(account.address)
#txn_TARGET = TARGET.functions.updateSensors(10).build_transaction({
#                                                                   'chainId':0,
#                                                                   'from':account.address,
#                                                                   'nonce':nonce
#                                                                  })

txn_TARGET = TARGET.functions.updateSensors(10).build_transaction({'nonce':nonce})
#TARGET.functions.updateSensors(10).call()
signed_txn_TARGET = w3.eth.account.sign_transaction(txn_TARGET,private_key=private_key)
print(signed_txn_TARGET.hash)
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
