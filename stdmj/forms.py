from django.shortcuts import render, redirect, reverse
from django import forms
from . models import Major, Student
from django.core.validators import MinLengthValidator

class MajorForm(forms.Form):
    major_id = forms.IntegerField(label="전공 아이디")
    major_title = forms.CharField(label="전공 이름", max_length=100, validators=[MinLengthValidator(3)])

class StudentForm(forms.Form):
    studentID = forms.IntegerField(label="학생 아이디")
    name = forms.CharField(label="학생 이름", max_length=30, validators=[MinLengthValidator(2)])
    major = forms.ModelChoiceField(queryset=Major.objects.all())
    phone = forms.CharField(label="전화번호", max_length=100, required=False)
    address = forms.CharField(label="주소", max_length=100, required=False)
    hobby =  forms.CharField(label="취미", max_length=300, required=False)
    skill = forms.CharField(label="보유 기술", max_length=100, required=False)
