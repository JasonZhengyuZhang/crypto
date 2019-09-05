import requests
import json
import time
from anytree import Node, RenderTree
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

# bitpay = [
#     "https://insight.bitpay.com/api/address/1KEkZ1LXj4VpohS6ZN1tHouW8r9yja5gbP",
#     "https://insight.bitpay.com/api//tx/7eaac3e74c906fa6376fbdfa732f0c1a079d5e20554a13d46845ef063c7afe12",
#     "https://insight.bitpay.com/api/block/0000000000000000001454d34ff552b26be18199dc80d4ed3bdeec439e4bf5c8"
# ]

# blockchain = [
#     "https://blockchain.info/rawblock/0000000000000bae09a7a393a8acded75aa67e46cb81f7acaa5ad94f9eacd103",
#     "https://blockchain.info/rawtx/b6f6991d03df0e2e04dafffcd6bc418aac66049e2cd74b80f14ac86db1e3f0da",
#     "https://blockchain.info/rawaddr/1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F"
# ]

# def identifyAddress(h):
#     allTrans = inputOutputAddress(h)
    
#     # allTrans is a list of Trans Object

#     # I should loop through allTrans and then for each individual Traansaction
#     # object and then figure out all the unique address, 

#     nodes = []
#     edges = []

#     id=0

#     If you want fresh rice, you 

#     for tx in allTrans:
#         node = {
#             'id': id,
#             'label': tx.hash
#         }
#         nodes.append(node)

#         edge = {
#             'from': sd
#         }
        
# @app.route('/')
# def hello_world():
#     return render_template('index.html')

# def trackTransaction(t, h):
#     # parse the transaction for all input and all output
#     res = buildCall('rawtx', h)


#     if type(res)!=str:
#         ti = parseTransaction(res['inputs'])
#         to = parseTransaction(res['out'])
        
#         print(type(res))
#         print(res)
#         print('popo\n')
#         print(json.dumps(res['inputs'], indent=2))
#         print(json.dumps(res['out'], indent=2))
#     else:
#         print('failed to call', res)
#         return 
    
def call(req):
    response = requests.get(req)
    print(req, response.status_code)
    return response.json()

def buildCall(t, h, offset=0):
    try:
        parameters = ''.join(['?offset=', str(offset)]) if offset!=0 else ''
        endpoint = 'https://blockchain.info/'+t+'/'+h+parameters
        res = call(endpoint)
        return res
    except Exception as e:
        return e

def parseBlock():
    pass

def fetchAllBlock():
    res = buildCall('rawblock', '000000000000000000123416369bded17411745b6bb42dcdf8d9b51cb414386c')
    #80seconds for 50 things
    temp = 0

    while  temp < 50:
        nextB = res['prev_block']
        
        res = buildCall('rawblock', nextB)

        print(nextB)
        print(res['n_tx'])
        print(len(res['tx']))
        print(temp)
        temp+=1


def parseAddress():
    pass

def parseTransaction(transaction):
    res = {}

    for item in transaction:
        try:
            res['out_addr']=item['prev_out']['addr']
        except:
            res['out_addr']=''

    return res

class LinkedList:
    def __init__(self, val):
        self.val = data
        self.next = None
        self.prev = None

def trackAddress(h, maxTraverse = 0, fullResult = [], t = 'rawaddr'):
    res = buildCall(t, h)
    transactions = res['txs']
    numTrans = len(transactions)

    tUpper=[]
    tLower=[]

    for tx in transactions:
        time = tx['time']
        txHash = tx['hash']

        for txI in tx['inputs']:
            pass

        for txO in tx['out']:
            pass

    ti=[]
    to=[]

    for index, item in enumerate(res['txs']):
        ti.append(parseTransaction(item['inputs']))
        to.append(parseTransaction(item['out']))
        
        print(h, index, numTrans)

    fullResult.append(ti)
    fullResult.append(to)

    if maxTraverse<=0:
        return fullResult
    else:
        return trackAddress(h, maxTraverse-1)   

class BTCTx:
    def __init__(self, hash):
        self.hash = hash
        self.blockIndex = None
        self.time = None
        self.lhs = None
        self.rhs = None

def extractLedger(ledger, side):
    res=[]
    for row in ledger:
        try:
            addr = row['prev_out']['addr'] if side==0 else row['addr']
        except: 
            addr = 'Newly Generated Coins' if side==0 else 'Unable to decode address'

        try:
            value = row['prev_out']['value'] if side==0 else row['value']
        except:
            value = 'Unable to decode'

        temp = {
                'address': addr,
                'value': value/100000000
            }
        res.append(temp)

    return res 

def inputOutputAddress(h, offset=0, newTxOffset=0, TxHashes=[], val=[]):
    # the applications first check will be to call on offset with whatever
    # the current value is, it wil then check whether the number of transactions
    # from thr result is equal to the current number of elements in TxHashes

    # call the hash and offset by how much, starts at 0
    res = buildCall('rawaddr', h, offset)
    # the total number of transactions that is currently on the api call
    numTrans = res['n_tx']

    if len(val) == numTrans:
        return val
    else:
        transactions = res['txs']
        for tx in transactions:
            currentTX = BTCTx(tx['hash'])
            currentTX.blockIndex = tx['block_index']
            currentTX.time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(tx['time'])))
            currentTX.lhs = extractLedger(tx['inputs'], 0)
            currentTX.rhs = extractLedger(tx['out'], 1)

            val.append(currentTX)
        
        return inputOutputAddress(h, offset+50, 0, [], val)

if __name__ == '__main__':
    # app.run(host= '0.0.0.0', port=80)

    # fetchAllBlock()

    # h = "1FzWLkAahHooV3kzTgyx6qsswXJ6sCXkSR"
    # tempRes=identifyAddress(h)

    h = "1FzWLkAahHooV3kzTgyx6qsswXJ6sCXkSR"
    tempRes=trackAddress(h)
    print(tempRes, len(tempRes))
    