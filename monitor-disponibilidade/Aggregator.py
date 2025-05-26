import redis
import time
from datetime import datetime

# Conecta ao Redis
from Tasks import redis_client as r

import time

def aggregator_latencias_erros():
    print("URLs mais lentas (top 5):")

    latency_data = []
    for key in r.scan_iter("latencies:*"): # percorre todos as chaves que começa com latencies:
        url = key.decode().split("latencies:")[1] # pega a url da chave
        
        latencies = r.lrange(key, 0, -1) # pega a lista completa de latencia pela chave
        latencies = [float(l.decode()) for l in latencies] # pega as latencias

        if latencies:
            avg_latency = sum(latencies) / len(latencies) # divide a soma das latencias pelo numero de latencia (média)
            latency_data.append((url, avg_latency)) #adiciona na lista de latencias

    # Ordena por média de latência decrescente
    top_latencies = sorted(latency_data, key=lambda x: x[1], reverse=True)[:5] # ordena de maior pra menor e pega as 5 primeiras

    for i, (url, latency) in enumerate(top_latencies, 1):
        print(f"{i}. {url} ({latency:.3f} ms)")

    #prepara pra mostrar os erros de todas as urls nas ultimas 24 horas
    now = time.time()
    past_24h = now - 86400
    total_erros = 0

    for key in r.scan_iter("errors:*"):
        timestamps = r.lrange(key, 0, -1) # pega todas as timestamp pela chave
        erros_recent = [float(ts.decode()) for ts in timestamps if float(ts.decode()) >= past_24h] # itera as timestamps e coloca numa lista se forem no periodo de 24 horas
        total_erros += len(erros_recent) # soma a quantidade de erros

    print(f"Total de erros nas últimas 24 horas: {total_erros}")

def mostrar_resumo_por_url():
    now = time.time()
    past_24h = now - 86400  # 24 horas atrás

    for key in r.scan_iter("latencies:*"):
        url = key.decode().split("latencies:")[1]

        # Pega as latências
        latencies_raw = r.lrange(key, 0, -1)
        latencies = [float(l.decode()) for l in latencies_raw]

        # Busca erros por url
        error_key = f"errors:{url}"
        error_timestamps = r.lrange(error_key, 0, -1)
        error_times = [float(ts.decode()) for ts in error_timestamps]
        recent_errors = [ts for ts in error_times if ts >= past_24h]

        print(f"URL: {url}")
        print(f"  Latências: {latencies}")
        print(f"  Erros nas últimas 24h: {len(recent_errors)}")
        print("-" * 40)

        