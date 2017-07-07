from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.students_full_list, name='students_full_list'),
    url(r'^course_id=(?P<pk>[0-9]+)$', views.students_list, name='students_list'),
]
