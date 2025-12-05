from django.contrib import admin

# Register your models here.
from .models import UploadedFile
class Uploadsfileadmin(admin.ModelAdmin):
    list_display = ['model_name','uploaded_at']
admin.site.register(UploadedFile,Uploadsfileadmin)
