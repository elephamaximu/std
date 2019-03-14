from django.db import models
from django.utils import timezone
from django import forms

class Major(models.Model):
    major_id = models.IntegerField(primary_key=True)
    major_title = models.CharField(max_length=100)

    class Meta:
        ordering = ('major_id',)
    
    def __str__(self):
        return self.major_title

    def get_absolute_url(self):
        return reverse('stdmj:major_list')

class Student(models.Model):
    studentID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, null=True,blank=True)
    address = models.CharField(max_length=100, null=True,blank=True)
    hobby = models.CharField(max_length=300, null=True,blank=True)
    skill = models.CharField(max_length=100, null=True,blank=True)

    class Meta:
        ordering = ('studentID',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stdmj:student_list')

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentID', 'name', 'major', 'phone', 'address', 'hobby', 'skill']
        labels = {'studentID':'학생 아이디', 'name':'학생 이름', 'major':'학생 전공', 'phone':'전화번호', 
                    'address':'주소', 'hobby':'취미', 'skill':'보유 기술'}
        help_texts = {'name':'이름은 2자 이상'}

class MajorModelForm(forms.ModelForm):
    class Meta:
        model = Major
        fields = ['major_id', 'major_title']
        labels = {'major_id':'전공 아이디', 'major_title':'전공명'}
        help_texts = {'major_title':'3글자 이상 입력하세요'}
