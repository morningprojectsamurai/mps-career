from django.views.generic.list import ListView
from django.shortcuts import render
from atelier import models


# Create your views here.
class ScheduleList(ListView):
    model = models.Schedule
