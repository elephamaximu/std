from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = "stdmj"

urlpatterns = [
    path('', views.student_list, name='student_list'),
]

