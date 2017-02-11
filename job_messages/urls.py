from django.conf.urls import url
from job_messages import views


urlpatterns = [
    url(r'^$', views.JobMessageList.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.JobMessageDetail.as_view(), name='list'),
]
