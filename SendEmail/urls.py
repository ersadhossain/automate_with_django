from django.urls import path
from SendEmail.views import send_email,open_email,click_email,tracking_email,email_stats

urlpatterns = [
    path('send_email/',send_email , name= 'send_email'),
    path('click/email/<unique_id>/', click_email,name = 'click_email'),
    path('open/email/<unique_id>/', open_email,name = 'open_email'),
    path('tracking_email/',tracking_email,name="tracking_email"),
    path("tracking_email/<int:id>/", email_stats),
]
