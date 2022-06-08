# from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Owner(models.Model):
	name = models.CharField(max_length=45, null=True)
	email = models.CharField(max_length=300, null=True)
	age = models.IntegerField(null=True)

	class Meta:
		db_table = 'owners'

class Dog(models.Model):
	owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
	name = models.CharField(max_length=45, null=True)
	age = models.IntegerField(null=True)

	class Meta:
		db_table = 'dogs'
