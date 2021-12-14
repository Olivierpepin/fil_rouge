import websocket, json
from json import loads
from elasticsearch import Elasticsearch
from datetime import datetime
from time import sleep
from dotenv import load_dotenv  # Permet le stockage de données sensible dans un fichier à part
import os                       # Fonction liée à l'operating system

# Recuperation des variables d'environnements.

BASEDIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(BASEDIR, '.env'))

IP_ES = os.getenv("IP_ES")

cc = "adausdt"

socket = f"wss://stream.binance.com:9443/ws/{cc}@trade"

es = Elasticsearch([IP_ES])

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