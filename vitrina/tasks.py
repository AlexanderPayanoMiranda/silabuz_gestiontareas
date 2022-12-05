from time import sleep
from celery import shared_task


@shared_task
def send_book(nombre, email):
    sleep(20)
    print(nombre + ' ' + email)
