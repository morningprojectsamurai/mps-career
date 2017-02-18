
from django.conf.urls import url
from atelier import views


urlpatterns = [
    url(r'^$', views.ScheduleList.as_view(), name='schedule_list'),
]
