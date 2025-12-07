from sqlite3.dbapi2 import Timestamp
from django.apps import apps
from django.core.management import CommandError
import csv
import datetime
import os
# from datetime import datetime

from django.conf import settings
from django.core.mail import EmailMessage
from django.conf import settings


def get_all_models():
    all_models = []
    default = ['LogEntry', 'Permission', 'Group', 'User', 'ContentType', 'Session', 'UploadedFile']

    for model in apps.get_models():
        if model.__name__ not in default:
            all_models.append(model.__name__)

    return all_models


def check_csv_error(file_path, model):
    models = None

    # Find model in any installed app
    for app_config in apps.get_app_configs():
        try:
            models = apps.get_model(app_config.label, model)
            break
        except LookupError:
            continue

    if not models:
        raise CommandError(f"Model {model} not found in any app")

    # Get model fields except 'id'
    model_field = [field.name for field in models._meta.fields if field.name != 'id']

    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            csv_header = [header.strip() for header in reader.fieldnames]

            if csv_header != model_field:
                raise CommandError(f"CSV file does not match with model fields ({model}).")

    except CommandError as e:
        raise e

    return models
def send_email_notification(mail_subject,message ,to_email ,attachment = None):
    try:
        from_email = settings.DEFAULT_FROM_EMAIL
        mail = EmailMessage(mail_subject,message,from_email,to=[to_email])
        if attachment:
            mail.attach_file(attachment)
        mail.send()
    except Exception as e:
        raise str(e)

def generate_csv_file(model):
    EXPORT = 'export_entry'
    export_dir = os.path.join(settings.MEDIA_ROOT, EXPORT)

    # Create directory if missing
    os.makedirs(export_dir, exist_ok=True)

    file_name = f"{model}_export{Timestamp}.csv"
    file_path = os.path.join(export_dir, file_name)

    return file_path

