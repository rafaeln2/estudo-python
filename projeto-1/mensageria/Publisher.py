import pika
import json
from typing import Dict

class RabbitmqPublisher:
    def __init__(self):
        self.__host = 'rabbitmq'
        self.__port = 5672
        self.__username = 'guest'
        self.__password = 'guest'
        self.__exchange = "demo-exchange-fanout"
        self.__routing_key = ""
        self.__channel = self.__create_channel()
    
    def __create_channel(self):
        credentials = pika.PlainCredentials(username=self.__username, password=self.__password)
        parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=credentials,
        )
        connection = pika.BlockingConnection(parameters)
        return connection.channel()
    
    def send_message(self, body: Dict):
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__routing_key,
            body=json.dumps(body),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )
        