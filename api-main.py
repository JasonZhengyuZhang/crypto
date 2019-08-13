import requests
import json

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

def call(req):
    response = requests.get(req)
    print(req, response.status_code)
    return response.json()

def buildCall(t, h):
    try:
        endpoint = 'https://blockchain.info/'+type+'/'+h
        res = call(endpoint)
        return res
    except Exception as e:
        return e

def parseBlock():
    pass

def parseTransaction():
    pass

def parseAddress():
    pass

def track(h):
    # parse the transaction for all input and all output
    res = buildCall('rawtx', h)

    if type(res)!==str:
        print(type(res))
        print(res)
    else:
        print('failed to call', res)



h = "de1feb1a1d89f59dd2f6b7f0abe012cd141180b93ec56fcbe437936ad679061b"
track(h)