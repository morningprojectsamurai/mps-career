
from django.conf.urls import url
from jobs import views


urlpatterns = [
    url(r'^$', views.JobList.as_view(), name='job_list'),
    #url(r'^entry/list/$', views.EntryList.as_view(), name='entry_list'),
    url(r'^entry/create/$', views.EntryCreate.as_view(), name='entry_create'),
]
