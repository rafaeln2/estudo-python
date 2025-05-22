import os
import time
from fastapi import APIRouter, Depends, File, UploadFile
import requests
from tasks import processar_disponibilidade
from Aggregator import aggregator, print_all
from dotenv import load_dotenv
load_dotenv()

router = APIRouter()

@router.get("/ligar-task")
def prepara_verificacao_disponibilidade_ceps():
    # while True:
        for nome, url in lista_servicos.items():
            for cep in ceps:                
                try:                
                    start = time.perf_counter()
                    url_formatada = url.format(cep)
                    response = requests.get(url_formatada, timeout=15)
                    finish = time.perf_counter()
                    latencia_requisicao = round((finish - start), 3)
                    json_data = {
                        "url": url_formatada,
                        "status_code": response.status_code,
                        "latency_ms": latencia_requisicao
                    }

                    processar_disponibilidade.delay(json_data) 
                    time.sleep(10)            
                except requests.Timeout:
                    print(f"Erro: Timeout {nome} para o CEP {cep}.")
                except requests.RequestException as exc:
                    print(f"Erro ao acessar o {nome} para o CEP {cep}: {str(exc)}")
                except Exception as e:
                    print(f"Erro desconhecido {nome} para o  CEP {cep}: {str(e)}")
        # aggregator()
        print_all()

        # time.sleep(300)

def prepara_verificacao_disponibilidade():
    while True:
        urls = os.getenv("SITES_MONITORAMENTO","") 
        sites = urls.split(",") if urls else []
        for site in sites:            
            try:                
                start = time.perf_counter()
                response = requests.get(site, timeout=15)
                finish = time.perf_counter()
                latencia_requisicao = round((finish - start), 3)
                json_data = {
                    "url": site,
                    "status_code": response.status_code,
                    "latency_ms": latencia_requisicao
                }

                processar_disponibilidade.delay(json_data) 
                # time.sleep(10)            
            except requests.Timeout:
                print(f"Erro: Timeout para o site {site}.")
            except requests.RequestException as exc:
                print(f"Erro ao acessar o {site}: {str(exc)}")
            except Exception as e:
                print(f"Erro desconhecido {site}: {str(e)}")
        aggregator()
        time.sleep(120)
        # print_all()
