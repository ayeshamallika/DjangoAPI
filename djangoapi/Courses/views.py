from django.shortcuts import render
from rest_framework import viewsets
from .models import Courses
from .serializers import CoursesSerializer
# Create your views here.

class CourseView(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
