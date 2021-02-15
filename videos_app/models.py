from django.conf import settings
from django.db import models
from training_center.models import TrainingCenter


User = settings.AUTH_USER_MODEL

# Create your models here.
class Videos(models.Model):
    author          = models.ManyToManyField(User, blank=True)
    training_center = models.ForeignKey(TrainingCenter, on_delete=models.CASCADE)
    title           = models.CharField(max_length=220)
    url             = models.URLField()
    description     = models.TextField()
    certificate     = models.CharField(max_length=220)
    Audience        = models.CharField(max_length=220)
    length          = models.IntegerField()
    views           = models.IntegerField()
    # like            = models.ManyToManyField(Like, on_delete=models.CASCADE)
    active          = models.BooleanField(default=True)
    created         = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Videos'