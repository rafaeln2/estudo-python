from collections import defaultdict
import json
import redis
import time
from datetime import datetime
from DatabaseConnection import buscar_logs_aceitos, buscar_logs_rejeitados

# Conecta ao Redis
from Tasks import redis_client as r

import time

# lista todos os aceitas e rejeitadas por IP
def aggregator_latencias_erros():
    stats = defaultdict(lambda: {"aceitas": 0, "rejeitadas": 0})

    # Pega todas as requisições da fila de aceitos
    aceitas = buscar_logs_aceitos()
    for item in aceitas:
        try:
            ip = item[1]
            stats[ip]["aceitas"] += 1
        except Exception as e:
            print("Erro ao ler aceitos:", e)

    # Pega todas as requisições rejeitadas
    rejeitadas = buscar_logs_rejeitados()
    for item in rejeitadas:
        try:            
            ip = item[1]
            stats[ip]["rejeitadas"] += 1
        except Exception as e:
            print("Erro ao ler rejeitadas:", e)

    # Mostra resultado
    print("\n📊 Snapshot de Requisições por IP:")
    for ip, contagem in stats.items():
        print(f"IP {ip} - Aceitas: {contagem['aceitas']}, Rejeitadas: {contagem['rejeitadas']}")
    print("-" * 40)