# GestionTareas/__init__.py

from GestionTareas.celery import app as celery_app

__all__ = ('celery_app',)
