from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudentApplication(models.Model):
    DEPARTMENT_CHOICES = (
        ('CE', 'Civil Engineering'),
        ('CSE', 'Computer Science Engineering'),
        ('ECE', 'Electronics Communtication Engineering'),
        ('EEE', 'Electronics Electrical Engineering'),
        ('ME', 'Mechanical Engineering')
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    student_name = models.CharField(max_length=25)
    student_email = models.EmailField()
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES)
    ssc_marks = models.IntegerField()
    inter_marks = models.IntegerField()
    is_approved = models.BooleanField(default=False)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)

class Student(models.Model):
    student = models.OneToOneField(User, related_name="student_info", on_delete=models.CASCADE)
    mobile = models.IntegerField()
    department = models.CharField(max_length=25)
    profile_pic = models.ImageField('pictures/')
    father_name = models.CharField(max_length=25)



class Staff(models.Model):
    staff = models.ForeignKey(User, related_name="staff_info", on_delete=models.CASCADE)
    staff_mob = models.IntegerField()
    experience = models.CharField(max_length=10)
    qualification = models.TextField(max_length=10)
    staff_dept = models.CharField(max_length=25)
    staff_pic = models.ImageField('pictures/')