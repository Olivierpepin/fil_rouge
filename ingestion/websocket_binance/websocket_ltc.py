## Documentation Binance : https://binance-docs.github.io/apidocs/spot/en/#aggregate-trade-streams

import websocket, json                  # Docs : https://websocket-client.readthedocs.io/en/latest/examples.html
from elasticsearch import Elasticsearch # Docs : https://elasticsearch-py.readthedocs.io/en/v7.16.2/
from datetime import datetime           # Docs : https://docs.python.org/fr/3/library/datetime.html
from time import sleep                  # Docs : https://docs.python.org/fr/3/library/time.html
from dotenv import load_dotenv  # Permet le stockage de données sensible dans un fichier à part
import os                       # Fonction liée à l'operating system

# Recuperation des variables d'environnements.

BASEDIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(BASEDIR, '.env'))

IP_ES = os.getenv("IP_ES")

# Attribution des variables des channels de websockets et adresse IP ES

cc = "ltcusdt"

socket = f"wss://stream.binance.com:9443/ws/{cc}@trade"

es = Elasticsearch([IP_ES])

# Fonction de récupération payloads websocket, creation d'un document avec selection element du payload, envoi a ES

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

# Fonction impression erreur dans la console

def on_error(ws, error):
    print(error)

# Envoi requete websocket

ws = websocket.WebSocketApp(socket, on_message = on_message, on_error= on_error)

# Connexion continu au websocket

ws.run_forever(ping_interval=50)