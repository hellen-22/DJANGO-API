from rest_framework import serializers
from accounts.models import *
from activities.models import *

class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Blog
		fields = '__all__'
	

class AnnouncementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Announcement
		fields = '__all__'


class SuggestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Suggestion
		fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
	class Meta:
		model = School 
		fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Department 
		fields = '__all__'



class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course 
		fields='__all__'


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudentProfile
		fields = '__all__'


class LecturerSerializer(serializers.ModelSerializer):
	class Meta:
		model = LecturerProfile
		fields = '__all__'

