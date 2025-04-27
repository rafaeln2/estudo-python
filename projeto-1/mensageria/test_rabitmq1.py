import pika
import logging

logging.basicConfig(level=logging.DEBUG)

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(
    host='host.docker.internal',
    port=5672,
    virtual_host='/',
    credentials=credentials,
    connection_attempts=3,
    retry_delay=2,
    socket_timeout=5,
    blocked_connection_timeout=10
)

try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='demo-queue', durable=True)
    print("✅ Conectado ao RabbitMQ com sucesso!")
except Exception as e:
    print(f"❌ Erro ao conectar com RabbitMQ: {e}")
