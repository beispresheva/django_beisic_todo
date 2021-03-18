from django.db import models
from django.utils import timezone
from datetime import datetime, date
from django.contrib.auth.models import User

# Label Model
class Label(models.Model):
	label = models.CharField(max_length=30)

	def __str__(self):
		return self.label

# Priority Model
class Priority(models.Model):
	priority = models.CharField(max_length=8)
	
	def __str__(self):
		return self.priority

# Task Model
class Task(models.Model):
	title = models.CharField(max_length=150)
	description = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)
	taskdate = models.DateTimeField("Task Date (mm/dd/yy)", auto_now_add=False, auto_now=False, blank=True)
	completed = models.BooleanField(default=False)
	priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
	label = models.ForeignKey(Label, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title