import time
import threading
import multiprocessing
import os

# ---------- CPU-bound task ----------
def cpu_bound(n):
    count = 0
    for i in range(n):
        count += i*i
    return count

# ---------- IO-bound task ----------
def io_bound():
    time.sleep(1)

# ---------- Threading benchmark ----------
def run_threads(task, num_tasks, *args):
    threads = []
    for _ in range(num_tasks):
        t = threading.Thread(target=task, args=args)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

# ---------- Multiprocessing benchmark ----------
def run_processes(task, num_tasks, *args):
    processes = []
    for _ in range(num_tasks):
        p = multiprocessing.Process(target=task, args=args)
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

# ---------- Benchmark runner ----------
def benchmark():
    NUM_TASKS = os.cpu_count() or 4  # Usa todos os núcleos disponíveis

    print(f"\n🔁 Executando {NUM_TASKS} tarefas (CPU-bound) com Threading...")
    start = time.perf_counter()
    run_threads(cpu_bound, NUM_TASKS, 10_000_000)
    end = time.perf_counter()
    print(f"Threading (CPU-bound): {end - start:.2f} segundos")

    print(f"\n🧠 Executando {NUM_TASKS} tarefas (CPU-bound) com Multiprocessing...")
    start = time.perf_counter()
    run_processes(cpu_bound, NUM_TASKS, 10_000_000)
    end = time.perf_counter()
    print(f"Multiprocessing (CPU-bound): {end - start:.2f} segundos")

    print(f"\n💤 Executando {NUM_TASKS} tarefas (I/O-bound) com Threading...")
    start = time.perf_counter()
    run_threads(io_bound, NUM_TASKS)
    end = time.perf_counter()
    print(f"Threading (I/O-bound): {end - start:.2f} segundos")

    print(f"\n💤 Executando {NUM_TASKS} tarefas (I/O-bound) com Multiprocessing...")
    start = time.perf_counter()
    run_processes(io_bound, NUM_TASKS)
    end = time.perf_counter()
    print(f"Multiprocessing (I/O-bound): {end - start:.2f} segundos")

if __name__ == "__main__":
    benchmark()


    
    