import redis
import time
from datetime import datetime

# Conecta ao Redis
from tasks import redis_client as r

import time

def aggregator_latencias_erros():
    print("URLs mais lentas (top 5):")

    latency_data = []
    for key in r.scan_iter("latencies:*"):
        url = key.decode().split("latencies:")[1]

        # Pega os valores da lista de latência (convertendo para float)
        latencies = r.lrange(key, 0, -1)
        latencies = [float(l.decode()) for l in latencies]

        if latencies:
            avg_latency = sum(latencies) / len(latencies)
            latency_data.append((url, avg_latency))

    # Ordena por média de latência decrescente
    top_latencies = sorted(latency_data, key=lambda x: x[1], reverse=True)[:5]

    for i, (url, latency) in enumerate(top_latencies, 1):
        print(f"{i}. {url} ({latency:.3f} ms)")

    #prepara pra mostrar os erros de todas as urls nas ultimas 24 horas
    now = time.time()
    past_24h = now - 86400
    total_erros = 0

    for key in r.scan_iter("errors:*"):
        timestamps = r.lrange(key, 0, -1)
        # Converte e filtra os timestamps dentro das últimas 24h
        erros_recent = [float(ts.decode()) for ts in timestamps if float(ts.decode()) >= past_24h]
        total_erros += len(erros_recent)

    print(f"Total de erros nas últimas 24 horas: {total_erros}")

def mostrar_resumo_por_url():
    now = time.time()
    past_24h = now - 86400  # 24 horas atrás

    for key in r.scan_iter("latencies:*"):
        url = key.decode().split("latencies:")[1]

        # Pega a lista de latências (mais recentes primeiro)
        latencies_raw = r.lrange(key, 0, -1)
        latencies = [float(l.decode()) for l in latencies_raw]

        # Conta erros nas últimas 24h para essa URL
        error_count = r.zcount("errors", past_24h, now)
        # Filtra apenas os que têm o nome da URL
        url_errors = [member for member in r.zrangebyscore("errors", past_24h, now, withscores=False) if member.decode() == url]
        url_error_count = len(url_errors)

        print(f"URL: {url}")
        print(f"  Latências: {latencies}")
        print(f"  Erros nas últimas 24h: {url_error_count}")
        print("-" * 40)