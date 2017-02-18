from django.db import models


# Create your models here.
class Schedule(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    dk_event_id = models.PositiveIntegerField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    fee = models.FloatField(null=True)
    open_to_public = models.BooleanField()
    title = models.CharField(max_length=128)
    detail = models.TextField(default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
