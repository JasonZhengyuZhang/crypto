import requests
import json
import time
from anytree import Node, RenderTree


bitpay = [
    "https://insight.bitpay.com/api/address/1KEkZ1LXj4VpohS6ZN1tHouW8r9yja5gbP",
    "https://insight.bitpay.com/api//tx/7eaac3e74c906fa6376fbdfa732f0c1a079d5e20554a13d46845ef063c7afe12",
    "https://insight.bitpay.com/api/block/0000000000000000001454d34ff552b26be18199dc80d4ed3bdeec439e4bf5c8"
]

blockchain = [
    "https://blockchain.info/rawblock/0000000000000bae09a7a393a8acded75aa67e46cb81f7acaa5ad94f9eacd103",
    "https://blockchain.info/rawtx/b6f6991d03df0e2e04dafffcd6bc418aac66049e2cd74b80f14ac86db1e3f0da",
    "https://blockchain.info/rawaddr/1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F"
]

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

def buildCall(t, h):
    try:
        endpoint = 'https://blockchain.info/'+t+'/'+h
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

def extractLedger(ledger, ver):
    res=[]
    for row in ledger:
        addr = row['addr'] if ver==1 else row['prev_out']['addr']
        temp = {
                'address': row['addr'],
                'value': row['value']/100000000
            }
        res.append(temp)

    return res 

def inputOutputAddress(h):
    res = buildCall('rawaddr', h)
    transactions = res['txs']
    numTrans = len(transactions)

    allTrans = []

    for tx in transactions:
        tVer = 1 if tx['ver']==1 else 2

        currentTX = BTCTx(tx['hash'])        
        currentTX.blockIndex = tx['block_index']
        currentTX.time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(tx['time'])))
        currentTX.lhs = extractLedger(tx['inputs'], tVer)
        currentTX.rhs = extractLedger(tx['out'], tVer)

        allTrans.append(currentTX)

    return allTrans

def identifyAddress(h):
    allTrans = inputOutputAddress(h)
    
    # allTrans is a list of Trans Object

    # I should loop through allTrans and then for each individual Traansaction
    # object and then   

    for tx in allTrans:
        print(tx)
        print(tx.hash)
        print(tx.lhs)

        

h = "1FzWLkAahHooV3kzTgyx6qsswXJ6sCXkSR"
tempRes=identifyAddress(h)

# h = "1FzWLkAahHooV3kzTgyx6qsswXJ6sCXkSR"
# tempRes=trackAddress(h)
# print(tempRes, len(tempRes))
# fetchAllBlock()