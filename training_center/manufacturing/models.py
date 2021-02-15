from django.conf import settings
from django.db import models
from training_center.models import TrainingCenter


User = settings.AUTH_USER_MODEL

# Create your models here.
class Manufacturing(models.Model):
    author          = models.ManyToManyField(User, blank=True)
    extra_field     = models.CharField(max_length=220, default='manufacturing')
    title           = models.CharField(max_length=500)
    todays_events   = models.URLField(blank=True)
    upcoming_events = models.URLField(blank=True)
    ondemand_events = models.URLField(blank=True)
    description     = models.TextField(blank=True)
    certificate     = models.CharField(max_length=220)
    Audience        = models.CharField(max_length=220)
    length          = models.IntegerField(blank=True)
    views           = models.IntegerField(blank=True)
    # like            = models.ManyToManyField(Like, on_delete=models.CASCADE)
    active          = models.BooleanField(default=True)
    created         = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Manufacturing_Videos'