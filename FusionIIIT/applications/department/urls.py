from django.conf.urls import url

from . import views

app_name = 'dep'

urlpatterns = [

    url(r'^$', views.hod, name='dep'),
    url(r'^file_complaint/$', views.file_complaint, name='file_complaint')
]