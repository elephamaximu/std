from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.http import HttpResponse
from . models import Major, Student


student_list = ListView.as_view(model=Student)

