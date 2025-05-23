import json
import pika
import redis
import time
from config import get_rabbitmq_channel

redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

channel = get_rabbitmq_channel()

def run_consumer_processar_disponibilidade():
    print("Iniciando consumo...")
    while True:
        method_frame, properties, body = channel.basic_get(queue='service_monitor', auto_ack=False)

        if method_frame:
            processar_disponibilidade(channel, method_frame, properties, body)
        else:
            print("Fila vazia. Encerrando consumidor.")
            break
    
    
def processar_disponibilidade(ch, method, properties, body):
    try:
        json_data = json.loads(body)        
        timestamp = int(time.time())
        status_code = json_data.get("status_code")
        latency_ms = json_data.get("latency_ms")
        url = json_data.get("url")
        
        redis_client.zadd("latencies", {url: latency_ms})
        # Se for erro (status >= 400), registra no Sorted Set de erros com o timestamp   
        if status_code >= 400:
            redis_client.zadd("errors", {url: timestamp})
            print(f"URL: {url}, Status code: {status_code}, json = {json_data}")
        else:
            print(f"URL: {url}, Status code: {status_code}, json = {json_data}")
        channel.basic_ack(delivery_tag=method.delivery_tag)
        
    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")
        channel.basic_nack(delivery_tag=method.delivery_tag, requeue=False)  # descarta

