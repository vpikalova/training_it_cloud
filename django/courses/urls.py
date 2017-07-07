from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.courses_list, name='courses_list'),
    url(r'^(?P<pk>[0-9]+)/$',views.course_detail, name='course_detail'),
]
