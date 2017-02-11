from django.contrib import admin
from job_messages import models

# Register your models here.
@admin.register(models.JobMessage)
class JobMessage(admin.ModelAdmin):
    pass
