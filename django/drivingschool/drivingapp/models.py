from django.db import models

# Create your models here.

class Planning(models.Model):
	id_student= models.IntegerField(max_length=100)
	id_instructor= models.IntegerField(max_length=100)
	date= models.CharField(max_length=100)
	lieu= models.CharField(max_length=100)