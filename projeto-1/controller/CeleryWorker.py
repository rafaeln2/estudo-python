import asyncio
from celery import Celery
from fastapi import Depends, File
import requests
from sqlalchemy import true


from mensageria.Consumer import RabbitmqConsumer
from mensageria.Publisher import RabbitmqPublisher

from repository.ViacepRepositorySync import ViacepRepositorySync
from repository.BrasilApiCepSyncRepository import BrasilApiCepSyncRepository
from models.entities.ViaCep import ViaCep
from models.entities.BrasilApiCep import BrasilApiCep
from config.session import get_db, get_db_sync
from config.celery import celery_app


via_cep_url = 'https://viacep.com.br/ws/{}/json/'
brasil_api_url = 'https://brasilapi.com.br/api/cep/v1/{}'


@celery_app.task(bind=True, max_retries=3, retry_backoff=True, time_limit=10)
def processar_cep(self, cep):
    print(f"Processando CEP: {cep}")
    db = next(get_db_sync())
    
    repo = ViacepRepositorySync(db)
    is_cep_already_in_db = repo.get_viacep_by_cep(cep) is not None
    print(f"CEP já no banco: {is_cep_already_in_db}")
    
    if not is_cep_already_in_db:
        try:
            print(f"Fazendo requisição ao ViaCEP para o CEP {cep}...")
            response = requests.get(via_cep_url.format(cep.replace('-', '')), timeout=10)
            print(f"Resposta recebida: {response.status_code}")
            
            endereco = response.json()
            print(f"Validando dados recebidos...")

            if response.status_code == 200 and "erro" not in endereco:
                print("Salvando dados no banco...")
                repo.create_viacep(ViaCep(**endereco))
                print(f"CEP {cep} processado com sucesso!")
            else:
                raise ValueError(f"Erro ao buscar dados do CEP {cep}: {response.status_code} - {endereco.get('erro', 'Desconhecido')}")
        
        except (requests.Timeout, requests.RequestException, ValueError) as exc:
            print(f"Erro ao processar o CEP {cep}, tentando novamente... ({str(exc)})")
            raise self.retry(exc=exc, countdown=30)  # Tenta de novo em 30 segundos
        
        except Exception as e:
            print(f"Erro inesperado: {e}")
            raise self.retry(exc=e, countdown=30)

    else:
        print(f"CEP {cep} já existe no sistema.")

@celery_app.task(rate_limit='1/m') #bind=True, autoretry_for=(Exception,), retry_backoff=True, time_limit=10
def processar_cep_BrasilApiCep(cep):
    print(f"Processando CEP: {cep}")
    db = next(get_db_sync())
    
    repo = BrasilApiCepSyncRepository(db)
    is_cep_already_in_db = True if repo.get_brasil_api_cep_by_cep(cep) is not None else False
    print(f"CEP já no banco: {is_cep_already_in_db}")
    
    if not is_cep_already_in_db:
        try:
            print(f"Fazendo requisição ao BrasilAPI para o CEP {brasil_api_url.format(cep.replace('-', ''))}...")
            response = requests.get(brasil_api_url.format(cep.replace('-', '')), timeout=10)  # Timeout de 10 segundos
            print(f"Resposta recebida: {response.status_code}")
            
            endereco = response.json()
            print(f"Validando dados recebidos...")

            if response.status_code == 200 and "erros" not in endereco:
                print("Salvando dados no banco...")
                repo.create_brasil_api_cep(BrasilApiCep(**endereco))
                print(f"CEP {cep} processado com sucesso!")
            else:
                print(f"Erro ao buscar dados do CEP {cep}: {response.status_code} - {endereco.get('erro', 'Desconhecido')}")
        except requests.Timeout:
            print(f"Erro: Timeout ao tentar acessar o BrasilAPI para o CEP {cep}.")
        except requests.RequestException as exc:
            print(f"Erro ao acessar o BrasilAPI para o CEP {cep}: {str(exc)}")
        except Exception as e:
            print(f"Erro ao processar o CEP {cep}: {str(e)}")
    else:
        print(f"CEP {cep} já existe no sistema.")
        
@celery_app.task(bind = True, max_retries=3, retry_backoff=True, retry_backoff_max=10)
def teste_connection(self, msg: str):
    print("Testando conexão...")
    try:
        google = requests.get("https://brasilapi.com.br/api/cep/v1/88117260")
        print(google.json())
        # print(google.json())
        print("Conexão com estabelecida com sucesso!")
    except requests.Timeout as exc:
        raise self.retry(exc=exc, countdown=10)
    except Exception as e:
        print(f"Erro ao conectar: {str(e)}")