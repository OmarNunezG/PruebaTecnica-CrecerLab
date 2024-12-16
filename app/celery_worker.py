import os
import time

from celery import Celery
from dotenv import load_dotenv

load_dotenv(".env")

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")


@celery.task(name="create_task")
def create_task(event_id, user_id, description):
    time.sleep(10)

    return f"El evento {event_id} ha sido enviado a {user_id}: {description}"
