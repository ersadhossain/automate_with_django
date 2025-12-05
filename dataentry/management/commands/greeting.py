from django.core.management.base import BaseCommand
#write twince for practice
# from django.core.management.base import BaseCommand
class Command(BaseCommand):
    help = 'wishing one some'
    def add_arguments(self, parser):
        parser.add_argument('name',type =str, help='your name')

    # print(help)
    def handle(self, *args, **kwargs):
        name = kwargs['name']
        self.stdout.write(self.style.SUCCESS(f'Hello, {name}!'))



# class Command(BaseCommand):
#     help = 'Outputs a greeting message'
#     def add_arguments(self, parser):
#         parser.add_argument('name', type=str, help='Your name')

#     def handle(self, *args, **kwargs):
#         name = kwargs['name']

#         self.stdout.write(self.style.SUCCESS(f'Hello, {name}!'))