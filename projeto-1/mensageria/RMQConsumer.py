import pika
# from pika import RobustConnection

def minha_callback(ch, method, properties, body):
    print(f"Mensagem recebida: {body}")

credentials = pika.PlainCredentials('user', 'password')
# parameters = pika.ConnectionParameters(
#     host='127.0.0.1', #172.18.0.3
#     port=5672,
#     virtual_host='/',
#     credentials=credentials
# )

parameters = pika.URLParameters(url="amqp://guest:guest@localhost:15672/")

channel = pika.BlockingConnection(parameters).channel()
channel.queue_declare(
    queue='demo-queue',
    durable=True
)
channel.basic_consume(
    queue='demo-queue',
    auto_ack=True,
    on_message_callback=minha_callback
)

print(f"Listen rabbitmq on port 5672")
channel.start_consuming()