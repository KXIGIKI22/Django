from celery import shared_task
from django.contrib.auth.models import User
from celery.utils.log import get_task_logger
import time
from celery import Celery
from Django22 import User

app = Celery('Django22')

@shared_task
def print_text(text):
    print(text)

@shared_task
def print_purchase_count(user_id):
    user = User.objects.get(id=user_id)
    purchase_count = user.purchase_set.count()
    logger.info(f"User {user.username} has made {purchase_count} purchases.")

@app.task
def print_user_count():
    user_count = User.objects.count()
    print(f"Total number of users in the database: {user_count}")