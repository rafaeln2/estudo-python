from celery import Celery

celery_app = Celery(main='tasks', broker="amqp://guest:guest@rabbitmq:5672/")

celery_app.conf.task_routes = {
    "app.tasks.exemplo_task": {"queue": "default"},
}
