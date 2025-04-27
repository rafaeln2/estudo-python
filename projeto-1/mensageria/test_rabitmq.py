import pika
import subprocess
import logging
import requests
from requests.auth import HTTPBasicAuth
logging.basicConfig(level=logging.DEBUG)


credentials = pika.PlainCredentials('nome', 'senha')  # substitua por nome e senha reais

#wsl ip 192.168.0.60
# docker ip 172.18.0.3
parameters = pika.ConnectionParameters(
    host='host.docker.internal',  # ou o IP da máquina onde está o RabbitMQ
    port=5672,
    virtual_host='/',  # padrão
    credentials=credentials,
    connection_attempts=5,         # tenta conectar 5 vezes
    retry_delay=2,                 # espera 2 segundos entre tentativas
    socket_timeout=10,            # timeout da conexão em segundos
    blocked_connection_timeout=30
)



# url = "amqp://guest:guest@192.168.0.1:5672/%2f"  # %2f é o `/` codificado
# parameters = pika.URLParameters(url)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# garante que a fila existe
channel.queue_declare(queue='demo-queue', durable=True)

def minha_callback(ch, method, properties, body):
    print(f"Mensagem recebida: {body.decode()}")

channel.basic_consume(
    queue='demo-queue',
    on_message_callback=minha_callback,
    auto_ack=True
)

print("Esperando mensagens...")
channel.start_consuming()