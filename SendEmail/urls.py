from django.urls import path
from SendEmail.views import send_email

urlpatterns = [
    path('send_email/',send_email , name= 'send_email')
]
