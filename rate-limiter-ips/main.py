# main.py
import time
from Publisher import envia_dados_requisicoes
from Tasks import run_consumer_processar_limites_de_acesso
from Aggregator import aggregator_latencias_erros
import schedule

def job():
    envia_dados_requisicoes()
    # time.sleep(1)
    run_consumer_processar_limites_de_acesso()

def main():
    schedule.every(1).seconds.do(job)
    schedule.every(60).seconds.do(aggregator_latencias_erros)

    while True:
        schedule.run_pending()
        time.sleep(5)
    

if __name__ == "__main__":
    main()