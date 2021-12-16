from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from dotenv import load_dotenv  # Permet le stockage de données sensible dans un fichier à part
import os                       # Fonction liée à l'operating system
import websocket, json
from json import loads
from elasticsearch import Elasticsearch

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))
IP_ES = os.getenv("IP_ES")

default_args = {
    'owner': 'Mangouste',
    'start_date': datetime.utcnow(),
    "retries": 1,
    "retry_delay": timedelta(seconds=5)
}

dag = DAG(
    "tutorial",
    default_args=default_args,
    start_date=datetime(2015, 12, 1),
    description="Extraction du cours de l'ADA",
    schedule_interval='* * * * * *',
    catchup=False
)

XYZ = DAG('websocket_ada', default_args=default_args)

####### Definition des Fonctions / Executions #######

def on_message(ws, message):
    es = Elasticsearch([IP_ES])
    cc = "adausdt"
    json_message = json.loads(message)
    price_int = json_message['p']
    price = float(price_int)
    doc = {
    'exchanger' : 'Binance',
    'price_int' : price,
    'symbol' : json_message['s'],
    'timestamp' : datetime.now()
    }
    es.index(index="test_websocket", document=doc)
    socket = f"wss://stream.binance.com:9443/ws/{cc}@trade"
    ws = websocket.WebSocketApp(socket, on_message = on_message)
    ws.run()

P1 = PythonOperator(
    task_id='queryyy_websocket',
    python_callable=on_message,
    dag=XYZ
)

####### Definition des Etapes #######

P1