from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=225)
    created_at = models.DateField(auto_now=True)
    deadline = models.DateField(auto_now=True)