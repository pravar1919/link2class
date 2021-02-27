from django.conf import settings
from django.db import models
# from training_center.models import TrainingCenter


User = settings.AUTH_USER_MODEL

# Create your models here.
class Benifits(models.Model):
    author          = models.ManyToManyField(User, blank=True)
    extra_field     = models.CharField(max_length=220, default='benifits')
    title           = models.CharField(max_length=500)
    todays_events   = models.URLField(null=True,blank=True)
    upcoming_events = models.URLField(null=True,blank=True)
    ondemand_events = models.URLField(null=True,blank=True)
    description     = models.TextField(null=True,blank=True)
    certificate     = models.CharField(null=True,max_length=220,blank=True)
    Audience        = models.CharField(null=True,max_length=220,blank=True)
    length          = models.IntegerField(null=True,blank=True)
    views           = models.IntegerField(null=True,blank=True)
    liked = models.ManyToManyField(
        User, blank=True, related_name='likes')
    active          = models.BooleanField(default=True)
    created         = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def num_likes(self):
        return self.liked.all().count()
    
    class Meta:
        verbose_name_plural = 'Benifits'

    def get_authors(self):
        author = [a for a in self.author.all()]
        return author

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Benifits, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"
