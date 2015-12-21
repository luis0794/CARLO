from __future__ import unicode_literals

from django.db import models

from django.conf import settings

# Create your models here.
#class usuarios(models.Model):
##	name= models.CharField(max_length=10)
#	last_name=models.CharField(max_length=10)
#	date_create=models.DateTimeField('fecha de creacion')
#	password=models.CharField(max_length=6)##

class UserProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='profiles', blank=True, null=True)
    def __str__(self):
    	return self.user.username