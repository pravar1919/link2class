from django.conf import settings
from django.db import models
from accounts.models import *

User = settings.AUTH_USER_MODEL

# Create your models here.
class TrainingCenter(models.Model):
    title = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'TrainingCenter'

class SentMessage(models.Model):
    reciever = models.ForeignKey(CustomUser, related_name='To', on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser, related_name='From', on_delete=models.CASCADE)
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return self.reciever

