from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

# Create your tasks here

@shared_task
def add(x, y):
    sleep(2)
    return x + y

@shared_task
def clear_session_cache(id):
    print(f"Session Cache Cleared: {id}")
    return id

@shared_task
def clear_Rabbit_cache(id):
    print(f"Session Cache Cleared: {id}")
    return id

schedule, created = IntervalSchedule.objects.get_or_create(every=20, period=IntervalSchedule.SECONDS)

PeriodicTask.objects.get_or_create(
    name="Clear RabbitMQ Periodic Task",
    task="myapp.tasks.clear_Rabbit_cache",
    interval=schedule,
    args=json.dumps(["Hello"]),
)