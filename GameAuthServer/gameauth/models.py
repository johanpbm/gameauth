from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    def __str__(self):
        return self.name
    def operation_activity(self):
        return self.name +  " -  " + self.description
    
class ILO(models.Model):
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.description
    
    
