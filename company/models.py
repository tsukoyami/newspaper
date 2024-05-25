
import uuid
from django.db import models
from django.urls import reverse

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name