from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = "stdmj"

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('mj', views.major_list, name='major_list'),
    path('<pk>/detail/', views.student_detail, name='student_detail'),
    path('mj/<pk>/detail/', views.major_detail, name='major_detail'),
    path("<pk>/delete/", views.student_delete, name="student_delete"),
    path("mj/<pk>/delete/", views.major_delete, name="major_delete"),
    path("new/", views.student_new, name="student_new"),
    path('mj/new', views.major_new, name="major_new"),
    path("<pk>/edit/", views.student_edit, name="student_edit"),
    path("mj/<pk>/edit/", views.major_edit, name="major_edit"),
]

