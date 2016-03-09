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
		return unicode(self.id)

# class User(models.Model):
# 	username = models.CharField(max_length=32, unique=True)
# 	def __unicode__(self):
# 		return unicode(self.username)

class Answer(models.Model):
	id = models.AutoField(primary_key=True)
	text = models.CharField(max_length=1024)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	#author = models.ForeignKey(User, on_delete=models.CASCADE)
	def __unicode__(self):
		return unicode(self.id)

class Votes(models.Model):
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
	#voter = models.ForeignKey(User, on_delete=models.CASCADE)
	score = models.IntegerField()

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    score = models.IntegerField(default=0)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username