from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here
class Specialization(models.Model):
    Animation = models.ImageField(upload_to='images/')
    Title = models.CharField(max_length=20)
    Summary = models.CharField(max_length= 30)
    
    
    def __str__(self):
        return self.Title
    
    
    
    
class Specialty(models.Model):
    Title = models.CharField(max_length=50)
    summary = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.Title
    
    
    
class Project(models.Model):
    Title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50)
    Images = models.ImageField(upload_to='images/')
      
    
    def __str__(self):
        return self.Title
    
    
    
class Testimonial(models.Model):
    name = models.CharField(max_length=10)
    Images = models.ImageField(upload_to='images/')
    body = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
    