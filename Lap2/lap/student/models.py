from django.db import models
from staff.models import *
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(default='m', unique=True)
    staffRef = models.ForeignKey(to='staff.Staff', on_delete=models.CASCADE, default=1)




