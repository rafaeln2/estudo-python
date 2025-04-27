from fastapi import APIRouter

from mensageria.Consumer import RabbitmqConsumer
from mensageria.Publisher import RabbitmqPublisher


router_publico = APIRouter()

@router_publico.get("/teste-consumer")
async def TesteConsumer():
    def minha_callback(ch,method,properties,body):
        print(f"Mensagem recebida: {body}")
    rabitmq_consumer = RabbitmqConsumer(minha_callback);
    rabitmq_consumer.start()
    return print("finalizado callback")


@router_publico.get("/teste-publisher")
async def TestePublisher():
    rabbitmq_publisher = RabbitmqPublisher()
    rabbitmq_publisher.send_message(body={"message": "Hello World!"})
    return print("finalizado callback")
