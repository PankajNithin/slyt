from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Shortener(models.Model):
	short_url_tag = models.CharField(max_length=250,primary_key=True)
	original_url = models.CharField(max_length = 300)
	custom_tag = models.CharField(max_length=250,blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now)
	short_url  = models.CharField(max_length = 200)
	
	def __str__(self):
			return self.short_url


	
