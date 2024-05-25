
from django.db import models
from company.models import Company
import uuid

class RegisteredUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    company = models.ManyToManyField(Company, blank=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return self.username

