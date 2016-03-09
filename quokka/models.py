# from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Set(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=128, unique=True)
	def __unicode__(self):
		return unicode(self.name)

class Question(models.Model):
	id = models.AutoField(primary_key=True)
	text = models.CharField(max_length=512)
	def __unicode__(self):
		return unicode(self.text)

class Answer(models.Model):
	id = models.AutoField(primary_key=True)
	text = models.CharField(max_length=1024)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	def __unicode__(self):
		return unicode(self.text)

class Vote(models.Model):
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
	voter = models.ForeignKey(User, on_delete=models.CASCADE)
	score = models.IntegerField() # should be 1 or -1, depending on whether it's a vote up or down