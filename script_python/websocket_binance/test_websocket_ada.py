import websocket, json
from json import loads
from elasticsearch import Elasticsearch
from datetime import datetime
from time import sleep

cc = "adausdt"

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