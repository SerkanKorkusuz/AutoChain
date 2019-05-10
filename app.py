from datetime import datetime
from hashlib import sha256
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.all_dataPayloads = {}
        self.genesis_block()

    def genesis_block(self):
        dataPayloads = {"This is the first block\'s first datapayload: The automabiles\' safe future is at our hands!   by AutoChain"}
        global remarks
        remarks = "This block contains logistics and traffic datapayloads related to RegionABCD1234"
        self.chain.append(Block(dataPayloads, "0"*32, remarks))
        return self.chain

    def print_blocks(self):
        myBlocks = {}
        for i in range(len(self.chain)):
          current_block = self.chain[i]
          print("Block {} {}".format(i, current_block))
          myBlocks["Block {}".format(i)] = str(current_block)+" "+str(current_block.print_block()) + "\n"
        return myBlocks

    def add_block(self, dataPayloads, remarks):
       previous_block_hash = self.chain[len(self.chain)-1].hash
       new_block = Block(dataPayloads, previous_block_hash, remarks)
       proof = self.proof_of_stake(new_block)
       if (self.validate_chain()):
            self.chain.append(new_block)
       return new_block, proof, new_block.print_block()

    def validate_chain(self):
          for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != self.chain[i].generate_hash():
                invalid = "!!!!!!!!!!!!!!!!!!Invalid Block!!!!!!!!!!!!!!!!!!"
                print(invalid)
                return False
            if previous.hash != self.chain[i-1].generate_hash():
                invalid = "!!!!!!!!!!!!!!!!!!Invalid Block!!!!!!!!!!!!!!!!!!"
                print(invalid)
                return False
          valid = "Valid Block"
          print(valid)
          return True

    def proof_of_stake(self, block, difficulty=2):
        proof = block.generate_hash()
        while proof[:difficulty] != '0'*difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof


class Block:
    def __init__(self, dataPayloads, previous_hash, remarks):
        self.timestamp = datetime.now()
        self.dataPayloads = dataPayloads
        self.previous_hash = previous_hash
        self.remarks = remarks
        self.nonce = 0
        block_contents = str(self.timestamp) + str(self.dataPayloads) + str(self.previous_hash) + str(self.nonce)
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_contents = str(self.timestamp) + str(self.dataPayloads) + str(self.previous_hash) + str(self.nonce) + str(self.remarks)
        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()

    def print_block(self):
        myBlock = {"timestamp" : self.timestamp,
                   "dataPayloads" : self.dataPayloads,
                   "current hash" : self.hash,
                   "previous hash" : self.previous_hash,
                   "remarks" : self.remarks}
        print(myBlock)
        return myBlock

block_one_dataPayloads = {"driver":"Serkan", "traffic_light": "red", "parking_available":"yes"}
block_two_dataPayloads = {"driver":"Alp", "traffic_light": "green", "nearest_fuelStation":"between 50 and 60 kms"}
block_three_dataPayloads = {"driver":"Mücahit", "traffic_light": "yellow", "road_maintanence":"no"}
fake_dataPayloads = {"driver":"Çağatay", "traffic_police": "yes", "weather_condition":"proper"}
        
local_blockchain = Blockchain()

local_blockchain.add_block(block_one_dataPayloads, remarks)
local_blockchain.add_block(block_two_dataPayloads, remarks)
local_blockchain.add_block(block_three_dataPayloads, remarks)
local_blockchain.validate_chain()

#local_blockchain.chain[2].dataPayloads = {"driver":"Çağatay", "road_toll": "free", "weather_condition":"improper"}

local_blockchain.validate_chain()

dataPayload1 = {
    "start_at": "1513005534000",  
    "latitude": "32.798780",
    "longitude": " 33.456553", 
    "radius": "10000",
    "height": "200", 
    "width": "120",
    "length": "330",
    "weight": "1200",
    "facilities": "2" }

dataPayload2 = { 
    "need_id": "at9uk0b52s2895f",
    "expires_at": "1513005539000", 
    "price": "30000000, 50000000",
    "price_type": "hour",
    "price_description": "Price per hour, City tax",
    "latitude": "32.798780",
    "longitude": " 33.456553", 
    "entrance_latitude": "32.885878", 
    "entrance_longitude": " 33.935558", 
    "exit_latitude": "32.439818", 
    "exit_longitude": "33.771208",
    "location_floor": "2", 
    "location_name": "ForumAVM parking lot B" }

dataPayload3 = { 
    "location_name_lang": "tr",
    "location_house_number": "159",
    "location_street": "Ataturk",
    "location_city": "Sariyer", 
    "location_postal_code": "34467",
    "location_county": "Istanbul",
    "location_country": "TR", 
    "available_from": "1513005534000",
    "available_until": "1513091934000",
    "height": "300", "width": "200", 
    "length": "580", "weight": "10000",
    "facilities": "2,3,8"}

dataPayload4 = { 
    "start_at": "1513005534000", 
    "start_latitude": " 33.456553", 
    "start_ongitude": " 32.456553", 
    "end_latitude": "33.807643", 
    "end_longitude": "32.587960", 
    "vehicle_type": "car", 
    "max_altitude": "400", 
    "height": "11", 
    "width": "22", 
    "length": "28", 
    "weight": "2" }

dataPayload5 = { 
    "need_id": "br6gp8i75d0329h", 
    "expires_at": "1513005539000", 
    "price": "100000000000000000", 
    "price_type": "flat", 
    "price_description": "Total price", 
    "eta": "1513178334000"}

dataPayload6 = { 
  "amount": "400",
  "sender": "AutoChain",
  "receiver": "Charging Station" }

dataPaylod_pool = [dataPayload1, dataPayload2, dataPayload3, dataPayload4, dataPayload5, dataPayload6]

dataPayload7 = {
  "amount" : "",
  "sender" : "",
  "receiver" : ""
}

dataPaylod_pool.append(dataPayload7)

block_four_dataPayloads = []

block_four_dataPayloads.append(dataPaylod_pool[0:3])
#local_blockchain.add_block(block_four_dataPayloads, remarks)
local_blockchain.validate_chain()

for i in range(5):
        new_block = []
        local_blockchain.add_block(dataPaylod_pool[3:], remarks)
        local_blockchain.validate_chain()
        time.sleep(2)

local_blockchain.chain[3].remarks = "This block contains logistics and traffic datapayloads related to RegionACCD1234"
local_blockchain.validate_chain()

from flask import Flask, render_template, jsonify
import os
 
app = Flask(__name__)
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/_get_data/', methods=['POST'])

def _get_data():
    myList = local_blockchain.print_blocks(), local_blockchain.validate_chain()
    return jsonify({'data': render_template('response.html', myList=myList)})

if __name__ == "__main__":
    app.run(debug=True)


   









