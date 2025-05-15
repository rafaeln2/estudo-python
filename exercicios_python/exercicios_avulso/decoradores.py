import time  # necessário para medir o tempo

def tempo_execucao(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

@tempo_execucao
def dormir():
    time.sleep(2)
    return "Pronto!"

print(dormir())
