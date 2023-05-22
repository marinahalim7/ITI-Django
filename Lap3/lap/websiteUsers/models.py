from django.db import models

class websiteUsers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(default='m', unique=True)
    password = models.CharField(max_length=10)

