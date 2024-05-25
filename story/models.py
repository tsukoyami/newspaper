
from django.db import models
from django.urls import reverse
from registereduser.models import RegisteredUser
from source.models import Source

class Story(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE, related_name='created_stories', default=None)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='stories', blank=True)
    title = models.CharField(max_length=500)
    published_date = models.DateTimeField()
    body_text = models.TextField()
    url = models.URLField()
    tags = models.CharField(max_length=50)

    class Meta:
        unique_together = ('url', 'created_by')

    def __str__(self):
        return f"{self.title} ({self.source.source_name})"
