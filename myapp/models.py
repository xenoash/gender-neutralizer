from django.db import models
from django.contrib import admin

class Entry(models.Model):
	nick=models.CharField(max_length=50)
	url=models.URLField(blank=True)
	date=models.DateTimeField(auto_now_add=True)
	text=models.TextField()
try:
	admin.site.register(Entry)
except admin.sites.AlreadyRegistered:
	pass