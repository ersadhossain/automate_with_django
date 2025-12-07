import csv
from django.core.management.base import BaseCommand
# import datetime
from dataentry.utils import generate_csv_file 
from django.apps import apps

class Command(BaseCommand):
    help = 'Export model data to a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Model to export data from')

    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name']

        # Fix: get model class from any installed app
        Model = None
        for app_config in apps.get_app_configs():
            try:
                Model = app_config.get_model(model_name)
                break
            except LookupError:
                continue

        if Model is None:
            self.stdout.write(self.style.ERROR(f"Model '{model_name}' not found"))
            return

        # Query data
        data = Model.objects.all()
        file_path = generate_csv_file(model_name)

        

        # Write CSV
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([field.name for field in Model._meta.fields])

            for obj in data:
                writer.writerow([getattr(obj, field.name) for field in Model._meta.fields])

        self.stdout.write(self.style.SUCCESS(f"Data exported successfully to {file_path}"))
