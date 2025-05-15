
import time
from threading import Thread, Lock
from urllib.request import urlopen
import asyncio


lock = Lock()

def do_cpu_work():
    for i in range(10000000):
        2**1
        
def do_io_work():
    with lock:
        print("Iniciando I/O work")
        time.sleep(1)
        url = "https://www.google.com"
        urlopen(url)
        print("Finalizando I/O work")
    

if __name__ == "__main__":
    threads = []
    start = time.perf_counter()
    
    for _ in range(10):
        t = Thread(target=do_io_work)
        threads.append(t)
        t.start()
        
    for t in threads:
            t.join()
        # do_cpu_work()
    print(f"Tempo total: {time.perf_counter() - start:.2f} segundos")
    