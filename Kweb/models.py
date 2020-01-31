from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here

    
    
class Project(models.Model):
    Title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50)
    Images = models.ImageField(upload_to='images/')
      
    
    def __str__(self):
        return self.Title
    
 