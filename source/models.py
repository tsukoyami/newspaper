
from django.db import models
from registereduser.models import RegisteredUser

class Source(models.Model):
    id = models.AutoField(primary_key=True)
    source_user = models.ForeignKey(RegisteredUser, verbose_name=("user"), on_delete=models.CASCADE)
    source_name = models.CharField(max_length=5000)
    source_url = models.URLField(max_length=2000)
    story_count = models.PositiveIntegerField( default=0)
    tags = models.CharField(max_length=50)

    class Meta:
        unique_together = ('source_user', 'source_url')

    def __str__(self):
        return f"{self.source_user.username} - {self.source_name}"