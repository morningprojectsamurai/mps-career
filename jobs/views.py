from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.http import HttpResponseBadRequest, Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from jobs import models


# Create your views here.
class JobList(ListView):
    model = models.Job

    def get_context_data(self, **kwargs):
        context = super(JobList, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['entried'] = models.Job.objects.filter(
                entries__in=models.Entry.objects.filter(user=self.request.user, is_deleted=False))
        else:
            context['entried'] = []
        return context
        

class JobDetail(DetailView):
    model = models.Job


@method_decorator(login_required, name='dispatch')
class EntryCreate(CreateView):
    model = models.Entry
    fields = ['user',  'job', ]
    success_url = reverse_lazy('jobs:job_list')

    def post(self, request, *args, **kwargs):
        response = super(EntryCreate, self).post(request, *args, **kwargs)
        send_mail(
            'MPS Career Entry',
            'Entry ID %s:\n\nApplicant: %s (USER ID: %s)\nJob: %s (JOB ID: %s).' % (
                self.object.pk, self.object.user.username, self.object.user.pk,
                self.object.job.title, self.object.job.pk),
            'no-reply@mpsamurai.org',
            ['junya@mpsamurai.org', ],
            fail_silently=False,
        )
        send_mail(
            'MPS Career Entry Completed',
            'Hi %s!\n\n' % self.object.user.username + \
            'We received your application for the job %s.\n\n' % self.object.job.title + \
            'We will send you a message within 3 days.\n\nThenk you!',
            'no-reply@mpsamurai.org',
            [self.object.user.email, ],
            fail_silently=False,
        )
        return response
