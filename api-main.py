import requests
import json
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

def parseAddress():
    pass

def parseTransaction(transaction):
    res = {}

    for item in transaction:
        res['addr']=item['addr']

    return res

def trackAddress(h, maxTraverse = 0, fullResult = [], t = 'rawaddr'):
    res = buildCall(t, h)
    transactions = res['txs']
    numTrans = transactions.length

    ti=[]
    to=[]

    for index, item in enumerate(res['txs']):
        ti.append(parseTransaction(res['inputs']))
        to.append(parseTransaction(res['out']))
        print(h, index, numTrans)

    fullResult.append(ti)
    fullResult.append(to)

    if maxTraverse<=0:
        return fullResult
    else:
        return trackAddress(h, maxTraverse-1)   

h = "1FzWLkAahHooV3kzTgyx6qsswXJ6sCXkSR"
tempRes=trackAddress(h)

print(tempRes, len(tempRes))