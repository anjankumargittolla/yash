from django.shortcuts import render
from .models import StudentApplication, StudentRegistration, StaffRegistration
# Create your views here.


def home(request):
    return render(request, 'student/home.html')


def student_application(request):
    return render(request, 'student/application.html')