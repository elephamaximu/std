from django.db import models
from django.utils import timezone

class Major(models.Model):
    major_id = models.IntegerField(primary_key=True)
    major_title = models.CharField(max_length=100)

    class Meta:
        ordering = ('major_id',)
    
    def __str__(self):
        return self.major_title

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



