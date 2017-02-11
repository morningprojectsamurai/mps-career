from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MultipleEntriesToOneJob(Exception):
    pass


class Tag(models.Model):
    name = models.CharField(max_length=24)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Job(models.Model):
    title = models.CharField(max_length=128)
    summary = models.TextField()

    start = models.DateTimeField()
    end = models.DateTimeField()

    remuneration = models.FloatField()
    
    tags = models.ManyToManyField(Tag, blank=True)

    employer = models.ForeignKey(User)
    num_employee = models.PositiveIntegerField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Entry(models.Model):
    user = models.ForeignKey(User, related_name='users')
    job = models.ForeignKey(Job, related_name='entries')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return '%s (%s)' % (self.job.title, self.user.username)

    def save(self, *args, **kwargs):
        if Entry.objects.filter(user=self.user, job=self.job, is_deleted=False).exists():
            raise MultipleEntriesToOneJob
        super(Entry, self).save(*args, **kwargs)
