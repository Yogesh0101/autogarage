from django.db import models


class user(models.Model):
	name=models.CharField(max_length=50)
	mobile=models.CharField(max_length=10)
	password=models.CharField(max_length=50)	
class auser(models.Model):
	name=models.CharField(max_length=50)
	mobile=models.CharField(max_length=10)
	password=models.CharField(max_length=50)
class usera(models.Model):
	name=models.CharField(max_length=50)
	mobile=models.CharField(max_length=10)
	password=models.CharField(max_length=50)