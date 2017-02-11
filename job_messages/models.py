from django.db import models
from jobs.models import Entry

# Create your models here.
class JobMessage(models.Model):
    entry = models.ForeignKey(Entry)

    message = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message[:32]
