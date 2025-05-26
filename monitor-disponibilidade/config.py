import pika
import time

def get_rabbitmq_channel(host='rabbitmq', port=5672, exchange='service_monitor', queue='service_monitor', routing_key=''):
    for _ in range(5):  # Tenta várias vezes (útil quando containers estão subindo)
        try:
            connection = pika.BlockingConnection(
                parameters=pika.ConnectionParameters(host=host, port=port)
            )
            channel = connection.channel()

            channel.exchange_declare(exchange=exchange, exchange_type='direct', durable=True)
            channel.queue_declare(queue=queue, durable=True)
            channel.queue_bind(exchange=exchange, queue=queue, routing_key=routing_key)

            return channel
        except pika.exceptions.AMQPConnectionError as e:
            print(f"❌ Falha ao conectar ao RabbitMQ: {e}. Tentando novamente em 5s...")
            time.sleep(5)

    raise ConnectionError("🚨 Não foi possível conectar ao RabbitMQ após múltiplas tentativas.")
