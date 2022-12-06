# GestionTareas/__init__.py
from __future__ import absolute_import
from GestionTareas.celery import app as celery_app

__all__ = ('celery_app',)
