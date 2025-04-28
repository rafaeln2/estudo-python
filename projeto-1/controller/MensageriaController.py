import asyncio
import csv
from io import StringIO
import threading
from fastapi import APIRouter, Depends, File, UploadFile
import requests
import httpx
from sqlalchemy.ext.asyncio import AsyncSession

from mensageria.Consumer import RabbitmqConsumer
from mensageria.Publisher import RabbitmqPublisher

from repository.ViacepRepository import ViacepRepository
from config.session import get_db
from models.entities import Usuario, ViaCep

router_publico = APIRouter()
via_cep_url = 'https://viacep.com.br/ws/{}/json/'

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

@router_publico.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):    
    publisher = RabbitmqPublisher()
    contents = await file.read()
    stringio = StringIO(contents.decode()) 
    csv_reader = csv.DictReader(stringio)
    next(csv_reader)
    for row in csv_reader:
        cep = row['CEP']
        publisher.send_message(cep)
        print(f"Enviando mensagem para o RabbitMQ: {cep}")
    return {"message": "Arquivo recebido! CPFs serão processados."}

async def callback_cep(ch, method, properties, body, db: AsyncSession = Depends(get_db)):
    print(f"Processando CEP: {body}")
    repo = ViacepRepository(db)
    cep = await repo.get_viacep_by_cep(body)
    if not cep:
        async with httpx.AsyncClient() as client:
            response = await client.get(via_cep_url.format(body))
            endereco = response.json()
            if response.status_code == 200 and "erro" not in endereco:
                endereco = response.json()
                await repo.create_viacep(ViaCep(**endereco)) 
                print(f"CEP {body} processado com sucesso!")            
            else:
                print(f"Erro ao buscar dados do CEP {body}: {response.status_code}")
    else:
        print(f"CEP {body} já existe no sistema.")
@router_publico.post("/process-csv")
async def process_csv():    
    consumer = RabbitmqPublisher()
    rabitmq_consumer = RabbitmqConsumer(callback_cep)
    thread = threading.Thread(target=rabitmq_consumer.start)
    print("Iniciando o consumidor...")
