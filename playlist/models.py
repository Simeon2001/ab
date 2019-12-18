from django.db import models
from django.urls import reverse

# Create your models here.
class Urlinker (models.Model):
    username = models.CharField(max_length = 10)
    website_link = models.CharField(max_length = 500)
    description = models.CharField(max_length = 100)
    images = models.ImageField(upload_to='images/',
    default='images/def.jpg',
    blank=True,
    null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def get_absolute_url(self):
        return reverse('Home')
    def __str__(self):
        return self.username
