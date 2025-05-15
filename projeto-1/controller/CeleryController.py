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
from models.entities.ViaCep import ViaCep
from controller.CeleryWorker  import processar_cep, processar_cep_BrasilApiCep, teste_connection

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
    contents = await file.read()
    stringio = StringIO(contents.decode()) 
    csv_reader = csv.DictReader(stringio)
    # print(csv_reader[0]['CEP'])
    # next(csv_reader)
    for row in csv_reader:
        cep = row['CEP']
        print(f"Enviando mensagem para o RabbitMQ: {cep}")
        processar_cep.apply_async(args=[cep], countdown=5)
    return {"message": f"Arquivo recebido! CPFs serão processados."}

@router_publico.post("/upload-csv-brasilapi")
async def upload_csv_brasilapi(file: UploadFile = File(...)):    
    contents = await file.read()
    stringio = StringIO(contents.decode()) 
    csv_reader = csv.DictReader(stringio)
    # print(csv_reader[0]['CEP'])
    # next(csv_reader)
    for row in csv_reader:
        cep = row['CEP']
        print(f"Enviando mensagem para o RabbitMQ: {cep}")
        processar_cep_BrasilApiCep.delay(cep)
    return {"message": f"Arquivo recebido! CPFs serão processados."}

@router_publico.post("/teste-request")
async def teste_request():
    teste_connection.delay("teste")
    return "feito o delay"

@router_publico.get("/teste-apply-async")
async def teste_api_async():
    processar_cep.apply_async(args=["88058000"], countdown=5)
    return "feito o async"

