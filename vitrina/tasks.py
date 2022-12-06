from time import sleep
from celery import Celery
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

# app = Celery(
#     'tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0'
# )


# @app.task
@shared_task
def send_book(nombre, email):

    send_mail(
        'Subject',
        'Here is your book ' + nombre,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False
    )

    return 'Done'
