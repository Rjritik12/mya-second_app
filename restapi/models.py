from django.db import models

# Create your models here.

class Emp(models.Model):
    name = models.CharField(max_length=50)
    salary = models.CharField(max_length=60)
    post = models.CharField(max_length=10)
