from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class query(models.Model):
  name = models.CharField(max_length=30)
  desc = models.CharField(max_length=100)
  view = models.CharField(max_length=15)
