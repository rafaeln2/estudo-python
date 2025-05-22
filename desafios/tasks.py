from celery import Celery
import redis
from fastapi import Depends, File
import time

redis_client = redis.StrictRedis(host='redis', port=6379, db=0)
celery_app = Celery(main='desafio', broker="amqp://guest:guest@rabbitmq:5672/")
celery_app.conf.task_routes = {
    "tasks.processar_disponibilidade": {"queue": "service_monitor"},
}

@celery_app.task()
def processar_disponibilidade(json):
    print(f"JSON: {json}")
    timestamp = int(time.time())
    status_code = json.get("status_code")
    latency_ms = json.get("latency_ms")
    url = json.get("url")
    
    redis_client.zadd("latencies", {url: latency_ms})
    # Se for erro (status >= 400), registra no Sorted Set de erros com o timestamp   
    if status_code >= 400:
        redis_client.zadd("errors", {url: timestamp})
        print(f"URL: {url}, Status code: {status_code}, json = {json}")
    else:
        print(f"URL: {url}, Status code: {status_code}, json = {json}")
    
    