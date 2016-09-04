from django.db import models

# Create your models here.

class dmSection(models.Model):
  name = models.CharField(max_length=10)
  order = models.IntegerField
