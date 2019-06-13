from django.db import models

# Create your models here.

class Planning(models.Model)
	id_student.IntegerField(max_length=100)
	id_instructor.IntegerField(max_length=100)
	date.CharField(max_length=100)
	lieu.CharField(max_length=100)