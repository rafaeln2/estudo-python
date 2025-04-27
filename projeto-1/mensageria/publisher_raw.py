import pika

connection_parameters = pika.ConnectionParameters(
    host='rabbitmq',
    port=5672,
    credentials=pika.PlainCredentials('guest', 'guest'))

channel = pika.BlockingConnection(connection_parameters).channel()

channel.basic_publish(
    exchange='demo-exchange-fanout',
    routing_key='',
    body='direto do python'.encode(),
    properties=pika.BasicProperties(
        delivery_mode=2
    )
)