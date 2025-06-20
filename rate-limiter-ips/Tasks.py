import json
import pika
import redis
import time
from config import get_rabbitmq_channel
from DatabaseConnection import registrar_log

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
        timestamp = json_data.get("timestamp")   

        rate_limiter_key = f"rl:{ip}:{endpoint}" # prepara chave da fila de taxa de limite
        
        qntd_acessos = redis_client.incr(rate_limiter_key) # insere na fila das taxas com increase
        
        # se for a primeira requisição, define a expiração da chave
        if qntd_acessos == 1:
            redis_client.expire(rate_limiter_key, WINDOW_SECONDS)

        # se a qntd de acessos for maior que o limite
        if qntd_acessos > RATE_LIMIT:
            # excedeu o limite — envia para fila "rejeitados"            
            registrar_log(ip, endpoint, False, timestamp)            
            print(f"[REJEITADO] {ip} {endpoint} ({qntd_acessos})")
        else:
            # ainda dentro do limite — envia para fila "aceitos"
            registrar_log(ip, endpoint, True, timestamp)            
            print(f"[ACEITO] {ip} {endpoint} ({qntd_acessos})")

        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)


