import websocket, json
from json import loads
from elasticsearch import Elasticsearch
from datetime import datetime
from time import sleep

cc = "btcusdt"

socket = f"wss://stream.binance.com:9443/ws/{cc}@aggTrade"

es = Elasticsearch(["http://elastic:iTDviTnRisEubZjSx739@localhost:9200"])

def on_message(ws, message):
    json_message = json.loads(message)
    print(json_message)

ws = websocket.WebSocketApp(socket, on_message = on_message)

ws.run_forever()
