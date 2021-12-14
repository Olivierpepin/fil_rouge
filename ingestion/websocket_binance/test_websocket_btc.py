import websocket, json
from json import loads
from elasticsearch import Elasticsearch
from datetime import datetime
from time import sleep

# Channel trade sur Binance : 

'''{
  "e": "trade",     // Event type
  "E": 123456789,   // Event time
  "s": "BNBBTC",    // Symbol
  "t": 12345,       // Trade ID
  "p": "0.001",     // Price
  "q": "100",       // Quantity
  "b": 88,          // Buyer order ID
  "a": 50,          // Seller order ID
  "T": 123456785,   // Trade time
  "m": true,        // Is the buyer the market maker?
  "M": true         // Ignore
}'''

cc = "btcusdt"

socket = f"wss://stream.binance.com:9443/ws/{cc}@trade"

es = Elasticsearch(["http://elastic:iTDviTnRisEubZjSx739@localhost:9200"])

def on_message(ws, message):
    json_message = json.loads(message)
    price_int = json_message['p']
    price = float(price_int)
    doc = {
    'exchanger' : 'Binance',
    'price_int' : price,
    'symbol' : json_message['s'],
    'timestamp' : datetime.now()
    }
    res = es.index(index="test_websocket", document=doc)
    print(res)
    sleep(1)

ws = websocket.WebSocketApp(socket, on_message = on_message)

ws.run_forever()