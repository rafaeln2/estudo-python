# main.py
import time
from Publisher import verifica_disponibilidade
from Tasks import run_consumer_processar_limites_de_acesso
from Aggregator import aggregator_latencias_erros
import schedule

def job():
    verifica_disponibilidade()
    run_consumer_processar_limites_de_acesso()

def main():
    schedule.every(1).seconds.do(job)
    schedule.every(10).seconds.do(aggregator_latencias_erros)
    # schedule.every(90).seconds.do(mostrar_resumo_por_url)
    ##
    while True:
        schedule.run_pending()
        time.sleep(5)
    

if __name__ == "__main__":
    main()
