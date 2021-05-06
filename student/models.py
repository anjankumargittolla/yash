from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class StudentApplication(models.Model):
    student_name = models.CharField(max_length=25)
    student_email = models.EmailField()
    ssc_marks = models.IntegerField()
    inter_marks = models.IntegerField()


class StudentRegistration(models.Model):
    student_email = models.ForeignKey(StudentApplication,on_delete=models.CASCADE)
    mobile = models.IntegerField()
    department = models.CharField(max_length=25)
    password = models.CharField(max_length=15)
    profile_pic = models.ImageField('pictures/')
    father_name = models.CharField(max_length=25)


class StaffRegistration(models.Model):
    staff_name = models.CharField(max_length=25)
    staff_email = models.EmailField()
    password = models.CharField(max_length=15)
    mobile = models.IntegerField()
    experience = models.CharField(max_length=10)
    qualification = models.TextField(max_length=10)
    department = models.CharField(max_length=25)
    profile_pic = models.ImageField('pictures/')