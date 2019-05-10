from easy_blockchain.wallet import Wallet
from easy_blockchain.blockchain import Block, BlockChain
import json, time

wallet = Wallet()
peerNode1 = wallet.getPublicKey()

dataPayload1 = wallet.create_transaction('test01', 1, 0.5, "one message")
dataPayload2 = dataPayload1.copy()
print("Check if a forgery attack have same as real transaction")
print("dataPayload1 == dataPayload2", dataPayload1 == dataPayload2)
print(dataPayload1)

wallet2 = Wallet()
peerNode2 = wallet2.getPublicKey()
dataPayload3 = wallet2.create_transaction(peerNode1, 1.5, 0.12, "peerNode2 send to peerNode1")
print(dataPayload3)

block = Block()
block.add_transaction(dataPayload1)
block.add_transaction(dataPayload2)  
block.add_transaction(dataPayload3)
print("--------------------------------------")
print("The block 1 has 2 real transaction:")
print(json.dumps(block.transactions, indent=2))

coin = BlockChain()
proof = coin.mine_proof()
print("The first proof is:", proof)
coin.save_chain()

print("--------------------------------------")
print("The transaction history and the balance of users:")

mycoin = coin.get_history(peerNode1)
print("User: peerNode1 balance:", coin.get_balance(peerNode1))
print(json.dumps(mycoin, indent=4))

mycoin2 = coin.get_history(peerNode2)
print("User: peerNode2 balance:", coin.get_balance(peerNode2))
print(json.dumps(mycoin2, indent=4))

for i in range(100):
    dataPayload_1 = wallet.create_transaction('test01', i, 0.5, "one message")
    dataPayload_2 = wallet2.create_transaction('test02', i+3, 0.5, "two message")
    block.add_transaction(dataPayload_1)
    block.add_transaction(dataPayload_2)
print(json.dumps(block.transactions, indent=4))










