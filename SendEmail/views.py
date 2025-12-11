from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum

from .task import email_send_task
from .models import Email,List,Subscriber,Sent

# from django.conf import settings

from django.http import JsonResponse
@api_view(['POST','GET'])
def send_email(request):

    if request.method == "POST":
        
        Email_list = request.POST.get('Email-List')
        
        mail_subject = request.POST.get('subject')
        message = request.POST.get('body')
        file_path = request.FILES.get('Attachment')
       
        
       
       

        list_instance, created = List.objects.get_or_create(email_list=Email_list)
        email = Email(email_list=list_instance, subject=mail_subject, body=message)
        email.save()
        if file_path:
            email.attachment = file_path
            email.save()

        
        subscriber = Subscriber.objects.filter(email_list=list_instance)
        if email.attachment:
            attachment = email.attachment.path
        else:
            attachment = None
        
        to_email = [s.email_address for s in subscriber]
      
        email_id = email.id
        email_send_task.delay(mail_subject,message ,to_email ,attachment ,email_id)
       
        #insid  e emaill address we have all data respective to their list
        
        

        return Response({
            "message": "Email saved successfully",
            "list": Email_list,
            "subject": mail_subject,
            "body": message,
            "recipients":to_email,
        })

    # -------- GET REQUEST ----------
    all_models = List.objects.values_list("email_list", flat=True)

    return Response({
        "email_lists": list(all_models)  # convert QuerySet to list
    })

def open_email(request):
    return Response({
       ' message':"hello "
    })
def click_email(request):
    return Response({
       ' message':"bye bye "
    })
@api_view(['GET'])
def tracking_email(request):    
    emails = Email.objects.all()
   

    data = []

    for e in emails:
        total_sent = e.sents.aggregate(total=Sum('total_sent'))['total'] or 0
        data.append({
            "id": e.id,
            "subject": e.subject,
            "list_name": e.email_list.email_list,   # show list name instead of ID
            "body": e.body,
            "attachment": e.attachment.url if e.attachment else None,
            "sent_at": e.sent_at,
            "total_sent": total_sent,
            "open_rate": e.open_rate(),
            "click_rate": e.click_rate(),
            
        })
    

    return Response({"data": data})
@api_view(['GET'])
def email_stats(request, id):
    try:
        email = Email.objects.get(id=id)
        
        sent = Sent.objects.get(email=email)
        
        
        data = {
            "id": email.id,
            "subject": email.subject,
            "body": email.body,
            "list_name": email.email_list.email_list,
            "sent_at": email.sent_at,
            "attachment": email.attachment.url,
            "total_sent":sent.total_sent,
            "open_rate": email.open_rate(),
            "click_rate": email.click_rate()
            
        }
        return Response({"data":data})
       
    except Email.DoesNotExist:
        return Response({"error": "Not found"}, status=404)







