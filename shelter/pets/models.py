from __future__ import unicode_literals
from django.db import models
import datetime

class Profile(models.Model):
	STATUS_CHOICES = (('AED', 'adopted'), 
					  ('ALE', 'adoptable'),
					  ('L', 'lost'),
					  ('F', 'found'))
	GENDER_CHOICES = (('M','male'), 
					  ('F','female'))

	name   		 = models.CharField(max_length=255, primary_key=True, 
									unique=True,    blank=False)
	status 		 = models.CharField(max_length=255, choices=STATUS_CHOICES)
	arrivalDate  = models.DateField(blank=False,default=datetime.date.today)
	estBirthDate = models.DateField(blank=False,default=datetime.date.today)
	creationDate = models.DateField(blank=False,default=datetime.date.today)
	description  = models.CharField(max_length=400)
	gender       = models.CharField(max_length=10, choices=GENDER_CHOICES)

	def __str__(self):
		return ' '.join([self.name, self.status])

class Categories(models.Model):
	name = models.CharField(max_length=255, unique=True)

	def __str__(self):
		return ' '.join([self.name])