from __future__ import absolute_import,unicode_literals
from celery import shared_task
from . import views

@shared_task
def email_conferm(password,email):
    return views.send_conf_mail(password,email)
