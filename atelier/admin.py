from django.contrib import admin
from atelier import models

# Register your models here.
@admin.register(models.Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass
