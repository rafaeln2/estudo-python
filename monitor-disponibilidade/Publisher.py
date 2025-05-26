import os
import time
from fastapi import APIRouter
import requests
from Aggregator import aggregator_latencias_erros
from dotenv import load_dotenv
load_dotenv()

import pika
import json
from config import get_rabbitmq_channel

router = APIRouter()

# Puxa do env a lista de sites para fazer as requisições e manda a url, status_code e latency pro rmq
def verifica_disponibilidade():
    try:
        # while True: 
        channel = get_rabbitmq_channel()
        print("inicio dos envios pro rmq")          
        urls = os.getenv("SITES_MONITORAMENTO","") 
        sites = urls.split(",") if urls else []
        for site in sites:            
            try:                
                start = time.perf_counter()
                response = requests.get(site, timeout=15)
                finish = time.perf_counter()
                latencia_requisicao = round((finish - start), 3)
                json_data = {
                    "url": site,
                    "status_code": response.status_code,
                    "latency_ms": latencia_requisicao
                }
                
                print("enviando mensagem pro rabbitmq...")
                channel.basic_publish(
                    exchange='service_monitor',
                    routing_key='',
                    body=json.dumps(json_data),
                    properties=pika.BasicProperties(
                        delivery_mode=2
                    )
                )
                print("finalizado envio de mensagem!")
            except requests.Timeout:
                print(f"Erro: Timeout para o site {site}.")
            except requests.RequestException as exc:
                print(f"Erro ao acessar o {site}: {str(exc)}")
            except Exception as e:
                print(f"Erro desconhecido {site}: {str(e)}")
    except Exception as e:
        print(f"Erro publisher: {e}")
        