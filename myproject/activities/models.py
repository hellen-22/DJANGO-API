from django.db import models
from django.contrib.auth.models import AbstractUser, User
from accounts.models import LecturerProfile, StudentProfile
# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=500)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.CharField(max_length=1000)
	date_posted = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title
    

class Announcement(models.Model):
	title = models.CharField(max_length=500)
	content = models.CharField(max_length=500)
	lecturer = models.ForeignKey(LecturerProfile, on_delete=models.CASCADE)
	date_posted = models.DateTimeField(auto_now_add=True)


	
	def __str__(self):
		return self.title



class Suggestion(models.Model):
	description = models.CharField(max_length=200)
	content = models.CharField(max_length=500)
	date_posted = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title 
	
    	

