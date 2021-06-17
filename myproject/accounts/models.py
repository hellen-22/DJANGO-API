from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here

class YearOfStudy(models.Model):
	year = models.CharField(max_length=10)

	def __str__(self):
		return self.year


class School(models.Model):
	name = models.CharField(max_length=200)
	code = models.CharField(max_length=200)

	def __str__(self):
		return self.name 


class Department(models.Model):
	name = models.CharField(max_length=200)
	school = models.ForeignKey(School, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Course(models.Model):
	name = models.CharField(max_length=200)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	school = models.ForeignKey(School, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class StudentProfile(models.Model):
	name = models.CharField(max_length=200)
	reg_no = models.CharField(max_length=20)
	year = models.ForeignKey(YearOfStudy, on_delete=models.CASCADE)
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	hostel = models.CharField(max_length=200)

	def __str__(self):
		return self.reg_no


class LecturerProfile(models.Model):
	name = models.CharField(max_length=200)
	reg_no = models.CharField(max_length=20)
	school = models.ForeignKey(School, on_delete=models.CASCADE)

	def __str__(self):
		return self.reg_no