from django.conf import settings
from django.db import models

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

