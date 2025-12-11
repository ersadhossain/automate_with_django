from django.db import models



# Create your models here.
class List(models.Model):
    email_list = models.CharField(max_length=25)


    def  __str__(self):
        return self.email_list
    
    def count_email(self):
        count = Subscriber.objects.filter(email_list = self).count()
        return count

class Subscriber(models.Model):
    email_list = models.ForeignKey(List, on_delete=models.CASCADE)
    email_address = models.EmailField(max_length=50)
    
    
    def __str__(self):
        return self.email_address


class Email(models.Model):
    email_list = models.ForeignKey(List,on_delete=models.CASCADE)
    subject = models.CharField(max_length=1000)
    body = models.TextField(max_length=500)
    attachment= models.FileField(upload_to='email_attachment/')
    sent_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.subject
        
    def click_rate(self):
            total_sent=self.email_list.count_email()
            click_count=EmailTracking.objects.filter(email=self,clicked_at__isnull=False).count()
            click_rate=(click_count/total_sent)*100 if total_sent>0 else 0
            return round(click_rate,2)


    def open_rate(self):
        total_sent=self.email_list.count_email()
        opened_count=EmailTracking.objects.filter(email=self,opened_at__isnull=False).count()
        open_rate=(opened_count/total_sent)*100 if total_sent>0 else 0
        return round(open_rate,2)

class Sent(models.Model):
    email=models.ForeignKey(Email,related_name="sents",on_delete=models.CASCADE,null=True,blank=True)
    total_sent=models.IntegerField()

    def __str__(self):
        return f"{str(self.email)} - {str(self.total_sent)} Emails Sent"

class EmailTracking(models.Model):
    email= models.ForeignKey(Email,null = True,blank=True, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(Subscriber,null=True,blank=True,on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=255,unique=True)
    opened_at = models.DateTimeField(null = True,blank=True)
    clicked_at = models.DateTimeField(null = True,blank=True)

    def __str__(self):
        return self.email.subject


    
