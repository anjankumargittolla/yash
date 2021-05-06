from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home , name = 'home'),
    path('application/',views.student_application, name = 'student_application'),
 ]