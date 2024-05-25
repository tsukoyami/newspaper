
from django.db import models
from company.models import Company
from registereduser.models import RegisteredUser


class Subscriber(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'company')

    def __str__(self):
        return f"{self.user.username} - {self.company.name}"