from django.contrib import admin
from .models import List,Email,Subscriber


# Register your models here.
admin.site.register(List)
admin.site.register(Email)
admin.site.register(Subscriber)