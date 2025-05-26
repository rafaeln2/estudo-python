# main.py
import time
from Publisher import verifica_disponibilidade
from tasks import processar_disponibilidade, run_consumer_processar_disponibilidade
from Aggregator import aggregator_latencias_erros, mostrar_resumo_por_url
import schedule

def job():
    verifica_disponibilidade()
    run_consumer_processar_disponibilidade()

def main():
    schedule.every(60).seconds.do(job)
    schedule.every(90).seconds.do(aggregator_latencias_erros)
    schedule.every(90).seconds.do(mostrar_resumo_por_url)

    while True:
        schedule.run_pending()
        time.sleep(5)
    

if __name__ == "__main__":
    main()
