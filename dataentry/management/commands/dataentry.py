from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv

class Command(BaseCommand):
    help = 'Imports data from a CSV into a model'

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str)
        parser.add_argument('model_name', type=str)

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        model_name = kwargs['model_name']

        # FIXED: Load model properly
        try:
            model = apps.get_model('dataentry', model_name)
            # print("model",model)
        except LookupError:
            raise CommandError(f'Model "{model_name}" not found in app "dataentry"')

        # Import CSV
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
