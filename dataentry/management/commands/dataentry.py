from django.core.management.base import BaseCommand,CommandError
import csv
from django.apps import apps
from dataentry.models import Student
from django.contrib import messages
from dataentry.utils import check_csv_error
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_path',type=str,help="Path to Csv File ")
        parser.add_argument('model_name',type=str,help="Path to Csv File ")

    def handle(self, *args, **options): 
        file_path=options['file_path']#this is for getting argument
        model=options['model_name'].capitalize()
        # print(model)
        try:
            models = check_csv_error(file_path,model)
        except CommandError as e:
            raise e
        
        with open(file_path,'r')as f:
            reader=csv.DictReader(f)
            for row in reader: 
                # data={key:value for key,value in row.items() if key in model_field}
                models.objects.create(**row)
                # models.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Insert Data Sucessfully '))