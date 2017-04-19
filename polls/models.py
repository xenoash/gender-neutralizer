from django.db import models
from django.contrib import admin

class GenderFile(models.Model):
    word = models.CharField(max_length=100)
    equivalent = models.CharField(max_length=100)

try:
	admin.site.register(GenderFile)
except admin.sites.AlreadyRegistered:
	pass