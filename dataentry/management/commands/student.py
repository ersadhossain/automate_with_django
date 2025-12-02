from django.core.management.base import BaseCommand
from dataentry.models import Student
class Command(BaseCommand):
    help = 'student data upload command'

    def handle(self, *args, **kwargs):
        s =[
            {'roll_number': 101, 'name': 'Ersad', 'age': 19},
            {'roll_number': 102, 'name': 'Hossain', 'age': 20},
            {'roll_number': 103, 'name': 'Ayesha', 'age': 18},
            {'roll_number': 104, 'name': 'Rahim', 'age': 21},
            {'roll_number': 105, 'name': 'Karim', 'age': 22},
            {'roll_number': 106, 'name': 'Salma', 'age': 20},
            {'roll_number': 107, 'name': 'Nabila', 'age': 19},
            {'roll_number': 108, 'name': 'Jamal', 'age': 23},
            {'roll_number': 109, 'name': 'Rina', 'age': 18},
            {'roll_number': 110, 'name': 'Sakib', 'age': 21},
            {'roll_number': 101, 'name': 'Ersad', 'age': 19},
        ]
        for student in s:
           
            R = student['roll_number']
            # print(student_roll,"student_roll")
            exist_record= Student.objects.filter(roll_number=R).exists()
            print(exist_record,"exist_record")
            if not exist_record:
                Student.objects.get(**student).delete
                self.stdout.write(self.style.SUCCESS(f'Student {student["name"]} with roll number {R} added successfully.'))
          
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll number {R} already exists. Skipping entry.'))
        self.stdout.write(self.style.SUCCESS('Student data upload command executed successfully!'))