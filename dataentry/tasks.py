from awd.celery import app as celery_app
from django.core.management import call_command
from django.conf import settings
from dataentry.utils import send_email_notification
from .utils import generate_csv_file
# i want to import mail


    
import time
app = celery_app


# @app.task
# def celery_task():
#     mail_subject = "testing"
#     message = 'this is a test email'
#     to_email = settings.DEFAULT_TO_EMAIL
#     send_email_notification(mail_subject,message,to_email)

   
#     return "Task Completed"
@app.task
def dataentry_task(full_path, model_name):
    try:
        call_command('dataentry', full_path, model_name)
    except Exception as e:
        raise e
    mail_subject = "csv file imported"
    message = 'your data is imported successfully '
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject,message,to_email)

@app.task
def exported_data(model_name):
    try:
        call_command('exportdata', model_name)
    except Exception as e:
        raise e
    file_path = generate_csv_file(model_name)
    # print(file_path)
    
    mail_subject = "your file export "
    message = 'your data is exported successfully '
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject,message,to_email,attachment=file_path)
    