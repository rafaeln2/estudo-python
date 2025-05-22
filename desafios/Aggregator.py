import redis
import time
from datetime import datetime

# Conecta ao Redis
from tasks import redis_client as r

def aggregator():
    print("URLs mais lentas (top 5):")

    # Pega os 5 membros com maior score em latencies (ordem decrescente)
    top_latencies = r.zrevrange("latencies", 0, 4, withscores=True)
    for i, (url, latency) in enumerate(top_latencies, 1):
        print(f"{i}. {url} ({latency:.3f} ms)")

    print()

    # Timestamp atual e limite de 24h atrás
    now = time.time()
    past_24h = now - 86400  # 24 * 60 * 60

    # Conta membros com score nas últimas 24h
    error_count = r.zcount("errors", past_24h, now)
    print(f"Total de erros nas últimas 24 h: {error_count}")

def print_all():
    print("📊 LATENCIES (todas as URLs e latências):")
    latencies = r.zrevrange("latencies", 0, -1, withscores=True)
    if not latencies:
        print("Nenhuma URL registrada.")
    else:
        for i, (url, latency) in enumerate(latencies, 1):
            print(f"{i}. {url.decode() if isinstance(url, bytes) else url} ({latency:.3f} ms)")
            
    print("\n🛑 ERRORS (todos os erros registrados):")
    
    
    now = int(time.time())
    past_24h = now - 86400  # 24 * 60 * 60
    errors = r.zcount("errors", past_24h, now) #r.zrange("errors", 0, -1, withscores=True)
    
    if not errors:
        print("Nenhum erro registrado.")
    else:
        print(f"Total de erros nas últimas 24 h: {errors}")
        # for i, (key, timestamp) in enumerate(errors, 1):
        #     dt = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
        #     print(f"{i}. {key} (em {dt})")