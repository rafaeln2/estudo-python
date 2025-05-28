import json
import pika
import redis
import time
from config import get_rabbitmq_channel

redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

channel = get_rabbitmq_channel()

# Configuração do rate limit
RATE_LIMIT = 10       # Máximo de requisições
WINDOW_SECONDS = 60   # Por 60 segundos

def run_consumer_processar_limites_de_acesso():
    print("Iniciando consumo...")
    while True:
        method_frame, properties, body = channel.basic_get(queue='service_monitor', auto_ack=False)
        if method_frame:
            processar_limites_de_acesso(channel, method_frame, properties, body)
        else:
            print("Fila vazia. Encerrando consumidor.")
            break

def processar_limites_de_acesso(ch, method, properties, body):
    try:
        json_data = json.loads(body)
        ip = json_data.get("ip")
        endpoint = json_data.get("endpoint")        

        rate_limiter_key = f"rl:{ip}:{endpoint}"
        
        current = channel.incr(rate_limiter_key)
        
        # Se for a primeira requisição, define a expiração da chave
        if current == 1:
            channel.expire(rate_limiter_key, WINDOW_SECONDS)

        if current > RATE_LIMIT:
            # Excedeu o limite — envia para fila "rejeitados"
            channel.rpush("fila:rejeitados", json.dumps({"ip": ip, "endpoint": endpoint}))
            print(f"[REJEITADO] {ip} {endpoint} ({current})")
        else:
            # Ainda dentro do limite — envia para fila "aceitos"
            channel.rpush("fila:aceitos", json.dumps({"ip": ip, "endpoint": endpoint}))
            print(f"[ACEITO] {ip} {endpoint} ({current})")

        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)


