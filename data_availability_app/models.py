from django.db import models
from datetime import datetime 
# Create your models here.

class DataPoint(models.Model):
	value = models.FloatField(null = True, blank = True)
	timestamp = models.DateTimeField(default=datetime.now(), blank=True, null=True)