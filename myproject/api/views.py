from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *


# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
	queryset = Announcement.objects.all()
	serializer_class = AnnouncementSerializer


class SuggestionViewSet(viewsets.ModelViewSet):
	queryset = Suggestion.objects.all()
	serializer_class = SuggestionSerializer	


class SchoolViewSet(viewsets.ModelViewSet):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer


class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer


class StudentViewSet(viewsets.ModelViewSet):
	queryset = StudentProfile.objects.all()
	serializer_class = StudentSerializer


class LecturerViewSet(viewsets.ModelViewSet):
	queryset = LecturerProfile.objects.all()
	serializer_class = LecturerSerializer			