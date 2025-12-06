from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll = models.IntegerField(null=True)

    def __str__(self):
        return self.name
class Customer(models.Model):
    customer_id=models.IntegerField(null=True, unique=True)
    customer_name=models.CharField(max_length=100)  
    customer_segment=models.CharField(null=True,blank=True,max_length=100)
    customer_city=models.CharField(max_length=101)
    customer_state=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.customer_name

