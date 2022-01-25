from django.core import management

from McGillCSCareers import celery_app


@celery_app.task
def clearsessions():
    management.call_command('clearsessions')
