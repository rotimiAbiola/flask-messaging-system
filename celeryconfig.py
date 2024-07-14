from celery import Celery

app = Celery('tasks', broker='amqp://<RABBITMQ-USER>:<RABBITMQ-PASSWORD>@localhost//')

app.conf.update(
    result_backend='rpc://',
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
)

app.autodiscover_tasks(['tasks'])