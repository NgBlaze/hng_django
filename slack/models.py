import ssl
from django.db import models

# Create your models here.

class SlackUser(models.Model):
    id = models.IntegerField(primary_key=True)
    slackUsername = models.CharField(max_length=200)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.TextField()
    