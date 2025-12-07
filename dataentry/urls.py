from django.urls import path
from .views import data_entry_view,export_data

urlpatterns = [
    path('data_entry_view/', data_entry_view, name='data_entry_view'),
    path('export_data/', export_data, name='export_data'),
]
