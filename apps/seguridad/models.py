from __future__ import unicode_literals

from django.db import models

# Create your models here.

class usuarios(models.Model):
	name= models.CharField(max_length=10)
	last_name=models.CharField(max_length=10)
	date_create=models.DateTimeField('fecha de creacion')
	password=models.CharField(max_length=6)
