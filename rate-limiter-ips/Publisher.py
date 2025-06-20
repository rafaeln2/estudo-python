from datetime import datetime
import os
import random
import time
from zoneinfo import ZoneInfo
from fastapi import APIRouter
import requests
from Aggregator import print_estatisticas
from dotenv import load_dotenv
load_dotenv()

import pika
import json
from config import get_rabbitmq_channel

router = APIRouter()

ips = [
    "192.168.1.10",
    "10.0.0.25",
    "10.0.0.25",
    # "172.16.0.42"
    # "203.0.113.7",
    # "8.8.8.8"
    # "198.51.100.23",
    # "192.0.2.5",
    # "185.60.216.35",
    # "100.64.0.1",
    # "45.33.32.156"
]
endpoints = [
    "/login",
    "/projetos/consultas",
    "/projetos/cadastro"
]

def verifica_disponibilidade():
    try:        
        channel = get_rabbitmq_channel()
        for ip in ips:            
            try:                            
                json_data = {
                    "ip": ip,
                    "endpoint": endpoints[0], #random.choice(endpoints)
                    "timestamp": datetime.now(ZoneInfo('America/Sao_Paulo')).isoformat()
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
            except Exception as e:
                print(f"Erro desconhecido {ip}: {str(e)}")
        print("finalizado envio de mensagem!")
    except Exception as e:
        print(f"Erro publisher: {e}")
        