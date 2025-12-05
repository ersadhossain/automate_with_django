from django.urls import path
from .views import data_entry_view

urlpatterns = [
    path('data_entry_view/', data_entry_view, name='data_entry_view'),
]
