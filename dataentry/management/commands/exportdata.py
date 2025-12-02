import csv
from django.core.management.base import BaseCommand
# from dataentry.models import Student
import datetime
from django.apps import apps

#propose command - python3 manage.py exportdata --model dataentry.Customer --output customers.json --format json
class Command(BaseCommand):
    help = 'export Student data to a CSV file'
    def add_arguments(self, parser):
        parser.add_argument('model_name',type= str, help='Model to export data from')


    def handle(self, *args, **kwargs):
        model = kwargs['model_name'].capitalize()
        for app_config in apps.get_app_configs():
            try:
                model = app_config.get_model(app_config.label,model)
            except LookupError:
                continue

        data = model.objects.all()
        timestamp = datetime.datetime.now().strftime("_%Y-%m-%d_%H-%M-%S")

        
        file_path = f'students_export{timestamp}.csv'
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([field.name for field in model._meta.fields])
            for dt in data:
                writer.writerow([getattr(dt,field.name) for field in model._meta.fields])
            

            
        self.stdout.write(self.style.SUCCESS(f'Data exported successfully to {file_path}'))