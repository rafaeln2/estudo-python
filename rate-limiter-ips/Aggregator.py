from collections import defaultdict
import json
import redis
import time
from datetime import datetime

from Tasks import redis_client as r

# lista todos os aceitas e rejeitadas por IP
def print_estatisticas():
    stats = prepara_dados_estatisticas()

    # Mostra resultado
    print("\n📊 Snapshot de Requisições por IP:")
    for ip, contagem in stats.items():
        print(f"IP {ip} - Aceitas: {contagem['aceitas']}, Rejeitadas: {contagem['rejeitadas']}")
    print("-" * 40)

def prepara_dados_estatisticas():
    stats = defaultdict(lambda: {"aceitas": 0, "rejeitadas": 0})

    # Pega todas as requisições da fila de aceitos
    aceitas = r.lrange("fila:aceitos", 0, -1)
    for item in aceitas:
        try:
            item_json = json.loads(item)
            ip = item_json["ip"]
            stats[ip]["aceitas"] += 1
        except Exception as e:
            print("Erro ao ler aceitos:", e)

    # Pega todas as requisições rejeitadas
    rejeitadas = r.lrange("fila:rejeitados", 0, -1)
    for item in rejeitadas:
        try:
            item_json = json.loads(item)
            ip = item_json["ip"]
            stats[ip]["rejeitadas"] += 1
        except Exception as e:
            print("Erro ao ler rejeitadas:", e)
    return stats