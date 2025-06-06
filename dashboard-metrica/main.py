# main.py
import time
from Publisher import verifica_disponibilidade
from Tasks import run_consumer_processar_limites_de_acesso
from Aggregator import print_estatisticas
import schedule

def job():
    verifica_disponibilidade()
    time.sleep(5)
    run_consumer_processar_limites_de_acesso()

def main():
    schedule.every(1).seconds.do(job)
    schedule.every(60).seconds.do(print_estatisticas)
    # schedule.every(90).seconds.do(mostrar_resumo_por_url)
    ##
    while True:
        schedule.run_pending()
        time.sleep(5)
    

if __name__ == "__main__":
    main()