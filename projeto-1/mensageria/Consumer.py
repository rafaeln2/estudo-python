import pika

class RabbitmqConsumer:
    def __init__(self, callback):
        self.__host = 'rabbitmq'
        self.__port = 5672
        self.__username = 'guest'
        self.__password = 'guest'
        self.__queue_name = 'demo-queue'
        self.__callback = callback
        self.__channel = self.__create_channel()
        
    def __create_channel(self):
        credentials = pika.PlainCredentials(self.__username, self.__password)
        parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            virtual_host='/',
            credentials=credentials,
            connection_attempts=3,
            retry_delay=2,
            socket_timeout=5,
            blocked_connection_timeout=10
        )
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue=self.__queue_name, durable=True)
        channel.basic_consume(
            queue=self.__queue_name,
            on_message_callback=self.__callback,
            auto_ack=True
        )
        return channel
    
    def start(self,) -> None:   
        print("Esperando mensagens...")
        self.__channel.start_consuming()
        
# def minha_callback(ch,method,properties,body):
#     print(f"Mensagem recebida: {body}")

        
# rabitmq_consumer = RabbitmqConsumer(minha_callback);
# rabitmq_consumer.start()