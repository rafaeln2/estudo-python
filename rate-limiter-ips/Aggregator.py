from collections import defaultdict
import json
import redis
import time
from datetime import datetime

# Conecta ao Redis
from Tasks import redis_client as r

import time

def aggregator_latencias_erros():
    stats = defaultdict(lambda: {"aceitas": 0, "rejeitadas": 0})

    # Pega todas as requisições aceitas
    aceitas = r.lrange("fila:aceitos", 0, -1)
    for item in aceitas:
        try:
            msg = json.loads(item)
            ip = msg["ip"]
            stats[ip]["aceitas"] += 1
        except Exception as e:
            print("Erro ao ler aceitos:", e)

    # Pega todas as requisições rejeitadas
    rejeitadas = r.lrange("fila:rejeitados", 0, -1)
    for item in rejeitadas:
        try:
            msg = json.loads(item)
            ip = msg["ip"]
            stats[ip]["rejeitadas"] += 1
        except Exception as e:
            print("Erro ao ler rejeitadas:", e)

    # Mostra resultado
    print("\n📊 Snapshot de Requisições por IP:")
    for ip, contagem in stats.items():
        print(f"IP {ip} - Aceitas: {contagem['aceitas']}, Rejeitadas: {contagem['rejeitadas']}")
    print("-" * 40)