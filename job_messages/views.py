from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from job_messages import models


# Create your views here.
class JobMessageList(ListView):
    model = models.JobMessage


class JobMessageDetail(DetailView):
    model = models.JobMessage
